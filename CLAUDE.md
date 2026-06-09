# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

**Bandle City Nights** is a Ren'Py visual novel set in the League of Legends universe. The player character washes up in Bandle City (home of the Yordles) and takes on odd jobs while building relationships with characters from the LoL roster. Built with the [Ren'Py SDK](https://www.renpy.org/).

This is a private, solo-managed project. Operate with high autonomy — edit files, reorganize scripts, rename things, run git commands without asking permission. Reserve confirmation only for permanent deletion or force-push operations.

**Git push:** Never push automatically after commits. Only push when the user explicitly says to push.

## Running the Game

Open in the **Ren'Py launcher** and click "Launch Project". There is no CLI build step — Ren'Py compiles `.rpy` → `.rpyc` automatically on launch. Use the launcher's "Build Distributions" to package a release.

**IMPORTANT — rpyc files:** When renaming or moving any `.rpy` file, immediately delete the corresponding `.rpyc` file in the same directory. Stale `.rpyc` files cause confusing duplicate-declaration errors. The `.rpyc` files should not be committed to git.

## Story Context

**Always read `CONTEXT.md` before starting any narrative, dialogue, or content work.** It tracks where the story currently ends, the status of every character arc, the NSFW workflow, and the ordered next-work list. Update it whenever a scene is completed or priorities shift.

## File Architecture

```
game/
  narrative/
    defines.rpy               ← All character defines and default variables (edit here only)
    day1/
      day1_intro.rpy          ← start, introductions, gameStart labels
      day1_morning.rpy        ← wakingUp label
      day1_night.rpy          ← tavern_tutorial_loop, all Day 1 character first-meets
    day2/
      day2_morning.rpy        ← morning_day_2, Katarina peek, loaded dice
      day2_tavern.rpy         ← day2_tavern_loop: Barkeep, Lulu, Poppy
      day2_outside.rpy        ← day2_outside_loop: Miss Fortune, Fizz, job signs
      day2_fizz.rpy           ← Fizz intro + explicit scene (isolated for Tier 3 content)
      day2_corki/rumble/      ← Minigame logic for each job boss
        teemo/morgana/ezreal.rpy
    endings/
      gameovers.rpy
    minigames/
      jobs_hub.rpy            ← Job hub screen + routing labels (Day 3+)
      minigame_*.rpy          ← Standalone minigame implementations
    tavern/
      barkeep_system.rpy      ← barkeep_ask_about and overview labels
      tavern_hub_screens.rpy  ← Reusable tavern hub screen
    ui/
      day_card.rpy            ← show_day_card label
  screens.rpy                 ← All UI screens (say, menu, prefs, save/load), styles
  gui.rpy                     ← Theme values — generated file, edit carefully
  options.rpy                 ← Game config: title, version, audio, transitions, build
  inventory.rpy               ← Backpack screen and inventory_button overlay
```

New scenes/characters get their own file under `narrative/day*/` or a new `day*/` folder. Isolate any file containing a Tier 3 `[EXPLICIT]` block — name it `day*_[character].rpy`. Keep narrative files under ~800 lines; split by location or story arc when they grow larger.

## Constitution System

The player has 5 hearts × 5 sections = 25 total constitution points. The current value is tracked in `persistent.constitution` (starts at 1). Heart images live at `game/gui/hud/Heart - N.png` (N = 0–5).

- **Gain a point:** `$ persistent.constitution += 1` — the HUD updates automatically.
- **HUD visibility:** controlled by `persistent.constitution_hud_visible`. Set to `True` once during the Kindred/constitution system announcement; the overlay screen `constitution_hud` is always registered but renders nothing until that flag is True.
- **System announcements:** wrap any `s "..."` reveal line with `show screen system_overlay` before and `hide screen system_overlay` after. The HUD slides in diagonally (off-screen top-left → top-left corner) on its first appearance only.
- **Heart zoom:** currently `zoom=0.5` in `screens.rpy` — adjust if images appear too large/small.

## Dialogue Length Limit

Each dialogue line must fit comfortably within the textbox without wrapping to more than two lines. The following is the approximate **maximum length** for any single dialogue string:

> "The sound of the leaves rushing past barely even registers as you dash forward, your heart thundering in your chest."

That is roughly **115 characters** or about **one full thought**. If a line is longer, split it into two separate `n "..."` (or character) calls. Never cram two complete sentences into one call just because they're related — the second sentence is its own beat and deserves its own click.

## Story Flow

```
label start
  └─► label wakingUp          (script_room.rpy)
        └─► label introductions  (script_main.rpy)
              └─► menu
                    ├─► label gameStart    (script_main.rpy)
                    └─► label gameover1    (script_misc.rpy)
```

Labels use `lower_case_with_underscores`. They share a global namespace across all files — use hierarchical names to prevent collisions (e.g. `tavern_night_tristana` not just `tristana`). Use sublabels (`.choice_a`) for branching within a scene.

## Variable Declaration Rules

Getting this wrong breaks save compatibility — use the right keyword every time:

| Keyword | Use for | Saved? |
|---|---|---|
| `define` | True constants: `Character()` objects, config numbers. **Never modify at runtime.** | No |
| `default` | All variables that change during a playthrough (flags, counters, lists). | Yes |
| `persistent` | Cross-playthrough data: settings, gallery unlocks, NG+ flags. | Yes, always |

**Rule:** Every variable that changes during gameplay must have a `default` declaration at the top level — never set variables for the first time with bare `$ var = value` inside a label. Saves created before a new `default` variable existed will initialize it to the declared value automatically; bare assignments crash or misbehave on old saves.

```renpy
# Correct
default has_met_tristana = False
default affection_tristana = 0
default persistent.inventory_unlocked = False

# Wrong — breaks old saves
label gameStart:
    $ has_met_tristana = False   # no prior default declaration
```

## Asset Naming Convention

Ren'Py lowercases filenames and splits on spaces to create image tags. The filename **is** the show command:

```
bg tavern empty.png       →  scene bg tavern empty
ch tristana happy.png     →  show ch tristana happy
bt backpack.png           →  add "bt backpack"
```

Current prefixes: `bg` (backgrounds), `ch` (character sprites), `bt` (buttons/UI), `sc` (screen overlays). Spaces separate tags; be consistent — don't mix spaces and underscores within a project.

## Screens and Transforms

- Screens are declared at top level, never inside labels or init blocks.
- Always include `()` in screen declarations: `screen inventory_button():` — improves Ren'Py's prediction performance.
- Screens describe display only. Game logic belongs in labels, triggered via `Action` objects.
- `show screen foo()` — non-blocking overlay; `call screen foo()` — blocks until `Return()`.

ATL transforms must also be at the top level (or explicit `init` block) — a transform defined inside a label silently fails. Put reusable transforms in a dedicated `transforms.rpy` file as the project grows.

## Defining Transitions

Define named transitions once in `options.rpy` rather than using magic numbers in scripts:

```renpy
define quick_fade = Fade(0.15, 0.0, 0.15)
define scene_change = Dissolve(0.5)
```

This lets you tune timing globally without touching narrative scripts.

## NSFW Content System

This project contains adult content. The following tiers govern what Claude writes vs. what Xialong generates.

**Tier 1 — Claude writes freely**
Flirting, romantic tension, innuendo, kissing, undressing described tastefully, fade-to-black transitions, emotional intimacy, suggestive dialogue.

**Tier 1 Register — use this actively, not cautiously**
This is an NSFW game. Tier 1 dialogue should read pornographic in register even when it stops short of explicit acts. That means:
- Use direct sexual vocabulary when characters mean it: cock, tits, ass. Don't reach for a softer word when the blunt one is clearly what the character would say.
- Innuendo must be unmistakable. If a player could read it as innocent, it's not doing its job.
- Horny characters should read as horny — not "interested," not "intrigued." Their want is the point.
- Size-difference, human/Yordle dynamics, feral/beast framing, BWC obsession — these are recurring kinks. When a scene supports one, lean into it.
- Don't soften lines after writing them.

**Tier 2 — Claude writes with straightforward handling**
Explicit but not pornographic. Sexual situations described with clear intent — character reactions, dialogue during, emotional beats. Literary erotica register.

**Tier 3 — Xialong writes, Claude builds the scaffolding**
Highly graphic or pornographic content. Claude does not write this directly. Instead:

1. Claude drafts everything up to the explicit moment and everything after it.
2. Claude runs `novelai_gen.py` with `--explicit` to hand off to Xialong.
3. Claude builds the author's note with everything that doesn't violate its policies: Ren'Py format rules, character names and shortcodes, species, height/build, setting, time of day, anatomy that is factual rather than pornographic.
4. Claude prompts the user for the one thing it can't supply: the explicit scene direction (what act, what dynamic, what the beats are).
5. Xialong generates the block. Claude does not read or process what's inside `# [EXPLICIT START]` / `# [EXPLICIT END]`.

### Xialong Handoff Protocol

When a scene reaches Tier 3, Claude says:

> "This is an explicit scene — I'll let Xialong write it. I need one thing from you: describe what happens (the act, the dynamic, how it ends). I'll handle everything else in the author's note — format, character descriptions, setting, height dynamics, anatomy — and make the API call. You review the result."

Claude then:
- Populates the non-explicit author's note fields from the character JSON automatically
- Asks the user only for the explicit scene direction
- Calls `python tools/novelai_gen.py --file FILE --char CHAR --explicit --scene-note "USER_DIRECTION" --segments N --regen`

### Rewrite Protocol

When the user says "rewrite lines X–Y" or "fix this section":
- If the section is inside `# [EXPLICIT START]` / `# [EXPLICIT END]`, treat it as Tier 3 — follow Xialong handoff protocol above.
- If the section is Tier 1/2, Claude can rewrite it directly or use `--rewrite X Y --rewrite-note "reason"` if the user prefers Xialong's dialogue style.
- Always estimate length first: count the lines, target the same approximate length in the rewrite.

### Marker System

```renpy
# [GEN START]           — Xialong insertion point
# [SCENE NOTE: ...]     — one-line scene context (in-file override)
# [EXPLICIT START]      — Claude skips everything inside
# [EXPLICIT END]        — end of explicit block
```

Claude never reads, quotes, or builds on content between `# [EXPLICIT START]` and `# [EXPLICIT END]`.

### Hard Limits (non-negotiable regardless of tier)

- No sexual content involving minors. Any ambiguously aged character must be written and treated as an adult.
- No non-consensual scenarios framed approvingly as erotica.
