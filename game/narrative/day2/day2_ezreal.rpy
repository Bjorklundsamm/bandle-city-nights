# narrative/day2/day2_ezreal.rpy
# Ezreal's Target Practice — 10 sequential click targets.
# Each target appears at a random position and expires after 1.5s.
# Click before expiry = hit. Miss/expire = 0.
# Ezreal trash-talks throughout; goes silent at a 5-hit streak (means he's impressed).
# Rewards based on accuracy: 80%+ = +5 STR, 50-79% = +3 STR, under 50% = +1 STR.


## ── Screen ───────────────────────────────────────────────────────────────────

screen ezreal_target(x, y, target_num):
    """Single target at (x, y). Click = hit, timer expiry = miss."""
    modal True
    zorder 100

    text "Target [target_num] / 10" xpos 20 ypos 14 size 26 color "#ffffff" outlines [(2, "#000000", 0, 0)]

    # Placeholder target — replace with bt target bullseye.png / bt target ring.png
    textbutton "[ O ]":
        xpos x
        ypos y
        xsize 80
        ysize 80
        text_xalign 0.5
        text_yalign 0.5
        text_size 36
        text_color "#ff4444"
        action Return("hit")

    timer 1.5 action Return("miss")


## ── Label ────────────────────────────────────────────────────────────────────

label loc_ezreal_range:

    $ energy -= 1
    $ renpy.block_rollback()

    scene bg black  # placeholder — bg ezreal target range / rooftop
    n "[Ezreal's Target Range — bg placeholder]"
    # TODO: Ezreal intro trash-talk

    python:
        import random
        _ez_targets      = [(random.randint(150, 1750), random.randint(120, 700)) for _ in range(10)]
        _ez_hits         = 0
        _ez_streak       = 0
        _ez_best_streak  = 0
        _ez_i            = 0
        _ez_first_miss   = True
        _ez_streak_noted = False

    while _ez_i < 10:

        $ _ex = _ez_targets[_ez_i][0]
        $ _ey = _ez_targets[_ez_i][1]
        call screen ezreal_target(_ex, _ey, _ez_i + 1)

        if _return == "hit":
            $ _ez_hits   += 1
            $ _ez_streak += 1
            if _ez_streak > _ez_best_streak:
                $ _ez_best_streak = _ez_streak
            if _ez_streak >= 5 and not _ez_streak_noted:
                ez "..."
                $ _ez_streak_noted = True
        else:
            if _ez_first_miss:
                ez "You're not even trying, are you?"
                $ _ez_first_miss = False
            $ _ez_streak       = 0
            $ _ez_streak_noted = False

        $ _ez_i += 1

    # ── Score ─────────────────────────────────────────────────────────────────
    python:
        _ez_accuracy = int((_ez_hits / 10) * 100)

    show screen system_overlay

    if _ez_accuracy >= 80:
        s "Accuracy: [_ez_accuracy]%   Strength +5"
        $ strength += 5
    elif _ez_accuracy >= 50:
        s "Accuracy: [_ez_accuracy]%   Strength +3"
        $ strength += 3
    else:
        s "Accuracy: [_ez_accuracy]%   Strength +1"
        $ strength += 1

    call screen system_got_it
    hide screen system_overlay

    if _ez_accuracy >= 80:
        ez "..."
        ez "Fine. You can shoot."
    elif _ez_accuracy >= 50:
        ez "Mediocre. Work on it."
    else:
        ez "I've seen better aim from a blindfolded gremlin."

    if _ez_best_streak > persistent.ezreal_best:
        $ persistent.ezreal_best = _ez_best_streak

    $ persistent.ezreal_visits += 1

    return
