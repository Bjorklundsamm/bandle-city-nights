# narrative/day2/day2_tavern.rpy
# Day 2 daytime tavern: the hub loop and interactions with
# Barkeep (Bilgewater tip), Lulu, and Poppy.
#
# Exits to day2_outside_loop when player heads outside.


## ── Day 2 tavern loop ────────────────────────────────────────────────────────

label day2_tavern_loop:

    scene bg tavern empty - daytime with Dissolve(1.0)
    show screen inventory_button
    play music "audio/music/impish_delight.mp3" fadein 2.0 volume 0.5

    $ _day2_tavern_running = True

    while _day2_tavern_running:
        window hide
        call screen day2_tavern_hub
        window show

        if _return == "outside":
            $ _day2_tavern_running = False

        elif _return == "leave":
            call day2_tavern_nudge_outside

        elif _return == "barkeep":
            call day2_barkeep

        elif _return == "lulu":
            call day2_lulu

        elif _return == "poppy":
            call day2_poppy

    stop music fadeout 1.5

    jump day2_outside_loop


screen day2_tavern_hub():
    default outside_hovered = False
    default room_hovered = False
    zorder 100
    modal True

    ## Barkeep — behind the bar, left side
    button:
        style "patron_button"
        focus_mask True
        xsize 1920
        ysize 1088
        action Return("barkeep")
        hover_sound "audio/sfx/hover_selectable.mp3"
        activate_sound "audio/sfx/click_selectable.mp3"
        add "ch barkeep tavern position" at patron_zoom

    ## Lulu — seated at bar, center (only while she hasn't left for the day)
    if lulu_in_tavern:
        button:
            style "patron_button"
            focus_mask True
            xsize 1920
            ysize 1088
            action Return("lulu")
            hover_sound "audio/sfx/hover_selectable.mp3"
            activate_sound "audio/sfx/click_selectable.mp3"
            add "ch lulu tavern position" at patron_zoom

    ## Poppy — near the door, right side
    button:
        style "patron_button"
        focus_mask True
        xsize 1920
        ysize 1088
        action Return("poppy")
        hover_sound "audio/sfx/hover_selectable.mp3"
        activate_sound "audio/sfx/click_selectable.mp3"
        add "ch poppy tavern position" at patron_zoom

    ## Down arrow — head outside.
    button:
        xalign 0.5
        yalign 0.93
        background None
        hover_background Frame("gui/fade_choice_bar.png", 80, 0)
        padding (14, 8)
        hover_sound "audio/sfx/hover_selectable.mp3"
        activate_sound "audio/sfx/click_selectable.mp3"
        hovered SetScreenVariable("outside_hovered", True)
        unhovered SetScreenVariable("outside_hovered", False)
        action Return("outside")
        vbox:
            xalign 0.5
            spacing 4
            text "Head outside":
                xalign 0.5
                color "#e8e0d000"
                hover_color "#e8e0d0ee"
                size 22
                font gui.name_text_font
            if outside_hovered:
                add Transform("pointer arrow", zoom=0.5, rotate=90, alpha=0.6) at nav_arrow_bounce xalign 0.5
            else:
                add Transform("pointer arrow", zoom=0.5, rotate=90, alpha=0.6) xalign 0.5

    ## Return to your room — always present; redirects outside during day 2.
    button:
        xalign 0.0
        yalign 1.0
        background None
        hover_background Frame("gui/fade_choice_bar.png", 80, 0)
        padding (14, 8)
        hover_sound "audio/sfx/hover_selectable.mp3"
        activate_sound "audio/sfx/click_selectable.mp3"
        hovered SetScreenVariable("room_hovered", True)
        unhovered SetScreenVariable("room_hovered", False)
        action Return("leave")
        hbox:
            spacing 10
            yalign 0.5
            if room_hovered:
                add Transform("pointer arrow", zoom=0.63, rotate=135, alpha=0.6) at nav_arrow_bounce_diag yalign 0.5
            else:
                add Transform("pointer arrow", zoom=0.63, rotate=135, alpha=0.6) yalign 0.5
            text "Return to your room":
                size 22
                color "#d4c4a800"
                hover_color "#d4c4a8ee"


## ── Room nudge ───────────────────────────────────────────────────────────────

label day2_tavern_nudge_outside:

    n "You glance toward the stairs."
    n "There's nothing waiting for you up there right now."
    n "You promised Barkeep you'd make yourself useful around town. Better get to it."
    return


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

    l "You slept well! I checked."

    mc "You — what?"

    l "I sent Pix. He said you were very still."
    l "Some people make faces. You didn't make any faces."

    n "She says this like it is a perfectly normal thing to have done. Pix offers nothing in his defense."

    l "I wanted to see what you looked like when you weren't doing anything. It's important data."

    mc "...About me specifically?"

    l "Mm-hm!"

    n "No elaboration. Completely cheerful about it."

    n "She pats the stool beside her. You sit."
    n "A flicker of motion from across the room — Poppy shifts her weight, gaze moving to Lulu."
    n "Not to the room. Not to the door. To Lulu specifically."

    mc "Is Poppy watching us?"

    l "Poppy is always watching me."
    l "Everyone is always watching me."

    n "She doesn't say it darkly. She says it the way you'd describe a persistent weather pattern."

    l "It comes from love. I know that. Poppy loves me and she's very good at it."

    n "A pause. Pix drifts off her shoulder and begins a slow orbit of your head."

    l "And I am going to lose my mind."

    mc "What?"

    l "There are things I want to know about."
    l "Things everyone else in this city apparently gets to know about — freely, loudly, repeatedly."
    l "Based on what I hear through walls."

    n "She gestures at the ceiling. The rooms above. The inn in general."

    l "Things that make everyone absolutely feral and I have no idea why because nobody explains it."
    l "I ask. People change the subject. Or laugh nervously. Or look at Poppy."

    mc "What kind of things?"

    l "The kind of things Katarina was doing to her latest visitor last night."

    n "She watches you for a reaction with complete, scientific interest."

    l "See. You went a very specific color just now."
    l "That is the reaction. Everyone does that. And nobody will tell me why."

    n "Pix lands back on her shoulder and pats her ear once."

    l "I've read about it. My theories are very thorough."
    l "But theory and practice are different things and I am very much a practical learner."

    mc "You've — read about it?"

    l "Extensively."

    l "I understand the mechanics. I understand the vocabulary."
    l "I just haven't — experienced any of it."

    n "She looks across the room. Poppy looks back immediately, the way she always does."
    n "Lulu waves. Poppy does not wave back."

    l "She means well."

    n "The frustration is real — not hot, not sharp. Just old. The kind that's been sitting long enough."

    l "I am not new to this world. I have been in it longer than most people in this darn village."
    l "I have done things alone that would make half this village's brains melt!"

    l "But I walk in here and everyone decides I need minding."
    l "I get sent home before the interesting hours."
    l "And the interesting hours are the whole point."

    mc "How long has it been like that?"

    l "Here? Since long, longggggg before you were born bucko. Us magic folk age a bit more gracefully."
    l "The village is very good at deciding what people need without asking them."

    n "A pause. Pix does something small and pointed near your ear."

    l "They think I'm a girl."
    l "They look at me and they see a tiny little girl and they act accordingly."
    l "I am not! I am older than most of the people in... in... in probably most the world!"
    l "I am not fragile. I am not confused. I am just — annoyed."

    n "She picks up her drink. Takes a slow sip."

    l "All the other yordle women come back from the evenings ranting."
    l "In very specific terms. Very specific."

    mc "About what?"

    l "About you. About humans in general. You'd be surprised how many Yordles have certain... preferences for humans."
    l "About a particular — attribute — that apparently makes everyone lose their composure entirely."

    n "She is not blushing. She is delivering this as field notes."

    l "I have heard this rant from many sources. In detail. With comparisons."
    l "I have no firsthand data and it is driving me actually mad."

    n "She sets the drink down and looks at you directly."
    n "Not performing. Not hinting. Just looking."

    l "You're not changing the subject."

    mc "No."

    l "Good."

    n "Pix tilts toward you with an expression that is, on a creature his size, unmistakably pointed."

    l "The problem is Poppy."
    l "She is here every day. She is very dedicated."
    l "She has decided protecting me from interesting things is a service she provides."

    n "She glances at Poppy again. Poppy has not moved."

    l "She does take days off. She has a gym she likes."
    l "And when she's gone, let's just say there is a lot less concern about where I sneak off to. And who I sneak off with."

    # [GEN START]

    # [EXPLICIT START]
    l "The next time she's not here, I'm not going home early."
    l "I'm going with you."
    l "And we are going to fill a notable gap in my education."

    n "No coyness. No question in her voice."
    n "This is a presentation. You are the subject of a study."

    l "Is that acceptable?"

    # [EXPLICIT END]

    menu:
        "Sorry Lulu, I think... Mabye someone else.":
            $ affection_lulu -= 1
            mc "I don't think I'm the right person for this."

            n "Something crosses her face. Not hurt — more like someone gave her an answer she's heard before and she is choosing not to argue it."

            l "Right."

            n "She picks up her drink. Takes a sip."

            l "Everyone finds a reason."
            l "I hoped you'd be different."

            n "She doesn't push. She doesn't explain herself. She's heard enough versions of this that the energy's gone out of it."
            n "Pix drifts back to her shoulder and sits there quietly."

            l "Enjoy your morning."

            n "She hops off the stool, staff in hand. Poppy tracks her across the room — always."
            n "Pix watches you from her shoulder as she goes."

        "So just find some time she's gone? Deal.":
            $ affection_lulu += 1
            mc "When Poppy takes that day off — come find me."

            n "She looks at you for a moment. The bright, evaluating kind of look."
            n "Then she smiles — wide, genuine, nothing complicated about it."

            l "Good."

            n "She picks up her drink and finishes it in one go."

            l "I'll be patient, kinda. But you better not forget."
            l "And be excited, I've got a list."
            
            mc "A list?"

            l """
            Oh yeah. I'm not gonna let you go until all my curiousities are

            Oh yeah. I'm not gonna let you go until all my curiousities are.

            Oh yeah. I'm not gonna let you go until all my curiousities are..

            Oh yeah. I'm not gonna let you go until all my curiousities are...
            """
            l "Satisfied."

            n "She hops off the stool and grabs her staff."
            n "Pix darts from her shoulder to hover briefly in front of your face — inspecting something — then rejoins her."
            n "Poppy watches her go from across the room and sighs once, quietly."

    # [SCENE NOTE: Lulu, Poppy-guarded tavern, daytime. Lulu names what she actually wants — directly, in her matter-of-fact idiom. She's not seducing, she's stating. She wants you to take her to your room the next time Poppy isn't here. She names the specific thing she wants from the rant-reports: to finally see and explore a cock. Her framing is entirely her own — fae-matter-of-fact, no nervousness, maybe even slight impatience at how long this has taken. Ren'Py format: l "..." lines. No narration lines in this block. 4-6 lines of dialogue.]

    $ lulu_in_tavern = False
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
