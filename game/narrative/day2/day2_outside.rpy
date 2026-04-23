# narrative/day2/day2_outside.rpy
# Day 2 outside: the city street hub and Miss Fortune's merchant introduction.
# Fizz's introduction is in day2_fizz.rpy (isolated for explicit content).


## ── Outside loop ─────────────────────────────────────────────────────────────

label day2_outside_loop:

    scene bg city outside daytime
    play ambient "audio/sfx/Tavern_ambience.mp3" fadein 1.5 volume 0.3

    n "The air outside is warm and bright, the city going about its morning."
    n "You can hear the market a few streets over — the familiar sounds of people selling things at each other."

    if not day2_outside_announced:
        $ day2_outside_announced = True
        $ energy_hud_visible = True
        show screen energy_intro
        show screen energy_arrow
        show screen system_overlay
        s "You have 3 Energy to spend today."
        s "Each job or interaction costs 1 — when it's gone, your body needs to rest."
        s "You can talk to people freely. It's the work that wears you down."
        call screen system_got_it
        hide screen energy_arrow
        hide screen energy_intro
        hide screen system_overlay

    $ _day2_outside_running = True

    while _day2_outside_running:
        window hide
        call screen day2_outside_hub
        window show

        if _return == "miss_fortune":
            call day2_meet_miss_fortune
            scene bg city outside daytime

        elif _return == "fizz":
            call day2_meet_fizz
            scene bg city outside daytime

        elif _return == "auto_repair":
            call loc_auto_repair
            scene bg city outside daytime
            if energy <= 0:
                $ _day2_outside_running = False

        elif _return == "roboshop":
            call loc_roboshop
            scene bg city outside daytime
            if energy <= 0:
                $ _day2_outside_running = False

        elif _return == "scout_training":
            call loc_scout_training
            scene bg city outside daytime
            if energy <= 0:
                $ _day2_outside_running = False

        elif _return == "hot_springs":
            call loc_hot_springs
            scene bg city outside daytime
            if energy <= 0:
                $ _day2_outside_running = False

        elif _return == "deep_woods":
            call loc_deep_woods
            scene bg city outside daytime
            if energy <= 0:
                $ _day2_outside_running = False

        elif _return == "kitchen":
            call loc_kitchen
            scene bg city outside daytime
            if energy <= 0:
                $ _day2_outside_running = False

        elif _return == "impish_delight":
            $ _day2_outside_running = False
            call loc_impish_delight
            scene bg city outside daytime

    stop ambient fadeout 1.0

    # TODO: jump to rest of day 2 when written
    return


screen day2_outside_hub():
    zorder 100
    modal True

    # Characters
    imagebutton:
        idle Transform("ch miss fortune outside position", alpha=0.88)
        hover Fixed(Transform("ch miss fortune outside position", zoom=1.005, anchor=(0.5, 1.0), align=(0.5, 1.0)), xysize=(1920, 1088))
        focus_mask True
        pos (0, 0)
        activate_sound "audio/sfx/click_selectable.mp3"
        action Return("miss_fortune")

    imagebutton:
        idle Transform("ch fizz outside position", alpha=0.88)
        hover Fixed(Transform("ch fizz outside position", zoom=1.005, anchor=(0.5, 1.0), align=(0.5, 1.0)), xysize=(1920, 1088))
        focus_mask True
        pos (0, 0)
        activate_sound "audio/sfx/click_selectable.mp3"
        action Return("fizz")

    # Navigation signs — gated by energy (NPC conversations are free; jobs cost 1)
    imagebutton:
        sensitive energy > 0
        idle Transform("bt auto repair", alpha=(0.5 if energy > 0 else 0.2))
        hover Fixed(Transform("bt auto repair", zoom=1.005, anchor=(0.5, 0.5), align=(0.5, 0.5)), xysize=(1920, 1088))
        focus_mask True
        pos (-2, -5)
        hover_sound "audio/sfx/hover_selectable.mp3"
        activate_sound "audio/sfx/click_selectable.mp3"
        action Return("auto_repair")

    imagebutton:
        sensitive energy > 0
        idle Transform("bt roboshop", alpha=(0.5 if energy > 0 else 0.2))
        hover Fixed(Transform("bt roboshop", zoom=1.005, anchor=(0.5, 0.5), align=(0.5, 0.5)), xysize=(1920, 1088))
        focus_mask True
        pos (-2, -5)
        hover_sound "audio/sfx/hover_selectable.mp3"
        activate_sound "audio/sfx/click_selectable.mp3"
        action Return("roboshop")

    imagebutton:
        sensitive energy > 0
        idle Transform("bt scout training", alpha=(0.5 if energy > 0 else 0.2))
        hover Fixed(Transform("bt scout training", zoom=1.005, anchor=(0.5, 0.5), align=(0.5, 0.5)), xysize=(1920, 1088))
        focus_mask True
        pos (-2, -5)
        hover_sound "audio/sfx/hover_selectable.mp3"
        activate_sound "audio/sfx/click_selectable.mp3"
        action Return("scout_training")

    imagebutton:
        sensitive energy > 0
        idle Transform("bt hot springs", alpha=(0.5 if energy > 0 else 0.2))
        hover Fixed(Transform("bt hot springs", zoom=1.005, anchor=(0.5, 0.5), align=(0.5, 0.5)), xysize=(1920, 1088))
        focus_mask True
        pos (-2, -5)
        hover_sound "audio/sfx/hover_selectable.mp3"
        activate_sound "audio/sfx/click_selectable.mp3"
        action Return("hot_springs")

    imagebutton:
        sensitive energy > 0
        idle Transform("bt deep woods", alpha=(0.5 if energy > 0 else 0.2))
        hover Fixed(Transform("bt deep woods", zoom=1.005, anchor=(0.5, 0.5), align=(0.5, 0.5)), xysize=(1920, 1088))
        focus_mask True
        pos (-2, -5)
        hover_sound "audio/sfx/hover_selectable.mp3"
        activate_sound "audio/sfx/click_selectable.mp3"
        action Return("deep_woods")

    imagebutton:
        sensitive energy > 0
        idle Transform("bt kitchen", alpha=(0.78 if energy > 0 else 0.2))
        hover Fixed(Transform("bt kitchen", zoom=1.002, anchor=(0.5, 0.5), align=(0.5, 0.5)), xysize=(1920, 1088))
        focus_mask True
        pos (-2, -6)
        hover_sound "audio/sfx/hover_selectable.mp3"
        activate_sound "audio/sfx/click_selectable.mp3"
        action Return("kitchen")

    imagebutton:
        idle Transform("bt impish delight", alpha=0.78)
        hover Fixed(Transform("bt impish delight", zoom=1.002, anchor=(0.5, 0.5), align=(0.5, 0.5)), xysize=(1920, 1088))
        focus_mask True
        pos (0, -6)
        hover_sound "audio/sfx/hover_selectable.mp3"
        activate_sound "audio/sfx/click_selectable.mp3"
        action Return("impish_delight")


## ── Miss Fortune ─────────────────────────────────────────────────────────────

label day2_meet_miss_fortune:

    if met_miss_fortune and mf_loan_active:
        n "Miss Fortune is moving fast — consolidating crates, checking straps on her packs."
        n "She gives you a quick nod but doesn't stop moving."
        n "Apparently 200 gold buys a lot of urgency."
        return

    if met_miss_fortune and not mf_loan_active:
        n "Miss Fortune is standing at the edge of the road, staring at the line of carts and carriages with a particular look on her face."
        n "The look of someone doing math they don't like."
        n "She doesn't seem to notice you."
        return

    $ met_miss_fortune = True

    show ch miss fortune profile default:
        xalign 0.5
        yalign 1.0

    n "She spots you before you're close enough to speak."
    n "Red hair. Long coat. Two pistols that look like they've been fired recently and cleaned immediately after."
    n "The kind of posture that says she's already assessed you and filed the report."

    $ emotion_icon = "ch miss fortune icon smile"
    mf "Another human. Interesting day."

    n "She extends a hand. The grip is firm and practiced."

    mf "Sarah Fortune. Merchant, trader, and depending on who's asking — occasional opportunist."
    mf "I run rare goods between Bilgewater and the interior. Specific materials, specific clients."
    mf "The kind of trade that keeps the city interesting."

    mc "Sounds profitable."

    mf "It is. Consistently. I'm very good at this."

    n "She says it the way someone states the weather. Pure fact, no performance."

    mf "I've moved goods through three active war zones in the last year and turned a profit on all three."
    mf "I have clients on four different continents. Two of them don't trust anyone else."
    mf "My reputation is, frankly, immaculate."

    n "A pause."
    n "Something shifts slightly in her posture. A hair. Almost nothing."

    $ emotion_icon = "ch miss fortune icon embarrassed"
    mf "Which makes this current situation particularly — irritating."

    mc "What situation?"

    mf """
    I may have

    I may have.

    I may have..

    I may have... Slightly.
    """

    mf "There was a celebration. Last port. A deal came through and I — commemorated it."
    mf "Appropriately. Enthusiastically. With other people's transport money."

    n "She looks somewhere past your shoulder."

    mf "I have a meeting two towns over. Tomorrow. A trade I cannot miss."
    mf "And the funds I set aside for the carriage hire are — less present than they were."

    mc "How much less present?"

    mf "Two hundred gold."

    n "She says it the same way she'd say anything else. Straight."

    mf "I have a contact coming back through in a few days — they'll cover the return."
    mf "I just need the front money to get there."

    n "She reaches back without looking and unclips one of the pistols at her hip."
    n "She holds it out, grip-first."
    n "It's enormous — engraved along the barrel, heavier than it has any right to be."
    n "It looks less like a pistol and more like someone miniaturized a cannon and added a handle."

    $ emotion_icon = "ch miss fortune icon smile"
    mf "One of mine. She's worth considerably more than two hundred gold."
    mf "You hold her while I'm gone. Trade closes, you get your money back plus fifty."
    mf "Deal falls through for any reason — she's yours."

    menu:
        "Lend her the gold.":
            if gold >= 200:
                mc "Two hundred gold. Pistol as collateral. Deal."

                n "Something in her face relaxes — just briefly."
                mf "Smart."
                n "She sets the pistol in your hands. The weight of it is remarkable."
                mf "I'll find you when I'm back. Few days at most."
                mf "Keep her clean. Don't point her at anyone I'd regret."

                $ gold -= 200
                $ has_mf_pistol = True
                $ mf_loan_active = True
                $ mf_scene_1_done = True

                show screen system_overlay
                s "You've lent 200 gold to Miss Fortune."
                s "Obtained: Large Pistol — one of Miss Fortune's matched pair."
                s "Held as collateral. She owes you 250 gold on return."
                call screen system_got_it
                hide screen system_overlay
            else:
                mc "I'd lend it if I had it. I'm short right now."
                n "She takes the pistol back."
                $ emotion_icon = "ch miss fortune icon embarrassed"
                mf "Story of this port."
                mf "If that changes before I leave — come find me."

        "I don't trust a pirate with my gold.":
            mc "No offense, but I just met you."

            n "She looks at you for a moment."
            n "Then she exhales through her nose — slow, deflated."

            $ emotion_icon = "ch miss fortune icon embarrassed"
            mf "Right."

            n "She clips the pistol back to her hip."

            mf "I suppose I'll figure something else out."
            mf "There's always — other arrangements."

            n "She says it quietly. The implication is not subtle."
            n "She's going to trade favors for a carriage ride and she is not happy about it."

            $ mf_scene_1_done = True

    hide ch miss fortune profile default
    $ emotion_icon = None
    return


## ── Stub location labels ─────────────────────────────────────────────────────

# loc_auto_repair  → day2_corki.rpy
# loc_roboshop      → day2_rumble.rpy
# loc_scout_training → day2_teemo.rpy
# loc_kitchen       → day2_morgana.rpy

label loc_hot_springs:
    scene bg hot springs
    n "PLACEHOLDER: Hot Springs — scene not yet built"
    return

label loc_deep_woods:

    scene bg black with dissolve

    if constitution < 10:
        n "The tree line at the edge of town. Older than the buildings, older than the road."
        n "Something past the first row of trunks makes the air feel different — heavier."
        n "Your body isn't ready for this. You can feel that clearly."

        menu:
            "Go in anyway.":
                jump gameover1
            "Turn back. Not today.":
                return

    n "PLACEHOLDER: Deep Woods / Kindred encounter — scene not yet built"
    return

label loc_impish_delight:
    scene bg black
    n "PLACEHOLDER: Impish Delight — bg impish delight interior needed"
    return
