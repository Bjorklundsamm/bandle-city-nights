#!/usr/bin/env python3
"""
novelai_gen.py — NovelAI generation tool for Bandle City Nights

MODES
─────
Generate (default)
    Fill in a # [GEN START] / # [EXPLICIT END] block. Chains multiple 200-token
    segments. Author's note is built dynamically from the character JSON — only
    the fields relevant to the scene type are included.

    python tools/novelai_gen.py --file FILE --char CHAR [--scene-note NOTE]
                                [--segments N] [--regen] [--explicit] [--dry-run]

Rewrite  (--rewrite START END)
    Replace specific lines with a NovelAI continuation. Provide the 1-based line
    range you want replaced and optionally a reason. The tool estimates how many
    tokens the original section used and targets the same length.

    python tools/novelai_gen.py --file FILE --char CHAR
                                --rewrite 45 67 --rewrite-note "Fizz keeps kneeling, fix the height dynamic"
                                [--scene-note NOTE] [--explicit]

Advance  (--advance)
    Move # [GEN START] to after the last complete sentence in the accepted block,
    trimming any dangling incomplete lines. No API call.

    python tools/novelai_gen.py --file FILE --advance

MARKERS IN .RPY FILES
─────────────────────
    # [GEN START]           insertion point for new generation
    # [SCENE NOTE: ...]     one-line scene context (overridden by --scene-note)
    # [EXPLICIT START]      Claude skips everything inside this block
    # [EXPLICIT END]        end of explicit block

AUTHOR'S NOTE STRATEGY
──────────────────────
Claude builds the author's note in layers. For every call it includes:
  - Ren'Py format rules (who n/mc/f etc. are, line length, format)
  - Setting (location, time of day from scene note or file context)
  - Character name, species, height/build

For explicit calls (--explicit flag) Claude also adds:
  - Physical distinguishing features relevant to the sex act
  - Anatomy notes from the character JSON nsfw_profile
  - Specific scene mechanics the user provides via --scene-note

Claude never writes explicit content itself — it builds the scaffolding
and hands off to Xialong.

ENVIRONMENT
───────────
    NAI_API_KEY — NovelAI persistent API token (.env or shell)

REQUIREMENTS
────────────
    pip install requests novelai-api
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Environment / config
# ---------------------------------------------------------------------------

def load_env():
    env_path = Path(__file__).parent.parent / ".env"
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, _, v = line.partition("=")
                    os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def get_api_key():
    key = os.environ.get("NAI_API_KEY")
    if not key:
        print("ERROR: NAI_API_KEY not set. Add it to .env or export it in your shell.")
        sys.exit(1)
    return key


# ---------------------------------------------------------------------------
# Character loading
# ---------------------------------------------------------------------------

def load_character(char_name: str) -> dict:
    char_file = Path(__file__).parent.parent / "characters" / f"{char_name}.json"
    if not char_file.exists():
        available = ", ".join(p.stem for p in char_file.parent.glob("*.json"))
        print(f"ERROR: No character file for '{char_name}'. Available: {available}")
        sys.exit(1)
    with open(char_file) as f:
        return json.load(f)


# ---------------------------------------------------------------------------
# Author's note builder
# ---------------------------------------------------------------------------

def build_authors_note(char: dict, scene_note: str | None, explicit: bool) -> str:
    """
    Build a focused author's note for Xialong.

    Always included (safe for Claude to write):
      - Ren'Py format rules
      - Character identifier, name, species
      - Height / build (critical for physical positioning)
      - Setting extracted from scene_note

    Added only when --explicit is passed (Claude writes the scaffolding,
    not the act itself — these are factual physical/anatomical notes):
      - Distinguishing physical features relevant to the act
      - nsfw_profile anatomy and fixation notes from the JSON
      - The user-supplied scene_note (which may contain explicit direction)
    """
    name = char.get("name", "Unknown")
    species = char.get("species", "")
    shortcode = _guess_shortcode(name)

    appearance = char.get("appearance", {})
    build = appearance.get("build", "")
    attire = appearance.get("usual_attire", "")
    features = appearance.get("distinguishing_features", "")
    coloring = appearance.get("coloring", "")

    lines = []

    # --- Always: Ren'Py format block ---
    lines += [
        "FORMAT: Ren'Py visual novel script.",
        f"  n \"...\" = narrator (third person, present tense, punchy)",
        f"  mc \"...\" = player character (male, tall human, broad build)",
        f"  {shortcode} \"...\" = {name}",
        "  Each line max ~115 characters. One thought per line. No stage directions.",
        "  Continue the scene in the same style as the context above.",
        "",
    ]

    # --- Always: Character identity + physical build ---
    lines.append(f"CHARACTER: {name} ({species})")
    if build:
        lines.append(f"  Build: {build}")
    if coloring:
        lines.append(f"  Appearance: {coloring}")
    if attire:
        lines.append(f"  Clothing: {attire}")

    # --- Always: Height dynamic (critical for positioning) ---
    height_note = _height_note(species, char)
    if height_note:
        lines.append(f"  {height_note}")

    lines.append("")

    # --- Always: Setting from scene_note (non-explicit part) ---
    if scene_note:
        setting = _extract_setting(scene_note)
        if setting:
            lines.append(f"SETTING: {setting}")
            lines.append("")

    # --- Explicit-only: physical/anatomy notes + full scene direction ---
    if explicit:
        if features:
            lines.append(f"PHYSICAL NOTES: {features}")
        nsfw = char.get("nsfw_profile", {})
        fixation = nsfw.get("primary_fixation", "")
        orientation = nsfw.get("orientation", "")
        exp = nsfw.get("experience_level", "")
        anat = nsfw.get("anatomy", "")  # some chars may have this
        if orientation:
            lines.append(f"  Orientation: {orientation}")
        if fixation:
            lines.append(f"  Fixation: {fixation}")
        if exp:
            lines.append(f"  Experience: {exp}")
        if anat:
            lines.append(f"  Anatomy: {anat}")
        lines.append("")
        if scene_note:
            lines.append(f"SCENE DIRECTION: {scene_note}")
            lines.append("")

    lines.append("Write the continuation now.")
    return "\n".join(lines)


def _guess_shortcode(name: str) -> str:
    """Map character name to their Ren'Py shortcode."""
    mapping = {
        "Fizz": "f", "Tristana": "t", "Poppy": "p", "Lulu": "l",
        "Vex": "vx", "Katarina": "k", "Ahri": "a", "Ezreal": "ez",
        "Neeko": "neo", "Nidalee": "ni", "Jinx": "j", "Miss Fortune": "mf",
        "Morgana": "mo", "Corki": "co", "Rumble": "ru", "Teemo": "te",
        "Kindred": "ki", "Lilia": "li",
    }
    return mapping.get(name, name[0].lower())


def _height_note(species: str, char: dict) -> str:
    """
    Return a concise height-dynamic note.
    This is the single biggest source of positioning errors from Xialong —
    being explicit about relative heights prevents 'kneeling' errors etc.
    """
    s = species.lower()
    name = char.get("name", "")
    if "yordle" in s:
        return (
            f"{name} is a Yordle — roughly 3 to 3.5 feet tall. "
            f"MC is a tall adult human (~6 feet). "
            f"Standing, {name}'s face is level with MC's groin — no kneeling needed for fellatio."
        )
    if "human" in s:
        return f"{name} is human, similar height to MC."
    return ""


def _extract_setting(scene_note: str) -> str:
    """
    Pull location/time/environment words from the scene note
    without touching any explicit content direction.
    Safe for Claude to process.
    """
    # Keywords that indicate setting rather than action
    setting_words = [
        "behind", "tavern", "forest", "woods", "bandlewood", "alley", "market",
        "outside", "inside", "night", "day", "evening", "morning", "dusk", "dawn",
        "quiet", "private", "edge", "treeline", "room", "street", "dock", "harbor",
    ]
    words = scene_note.lower()
    if any(w in words for w in setting_words):
        # Return first sentence only — likely to be the setting description
        first = re.split(r'[.!?]', scene_note)[0].strip()
        return first
    return ""


# ---------------------------------------------------------------------------
# File parsing
# ---------------------------------------------------------------------------

def read_file(path: Path) -> list[str]:
    with open(path) as f:
        return f.readlines()


def write_file(path: Path, lines: list[str]):
    with open(path, "w") as f:
        f.writelines(lines)


def find_markers(lines: list[str]) -> dict:
    """
    Returns dict with keys: gen_start, explicit_start, explicit_end, scene_note.
    Indices are 0-based line numbers. None if not found.
    """
    result = {"gen_start": None, "explicit_start": None, "explicit_end": None, "scene_note": None}
    for i, line in enumerate(lines):
        s = line.strip()
        if s == "# [GEN START]":
            result["gen_start"] = i
        elif s == "# [EXPLICIT START]":
            result["explicit_start"] = i
        elif s == "# [EXPLICIT END]":
            result["explicit_end"] = i
        else:
            m = re.match(r"#\s*\[SCENE NOTE:\s*(.+?)\]", s)
            if m:
                result["scene_note"] = m.group(1).strip()
    return result


def extract_context(lines: list[str], up_to_idx: int, max_lines: int) -> str:
    """Return up to max_lines lines before up_to_idx as a single string."""
    start = max(0, up_to_idx - max_lines)
    return "".join(lines[start:up_to_idx])


def estimate_tokens(lines: list[str]) -> int:
    """
    Rough token estimate for a block of Ren'Py lines.
    ~1 token per 3.5 characters is a reasonable average for prose.
    Minimum 80, maximum 200 (Xialong's cap per call).
    """
    text = "".join(lines)
    chars = len(text.strip())
    estimated = max(80, min(200, int(chars / 3.5)))
    return estimated


# ---------------------------------------------------------------------------
# Insert / replace helpers
# ---------------------------------------------------------------------------

def wrap_block(text: str, explicit: bool) -> list[str]:
    """Wrap generated text in appropriate markers."""
    result = []
    if explicit:
        result.append("    # [EXPLICIT START]\n")
    for line in text.splitlines():
        s = line.strip()
        result.append(f"    {s}\n" if s else "\n")
    if explicit:
        result.append("    # [EXPLICIT END]\n")
    return result


def insert_generated(lines: list[str], markers: dict, block: list[str], regen: bool) -> list[str]:
    """
    Insert block into lines at the correct position.
    If regen and explicit block exists, replace it.
    Otherwise insert after [GEN START].
    """
    gs = markers["gen_start"]
    es = markers["explicit_end"]

    if regen and es is not None and es > gs:
        before = lines[: gs + 1]
        after = lines[es + 1:]
    else:
        before = lines[: gs + 1]
        after = lines[gs + 1:]

    return before + ["\n"] + block + ["\n"] + after


# ---------------------------------------------------------------------------
# Advance marker
# ---------------------------------------------------------------------------

def advance_gen_start(rpy_path: Path):
    """
    Move # [GEN START] to after the last complete sentence inside the
    [EXPLICIT START] / [EXPLICIT END] block. Trims dangling incomplete lines.
    """
    lines = read_file(rpy_path)
    markers = find_markers(lines)

    es = markers["explicit_start"]
    ee = markers["explicit_end"]
    gs = markers["gen_start"]

    if es is None or ee is None:
        print("ERROR: No [EXPLICIT START]/[EXPLICIT END] block found.")
        sys.exit(1)

    block_lines = lines[es + 1: ee]
    terminal = re.compile(r'[.!?]["\']?\s*$')

    last_clean = None
    for i, line in enumerate(block_lines):
        s = line.strip()
        if s and not s.startswith("#") and terminal.search(s):
            last_clean = i

    if last_clean is None:
        insert_after = es
        print("WARNING: No complete sentence found. Placing [GEN START] at block start.")
    else:
        insert_after = es + 1 + last_clean

    # Lines to trim: after last_clean, inside the block
    if last_clean is not None:
        trim_from = es + 1 + last_clean + 1
        trim_to = ee
        remove = set(range(trim_from, trim_to))
        trimmed = sum(1 for i in remove if lines[i].strip() and not lines[i].strip().startswith("#"))
        if trimmed:
            print(f"Trimmed {trimmed} incomplete line(s).")
    else:
        remove = set()

    remove.add(gs)
    new_lines = [l for i, l in enumerate(lines) if i not in remove]

    removed_before = sum(1 for i in remove if i <= insert_after)
    insert_after -= removed_before

    new_lines.insert(insert_after + 1, "    # [GEN START]\n")
    write_file(rpy_path, new_lines)
    print(f"[GEN START] moved to line ~{insert_after + 2}.")


# ---------------------------------------------------------------------------
# Rewrite mode helpers
# ---------------------------------------------------------------------------

def extract_rewrite_block(lines: list[str], start_line: int, end_line: int) -> tuple[str, list[str]]:
    """
    start_line / end_line are 1-based (as shown in editors).
    Returns (context_above, target_lines).
    """
    idx_start = start_line - 1
    idx_end = end_line  # exclusive
    target = lines[idx_start:idx_end]
    context = lines[max(0, idx_start - 80): idx_start]
    return "".join(context), target


def apply_rewrite(lines: list[str], start_line: int, end_line: int, new_block: list[str]) -> list[str]:
    idx_start = start_line - 1
    idx_end = end_line
    return lines[:idx_start] + new_block + lines[idx_end:]


# ---------------------------------------------------------------------------
# NovelAI API
# ---------------------------------------------------------------------------

XIAOLANG_MODELS = {"xialong-v1", "xialong", "xiaolang-v1", "xiaolang"}


def build_xiaolang_prompt(context: str, authors_note: str) -> str:
    return (
        "[gMASK]<sop><|system|>\n"
        "You are Xialong (夏龍), an AI model finetuned by Anlatan. "
        "You follow instructions precisely and write with creativity and depth.\n"
        f"{authors_note}\n"
        "<|user|>\n***\nWrite./nothink<|assistant|>\n<think></think>\n"
        f"{context}"
    )


def call_xiaolang(api_key: str, context: str, authors_note: str, max_tokens: int) -> str:
    import requests
    prompt = build_xiaolang_prompt(context, authors_note)
    resp = requests.post(
        "https://text.novelai.net/oa/v1/completions",
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        json={
            "model": "xialong-v1",
            "prompt": prompt,
            "max_tokens": max_tokens,
            "temperature": 1.05,
            "top_p": 0.95,
            "repetition_penalty": 1.12,
        },
        timeout=60,
    )
    if resp.status_code == 401:
        print("ERROR: 401 — check NAI_API_KEY.")
        sys.exit(1)
    if not resp.ok:
        print(f"ERROR: NovelAI {resp.status_code}: {resp.text[:300]}")
        sys.exit(1)
    choices = resp.json().get("choices", [])
    return choices[0].get("text", "") if choices else ""


def call_erato(api_key: str, context: str, authors_note: str, max_tokens: int) -> str:
    import requests, base64, struct
    from novelai_api.Tokenizer import Tokenizer
    from novelai_api.Preset import Model as NAIModel

    tokens = Tokenizer.encode(NAIModel.Erato, context)
    b64 = base64.b64encode(struct.pack(f"<{len(tokens)}I", *tokens)).decode()
    note_ascii = authors_note.encode("ascii", errors="replace").decode("ascii")

    resp = requests.post(
        "https://text.novelai.net/ai/generate",
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        json={
            "input": b64,
            "model": "llama-3-erato-v1",
            "parameters": {
                "max_length": max_tokens, "min_length": 20,
                "temperature": 1.05, "top_p": 0.95,
                "tail_free_sampling": 0.925, "repetition_penalty": 1.12,
                "repetition_penalty_range": 2048,
                "memory": "", "authors_note": note_ascii,
            },
        },
        timeout=60,
    )
    if not resp.ok:
        print(f"ERROR: NovelAI {resp.status_code}: {resp.text[:300]}")
        sys.exit(1)
    raw = base64.b64decode(resp.json().get("output", ""))
    out_tokens = list(struct.unpack(f"<{len(raw)//4}I", raw))
    return Tokenizer.decode(NAIModel.Erato, out_tokens)


def call_novelai(api_key: str, context: str, authors_note: str, max_tokens: int, model: str) -> str:
    if model.lower() in XIAOLANG_MODELS:
        return call_xiaolang(api_key, context, authors_note, max_tokens)
    return call_erato(api_key, context, authors_note, max_tokens)


def generate_segments(api_key: str, context: str, authors_note: str,
                      tokens_per_seg: int, segments: int, model: str) -> str:
    accumulated = ""
    rolling = context
    for i in range(segments):
        if segments > 1:
            print(f"  Segment {i+1}/{segments}...")
        chunk = call_novelai(api_key, rolling, authors_note, tokens_per_seg, model)
        if not chunk.strip():
            print(f"  WARNING: Segment {i+1} empty, stopping.")
            break
        accumulated += chunk
        rolling += chunk
    return accumulated


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    load_env()

    parser = argparse.ArgumentParser(
        description="NovelAI generation tool for Bandle City Nights",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--file", required=True, help=".rpy file to work on")
    parser.add_argument("--char", default=None, help="Character name (matches characters/<name>.json)")
    parser.add_argument("--scene-note", default=None, help="Scene context / direction for the author's note")
    parser.add_argument("--explicit", action="store_true",
                        help="Explicit scene — adds physical/anatomy notes to author's note and wraps in EXPLICIT markers")
    parser.add_argument("--model", default="xialong", help="Model: xialong (default), erato, kayra, clio")
    parser.add_argument("--tokens", type=int, default=200, help="Tokens per segment (max 200, default 200)")
    parser.add_argument("--segments", type=int, default=3, help="Number of chained segments (default 3)")
    parser.add_argument("--context-lines", type=int, default=80, help="Lines of context to send (default 80)")
    parser.add_argument("--regen", action="store_true", help="Replace existing explicit block at [GEN START]")
    parser.add_argument("--dry-run", action="store_true", help="Print what would be sent, no API call")
    parser.add_argument("--advance", action="store_true",
                        help="Move [GEN START] to after last complete sentence in accepted block")
    # Rewrite mode
    parser.add_argument("--rewrite", nargs=2, type=int, metavar=("START", "END"),
                        help="Rewrite lines START–END (1-based). Estimates token count from original length.")
    parser.add_argument("--rewrite-note", default=None,
                        help="Reason / direction for the rewrite (e.g. 'Fizz keeps kneeling, fix height dynamic')")

    args = parser.parse_args()

    rpy_path = Path(args.file)
    if not rpy_path.exists():
        print(f"ERROR: File not found: {rpy_path}")
        sys.exit(1)

    # --advance: no API call needed
    if args.advance:
        advance_gen_start(rpy_path)
        return

    # Character is required for all generation modes
    if not args.char:
        print("ERROR: --char is required for generation.")
        sys.exit(1)

    char = load_character(args.char)
    lines = read_file(rpy_path)

    # ── REWRITE MODE ──────────────────────────────────────────────────────
    if args.rewrite:
        start_line, end_line = args.rewrite
        if start_line < 1 or end_line < start_line or end_line > len(lines):
            print(f"ERROR: Line range {start_line}–{end_line} is invalid (file has {len(lines)} lines).")
            sys.exit(1)

        context, target_lines = extract_rewrite_block(lines, start_line, end_line)
        token_target = estimate_tokens(target_lines)
        segments = max(1, round(token_target / 200))

        # Build a scene note that combines the rewrite direction + any user note
        rewrite_direction = []
        if args.rewrite_note:
            rewrite_direction.append(f"Rewrite direction: {args.rewrite_note}")
        rewrite_direction.append(f"Match the approximate length of the original ({len(target_lines)} lines).")
        combined_note = " ".join(rewrite_direction)
        if args.scene_note:
            combined_note = args.scene_note + " | " + combined_note

        authors_note = build_authors_note(char, combined_note, args.explicit)

        if args.dry_run:
            print(f"=== REWRITE TARGET (lines {start_line}–{end_line}) ===")
            print("".join(target_lines))
            print(f"\n=== ESTIMATED TOKENS: {token_target} (~{segments} segment(s)) ===")
            print("\n=== AUTHOR'S NOTE ===")
            print(authors_note)
            return

        api_key = get_api_key()
        print(f"Rewriting lines {start_line}–{end_line} (~{token_target} tokens, {segments} segment(s))...")
        output = generate_segments(api_key, context, authors_note, min(200, args.tokens), segments, args.model)

        if not output.strip():
            print("ERROR: Empty output from NovelAI.")
            sys.exit(1)

        new_block = wrap_block(output, args.explicit)
        updated = apply_rewrite(lines, start_line, end_line, new_block)
        write_file(rpy_path, updated)
        print(f"Done. Lines {start_line}–{end_line} replaced ({len(new_block)} new lines).")
        print("Review and run --advance if you want to continue from there.")
        return

    # ── GENERATE MODE (default) ───────────────────────────────────────────
    markers = find_markers(lines)

    if markers["gen_start"] is None:
        print(f"ERROR: No '# [GEN START]' marker found in {rpy_path}")
        print("  Add it to the .rpy file where you want content inserted.")
        sys.exit(1)

    scene_note = args.scene_note or markers["scene_note"]
    authors_note = build_authors_note(char, scene_note, args.explicit)
    context = extract_context(lines, markers["gen_start"], args.context_lines)

    if args.dry_run:
        print("=== CONTEXT (last 20 lines) ===")
        print("".join(context.splitlines(keepends=True)[-20:]))
        print("\n=== AUTHOR'S NOTE ===")
        print(authors_note)
        print(f"\n=== Model: {args.model}  Tokens/seg: {args.tokens}  Segments: {args.segments} ===")
        return

    api_key = get_api_key()
    segs = max(1, args.segments)
    print(f"Calling NovelAI ({args.model}, {args.tokens}t x{segs}) for {char.get('name')}...")
    output = generate_segments(api_key, context, authors_note, min(200, args.tokens), segs, args.model)

    if not output.strip():
        print("ERROR: Empty output from NovelAI.")
        sys.exit(1)

    block = wrap_block(output, args.explicit)
    updated = insert_generated(lines, markers, block, args.regen)
    write_file(rpy_path, updated)

    insert_line = markers["gen_start"] + 2
    print(f"Done. Inserted at line ~{insert_line} in {rpy_path}")
    print("Like it? Run --advance to accept and continue. Don't? Run --regen to replace.")


if __name__ == "__main__":
    main()
