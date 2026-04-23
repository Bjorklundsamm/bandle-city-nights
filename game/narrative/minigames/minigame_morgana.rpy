# minigames/minigame_morgana.rpy
# Morgana's Kitchen — Recipe Memory
#
# Ingredients: Carrot, Onion, Mushroom, Garlic, Berries (5 total).
# Look-alike pairs for hard mode: Carrot/Garlic, Mushroom/Berries.
#
# Normal mode: sequence 4–5 items, one correction allowed per round.
# Hard mode:   sequence always 5 items, zero corrections.
#
# Rewards
#   Normal pass:   +2 INT, +100g
#   Normal fail:   +1 INT
#   Hard pass:     +4 INT, +150g  → triggers morgana_reward_scene
#   Hard fail:     +1 INT
#
# Hard mode unlocked: persistent.morgana_hard_unlocked after first normal pass.
# Special: morgana_hard_unlocked = True + INT >= 25 → reward scene available.

init python:

    MORGANA_INGREDIENTS_NORMAL = [
        "Carrot", "Onion", "Mushroom", "Garlic", "Berries",
    ]

    # Hard mode — same pool; look-alike pairs (Carrot/Garlic, Mushroom/Berries) are the difficulty
    MORGANA_INGREDIENTS_HARD = [
        "Carrot", "Onion", "Mushroom", "Garlic", "Berries",
    ]

    MORGANA_INGREDIENT_IMAGES = {
        "Carrot":   "bt carrots.png",
        "Onion":    "bt onion.png",
        "Mushroom": "bt mushrooms.png",
        "Garlic":   "bt garlic.png",
        "Berries":  "bt berries.png",
    }

    def morgana_seq_length(visits, hard_mode=False):
        base = 4 if hard_mode else 3
        cap  = 5
        return min(base + visits, cap)

    def morgana_make_sequence(visits, hard_mode=False):
        import random
        pool = MORGANA_INGREDIENTS_HARD if hard_mode else MORGANA_INGREDIENTS_NORMAL
        length = morgana_seq_length(visits, hard_mode)
        return random.sample(pool, min(length, len(pool)))


screen morgana_memorize(sequence, current_index):
    frame:
        xalign 0.5
        yalign 0.35
        padding (20, 16)
        vbox:
            spacing 12
            text "Remember the order:" xalign 0.5 style "morgana_label"
            hbox:
                xalign 0.5
                spacing 8
                for i, ing in enumerate(sequence):
                    frame:
                        padding (8, 8)
                        if i == current_index:
                            background "#6a3090"
                        else:
                            background "#2a1040"
                        vbox:
                            add MORGANA_INGREDIENT_IMAGES[ing]:
                                xsize 64
                                ysize 64
                                xalign 0.5
                            text ing xalign 0.5 style "morgana_ingredient_label"


screen morgana_input(shuffled, entered, sequence, mistakes):
    frame:
        xalign 0.5
        yalign 0.35
        padding (20, 16)
        vbox:
            spacing 12
            text "Reconstruct the sequence:" xalign 0.5 style "morgana_label"

            # Progress slots
            hbox:
                xalign 0.5
                spacing 6
                for i in range(len(sequence)):
                    frame:
                        xsize 72
                        ysize 72
                        padding (4, 4)
                        background ("#2a5020" if i < len(entered) else "#2a1040")
                        if i < len(entered):
                            text entered[i]:
                                xalign 0.5
                                yalign 0.5
                                style "morgana_ingredient_label"

            # Input buttons
            hbox:
                xalign 0.5
                spacing 10
                for ing in shuffled:
                    if ing not in entered:
                        imagebutton:
                            idle  MORGANA_INGREDIENT_IMAGES[ing]
                            hover MORGANA_INGREDIENT_IMAGES[ing]
                            action Function(morgana_tap, ing)
                            xsize 64
                            ysize 64

style morgana_label:
    color "#c890f0"
    size 22
    bold True

style morgana_ingredient_label:
    color "#e0d0ff"
    size 14


## ── Labels ────────────────────────────────────────────────────────────────────

label morgana_job:
    $ energy -= 1
    $ persistent.morgana_visits += 1

    scene bg tavern kitchen
    show ch morgana kitchen position

    if persistent.morgana_visits == 1:
        mo "You. The human. I need someone to follow a recipe."
        mo "Don't speak. Don't improvise. Watch, then repeat."
    else:
        mo "Back again. Good. Today's sequence is longer."

    $ _mo_seq = morgana_make_sequence(persistent.morgana_visits, hard_mode=False)
    $ _mo_shuffled = list(_mo_seq)
    python:
        import random
        random.shuffle(_mo_shuffled)

    # Phase 1 — Memorize
    n "Watch carefully. Each ingredient appears once."
    $ _mo_idx = 0
    while _mo_idx < len(_mo_seq):
        show screen morgana_memorize(_mo_seq, _mo_idx)
        $ renpy.pause(1.5)
        $ _mo_idx += 1
    hide screen morgana_memorize

    $ renpy.pause(0.3)
    mo "Now. Reconstruct it."

    # Phase 2 — Input
    $ _mo_entered = []
    $ _mo_mistakes = 0
    $ _mo_passed = False
    $ _mo_reset = False

    while len(_mo_entered) < len(_mo_seq) and not _mo_reset:
        call screen morgana_input(_mo_shuffled, _mo_entered, _mo_seq, _mo_mistakes)
        if defined("_mo_tap_result"):
            if _mo_tap_result == "correct":
                $ _mo_entered.append(_mo_last_tap)
                if len(_mo_entered) == len(_mo_seq):
                    $ _mo_passed = True
            elif _mo_tap_result == "wrong":
                $ _mo_mistakes += 1
                show ch morgana profile default
                mo "Wrong."
                show ch morgana kitchen position
                if _mo_mistakes >= 1:
                    # Normal mode: one correction allowed then reset
                    $ _mo_reset = True

    if _mo_passed:
        jump morgana_success
    else:
        jump morgana_fail

label morgana_job_hard:
    $ energy -= 1
    $ persistent.morgana_visits += 1

    scene bg tavern kitchen
    show ch morgana kitchen position

    mo "You've survived this kitchen. Now let's see if you can actually think."
    mo "Longer sequence. No corrections. One wrong answer and we start over."

    $ _mo_seq = morgana_make_sequence(persistent.morgana_visits, hard_mode=True)
    $ _mo_shuffled = list(_mo_seq)
    python:
        import random
        random.shuffle(_mo_shuffled)

    n "Memorize carefully. Garlic and carrot look similar. So do mushroom and berries."
    $ _mo_idx = 0
    while _mo_idx < len(_mo_seq):
        show screen morgana_memorize(_mo_seq, _mo_idx)
        $ renpy.pause(1.5)
        $ _mo_idx += 1
    hide screen morgana_memorize

    $ renpy.pause(0.3)
    mo "Begin."

    $ _mo_entered = []
    $ _mo_mistakes = 0
    $ _mo_passed = False
    $ _mo_reset = False

    while len(_mo_entered) < len(_mo_seq) and not _mo_reset:
        call screen morgana_input(_mo_shuffled, _mo_entered, _mo_seq, _mo_mistakes)
        if defined("_mo_tap_result"):
            if _mo_tap_result == "correct":
                $ _mo_entered.append(_mo_last_tap)
                if len(_mo_entered) == len(_mo_seq):
                    $ _mo_passed = True
            elif _mo_tap_result == "wrong":
                # Hard mode: zero corrections
                show ch morgana profile default
                mo "No."
                $ _mo_reset = True

    if _mo_passed:
        jump morgana_hard_success
    else:
        jump morgana_hard_fail

label morgana_success:
    show ch morgana kitchen position
    mo "Correct. All of it."
    mo "..."
    mo "You may come back tomorrow."
    $ intellect += 2
    $ gold      += 100
    $ persistent.morgana_hard_unlocked = True
    show screen system_overlay
    s "Intellect +2. [100]g earned."
    hide screen system_overlay
    return

label morgana_fail:
    show ch morgana kitchen position
    mo "Wrong. At least you tried to pay attention."
    $ intellect += 1
    show screen system_overlay
    s "Intellect +1."
    hide screen system_overlay
    return

label morgana_hard_success:
    show ch morgana kitchen position
    mo "..."
    mo "Flawless. Every item, correct order."
    n "She sets the ladle down and looks at you — really looks at you — for the first time."
    mo "You're not useless after all."

    # Reward scene trigger (INT gate checked in hub before calling this label)
    $ intellect += 4
    $ gold      += 150
    $ persistent.morgana_reward_seen = True
    show screen system_overlay
    s "Intellect +4. [150]g earned."
    hide screen system_overlay

    # Scene: Morgana's reward
    n "She moves around the counter. The kitchen is quiet."
    mo "You've earned something."
    n "Her voice carries the same precision as her recipes — no warmth, but no cruelty either."
    mo "Don't read into it."

    # [REWARD SCENE — Tier 2]
    n "She is efficient and deliberate about this the same way she is about everything."
    n "She doesn't speak during. Afterward she rinses her hands at the sink."
    mo "Tomorrow the sequence starts at seven."
    n "That's all she says."
    # [END REWARD SCENE]

    $ morgana_reward_scene_done = True
    return

label morgana_hard_fail:
    show ch morgana kitchen position
    mo "I expected as much."
    $ intellect += 1
    show screen system_overlay
    s "Intellect +1."
    hide screen system_overlay
    return


## ── Screen action helper ──────────────────────────────────────────────────────

init python:
    _mo_tap_result = None
    _mo_last_tap   = None

    def morgana_tap(ingredient):
        global _mo_entered, _mo_seq, _mo_tap_result, _mo_last_tap
        _mo_last_tap = ingredient
        expected = _mo_seq[len(_mo_entered)]
        if ingredient == expected:
            _mo_tap_result = "correct"
        else:
            _mo_tap_result = "wrong"
        renpy.return_statement()
