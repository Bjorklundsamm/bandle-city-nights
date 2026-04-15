# minigames/minigame_teemo.rpy
# Teemo's Scout Training — Timed Branching Decisions
#
# Entirely narrative — no custom UI needed. Timer is a variable.
# scout_time starts at 10. Correct choice: +2. Wrong choice: -3.
# If time runs out mid-route: partial reward only.
#
# Normal mode: 6 decision points, 2 options each.
# Hard mode:   6 decision points, 2 options each but:
#               - 2 points have 3 options (only one correct)
#               - 1 trap: looks correct, costs -4 instead of +2
#               - starting time: 7 instead of 10
#
# Rewards
#   Normal clear:   +3 STR, +2 INT
#   Normal partial: +1 STR, +1 INT
#   Hard clear:     +4 STR, +3 INT
#   Hard partial:   +1 STR, +1 INT
#
# Hard mode unlocked: persistent.teemo_hard_unlocked after first normal clear.

## ── Normal Mode ───────────────────────────────────────────────────────────────

label teemo_job:
    $ persistent.energy -= 1
    $ persistent.teemo_visits += 1

    scene bg bandlewood trail
    show ch teemo neutral

    if persistent.teemo_visits == 1:
        te "You want to train? Fine. Try not to get left behind."
        te "Six checkpoints. Wrong moves cost time. Run out of time and I finish without you."
        te "Starting time: ten. Let's go."
    else:
        te "Back for more punishment. Good. Run."

    $ scout_time = 10
    $ scout_cleared = True

    # --- Checkpoint 1 ---
    te "Trail forks ahead. Enemy patrol spotted left flank. What's your call?"
    menu:
        "Take the left fork and shadow the patrol.":
            te "Correct. Shadow and surveil. That's scout doctrine."
            $ scout_time += 2
        "Sprint straight to the objective.":
            te "Wrong. You just announced yourself to an armed patrol. -3."
            $ scout_time -= 3

    if scout_time <= 0:
        $ scout_cleared = False
        jump teemo_partial

    # --- Checkpoint 2 ---
    te "Approach to a ridge. High ground, but exposed. Low ground is covered."
    menu:
        "Take the low ground. Cover first.":
            te "Good. Visibility matters less than surviving to report."
            $ scout_time += 2
        "Take the high ground. See further.":
            te "You're silhouetted against the sky. The enemy can see you just as well."
            $ scout_time -= 3

    if scout_time <= 0:
        $ scout_cleared = False
        jump teemo_partial

    # --- Checkpoint 3 ---
    te "River crossing. Current's strong. Stepping stones to the left, shallow ford to the right."
    menu:
        "Use the shallow ford.":
            te "Slower but predictable. You stay dry. Right call."
            $ scout_time += 2
        "Use the stepping stones.":
            te "One miss and you're soaked, cold, and making noise."
            $ scout_time -= 3

    if scout_time <= 0:
        $ scout_cleared = False
        jump teemo_partial

    # --- Checkpoint 4 ---
    te "Target building in sight. Two guards at the main entrance, none visible at the side."
    menu:
        "Approach the side entrance.":
            te "Exactly. Never confirm what you can observe from a distance."
            $ scout_time += 2
        "Wait and count guards before moving.":
            te "Good instinct, wrong priority. Scout doctrine: minimum exposure. Move."
            $ scout_time -= 3

    if scout_time <= 0:
        $ scout_cleared = False
        jump teemo_partial

    # --- Checkpoint 5 ---
    te "You're spotted. Enemy moving toward your position."
    menu:
        "Break off. Abort the run, circle back.":
            te "Right. Information is useless if you don't survive to report it."
            $ scout_time += 2
        "Hold position. Maybe they won't find you.":
            te "A Yordle scout does not 'maybe.' You are now compromised."
            $ scout_time -= 3

    if scout_time <= 0:
        $ scout_cleared = False
        jump teemo_partial

    # --- Checkpoint 6 ---
    te "Back at base. Secondary route still unscouted. Energy to spare?"
    menu:
        "Scout the secondary route before reporting.":
            te "The instinct is good. Incomplete intel is incomplete."
            $ scout_time += 2
        "Report immediately with what you have.":
            te "Hmm. Partial intel delivered fast beats complete intel delivered late."
            te "Acceptable call."
            $ scout_time += 1

    jump teemo_resolve

label teemo_resolve:
    if scout_cleared:
        jump teemo_clear
    else:
        jump teemo_partial

label teemo_clear:
    show ch teemo pleased
    te "Route complete. Time to spare."
    te "You're not terrible. Don't let it go to your head."
    $ persistent.strength  += 3
    $ persistent.intellect += 2
    $ persistent.teemo_hard_unlocked = True
    show screen system_overlay
    s "Strength +3. Intellect +2."
    hide screen system_overlay
    return

label teemo_partial:
    show ch teemo neutral
    te "Time's up. Route incomplete."
    te "You'd be dead in a real op. Come back tomorrow."
    $ persistent.strength  += 1
    $ persistent.intellect += 1
    show screen system_overlay
    s "Strength +1. Intellect +1."
    hide screen system_overlay
    return


## ── Hard Mode ─────────────────────────────────────────────────────────────────

label teemo_job_hard:
    $ persistent.energy -= 1
    $ persistent.teemo_visits += 1

    scene bg bandlewood trail
    show ch teemo neutral

    te "Hard mode. Seven seconds. Some forks have three paths."
    te "One of them is a trap. Don't fall for it."
    te "Move."

    $ scout_time = 7
    $ scout_cleared = True

    # --- Hard Checkpoint 1 ---
    te "Enemy patrol — armed, three strong. Moving perpendicular to your route."
    menu:
        "Shadow the patrol at distance.":
            te "Good. Shadow and observe."
            $ scout_time += 2
        "Accelerate and cross ahead of them.":
            te "You made it. Barely. Lucky, not skilled."
            $ scout_time += 0
        "Cut through underbrush to avoid entirely.":
            # Trap: looks safe, costs time
            te "Underbrush is loud. They heard you. You cost yourself the mission."
            $ scout_time -= 4

    if scout_time <= 0:
        $ scout_cleared = False
        jump teemo_hard_partial

    # --- Hard Checkpoint 2 ---
    te "Bridge or river ford. Bridge is faster but monitored."
    menu:
        "Use the ford.":
            te "Slower. Correct."
            $ scout_time += 2
        "Use the bridge quickly.":
            te "You're on a bridge with no cover. Classic."
            $ scout_time -= 3

    if scout_time <= 0:
        $ scout_cleared = False
        jump teemo_hard_partial

    # --- Hard Checkpoint 3 ---
    te "Target in sight. Two approaches. High ground, low ground, or wait for shift change."
    menu:
        "Take low ground cover.":
            te "Correct. Cover over visibility."
            $ scout_time += 2
        "High ground for observation.":
            te "Silhouetted. They have eyes too."
            $ scout_time -= 3
        "Wait for the shift change.":
            # Trap: sounds smart, costs time
            te "Guard shifts vary. You just wasted six minutes on a guess."
            $ scout_time -= 4

    if scout_time <= 0:
        $ scout_cleared = False
        jump teemo_hard_partial

    # --- Hard Checkpoint 4 ---
    te "You have partial intel. Full route scouted or report now?"
    menu:
        "Report immediately — partial intel beats late intel.":
            te "Correct priority."
            $ scout_time += 2
        "Complete the route — full intel is worth the time.":
            te "And if the situation changed while you were finishing? Think in tradeoffs."
            $ scout_time -= 3

    if scout_time <= 0:
        $ scout_cleared = False
        jump teemo_hard_partial

    # --- Hard Checkpoint 5 ---
    te "Spotted on approach. Three options."
    menu:
        "Break off. Abort and circle back.":
            te "Right. You live to report."
            $ scout_time += 2
        "Freeze and wait it out.":
            te "You froze for forty seconds. Time you don't have."
            $ scout_time -= 3
        "Shift to cougar-gait movement through undergrowth.":
            # Trap: sounds clever
            te "You don't know this terrain well enough for that. You made noise."
            $ scout_time -= 4

    if scout_time <= 0:
        $ scout_cleared = False
        jump teemo_hard_partial

    # --- Hard Checkpoint 6 ---
    te "Final approach. Gate is unguarded on one side. Two guards, other side."
    menu:
        "Unguarded side. Obvious choice.":
            te "You'd think. Unguarded means watched differently. But fine. You're in."
            $ scout_time += 1
        "Guarded side — create a distraction.":
            te "You don't have the time or resources for a distraction. Think situationally."
            $ scout_time -= 3

    if scout_time > 0:
        jump teemo_hard_clear
    else:
        $ scout_cleared = False
        jump teemo_hard_partial

label teemo_hard_clear:
    show ch teemo pleased
    te "..."
    te "Route complete. Time remaining."
    n "He's not smiling but he's not moving either. That is, you have learned, the same thing."
    te "The gym. Sixth bell. Bring boots that fit."
    n "He produces a small badge and slides it across the ground toward you with his foot."
    te "Don't lose it. It means something where I'm from."
    $ persistent.strength  += 4
    $ persistent.intellect += 3
    $ persistent.teemo_hard_unlocked = True
    show screen system_overlay
    s "Strength +4. Intellect +3. Scout badge earned."
    hide screen system_overlay
    return

label teemo_hard_partial:
    show ch teemo neutral
    te "Time's up. Hard mode. Were you expecting sympathy?"
    $ persistent.strength  += 1
    $ persistent.intellect += 1
    show screen system_overlay
    s "Strength +1. Intellect +1."
    hide screen system_overlay
    return
