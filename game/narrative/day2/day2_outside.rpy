# narrative/day2/day2_outside.rpy
# Day 2 outside: the city street hub and Miss Fortune's merchant introduction.
# Fizz's introduction is in day2_fizz.rpy (isolated for explicit content).


## ── Outside loop ─────────────────────────────────────────────────────────────

label day2_outside_loop:

    scene bg city outside daytime
    play ambient "audio/sfx/Tavern_ambience.mp3" fadein 1.5 volume 0.3

    n "The air outside is warm and bright, the city going about its morning."
    n "You can hear the market a few streets over — the familiar sounds of people selling things at each other."

    $ _day2_outside_running = True

    while _day2_outside_running:
        window hide
        call screen day2_outside_hub
        window show

        if _return == "back_inside":
            $ _day2_outside_running = False

        elif _return == "miss_fortune":
            call day2_meet_miss_fortune
            scene bg city outside daytime

        elif _return == "fizz":
            call day2_meet_fizz
            scene bg city outside daytime

        elif _return == "auto_repair":
            call loc_auto_repair
            scene bg city outside daytime

        elif _return == "roboshop":
            call loc_roboshop
            scene bg city outside daytime

        elif _return == "scout_training":
            call loc_scout_training
            scene bg city outside daytime

        elif _return == "hot_springs":
            call loc_hot_springs
            scene bg city outside daytime

        elif _return == "deep_woods":
            call loc_deep_woods
            scene bg city outside daytime

        elif _return == "kitchen":
            call loc_kitchen
            scene bg city outside daytime

        elif _return == "impish_delight":
            call loc_impish_delight
            scene bg city outside daytime

    stop ambient fadeout 1.0

    # TODO: jump to rest of day 2 when written
    return


screen day2_outside_hub():
    default back_hovered = False
    zorder 100
    modal True

    ## All images are 1920x1088 full-canvas composites.
    ## focus_mask True restricts clicks to non-transparent pixels only.
    ## All positioned at (0,0) — the canvas composition places each element.

    # Characters — size change on hover, no sound.
    imagebutton:
        idle "ch miss fortune outside position"
        hover Transform("ch miss fortune outside position", zoom=1.04, anchor=(0.5, 1.0))
        focus_mask True
        xalign 0.0
        yalign 0.0
        activate_sound "audio/sfx/click_selectable.mp3"
        action Return("miss_fortune")

    imagebutton:
        idle "ch fizz outside position"
        hover Transform("ch fizz outside position", zoom=1.04, anchor=(0.5, 1.0))
        focus_mask True
        xalign 0.0
        yalign 0.0
        activate_sound "audio/sfx/click_selectable.mp3"
        action Return("fizz")

    # Navigation signs — size change + hover sound.
    imagebutton:
        idle "bt auto repair"
        hover Transform("bt auto repair", zoom=1.05, anchor=(0.5, 0.5))
        focus_mask True
        xalign 0.0
        yalign 0.0
        hover_sound "audio/sfx/hover_selectable.mp3"
        activate_sound "audio/sfx/click_selectable.mp3"
        action Return("auto_repair")

    imagebutton:
        idle "bt roboshop"
        hover Transform("bt roboshop", zoom=1.05, anchor=(0.5, 0.5))
        focus_mask True
        xalign 0.0
        yalign 0.0
        hover_sound "audio/sfx/hover_selectable.mp3"
        activate_sound "audio/sfx/click_selectable.mp3"
        action Return("roboshop")

    imagebutton:
        idle "bt scout training"
        hover Transform("bt scout training", zoom=1.05, anchor=(0.5, 0.5))
        focus_mask True
        xalign 0.0
        yalign 0.0
        hover_sound "audio/sfx/hover_selectable.mp3"
        activate_sound "audio/sfx/click_selectable.mp3"
        action Return("scout_training")

    imagebutton:
        idle "bt hot springs"
        hover Transform("bt hot springs", zoom=1.05, anchor=(0.5, 0.5))
        focus_mask True
        xalign 0.0
        yalign 0.0
        hover_sound "audio/sfx/hover_selectable.mp3"
        activate_sound "audio/sfx/click_selectable.mp3"
        action Return("hot_springs")

    imagebutton:
        idle "bt deep woods"
        hover Transform("bt deep woods", zoom=1.05, anchor=(0.5, 0.5))
        focus_mask True
        xalign 0.0
        yalign 0.0
        hover_sound "audio/sfx/hover_selectable.mp3"
        activate_sound "audio/sfx/click_selectable.mp3"
        action Return("deep_woods")

    imagebutton:
        idle "bt kitchen"
        hover Transform("bt kitchen", zoom=1.05, anchor=(0.5, 0.5))
        focus_mask True
        xalign 0.0
        yalign 0.0
        hover_sound "audio/sfx/hover_selectable.mp3"
        activate_sound "audio/sfx/click_selectable.mp3"
        action Return("kitchen")

    imagebutton:
        idle "bt impish delight"
        hover Transform("bt impish delight", zoom=1.05, anchor=(0.5, 0.5))
        focus_mask True
        xalign 0.0
        yalign 0.0
        hover_sound "audio/sfx/hover_selectable.mp3"
        activate_sound "audio/sfx/click_selectable.mp3"
        action Return("impish_delight")

    ## Back inside the tavern.
    frame:
        xalign 0.5
        yalign 0.05
        background None
        button:
            background None
            hover_background None
            hover_sound "audio/sfx/hover_selectable.mp3"
            activate_sound "audio/sfx/click_selectable.mp3"
            hovered SetScreenVariable("back_hovered", True)
            unhovered SetScreenVariable("back_hovered", False)
            action Return("back_inside")
            vbox:
                xalign 0.5
                spacing 4
                if back_hovered:
                    add Transform("pointer arrow", zoom=0.5, rotate=90, alpha=0.6) at nav_arrow_bounce xalign 0.5
                else:
                    add Transform("pointer arrow", zoom=0.5, rotate=90, alpha=0.6) xalign 0.5
                text "Back inside":
                    xalign 0.5
                    color "#e8e0d0cc"
                    hover_color "#ffffff"
                    size 22
                    font gui.name_text_font


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

    mf "Which makes this current situation particularly — irritating."

    mc "What situation?"

    mf "I may have. Slightly."

    n "She stops. Starts again."

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
                mf "Story of this port."
                mf "If that changes before I leave — come find me."

        "I don't trust a pirate with my gold.":
            mc "No offense, but I just met you."

            n "She looks at you for a moment."
            n "Then she exhales through her nose — slow, deflated."

            mf "Right."

            n "She clips the pistol back to her hip."

            mf "I suppose I'll figure something else out."
            mf "There's always — other arrangements."

            n "She says it quietly. The implication is not subtle."
            n "She's going to trade favors for a carriage ride and she is not happy about it."

            $ mf_scene_1_done = True

    hide ch miss fortune profile default
    return


## ── Stub location labels ─────────────────────────────────────────────────────

label loc_auto_repair:
    scene bg black
    n "PLACEHOLDER: Auto Repair — bg auto repair interior needed"
    return

label loc_roboshop:
    scene bg black
    n "PLACEHOLDER: Roboshop — bg roboshop interior needed"
    return

label loc_scout_training:
    scene bg black
    n "PLACEHOLDER: Scout Training — bg scout training grounds needed"
    return

label loc_hot_springs:
    scene bg hot springs
    n "PLACEHOLDER: Hot Springs — scene not yet built"
    return

label loc_deep_woods:
    scene bg black
    n "PLACEHOLDER: Deep Woods — bg deep woods needed"
    return

label loc_kitchen:
    scene bg black
    n "PLACEHOLDER: Kitchen — bg kitchen interior needed"
    return

label loc_impish_delight:
    scene bg black
    n "PLACEHOLDER: Impish Delight — bg impish delight interior needed"
    return
