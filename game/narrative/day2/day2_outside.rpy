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
                text "▲":
                    xalign 0.5
                    color "#e8e0d0cc"
                    hover_color "#ffffff"
                    size 28
                    font gui.name_text_font
                text "Back inside":
                    xalign 0.5
                    color "#e8e0d0cc"
                    hover_color "#ffffff"
                    size 22
                    font gui.name_text_font


## ── Miss Fortune ─────────────────────────────────────────────────────────────

label day2_meet_miss_fortune:

    if met_miss_fortune:
        # MISSING: ch miss fortune profile default
        show screen ph_sprite("ch miss fortune profile default", xalign=0.5, yalign=1.0)
        mf "Still here. Come back when you've got gold to spend."
        hide screen ph_sprite
        return

    $ met_miss_fortune = True

    # MISSING: ch miss fortune profile default — human woman, red hair,
    # two pistols at her hips, fitted trader's coat. Confident posture.
    show screen ph_sprite("ch miss fortune profile default", xalign=0.5, yalign=1.0)

    n "She spots you before you're close enough to speak."
    n "Red hair. Two pistols. The kind of posture that says she's already calculated whether you're useful."

    mf "Well. A human. Wasn't expecting that."
    mf "You're the one they pulled out of the Bandlewood, aren't you."

    n "Not a question."

    mc "Word travels."

    mf "Bilgewater runs on information. I make it a habit."
    mf "Sarah Fortune. Merchant. Trader. Occasional opportunist, depending on who's asking."
    mf "I move goods between Bilgewater and the city. Rare things, specific things."
    mf "Things people want and can't get through normal channels."

    mc "Sounds like a good business."

    mf "It is when people pay on time."
    mf "Which they don't."

    n "She says it with a flat, practiced irritation — the kind that lives behind the eyes of someone who has had this particular frustration many times."

    mf "I've got a trade I'm trying to close by end of week. Specific materials."
    mf "Problem is one of my buyers paid late, which means I'm short on front money for the final leg."
    mf "Two hundred gold. That's all I need to lock the deal."

    n "She looks at you the way someone looks at a lock they're deciding whether to pick."

    mf "I don't ask for money without collateral. That's not how I work."

    n "She reaches back without looking and unclips one of the pistols at her hip."
    n "She holds it out, grip-first. It's beautiful — engraved, heavy, clearly not standard issue."

    mf "Shock and Awe. One of a matched pair. Worth considerably more than two hundred gold."
    mf "You hold onto her while I'm in the city. Trade closes, you get your two hundred back plus fifty interest."
    mf "Deal falls through for any reason — the pistol's yours to keep."

    menu:
        "Deal. I'll lend you the gold.":
            mc "Two hundred gold, one pistol as collateral. Deal."

            mf "Smart."
            n "She sets the pistol in your hand. The weight of it is significant."
            mf "I'll find you when the trade clears. Shouldn't be more than a few days."
            mf "Don't let anyone shoot it."

            $ has_mf_pistol = True
            $ mf_loan_active = True

            show screen system_overlay
            s "You've obtained: Shock and Awe (Miss Fortune's Pistol)"
            s "One of Miss Fortune's matched pair. Held as collateral on a 200 gold loan."
            s "She owes you 250 gold on return. Don't lose it."
            call screen system_got_it
            hide screen system_overlay

        "I don't have that kind of gold on me.":
            mc "I'd help but I don't have two hundred to spare."
            mf "Shame."
            n "She clips the pistol back without any visible disappointment."
            mf "If that changes, come find me."

        "I'm not in the business of lending to strangers.":
            mc "I don't lend money to people I just met."
            n "She tilts her head. Something like respect crosses her face."
            mf "Fair. I've met worse judgment calls."
            mf "If you change your mind before the end of the week — you know where I am."

    hide screen ph_sprite
    return
