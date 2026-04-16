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
    n "A flicker of motion from across the room — Poppy shifts her weight, gaze moving to Lulu."
    n "Not to the room. Not to the door. To Lulu specifically."

    mc "Is Poppy watching us?"

    l "Poppy is always watching me."
    l "Everyone is always watching me."

    n "She doesn't say it darkly. She says it the way you'd describe a persistent weather pattern."

    l "It comes from love. I know that. Poppy loves me and she's very good at it and I would not trade her for anything."

    n "A pause. Pix drifts off her shoulder and begins orbiting your head slowly."

    l "And I am going to lose my mind."

    mc "What?"

    l "There are things I want to know about."
    l "Things everyone else in this city apparently gets to know about freely and loudly and repeatedly based on what I hear through walls."

    n "She gestures vaguely at the ceiling. The rooms above. The inn in general."

    l "Things that seem to make everyone absolutely feral and I have no idea why because nobody will explain it to me properly."
    l "I ask questions and people change the subject. Or they laugh nervously. Or they look at Poppy."

    mc "What kind of things?"

    l "The kind of things Katarina was doing to her latest victim last night."

    n "She watches you for a reaction with enormous interest."

    l "See, you heard it too. You went a very specific color just now."
    l "That's the reaction. Everyone does that. And nobody will tell me why."

    n "Pix lands back on her shoulder and pats her ear once, sympathetically."

    l "I've read about it. Theory is very thorough."
    l "But theory and practical are different things and I am very much a practical learner."

    mc "You've — read about it?"

    l "Extensively."

    n "She says it without a trace of embarrassment. With, if anything, mild academic pride."

    l "I understand the mechanics. I understand the vocabulary. I just haven't — experienced any of it."
    l "Because every single time there's even a possibility, someone decides I need protecting and the possibility disappears."

    n "She looks across the room at Poppy. Poppy, as if sensing this, looks back immediately."
    n "Lulu waves. Poppy does not wave back."

    l "She means well."

    n "The frustration underneath it is real — not hot, not sharp, just old. The kind that's been sitting a long time."

    l "I'm not fragile. I'm not new. I've done things most people in this city couldn't imagine and I've done them alone."
    l "I just want — I want one thing that everyone else gets to have, and I want somebody to take it seriously instead of changing the subject."

    n "She looks back at you. Direct, steady, nothing coy about it."

    l "You're not changing the subject."

    mc "No."

    l "That's interesting."

    n "Pix tilts toward you with an expression that would, on a creature with a face, be a raised eyebrow."

    l "The problem is Poppy. She's here every day. Very dedicated."
    l "Very committed to making sure nothing interesting happens to me."

    n "She picks up her drink. Takes a slow sip."

    l "She does take days off sometimes. She mentioned the gym."
    l "I always know when she's gone because the room gets about thirty percent less supervised."

    n "She sets the drink down."

    l "Hypothetically, if someone wanted to — teach me things — practically, properly, without anyone changing the subject..."
    l "That would be the window."

    n "She says 'hypothetically' the way people say it when they mean the opposite."

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

    n "She hops off the stool eventually, staff in hand, glancing briefly toward Poppy — who is, of course, still watching."

    l "One of these days she's going to take a day off."
    l "Go do her hammer thing. Be somewhere that isn't here for a few hours."

    n "She says it casually. Conversationally. But Pix tilts toward you with a very specific kind of attention."

    l "I have a list."

    mc "A list of what?"

    l "Things I've been meaning to get around to."

    n "She smiles — the bright, uncomplicated one she uses when she's saying exactly what she means and counting on you not to realise it."

    l "Come find me if anything strange happens."
    l "Or if Poppy leaves early."

    n "Pix watches you from her shoulder as she goes. Whatever he's thinking, he keeps it to himself."
    n "For once."

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
