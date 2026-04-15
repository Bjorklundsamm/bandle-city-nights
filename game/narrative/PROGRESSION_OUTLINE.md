# Bandle City Nights — Progression Outline

## Stat System

### Stats and Maximums
| Stat | Max | Notes |
|---|---|---|
| Constitution | 50 | Displayed as 10 hearts × 5 sections; HP-adjacent, recovery through intimacy |
| Strength | 50 | Physical aptitude; arm wrestling, training, combat impressiveness |
| Charisma | 50 | Social persuasion, reading people, making scenes go your way |
| Intellect | 50 | Puzzle-solving, arcane sensitivity, reading the situation |

### Energy
- Resets to **3** every morning.
- Each job costs 1 energy. Free social interactions (tavern chat) cost nothing.
- When energy = 0, job buttons are greyed out ("You're running on fumes.").

### Gold
- `persistent.gold` — persists across saves.
- Used for: buying drinks (Barkeep affection), MF loan repayment, future items.

---

## Stat Budget Per Day (Design Target)

The game runs 31 days. Target caps for a player who does every available job each day:

| Day Range | Days | Jobs/Day | Approx Stat Gain / Day | Cumulative STR | Cumulative CHA | Cumulative INT |
|---|---|---|---|---|---|---|
| Days 1–2 | 2 | 0 (intro/story) | 0 | 1 | 1 | 1 |
| Days 3–7 | 5 | 3 | ~6 | ~16 | ~11 | ~11 |
| Days 8–14 | 7 | 3 | ~7 | ~35 | ~22 | ~27 |
| Days 15–21 | 7 | 3 | ~9 (hard modes available) | ~42 | ~35 | ~38 |
| Days 22–31 | 10 | 3 | ~9 | 50 | 50 | 50 |

**Key design rule:** No stat should hit 50 before Day 22 through jobs alone. Story beats and character intimacy bonuses can push individual stats over this schedule.

**Soft caps:** Several scenes gate on stats in the 25–40 range, reachable by mid-game only if the player has been consistent.

---

## Minigame Availability & Hard Mode Unlock

All five jobs become available **Day 3**. Hard mode unlocks after the player passes normal mode on that job for the **first time** (one-time unlock, permanent).

| Job | Location | Normal Clear Threshold | Hard Unlock Trigger | Hard Mode Reward |
|---|---|---|---|---|
| Corki's Auto-Repair | Corki's shop | Solve the pipe grid | Normal mode pass | +1 bonus STR & CHA on clears |
| Rumble's Robo-Workshop | Rumble's workshop | Sort 10+ parts | Sort 20+ parts | +1 bonus to all stats on clears |
| Morgana's Kitchen | Morgana's kitchen | Full sequence correct | Normal mode pass | Morgana handjob scene (Tier 2) |
| Teemo's Scout Training | Bandlewood trail | Finish within time limit | Normal mode pass | +1 bonus STR & INT on clears |
| Ezreal's Target Practice | Rooftop range | 50%+ accuracy | 80%+ accuracy | Ezreal shower invitation (Tier 2) |

---

## Stat Rewards by Job Mode

### Normal Mode
| Job | STR | CHA | INT | Gold |
|---|---|---|---|---|
| Corki (success) | +2 | +1 | 0 | +50g |
| Corki (fail) | +1 | 0 | 0 | 0 |
| Rumble (20+ parts) | +2 | +2 | +2 | +50g |
| Rumble (10–19 parts) | +1 | +1 | +1 | +50g |
| Rumble (<10 parts) | 0 | 0 | +1 | +25g |
| Morgana (pass) | 0 | 0 | +2 | +100g |
| Morgana (fail) | 0 | 0 | +1 | 0 |
| Teemo (clear) | +3 | 0 | +2 | 0 |
| Teemo (partial) | +1 | 0 | +1 | 0 |
| Ezreal (80%+) | +5 | 0 | 0 | 0 |
| Ezreal (50–79%) | +3 | 0 | 0 | 0 |
| Ezreal (<50%) | +1 | 0 | 0 | 0 |

### Hard Mode (additional on top of normal rewards)
| Job | Bonus STR | Bonus CHA | Bonus INT | Gold | Special |
|---|---|---|---|---|---|
| Corki hard (success) | +1 | +1 | 0 | +25g | — |
| Rumble hard (20+) | +1 | +1 | +1 | +25g | — |
| Morgana hard (pass) | 0 | 0 | +2 | +50g | Triggers reward scene |
| Teemo hard (clear) | +1 | 0 | +1 | 0 | — |
| Ezreal hard (80%+) | +2 | 0 | 0 | 0 | Triggers shower invite |

---

## Hard Mode Differences

### Corki Hard Mode
- Grid is 7×7 instead of 5×5.
- T-junction pipe pieces added.
- Two paths must connect simultaneously (START → END1 and START → END2).
- Rumble also present, critiquing Corki's pipe layout.

### Rumble Hard Mode
- Chaos threshold drops from 8 to 5 loose parts.
- A fifth bin added: Capacitors.
- Spawn rate is 20% faster from the start.
- Mixed/similar-looking parts (bolts vs. capacitors) appear.

### Morgana Hard Mode
- Sequence length starts at 6 (instead of 4), caps at 10.
- Zero corrections allowed — one wrong tap resets the round.
- Two ingredient icons look similar (herb bundle vs. dried herb).
- Morgana gives no hints; she simply watches.

### Teemo Hard Mode
- Starting time reduced from 10 to 7.
- Two decision points have *three* options instead of two; only one is correct.
- One trap decision looks correct but subtracts 4 time instead of adding 2.
- Teemo does not react until the end.

### Ezreal Hard Mode
- 15 targets instead of 10.
- Targets shrink in 1.0 seconds instead of 1.5.
- Three targets per round are "fakes" (decoys) — clicking them subtracts one from hit count.
- Ezreal trash-talk escalates; if player hits 12+ he goes silent for the rest.

---

## Sexual Scene Stat Gates

Unless otherwise noted with a special unlock marker, **every sexual escalation trigger has a stat prerequisite**. Stats must be at or above threshold at the moment the scene is attempted.

Characters are listed with their gate conditions. "Affection" values refer to `affection_[character]` variables (current max: 10).

### Fizz
| Scene | Gate |
|---|---|
| Day 2 proposition (normal) | No gate — happens automatically on meet |
| Fizz wants to be held (soft emotional beat) | affection_fizz ≥ 3 |

### Tristana
| Scene | Gate |
|---|---|
| Aggressive tavern flirtation (Tier 1) | No gate |
| Drunk confession / trust beat (Tier 1–2) | affection_tristana ≥ 3, CHA ≥ 10 |
| Katarina debt reveal / emotional crack (Tier 1–2) | affection_tristana ≥ 5 |
| Katarina arc resolution — explicit (Tier 3) | affection_tristana ≥ 7, CHA ≥ 20 |

### Poppy
| Scene | Gate |
|---|---|
| Arm wrestling challenge available | **STR ≥ 20** |
| Win arm wrestling (STR check vs. Poppy's 30) | STR ≥ 30 |
| Gym invite / first form corrections | Win arm wrestling |
| Orlon disclosure (Tier 1) | affection_poppy ≥ 3 |
| Hammer disclosure / emotional turning point (Tier 1–2) | affection_poppy ≥ 5 |
| "Stay after the gym" — explicit (Tier 3) | affection_poppy ≥ 8, STR ≥ 35 |

### Lulu
| Scene | Gate |
|---|---|
| Pix-watching conversation available | Poppy absent from tavern (checked via `poppy_off_duty` flag), affection_lulu ≥ 2 |
| First physical intimacy (Tier 1–2) | Poppy absent, affection_lulu ≥ 4 |
| Arc deepens — explicit (Tier 3) | Poppy absent, affection_lulu ≥ 7, **INT ≥ 15** (she responds to curiosity-as-comprehension) |
| **Permanent block:** | If player has been intimate with Lulu, Ahri arc is permanently closed |

### Katarina
| Scene | Gate |
|---|---|
| First real conversation (Tier 1) | CHA ≥ 8 |
| Tension/danger beat (Tier 1–2) | affection_katarina ≥ 3, CHA ≥ 15 |
| Explicit encounter (Tier 3) | affection_katarina ≥ 6, CHA ≥ 25 — OR — Tristana arc at max (Katarina leverage scene) |

### Vex
| Scene | Gate |
|---|---|
| First real conversation past hostility | INT ≥ 8 |
| Emotional crack / genuine moment (Tier 1–2) | affection_vex ≥ 3, INT ≥ 18 |
| Explicit (Tier 3) | affection_vex ≥ 6, INT ≥ 28 |

### Ahri
| Scene | Gate |
|---|---|
| First encounter — deferral | No gate (she defers regardless) |
| Re-approach with changed essence (Tier 1–2) | **Must have been intimate with Tristana + Vex + Poppy** (3 Yordle-essence layers); STR ≥ 30, INT ≥ 30 |
| Explicit (Tier 3) | Above + affection_ahri ≥ 5 |
| **Permanent block:** | If Lulu arc is active/complete, Ahri is permanently unavailable |

### Neeko
| Scene | Gate |
|---|---|
| Sho'ma reading / first real attention | affection_neeko ≥ 2 |
| Nidalee-collision handling earns trust (Tier 1–2) | affection_neeko ≥ 4, CHA ≥ 15 |
| Nidalee-absent night — explicit (Tier 3) | affection_neeko ≥ 6, CHA ≥ 20, INT ≥ 20 |

### Nidalee
| Scene | Gate |
|---|---|
| First confrontation (territorial evaluation) | Must have been intimate with Neeko |
| Not-flinching re-evaluation (Tier 2) | STR ≥ 35, affection_nidalee ≥ 2 (earned through not fleeing) |
| Explicit claiming (Tier 3) | STR ≥ 40, affection_nidalee ≥ 4 |

### Ezreal
| Scene | Gate |
|---|---|
| Training session available | STR ≥ 15, met_ezreal = True |
| Post-shower scene available (Tier 2) | **ezreal_hard_unlocked = True** (hard mode pass), STR ≥ 30 |
| Second session — negotiated encounter (Tier 2–3) | First shower scene complete, STR ≥ 35, affection_ezreal ≥ 4 |

### Morgana (Kitchen)
| Scene | Gate |
|---|---|
| Kitchen job available | met_morgana = True (Day 3+) |
| Hard mode kitchen scene — handjob (Tier 2) | **morgana_hard_unlocked = True** (hard mode pass), INT ≥ 25 |
| Deeper Morgana arc (Tier 2–3, if extended) | morgana_reward_seen = True, affection_morgana ≥ 5, INT ≥ 35 |

### Jinx
| Scene | Gate |
|---|---|
| All Jinx arcs | Requires **Tristana romance at max** (affection_tristana ≥ 10) |
| Gate conversation (Tier 1) | affection_tristana ≥ 10 |
| Threesome proposal (Tier 3) | affection_tristana ≥ 10, affection_jinx ≥ 4, CHA ≥ 30 |

### Midna (Barkeep)
| Scene | Gate |
|---|---|
| True identity arc begins | INT ≥ 20, affection_barkeep ≥ 5 |
| Romance lock — true form reveal | Evidence puzzle complete, INT ≥ 35, affection_barkeep ≥ 8 |

### Miss Fortune
| Scene | Gate |
|---|---|
| Flirtation / loan negotiation (Tier 1) | CHA ≥ 12 |
| Deeper arc (Tier 1–2) | Loan repaid, affection_miss_fortune ≥ 4, CHA ≥ 25 |

---

## Corki, Rumble, Teemo — No Sexual Content

These three characters have no sexual escalation arc. Their hard mode rewards are **purely mechanical**:

- **Corki hard mode**: +1 STR/CHA bonus; Corki gives you a component you can trade (future item system).
- **Rumble hard mode**: +1 all stats bonus; Rumble builds you a small gadget (future item). He never fully faces you or acknowledges it directly.
- **Teemo hard mode**: +1 STR/INT bonus; Teemo gives you a scout badge and a single line of genuine approval. He resumes being smug immediately.

---

## Day Unlocks (Recommended Schedule)

| Day | Unlock |
|---|---|
| 1 | Intro, character meets, constitution HUD, inventory, journal |
| 2 | Outside hub, Miss Fortune, Fizz encounter, loaded dice |
| 3 | All 5 jobs open, energy system active, gold system active |
| 5 | First hard mode potentially reachable (Morgana/Teemo easiest) |
| 7 | Poppy arm wrestling threshold reachable (STR ≥ 20) |
| 10 | Ahri first deferral encounter, Katarina first real scene gate (CHA ≥ 8) |
| 14 | Poppy win threshold reachable (STR ≥ 30) |
| 18 | Lulu arc gate reachable (affection ≥ 4 + Poppy off-duty) |
| 20 | Ezreal shower scene potentially reachable (hard mode + STR ≥ 30) |
| 22 | Neeko explicit arc gate reachable |
| 25 | Ahri re-approach reachable (3 Yordle layers + stat gates) |
| 28 | Nidalee explicit arc reachable (STR ≥ 40) |
| 31 | End state |
