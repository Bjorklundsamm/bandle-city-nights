# narrative/day2/day2_morgana.rpy
# Morgana's Kitchen — recipe memory minigame.
# Phase 1: watch each ingredient appear for 1.5s (auto-advance timer).
# Phase 2: tap ingredients in the order shown. Wrong tap = Morgana reacts + full reset.
# Sequence length starts at 4, grows by 1 per visit (cap 8).
# Rewards: Intellect +2, Gold +100.
#
# NOTE: All Python functions/screens here use the d2_ prefix to avoid conflicts
# with minigame_morgana.rpy which defines the standalone job version.


## ── Python logic ─────────────────────────────────────────────────────────────

init python:

    _D2_MORGANA_POOL = ["carrot", "onion", "mushroom", "herb", "fish", "salt"]

    def d2_morgana_make_sequence(visits):
        import random
        length = min(4 + visits, 8)
        return [random.choice(_D2_MORGANA_POOL) for _ in range(length)]

    def d2_morgana_unique_buttons(sequence):
        """All unique ingredients from the pool, shuffled — used as input buttons."""
        import random
        buttons = list(_D2_MORGANA_POOL)
        random.shuffle(buttons)
        return buttons


## ── Hub screen ────────────────────────────────────────────────────────────────

screen loc_kitchen_hub():
    zorder 50

    imagebutton:
        idle  Transform("ch morgana kitchen position", alpha=0.9)
        hover Fixed(Transform("ch morgana kitchen position", zoom=1.005, anchor=(0.5, 1.0), align=(0.5, 1.0)), xysize=(1920, 1088))
        focus_mask True
        pos (0, 0)
        hover_sound "audio/sfx/hover_selectable.mp3"
        activate_sound "audio/sfx/click_selectable.mp3"
        action Return("interact")

    textbutton "← Leave":
        xalign 0.02
        yalign 0.96
        text_size 22
        text_color "#c8c8c8"
        text_hover_color "#ffffff"
        activate_sound "audio/sfx/click_selectable.mp3"
        action Return("leave")


## ── Memorise screen ──────────────────────────────────────────────────────────

screen d2_morgana_memorize(ingredient, index, total):
    """Shows one ingredient for 1.5s then auto-advances."""
    modal True
    zorder 100

    text "Memorise the recipe." xalign 0.5 ypos 100 size 22 color "#cccccc"

    text ingredient.upper():
        xalign 0.5
        yalign 0.45
        size 72
        color "#e8c87a"
        outlines [(3, "#000000", 0, 0)]

    text "[index + 1] / [total]" xalign 0.5 yalign 0.62 size 28 color "#888888"

    timer 1.5 action Return()


## ── Input screen ─────────────────────────────────────────────────────────────

screen d2_morgana_input(sequence, buttons, progress):
    """Ingredient tap screen. Returns the ingredient name the player tapped."""
    modal True
    zorder 100

    # Progress track — checkmarks for done, question marks for remaining
    hbox:
        xalign 0.5
        ypos 110
        spacing 10
        for _i in range(len(sequence)):
            if _i < progress:
                text "✓" size 30 color "#00cc66"
            else:
                text "?" size 30 color "#555555"

    text "Tap in order." xalign 0.5 ypos 170 size 22 color "#cccccc"

    # Ingredient buttons — 3-column grid
    grid 3 2:
        xalign 0.5
        yalign 0.55
        xspacing 16
        yspacing 16
        for _btn in buttons:
            textbutton _btn.upper():
                xsize 200
                ysize 72
                text_xalign 0.5
                text_yalign 0.5
                text_size 24
                action Return(_btn)


## ── Label ────────────────────────────────────────────────────────────────────

label loc_kitchen:

    scene bg tavern kitchen with dissolve

    call screen loc_kitchen_hub()
    if _return == "leave":
        return

    $ energy -= 1
    $ renpy.block_rollback()

    show ch morgana kitchen position
    # TODO: Morgana intro dialogue

    python:
        _mseq      = d2_morgana_make_sequence(persistent.morgana_visits)
        _mbtns     = d2_morgana_unique_buttons(_mseq)
        _mprogress = 0
        _mdone     = False

    # ── Phase 1: Memorise ─────────────────────────────────────────────────────
    n "Watch carefully."

    $ _memo_i = 0
    while _memo_i < len(_mseq):
        call screen d2_morgana_memorize(_mseq[_memo_i], _memo_i, len(_mseq))
        $ _memo_i += 1

    # ── Phase 2: Recall ───────────────────────────────────────────────────────
    n "Now repeat it."

    while not _mdone:
        call screen d2_morgana_input(_mseq, _mbtns, _mprogress)

        if _return == _mseq[_mprogress]:
            $ _mprogress += 1
            if _mprogress >= len(_mseq):
                $ _mdone = True
        else:
            mo "Wrong. From the beginning."
            $ _mprogress = 0

    # ── Reward ────────────────────────────────────────────────────────────────
    show screen system_overlay
    s "Recipe complete."
    s "Intellect +2   Gold +100"
    call screen system_got_it
    hide screen system_overlay

    $ intellect += 2
    $ gold      += 100
    $ persistent.morgana_visits += 1

    return
