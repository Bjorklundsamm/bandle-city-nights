# narrative/day2/day2_teemo.rpy
# Teemo's Scout Training — timed branching decisions.
# scout_time starts at 10. Correct choice (scout doctrine) +2, wrong -3.
# Hit 0 at any point = fail branch (partial reward).
# Clear all 6 decisions in time = full reward: Strength +3, Intellect +2.
# Partial reward: Strength +1, Intellect +1.
#
# Scout doctrine: high ground, stealth, patience, cover, information first.


label loc_scout_training:

    $ energy -= 1
    $ renpy.block_rollback()

    scene bg black  # placeholder — bg bandlewood exterior
    n "[Teemo's Scout Trail — bg placeholder]"

    $ scout_time = 10

    # TODO: brief Teemo intro dialogue before first fork

    ## ── Decision 1: Entry point ──────────────────────────────────────────────
    n "First fork. The ridge trail is slower but gives you clear line of sight."
    n "The valley cuts twenty minutes off the route."

    menu:
        "Take the ridge trail." if scout_time > 0:
            te "Eyes open, head up. That's the rule."
            $ scout_time += 2
        "Cut through the valley." if scout_time > 0:
            te "Blind corners. You'd never make it as a scout."
            $ scout_time -= 3

    if scout_time <= 0:
        jump scout_training_fail

    ## ── Decision 2: Patrol spotted ───────────────────────────────────────────
    n "You spot an enemy patrol ahead. They haven't seen you."

    menu:
        "Rush across before they're fully through." if scout_time > 0:
            te "You just bought them a free sighting. Awful."
            $ scout_time -= 3
        "Hold in cover and wait them out." if scout_time > 0:
            te "That's it. Let them do the walking."
            $ scout_time += 2

    if scout_time <= 0:
        jump scout_training_fail

    ## ── Decision 3: Strange sound ────────────────────────────────────────────
    n "Something moves in the brush to your left. Could be anything."

    menu:
        "Investigate — could be useful intel." if scout_time > 0:
            te "Could be a trap. Is a trap. You're terrible at this."
            $ scout_time -= 3
        "Mark the position and pull back to observe." if scout_time > 0:
            te "Information, not engagement. You're getting it."
            $ scout_time += 2

    if scout_time <= 0:
        jump scout_training_fail

    ## ── Decision 4: Open ground ──────────────────────────────────────────────
    n "There's a shortcut across open ground. Faster, but no cover."

    menu:
        "Stick to the tree line. Slower." if scout_time > 0:
            te "Always cover. You move like a shadow or you don't move."
            $ scout_time += 2
        "Use the open ground. Save time." if scout_time > 0:
            te "Every archer in range just lit up. Think."
            $ scout_time -= 3

    if scout_time <= 0:
        jump scout_training_fail

    ## ── Decision 5: Spotted at distance ──────────────────────────────────────
    n "A figure at the edge of the tree line. They might have seen you."

    menu:
        "Move to new cover — confirm they haven't locked on." if scout_time > 0:
            te "Movement confirms your position. You just told them where you are."
            $ scout_time -= 3
        "Go still. Don't move until they've passed." if scout_time > 0:
            te "The forest hid you. You let it. Good."
            $ scout_time += 2

    if scout_time <= 0:
        jump scout_training_fail

    ## ── Decision 6: Return route ─────────────────────────────────────────────
    n "You've got everything you need. Time to report back."

    menu:
        "Same route — you cleared it on the way in." if scout_time > 0:
            te "A route cleared once is a route the enemy watches. Never the same path."
            $ scout_time -= 3
        "New route back. Never retrace your steps." if scout_time > 0:
            te "That's the doctrine. You remembered."
            $ scout_time += 2

    if scout_time <= 0:
        jump scout_training_fail

    jump scout_training_success


label scout_training_success:

    show screen system_overlay
    s "Trail cleared. All six calls correct."
    s "Strength +3   Intellect +2"
    call screen system_got_it
    hide screen system_overlay

    $ strength  += 3
    $ intellect += 2
    $ persistent.teemo_visits += 1

    return


label scout_training_fail:

    show screen system_overlay
    s "Time ran out. Partial credit."
    s "Strength +1   Intellect +1"
    call screen system_got_it
    hide screen system_overlay

    $ strength  += 1
    $ intellect += 1
    $ persistent.teemo_visits += 1

    return
