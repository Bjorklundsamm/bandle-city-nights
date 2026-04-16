#!/usr/bin/env python3
"""
tagger.py — Booru tag assembler for Bandle City Nights

Assembles flat comma-separated tag lists from pre-defined tag_reference.json.
No NLP, no keyword inference — direct lookup by location, characters, act type.

Usage:
    python tools/tagger.py --location tavern --chars tristana
    python tools/tagger.py --location bedroom --chars fizz --explicit --act oral
    python tools/tagger.py --location outdoors --chars miss_fortune katarina --no-mc
    python tools/tagger.py --location tavern --chars jinx --flat --copy

Flags:
    --location LOCATION   Scene location. Choices: tavern, bedroom, outdoors
    --chars NAME...       Characters (e.g. fizz tristana mf kat). MC always added unless --no-mc
    --explicit            Include act tags
    --act ACT_TYPE        Act type for explicit. Choices: oral, penetration, general
    --no-mc               Exclude MC
    --flat                Output as single flat comma-separated list
    --copy                Copy flat output to clipboard (requires pbcopy/xclip)
    --list                List all known locations, characters, and act types

Output format:
    Quality:
        masterpiece, best quality, highly detailed, ...

    Scene:
        tavern interior, wooden walls, candlelight, ...

    Character: Tristana
        tristana (league of legends), tristana, yordle, female, ...

    Character: Mc
        boy, human, male, pov, tall, ...

    Act:        <- only with --explicit
        fellatio, deepthroat, oral, ...
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path


REF_PATH = Path(__file__).parent / "tag_reference.json"

CHAR_ALIASES = {
    "fizz": "fizz",
    "tristana": "tristana", "trist": "tristana",
    "jinx": "jinx",
    "miss_fortune": "miss_fortune", "mf": "miss_fortune",
    "katarina": "katarina", "kat": "katarina",
    "ahri": "ahri",
    "poppy": "poppy",
    "lulu": "lulu",
    "midna": "midna",
    "mc": "mc",
}

LOCATION_KEYS = {
    "tavern": "tavern",
    "inn": "tavern",
    "bar": "tavern",
    "bedroom": "bedroom",
    "room": "bedroom",
    "bed": "bedroom",
    "outdoors": "bandle_city_outdoors",
    "outdoor": "bandle_city_outdoors",
    "outside": "bandle_city_outdoors",
    "forest": "bandle_city_outdoors",
    "bandlewood": "bandle_city_outdoors",
    "alley": "bandle_city_outdoors",
}

ACT_TYPE_KEYS = {
    "oral": "oral",
    "blowjob": "oral",
    "fellatio": "oral",
    "penetration": "penetration",
    "sex": "penetration",
    "general": "general_sexual",
    "nsfw": "general_sexual",
    "size": "size_difference_specific",
    "size_difference": "size_difference_specific",
}


def load_ref() -> dict:
    if not REF_PATH.exists():
        print(f"ERROR: Tag reference not found at {REF_PATH}")
        sys.exit(1)
    with open(REF_PATH) as f:
        return json.load(f)


def dedupe(tags: list[str]) -> list[str]:
    seen = set()
    result = []
    for t in tags:
        key = t.lower()
        if key not in seen:
            seen.add(key)
            result.append(t)
    return result


def resolve_chars(char_args: list[str]) -> list[str]:
    resolved = []
    for c in char_args:
        key = c.lower().replace(" ", "_")
        if key in CHAR_ALIASES:
            resolved.append(CHAR_ALIASES[key])
        else:
            known = ", ".join(sorted(set(CHAR_ALIASES.values())))
            print(f"  WARNING: Unknown character '{c}' — skipping. Known: {known}")
    return resolved


def get_scene_tags(location: str, ref: dict) -> list[str]:
    loc_key = LOCATION_KEYS.get(location.lower())
    if not loc_key:
        known = ", ".join(sorted(set(LOCATION_KEYS.values())))
        print(f"  WARNING: Unknown location '{location}'. Known: {known}")
        return []
    return ref["scene"].get(loc_key, [])


def get_char_tags(char_key: str, ref: dict, explicit: bool) -> list[str]:
    chars = ref.get("characters", {})
    if char_key not in chars:
        return [char_key.replace("_", " ")]

    c = chars[char_key]
    tags = []
    tags += c.get("identity", [])
    tags += c.get("body", [])

    if not explicit:
        tags += c.get("outfit", [])

    tags += c.get("personality_tags", [])

    if char_key == "mc":
        tags += c.get("pov_tags", [])

    return dedupe(tags)


def get_act_tags(act_type: str, ref: dict) -> list[str]:
    act_key = ACT_TYPE_KEYS.get(act_type.lower())
    if not act_key:
        known = ", ".join(sorted(set(ACT_TYPE_KEYS.values())))
        print(f"  WARNING: Unknown act type '{act_type}'. Known: {known}")
        return []

    acts = ref.get("acts", {})
    tags = acts.get(act_key, [])

    # Always append size_difference_specific for context
    if act_key not in ("size_difference_specific",):
        tags = tags + acts.get("size_difference_specific", [])

    return dedupe(tags)


def format_grouped(sections: dict[str, list[str]]) -> str:
    lines = []
    for section, tags in sections.items():
        lines.append(f"{section}:")
        lines.append("    " + ", ".join(tags))
        lines.append("")
    return "\n".join(lines).strip()


def format_flat(sections: dict[str, list[str]]) -> str:
    all_tags = []
    for tags in sections.values():
        all_tags += tags
    return ", ".join(dedupe(all_tags))


def copy_to_clipboard(text: str) -> None:
    try:
        subprocess.run(["pbcopy"], input=text.encode(), check=True)
        print("Copied to clipboard.")
        return
    except Exception:
        pass
    try:
        subprocess.run(["xclip", "-selection", "clipboard"], input=text.encode(), check=True)
        print("Copied to clipboard.")
    except Exception:
        print("(Could not copy — pbcopy/xclip not available)")


def print_list(ref: dict) -> None:
    print("\nLocations:")
    for k in sorted(set(LOCATION_KEYS.values())):
        aliases = [a for a, v in LOCATION_KEYS.items() if v == k]
        print(f"  {k}  (aliases: {', '.join(aliases)})")

    print("\nCharacters:")
    by_char: dict[str, list[str]] = {}
    for alias, key in CHAR_ALIASES.items():
        by_char.setdefault(key, []).append(alias)
    for key in sorted(by_char):
        aliases = [a for a in by_char[key] if a != key]
        suffix = f"  (aliases: {', '.join(aliases)})" if aliases else ""
        print(f"  {key}{suffix}")

    print("\nAct types (use with --explicit --act TYPE):")
    for k in sorted(set(ACT_TYPE_KEYS.values())):
        aliases = [a for a, v in ACT_TYPE_KEYS.items() if v == k]
        print(f"  {k}  (aliases: {', '.join(aliases)})")
    print()


def main():
    parser = argparse.ArgumentParser(description="Booru tag assembler for Bandle City Nights")
    parser.add_argument("--location", default=None,
                        help="Scene location: tavern, bedroom, outdoors")
    parser.add_argument("--chars", nargs="*", default=None,
                        help="Characters: fizz tristana mc mf kat etc.")
    parser.add_argument("--explicit", action="store_true",
                        help="Include act tags")
    parser.add_argument("--act", default=None,
                        help="Act type (with --explicit): oral, penetration, general, size")
    parser.add_argument("--no-mc", action="store_true",
                        help="Exclude MC from output")
    parser.add_argument("--flat", action="store_true",
                        help="Output as single flat comma-separated list")
    parser.add_argument("--copy", action="store_true",
                        help="Copy flat output to clipboard")
    parser.add_argument("--list", action="store_true",
                        help="List all known locations, characters, and act types")
    args = parser.parse_args()

    ref = load_ref()

    if args.list:
        print_list(ref)
        return

    # Resolve characters
    char_keys = resolve_chars(args.chars) if args.chars else []
    if not args.no_mc and "mc" not in char_keys:
        char_keys.append("mc")

    # Build sections
    sections: dict[str, list[str]] = {}

    # Quality — always first
    sections["Quality"] = ref["quality_style"][:6]

    # Scene
    if args.location:
        scene_tags = get_scene_tags(args.location, ref)
        if scene_tags:
            sections["Scene"] = scene_tags

    # Characters
    for char_key in char_keys:
        label = f"Character: {char_key.replace('_', ' ').title()}"
        sections[label] = get_char_tags(char_key, ref, args.explicit)

    # Act — explicit only
    if args.explicit:
        act_type = args.act or "general"
        act_tags = get_act_tags(act_type, ref)
        if act_tags:
            sections["Act"] = act_tags

    # Output
    print("\n" + "─" * 60)
    if args.flat:
        output = format_flat(sections)
    else:
        output = format_grouped(sections)
    print(output)
    print("─" * 60)

    if args.copy:
        copy_to_clipboard(format_flat(sections))


if __name__ == "__main__":
    main()
