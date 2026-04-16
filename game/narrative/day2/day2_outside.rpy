# narrative/day2/day2_outside.rpy
# Day 2 outside: the city street hub and Miss Fortune's merchant introduction.
# Fizz's introduction is in day2_fizz.rpy (isolated for explicit content).


## ── Outside loop ─────────────────────────────────────────────────────────────

label day2_outside_loop:

    # MISSING: bg bandle city street — Bandle City daytime exterior.
    # Colorful, low Yordle-scale buildings. Cobblestones. Warm morning light.
    # Tavern exterior visible at one edge. Maybe a market stall or two.
    show screen ph_bg("bg bandle city street")
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
            hide screen ph_bg
            call day2_meet_miss_fortune
            show screen ph_bg("bg bandle city street")

        elif _return == "fizz":
            hide screen ph_bg
            call day2_meet_fizz
            show screen ph_bg("bg bandle city street")

    hide screen ph_bg
    stop ambient fadeout 1.0

    # TODO: jump to rest of day 2 when written
    return


screen day2_outside_hub():
    zorder 100
    modal True

    # MISSING: ch miss fortune tavern position — standing, arms crossed, confident,
    # merchant's pack at her side, two pistols at her hips.
    use ph_button("miss_fortune", xalign=0.30, yalign=0.45)

    # MISSING: ch fizz tavern position — leaning against the tavern wall,
    # one foot up, tail flicking, trying to look casual.
    use ph_button("fizz", xalign=0.65, yalign=0.50)

    ## Up arrow — back inside.
    frame:
        xalign 0.5
        yalign 0.05
        background None
        button:
            background None
            hover_background None
            hover_sound "audio/sfx/hover_selectable.mp3"
            activate_sound "audio/sfx/click_selectable.mp3"
            action Return("back_inside")
            vbox:
                xalign 0.5
                spacing 4
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

    # MISSING: ch miss fortune profile default — human woman, red hair,
    # two pistols at her hips, fitted trader's coat. Confident posture.
    show screen ph_sprite("ch miss fortune profile default", xalign=0.5, yalign=1.0)

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

    hide screen ph_sprite
    return
