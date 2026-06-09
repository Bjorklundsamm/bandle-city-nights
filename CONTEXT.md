# CONTEXT.md — Bandle City Nights

Living document. Update this whenever a scene is completed, a TODO is resolved, or priorities shift. Claude reads this at the start of any narrative or content work session.

---

## Story Progress

### Day 1 — COMPLETE

| Label | File | Status |
|---|---|---|
| `start` | `day1/day1_intro.rpy` | ✅ Chase sequence, collapse, Kindred touch |
| `wakingUp` | `day1/day1_morning.rpy` | ✅ Bedroom wake-up, broth smell |
| `introductions` | `day1/day1_intro.rpy` | ✅ Barkeep meet, constitution reveal, gold/pack |
| `gameStart` | `day1/day1_intro.rpy` | ✅ Tristana, Poppy, Lulu formal intros; journal + inventory unlock |
| `tavern_tutorial_loop` | `day1/day1_night.rpy` | ✅ Free roam: Barkeep, Poppy, Tristana (locked in game), Vex, Katarina, Ahri, Ezreal, Nidalee/Neeko, Jinx |
| `tavern_night_end` | `day1/day1_night.rpy` | ✅ Sleep, hear sounds through wall (Katarina), fade to Day 2 |

### Day 2 — IN PROGRESS

| Label | File | Status |
|---|---|---|
| `morning_day_2` | `day2/day2_morning.rpy` | ✅ Wake-up, constitution +1, optional Katarina room peek, optional loaded dice steal |
| `day2_tavern_loop` | `day2/day2_tavern.rpy` | ✅ Barkeep (Bilgewater tip), Lulu (education arc setup), Poppy (gym mention, training offer) |
| `day2_outside_loop` | `day2/day2_outside.rpy` | ✅ Energy system introduced. Miss Fortune (loan), Fizz (explicit done). Job signs on screen. |
| Corki's Auto-Repair | `day2/day2_corki.rpy` | ✅ Pipe puzzle minigame functional (placeholder bg) |
| Rumble's Roboshop | `day2/day2_rumble.rpy` | ✅ Parts sorter minigame functional (placeholder bg) |
| Teemo's Scout Training | `day2/day2_teemo.rpy` | ✅ Timed decisions minigame functional |
| Morgana's Kitchen | `day2/day2_morgana.rpy` | ✅ Recipe memory minigame functional |
| Ezreal's Target Practice | `day2/day2_ezreal.rpy` | ✅ Click targets minigame functional (placeholder target art) |
| Day 2 night | — | ❌ NOT WRITTEN — `day2_outside_loop` ends with a `return`, no night tavern or sleep yet |
| Hot Springs | `day2/day2_outside.rpy` | ❌ PLACEHOLDER only |
| Deep Woods | `day2/day2_outside.rpy` | ❌ PLACEHOLDER — locked behind `constitution < 10`; Kindred encounter not written |
| Impish Delight interior | `day2/day2_outside.rpy` | ❌ PLACEHOLDER — bg art needed |

### Day 3+ — NOT STARTED

---

## Character Arc Status

| Character | Met | Scene 1 | Explicit | Notes |
|---|---|---|---|---|
| **Barkeep** | ✅ Day 1 | — | — | Floating Yordle; shifting markings hint at Kindred connection. Arc not started. |
| **Tristana** | ✅ Day 1 | ❌ | ❌ | Saved the player. Losing at Katarina's dice game night 1. scenes 1-3 and explicit flagged in defines. |
| **Poppy** | ✅ Day 1 | ❌ | ❌ | Bouncer, gym arc hinted Day 2 (training offer). armwrestle, gym arc, Orlon story all flagged. |
| **Lulu** | ✅ Day 1 | ✅ Day 2 setup | ❌ | Day 2 tavern: directly propositions player for "educational" session on Poppy's next day off. `lulu_in_tavern = False` after. |
| **Vex** | ✅ Day 1 | ❌ | ❌ | 5 journal pages collectible unlock ultimate route. Scene 1 not written. |
| **Katarina** | ✅ Day 1 | ❌ | ❌ | Loaded dice can be stolen Day 2 morning. Explicit not written. |
| **Ahri** | ✅ Day 1 | ❌ | ❌ | Gated behind "Yordle essence" threshold (`ahri_available`). Scene 1 not written. |
| **Ezreal** | ✅ Day 1 | ❌ | ❌ | Shower scene unlockable via hard mode target practice. Explicit not written. |
| **Neeko** | ✅ Day 1 | ❌ | ❌ | Paired with Nidalee. `neeko_shoma_done` / `neeko_trust_done` arc flags. |
| **Nidalee** | ✅ Day 1 | ❌ | ❌ | Territorial intro. `nidalee_confronted` flag. |
| **Jinx** | ✅ Day 1 | ❌ | ❌ | Gated behind max Tristana affection (`jinx_gate_done`). |
| **Fizz** | ✅ Day 2 | ✅ | ✅ | Explicit done. Aftermath written (`day2_fizz_aftermath`). "Free use" offer standing. `sc fizz pre fellatio.png` asset exists. |
| **Miss Fortune** | ✅ Day 2 | ✅ (loan) | ❌ | Scenes 2-4 flagged. Scene 2 = pistol return. Scene 3 = titjob (Tier 2). Scene 4 = room (Tier 3). |
| **Morgana** | minigame only | ❌ | ❌ | `met_morgana` still False in defaults — no narrative intro written yet. |
| **Corki** | minigame only | ❌ | ❌ | No narrative intro written. |
| **Rumble** | minigame only | ❌ | ❌ | No narrative intro written. |
| **Teemo** | minigame only | ❌ | ❌ | No narrative intro written. |
| **Kindred** | referenced only | ❌ | ❌ | Deep Woods encounter gated behind constitution ≥ 10. |
| **Lilia** | defined only | ❌ | ❌ | Not introduced yet. |

---

## NSFW Content Workflow

### Tier Summary

| Tier | What it covers | Who writes it |
|---|---|---|
| 1 | Flirting, innuendo, undressing, fade-to-black, suggestive dialogue | Claude — freely, in pornographic register |
| 2 | Explicit but literary — reactions, emotional beats, clear intent | Claude — straightforward |
| 3 | Highly graphic / pornographic | Xialong (NovelAI) via `novelai_gen.py` |

**Tier 1 register note:** Use direct vocabulary (cock, tits, ass). Innuendo must be unmistakable. Recurring kinks — size difference, human/Yordle dynamics, BWC obsession — lean into them when the scene supports it.

### Calling novelai_gen.py (Tier 3)

```bash
python tools/novelai_gen.py \
  --file game/narrative/day2/day2_fizz.rpy \
  --char fizz \
  --explicit \
  --scene-note "USER_DIRECTION_HERE" \
  --segments 4 \
  --regen
```

Key flags:
- `--file` — the `.rpy` file containing the `# [GEN START]` marker
- `--char` — character shortcode (matches entry in `tools/tag_reference.json`)
- `--explicit` — activates Tier 3 generation; also sets appropriate NovelAI preset
- `--scene-note` — the explicit scene direction the user provides (what act, dynamic, beats)
- `--segments N` — number of generation passes to stitch together
- `--regen` — regenerate if prior output exists at that marker
- `--rewrite X Y` — rewrite lines X through Y (Tier 1/2 only)
- `--rewrite-note "reason"` — guidance for the rewrite pass

### File markers

```renpy
# [GEN START]              ← novelai_gen.py inserts generated content here
# [SCENE NOTE: ...]        ← one-line in-file context (overrides --scene-note if present)
# [EXPLICIT START]         ← Claude stops reading here
# [EXPLICIT END]           ← Claude resumes here
```

Claude never reads, quotes, or builds on content between `# [EXPLICIT START]` and `# [EXPLICIT END]`.

### Screen overlay assets (sc/ prefix)

`game/images/sc/` holds full-frame overlay images shown during or around explicit scenes. Naming: `sc [character] [moment description].png`. These are shown with `show screen` or `add` during narration beats that bracket the explicit block — not inside it.

Current assets: `sc fizz pre fellatio.png`

### Xialong handoff protocol

When a Tier 3 scene is reached, say:

> "This is an explicit scene — I'll let Xialong write it. Describe what happens (the act, the dynamic, how it ends). I'll handle everything else in the author's note and make the API call."

Then populate the non-explicit author's note fields from character JSON and call `novelai_gen.py` as above.

---

## Next Work Items (Priority Order)

1. **Day 2 night scene** — The `day2_outside_loop` currently dead-ends with `return`. Need: energy hits 0 or player chooses to go in → evening tavern loop (night cast) → sleep → Day 3 card. This is the primary blocker for any Day 3 work.

2. **Lulu arc — Poppy off-duty scene** — Lulu has propositioned the player (Day 2 tavern). Write the scene that fires when `poppy_off_duty = True`: player finds Lulu, she delivers on her promise. Tier 3 handoff needed for the explicit block. Scaffold the whole arc file `day_lulu_arc.rpy`.

3. **Miss Fortune scene 2 — pistol return** — MF returns to town after her trade run. Write the reunion: she pays back the 250g, the scene where she's grateful. Sets up scenes 3 and 4. Goes in `day_mf_arc.rpy` (new file).

4. **Day 2 minigame narrative intros** — The minigame bosses (Corki, Rumble, Teemo, Morgana) are encountered purely as mechanics. Each needs a short first-meeting dialogue scene (10-15 lines) before the minigame screen fires. These set `met_*` flags.

5. **Katarina scene 1** — First real conversation with Katarina after the tutorial night. She's won Tristana's money; Tristana has a debt to collect on. Runs sometime Day 2-3. Sets up the explicit arc.

6. **Poppy gym arc** — Day 2 Poppy offered to train the player "when you're not falling apart." Write the first gym session (sparring, arm-wrestling). Sets `poppy_armwrestle_done`. No explicit yet.

7. **Hot Springs** — `loc_hot_springs` is a stub. Background art exists (`bg hot springs.png`). Build a relaxation scene; likely a first meeting with Lilia or a quiet character moment (Vex? Ahri?).

8. **Ezreal shower scene** — Unlocked by hard mode target practice (`persistent.ezreal_shower_unlocked`). Tier 2 content. Needs `day_ezreal_arc.rpy`.

9. **Impish Delight interior** — `loc_impish_delight` is a stub. Need bg art and a purpose for the space (could be Barkeep's private office / the night tavern when the main room clears out).

10. **Kindred / Deep Woods** — Long-term. Gated behind constitution ≥ 10. The mechanic exists; the scene needs writing. This is the "true arc" payoff of the constitution system.
