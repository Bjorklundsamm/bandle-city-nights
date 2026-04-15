# narrative/day2/day2_tavern.rpy
# Day 2 daytime tavern: the hub loop and interactions with
# Barkeep (Bilgewater tip), Lulu, and Poppy.
#
# Exits to day2_outside_loop when player heads outside.


## ── Day 2 tavern loop ────────────────────────────────────────────────────────

label day2_tavern_loop:

    # MISSING: bg tavern daytime — same layout as bg tavern empty, morning light
    # through the windows, a few chairs still up, quieter than the night version.
    show screen ph_bg("bg tavern daytime")
    show screen inventory_button
    play music "audio/music/impish_delight.mp3" fadein 2.0 volume 0.5

    $ _day2_tavern_running = True

    while _day2_tavern_running:
        window hide
        call screen day2_tavern_hub
        window show

        if _return == "outside":
            $ _day2_tavern_running = False

        elif _return == "barkeep":
            hide screen ph_bg
            call day2_barkeep
            show screen ph_bg("bg tavern daytime")

        elif _return == "lulu":
            hide screen ph_bg
            call day2_lulu
            show screen ph_bg("bg tavern daytime")

        elif _return == "poppy":
            hide screen ph_bg
            call day2_poppy
            show screen ph_bg("bg tavern daytime")

    hide screen ph_bg
    stop music fadeout 1.5

    jump day2_outside_loop


screen day2_tavern_hub():
    zorder 100
    modal True

    # MISSING: ch barkeep tavern position daytime — behind bar, relaxed, hood up.
    use ph_button("barkeep", xalign=0.18, yalign=0.45)

    # MISSING: ch lulu tavern position daytime — seated at bar, feet off floor,
    # staff propped against the stool.
    use ph_button("lulu", xalign=0.45, yalign=0.40)

    # MISSING: ch poppy tavern position daytime — near the door, arms crossed,
    # mildly impatient, clearly would rather be at the gym.
    use ph_button("poppy", xalign=0.75, yalign=0.45)

    ## Down arrow — head outside.
    frame:
        xalign 0.5
        yalign 0.93
        background None
        button:
            background None
            hover_background None
            hover_sound "audio/sfx/hover_selectable.mp3"
            activate_sound "audio/sfx/click_selectable.mp3"
            action Return("outside")
            vbox:
                xalign 0.5
                spacing 4
                text "Head outside":
                    xalign 0.5
                    color "#e8e0d0cc"
                    hover_color "#ffffff"
                    size 22
                    font gui.name_text_font
                text "▼":
                    xalign 0.5
                    color "#e8e0d0cc"
                    hover_color "#ffffff"
                    size 28
                    font gui.name_text_font


## ── Barkeep ──────────────────────────────────────────────────────────────────

label day2_barkeep:

    show ch bartender profile default smiling with dissolve

    n "She's already looking at you when you reach the counter, the way she always seems to be."

    b "Slept well enough, I take it."
    b "There are a couple of merchants in from Bilgewater — came in last night after you'd gone up."
    b "Worth saying hello. People who travel that far usually have something interesting to offer, or need something found."
    b "They're just outside."

    menu:
        "I wanted to ask about someone.":
            call barkeep_ask_about
        "Just checking in.":
            b "Well. You know where to find me."

    hide ch bartender profile default smiling with dissolve
    return


## ── Lulu ─────────────────────────────────────────────────────────────────────

label day2_lulu:

    show ch lulu profile default with dissolve

    n "Lulu is already facing you as you approach, as though she heard you coming from across the room."
    n "Pix sits on her shoulder, pointing at you with the energy of someone who has been waiting to do exactly that."

    l "You slept! I could tell you were going to sleep well."
    l "You have a very restful face when you're unconscious."

    mc "That's... thanks."

    l "Pix noticed you come downstairs. He went to go tell me and I said I already knew."
    l "He was very put out about it."

    n "Pix makes a small, indignant sound."

    l "He'll recover."

    n "She pats the stool beside her. You sit."
    n "A flicker of motion from across the room — Poppy shifts her weight, gaze steady."
    n "She's not staring exactly. She's just... aware."

    mc "Is Poppy watching us?"

    l "Poppy watches everyone. It's her job."
    l "She watches you slightly more than everyone, which means she's decided you're worth the effort."

    n "She says it cheerfully, as though being kept under quiet surveillance is a compliment."

    menu:
        "What do you do during the day?":
            mc "What do you actually do during the day? When the bar's quiet like this?"

            l "Spells, mostly. Research. Pix and I have a project."
            l "We're trying to find out if you can enchant sound."
            l "Not just make noise magical — make the magic be the noise."
            l "We haven't gotten it right yet but we're very close."

            mc "What does 'close' look like?"

            l "The other day Pix laughed and it made a flower grow."
            l "We're not sure if that was us or just Pix, but we're counting it."

        "What's your read on this place?":
            mc "You've been here a while. What's your honest read on Bandle City?"

            l "It's small and loud and everyone knows everything about everyone."
            l "I wouldn't live anywhere else."

            n "She says it simply, without any wistfulness, the way you'd say the sky is blue."

            l "It has a heart. Most places don't."
            l "The Bandlewood keeps it honest. You can't get too comfortable when the forest is right there."

        "Tell me about Pix.":
            mc "Tell me about Pix. What is he, exactly?"

            l "He's Pix."
            l "I know that's not the answer you were looking for."

            n "She considers it for a moment, genuinely."

            l "He showed up when I was very small and we've been together since."
            l "I don't know what he is in the way you mean the question."
            l "But he knows things before they happen. He knew you were going to be important."

            mc "Important how?"

            l "He didn't specify. He usually doesn't."
            l "He said you had an interesting thread."

            n "Pix tilts his head at you, deeply satisfied with this description."

    n "She hops off the stool eventually, staff in hand, looking perfectly comfortable."

    l "Come find me if anything strange happens. Stranger than normal, I mean."
    l "Pix will know before you even get to me, but come find me anyway."

    n "She gives you one last look — warm, knowing, like she's checking a box she already knew would be checked."
    n "Pix glances back at you from her shoulder as she goes. His expression is hard to read."
    n "You're pretty sure he's pleased."

    hide ch lulu profile default with dissolve
    return


## ── Poppy ────────────────────────────────────────────────────────────────────

label day2_poppy:

    show ch poppy profile default with dissolve

    n "Poppy tracks you as you approach. She doesn't move from her post."

    p "Hey."

    mc "Hey. Slow morning?"

    p "Every morning is slow until it isn't."
    p "That's the job."

    n "She glances at the door, then back at you."

    p "You talk to Lulu?"

    mc "Yeah, just now."

    p "Mm."

    n "A pause. The kind that's doing something."

    p "She's good people. Just — keep it easy with her."
    p "She gets attached."

    n "She doesn't elaborate. You get the sense that's all you're going to get on that."

    mc "You look like you'd rather be somewhere else."

    p "I've got a session at the gym in an hour and I'm covering until Brea gets in."
    p "So yes."

    mc "What do you train?"

    p "Everything."
    n "She says it without any particular pride. Just as a fact."
    p "Hammer work, mostly. Some sparring."
    p "It's the only part of the day where nobody needs anything from me."

    n "She glances at the door again. Checks the room. Back to you."

    p "You should find something like that. Something physical."
    p "You're in rough shape. I can tell."

    n "She says it straightforwardly, no cruelty in it."

    p "The city will wear you down faster if you let yourself stay soft."

    menu:
        "Good advice.":
            mc "Fair enough. I'll think about it."
            p "Don't think about it. Do it."
            n "She turns back to the door. Conversation over."

        "Could you train me?":
            mc "Any chance you'd take on a student?"
            n "She looks at you. A full, considered look."
            p "Maybe. When you're not falling apart."
            p "Come back when you can move without looking like something the wood spat out."
            n "She turns back to the door. But there's something in it — not a dismissal, exactly."

    hide ch poppy profile default with dissolve
    return
