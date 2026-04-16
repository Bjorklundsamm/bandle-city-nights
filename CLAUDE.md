# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

**Bandle City Nights** is a Ren'Py visual novel set in the League of Legends universe. The player character washes up in Bandle City (home of the Yordles) and takes on odd jobs while building relationships with characters from the LoL roster. Built with the [Ren'Py SDK](https://www.renpy.org/).

This is a private, solo-managed project. Operate with high autonomy — edit files, reorganize scripts, rename things, run git commands without asking permission. Reserve confirmation only for permanent deletion or force-push operations.

## Running the Game

Open in the **Ren'Py launcher** and click "Launch Project". There is no CLI build step — Ren'Py compiles `.rpy` → `.rpyc` automatically on launch. Use the launcher's "Build Distributions" to package a release.

**IMPORTANT — rpyc files:** When renaming or moving any `.rpy` file, immediately delete the corresponding `.rpyc` file in the same directory. Stale `.rpyc` files cause confusing duplicate-declaration errors. The `.rpyc` files should not be committed to git.

## File Architecture

| File | Role |
|---|---|
| `script_main.rpy` | Character `define`s and the opening sequence (`start` → `introductions` → `gameStart`) |
| `script_room.rpy` | `wakingUp` label — bedroom scene bridging the intro chase to `introductions` |
| `script_misc.rpy` | Dead-end/game-over labels (e.g. `gameover1`) |
| `inventory.rpy` | `backpack_intro` and `inventory_button` screens; `persistent.inventory_unlocked` flag |
| `screens.rpy` | All UI screens (say, menu, prefs, save/load) and style definitions |
| `gui.rpy` | Theme values (`gui.*`) consumed by `screens.rpy` — generated file, edit carefully |
| `options.rpy` | Game config: title, version, audio channels, transitions, build settings |

New scenes/locations get their own `script_[location].rpy` file. Keep narrative files under ~800 lines; split by location or story arc when they grow larger.

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

This project contains adult content. The following tiers govern what Claude writes vs. what the user authors directly.

**Tier 1 — Claude writes freely**
Flirting, romantic tension, innuendo, kissing, undressing described tastefully, fade-to-black transitions, emotional intimacy, suggestive dialogue.

**Tier 1 Register — use this actively, not cautiously**
This is an NSFW game. Tier 1 dialogue should read pornographic in register even when it stops short of explicit acts. That means:
- Use direct sexual vocabulary when characters mean it: cock, tits, ass. Don't reach for a softer word when the blunt one is clearly what the character would say.
- Innuendo must be unmistakable. If a player could read it as innocent, it's not doing its job. The audience should always know exactly what's being implied.
- Horny characters should read as horny — not "interested," not "intrigued." Their want is the point.
- Size-difference, human/Yordle dynamics, feral/beast framing, BWC obsession — these are recurring kinks of this project. When a scene supports one, lean into it rather than around it.
- Don't soften lines after writing them. A character saying "your considerable situation" instead of "your cock" is a failure of nerve, not taste.

**Tier 2 — Claude writes with straightforward handling**
Explicit but not pornographic. Sexual situations described with clear intent — character reactions, dialogue during, emotional beats. Literary erotica register, not clinical or graphic.

**Tier 3 — User writes, Claude steps back**
Highly graphic or pornographic physical description. When a scene reaches this threshold, Claude drafts everything surrounding it (lead-up, aftermath, branching logic, stat/flag changes) and flags exactly where the user needs to fill in. Claude does not read, quote, reference, or build on content inside Tier 3 markers.

### Marker System

User-authored Tier 3 sections must be wrapped in these exact comments:

```renpy
# [EXPLICIT START]
    mc "..."
    t "..."
# [EXPLICIT END]
```

When Claude encounters these markers while reading any script file, it skips the enclosed block entirely and treats it as a black box.

### Handoff Language

When a scene escalates to Tier 3, Claude will say:

> "This is pushing past what I'll write directly. I've drafted through [X]. Author the explicit section yourself, wrap it in `# [EXPLICIT START]` / `# [EXPLICIT END]`, and I'll pick up from the aftermath."

### Hard Limits (non-negotiable regardless of tier)

- No sexual content involving minors. Any ambiguously aged character must be written and treated as an adult.
- No non-consensual scenarios framed approvingly as erotica.
