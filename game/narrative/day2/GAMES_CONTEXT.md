# Day 2 Minigames — Design Context

This file is a handoff document. It captures the fully designed minigame concepts
for the five daytime jobs available from Day 2 onward. Build from this, not from
conversation memory.

---

## System Overview

### Energy
- `persistent.energy` resets to **3** at the start of each day.
- Each job/activity costs **1 energy**.
- Free NPC conversations (tavern hub, street chat) cost nothing.
- When energy hits 0, the activity hub options are greyed out and the player is
  nudged toward wrapping up the day.

### Gold
- `persistent.gold` — tracks across saves.
- Some jobs pay gold in addition to stats.

### Stats (all `persistent.*`)
- `persistent.strength`
- `persistent.charisma`
- `persistent.intellect`
- `persistent.constitution` — already implemented; see CLAUDE.md

### Stat Gain Philosophy
Jobs that pay gold offer moderate stat gains.
Jobs with no gold pay offer higher stat gains — pure grind rewards more.

---

## The Five Jobs

### 1. Corki's Auto-Repair
**Location:** Corki's shop (new label + bg asset needed)
**Character:** Corki
**Stat rewards:**
- Success: +2 STR, +1 CHA, +50g
**Minigame: Pipe Puzzle**

A grid of pipe segments randomly rotated on load. Tile types:
- Straight pipe (one asset: `bt pipe straight.png`)
- Corner pipe (one asset: `bt pipe corner.png`)

Player clicks a tile to rotate it 90° clockwise. Goal: form a continuous connected
path from the START node (left edge) to the END node (right edge).

When the path is complete, animate a glow/flow effect through the connected tiles
and play a success sound.

**Ren'Py implementation notes:**
- Grid of `imagebutton`s, each tracking rotation state (0/90/180/270) in a Python list.
- On click: increment rotation mod 4, redraw.
- Connectivity check: Python function traces open pipe ends tile-to-tile from start node.
  Each tile type has a direction map per rotation (e.g. straight at 0° = left+right open,
  at 90° = up+down open). Trace until you reach the end node or hit a dead end.
- On solve: play sound, show system_overlay reward, return.

**Assets needed:**
- `bt pipe straight.png`
- `bt pipe corner.png`
- (Optional) `bt pipe t junction.png` for harder grids later

---

### 2. Rumble's Robo-Workshop
**Location:** Rumble's workshop (new label + bg asset needed)
**Character:** Rumble — sprite sits to one side, back mostly turned, absorbed in building.
  He never fully faces you. Too busy.
**Stat rewards:**
- 20+ parts sorted: +2 STR, +2 CHA, +2 INT, +50g
- 10–19 parts sorted: +1 STR, +1 CHA, +1 INT, +50g
- Under 10 parts sorted: +1 INT, +25g (INT always awarded — you learned something)

**Minigame: Parts Sorter (Chaos Mode)**

Rumble is building so fast that components are flying off his workbench in every
direction. The player's job is to sort them into four labeled bins before the
workshop hits critical mess.

**The chaos mechanic:**
- Parts spawn at random screen positions with a tumbling/arcing spawn animation.
- Once on screen, parts slowly drift or settle — they don't disappear on their own.
- A counter tracks simultaneous loose parts on screen.
- **Threshold: 8 loose parts = workshop overwhelmed.** Rumble stops. Game ends.
- Parts keep spawning throughout regardless of player speed.
- Spawn rate ramps up as player clears more — Rumble reads competence as a
  signal to go faster.

**The sorting mechanic:**
- Four bins sit along the bottom of the screen, always visible, always labeled.
- Player drags a part to any bin — it attempts to snap.
- **Correct bin:** snaps and disappears with a click sound.
- **Wrong bin:** bounces back to approximately where it came from. Still on screen.
  Still counts toward the chaos meter.
- Rumble reacts via dialogue to: hitting half the chaos meter, a personal best,
  the moment he realizes the player is actually keeping up.

**The four part types (one icon each):**
- Bolt → Bolts bin
- Gear → Gears bin
- Wire coil → Wires bin
- Metal plate → Plates bin

**Ren'Py implementation notes:**
- Use Ren'Py's native `Drag` and `DragGroup` system.
- Each spawned part is a `Drag` with a tag matching its type.
- Each bin is a `Drag` acting as a drop target, tagged with its accepted type.
- On drop: compare dragged tag to target tag. Match → remove from DragGroup, 
  increment sorted counter. No match → snap back.
- Chaos counter = len(active parts in DragGroup). Check after each spawn.
- Spawn timer: use `renpy.invoke_in_thread` or a loop with `renpy.pause` between spawns.
  Simpler alternative: spawn on a beat tied to Rumble dialogue triggers.

**Assets needed:**
- `bt rumble bolt.png`
- `bt rumble gear.png`
- `bt rumble wire.png`
- `bt rumble plate.png`
- Four bin images (can be a crate silhouette + text label, very simple)

---

### 3. Morgana's Kitchen
**Location:** Morgana's kitchen (new label + bg asset needed)
**Character:** Morgana — precise, exacting, slightly cold. Expects failure.
  Mildly interested when you don't.
**Stat rewards:**
- Success: +2 INT, +100g
**Minigame: Recipe Memory**

Morgana presents a recipe — a sequence of ingredients shown one at a time with
icon + name. Then they disappear and the player reconstructs the sequence from
a shuffled pool of ingredient buttons.

**Phase 1 — Memorize:**
Ingredients appear one at a time in sequence. Each shows for ~1.5 seconds.
No interaction, just watch.

**Phase 2 — Repeat:**
All ingredient icons appear shuffled as buttons. Player taps them in the order
they were shown. Correct tap highlights green. Wrong tap highlights red — Morgana
gives one correction, then the round resets. Full sequence correct = pass.

Sequence length increases with each successful visit (starts at 4, caps at 8).

**Assets needed:**
- Simple ingredient icons (think RPG inventory style, very small):
  - Carrot
  - Onion
  - Mushroom
  - Herb bundle
  - Fish
  - Salt jar
  - (Add more as recipe variety expands)

**Ren'Py implementation notes:**
- Store the recipe sequence as a Python list, shuffled from a pool.
- Display phase: iterate list, `renpy.pause(1.5)` per item, show/hide imagebutton.
- Input phase: render shuffled buttons. On click, compare to `expected_sequence[current_index]`.
  Match: advance index, highlight green. No match: highlight red, Morgana reacts, reset.
- Track visit count in `persistent.morgana_visits` to scale sequence length.

---

### 4. Teemo's Scout Training
**Location:** Bandlewood edge / scout trail (new bg asset needed)
**Character:** Teemo — earnest, demanding, slightly smug when you fail.
**Stat rewards:**
- Clear within time: +3 STR, +2 INT
- Partial clear: +1 STR, +1 INT
**Minigame: Timed Branching Decisions**

Fully narrative — no custom UI. Teemo runs you through a scouting route in the
Bandlewood. At each fork you choose between two options. Correct choices (Teemo's
scout doctrine) add time back to the clock. Wrong choices eat time. Run out of
time = partial reward only.

This is Ren'Py's native menu system with a timer variable checked between beats.
No assets needed beyond the bg. The "minigame" is entirely in the writing.

**Implementation notes:**
- Track `scout_time` as an integer (e.g. starts at 10).
- Each correct menu choice: `$ scout_time += 2`
- Each wrong menu choice: `$ scout_time -= 3`
- Check `if scout_time <= 0` after each beat — if so, jump to fail branch.
- Full route has ~6 decision points. Clear all 6 in time = full reward.

**Assets needed:**
- None beyond a Bandlewood exterior bg (may already exist or be placeholdered)

---

### 5. Ezreal's Target Practice
**Location:** Outdoor range / rooftop (new bg asset needed)
**Character:** Ezreal — trash-talks throughout. Stops talking if you bullseye 5+
  in a row. The silence means he's impressed.
**Stat rewards:**
- 80%+ accuracy: +5 STR
- 50–79% accuracy: +3 STR
- Under 50%: +1 STR
**Minigame: Click Targets**

Targets (circular, bullseye-style) appear at random screen positions and shrink
over ~1.5 seconds before disappearing. Player clicks as fast and accurately as
possible over a run of 10 targets.

**Scoring:**
- Click center ring = bullseye (full points)
- Click outer ring = hit (half points)
- Miss / target expires = 0
- Track bullseye streak for Ezreal's silence trigger.

**Ren'Py implementation notes:**
- Each target is an `imagebutton` added to the screen at a random (x, y).
- Target shrinks via ATL: `linear 1.5 zoom 0.1` then hides.
- On click: measure distance from center to determine ring hit. Award points.
- After 10 targets: calculate accuracy percentage, jump to appropriate reward label.
- Ezreal's commentary is triggered by events: first miss, first bullseye, 5-streak,
  final score.

**Assets needed:**
- Target image with distinct center ring and outer ring (one asset, two hit zones
  determined by click distance from center)

---

## Activity Hub Integration

These five jobs are accessible from a **town map** or extended outside hub.
Current `day2_outside_loop` has MF and Fizz — the jobs district is a separate
area or an expanded version of the same street screen.

Each job option in the hub should display remaining energy (out of 3) so the
player can plan. When energy = 0, job buttons are greyed out with a "Too tired"
tooltip.

Job availability on Day 2: all five are open. Future gating (e.g. must meet Corki
before his shop appears) is a later addition — don't implement flags for it yet.

---

## Open Questions (not yet decided)

1. **Gold variable:** `persistent.gold` vs session-only `default gold` — leaning
   persistent but not confirmed.
2. **Energy display:** in the HUD alongside constitution, or system_overlay only?
3. **Town map screen:** new screen or extend day2_outside_hub?
4. **Constitution recovery:** tied to NPC interactions, not hotsprings. Details TBD.
   Current thinking: Lulu (free, just talking), Barkeep (meal/drink, costs 20g),
   Fizz (on accept), Poppy date.
