# narrative/day2/day2_morning.rpy
# Day 2 morning: waking up, the cracked door in the hallway,
# Katarina's room peek, and the loaded dice theft.
#
# Flow: morning_day_2 → (optional) morning_day_2_peek_katarina
#       → (optional) morning_day_2_steal_dice → morning_day_2_downstairs
#       → day2_tavern_loop


label morning_day_2:

    $ current_day = 2
    call show_day_card

    stop ambient fadeout 1.5
    scene bg bedroom default with Dissolve(2.0)
    play ambient "audio/sfx/Tavern_ambience.mp3" fadein 2.0 volume 0.45

    n "Light. Not the desperate gray of dawn — real light, soft and amber, pressing through the gap under the door."
    n "You lie still for a moment, listening. The inn is quieter than last night but not silent."
    n "The low hum of the kitchen. Someone moving around downstairs."

    n "You sit up. Your body registers every complaint about yesterday in rough order of severity."
    n "Still, you slept. Actually slept — the kind that erases things."

    n "You push yourself upright and reach for the door."

    if met_katarina:

        n "The hallway is mostly empty."
        n "Mostly."
        n "Two doors down, one is sitting open a crack — not all the way, not latched."
        n "Just... not closed."

        n "The memory surfaces slowly. Last night. The sounds through the wall."
        n "You glance down the hall. No one around."

        menu:
            "Peek in.":
                jump morning_day_2_peek_katarina
            "Leave it alone.":
                n "None of your business. You head for the stairs."
                jump morning_day_2_downstairs

    else:

        jump morning_day_2_downstairs


label morning_day_2_peek_katarina:

    # MISSING: bg patron room — generic inn bedroom, dim, curtains drawn.
    # Darker/messier read than bg bedroom default. Reuse for any patron room visit.
    show screen ph_bg("bg patron room")

    n "You ease forward, just enough to see through the gap."
    n "The room is dim — curtains still drawn, the kind of dark a person makes deliberately."

    n "A shape on the bed. Sprawled out, completely unconscious, one arm hanging off the edge."
    n "Red hair. The unmistakable stillness of someone who ran themselves completely dry."

    n "Katarina."

    n "The room tells the story on its own."
    n "Two mugs. A chair at a bad angle. And on the small table by the window — Tristana's money, you'd guess."
    n "Whatever she'd promised herself last night, she'd collected."

    n "You're about to pull back when something on the table catches your eye."

    # MISSING: bt dice — small worn pair of dice on the table corner.
    # katarina_room_peek screen: click dice → Return("bt dice"), step back → Return("leave").
    call screen katarina_room_peek

    hide screen ph_sprite
    hide screen ph_bg

    if _return == "bt dice":

        n "A pair of dice, sitting in plain view on the corner of the table."
        n "Small. Worn. The kind that have seen a lot of hands."
        n "One of them is sitting at a very specific angle, and something about the weight looks... off."

        menu:
            "Take them.":
                jump morning_day_2_steal_dice
            "Leave them. Not worth it.":
                n "You pull back from the door before your luck runs out."

    jump morning_day_2_downstairs


screen katarina_room_peek():
    ## Overlaid on the patron room ph_bg.
    ## bt dice placeholder — table position right-center.
    ## "Step back" — bottom-left exits without touching anything.
    zorder 200

    # MISSING: ch katarina sleeping — fully dressed, sprawled on bed,
    # one arm off the edge, completely out cold.
    use ph_sprite("ch katarina sleeping", xalign=0.5, yalign=1.0)

    # MISSING: bt dice — small worn dice on table corner.
    use ph_button("bt dice", xalign=0.72, yalign=0.52)

    textbutton "Step back":
        xalign 0.02
        yalign 0.96
        text_color "#e8e0d0cc"
        text_hover_color "#ffffff"
        hover_sound "audio/sfx/hover_selectable.mp3"
        action Return("leave")


label morning_day_2_steal_dice:

    n "Your hand moves before your better judgment can catch up."
    n "Through the gap. Slow. Two fingers."
    n "The dice are heavier than they look."

    n "You pull back. Ease the door to exactly where it was."
    n "Katarina doesn't move."

    n "You hold your breath all the way to the end of the hallway."

    $ has_loaded_dice = True

    show screen system_overlay

    s "You've obtained: Loaded Dice"
    s "A worn pair of dice lifted from Katarina's table."
    s "They're weighted — subtly, expertly. They won't guarantee anything, but they'll tilt the odds."
    s "Don't use them too often. Katarina counts everything."

    call screen system_got_it

    hide screen system_overlay

    jump morning_day_2_downstairs


label morning_day_2_downstairs:

    scene bg black with Dissolve(0.8)
    stop ambient fadeout 1.0

    n "You head downstairs."

    jump day2_tavern_loop
