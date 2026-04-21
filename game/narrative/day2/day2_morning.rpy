# narrative/day2/day2_morning.rpy
# Day 2 morning: waking up, the cracked door in the hallway,
# Katarina's room peek, and the loaded dice theft.
#
# Flow: morning_day_2 → (optional) morning_day_2_peek_katarina
#       → (optional) morning_day_2_steal_dice → morning_day_2_downstairs
#       → day2_tavern_loop


label morning_day_2:

    $ current_day = 2
    $ energy = 3
    call show_day_card

    stop ambient fadeout 1.5
    scene bg bedroom default with Dissolve(2.0)
    play ambient "audio/sfx/Tavern_ambience.mp3" fadein 2.0 volume 0.45

    n "Light. Not the desperate gray of dawn — real light, soft and amber, pressing through the gap under the door."
    n "You lie still for a moment, listening. The inn is quieter than last night but not silent."
    n "The low hum of the kitchen. Someone moving around downstairs."

    n "You sit up. Your body registers every complaint about yesterday in rough order of severity."
    n "Still, you slept. Actually slept — the kind that erases things."

    $ constitution = 2
    show screen system_overlay
    show screen constitution_arrow
    s "Your body has recovered a little. Rest and a good meal each day will keep you on your feet."
    s "Don't skip either if you can help it."
    call screen system_got_it
    hide screen constitution_arrow
    hide screen system_overlay

    n "You push yourself upright and reach for the door."

    scene bg black with dissolve

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

    scene bg patron bedroom with dissolve
    show screen katarina_room_display()

    n "You ease forward. The room is dim — curtains drawn, deliberately dark."
    n "A shape on the bed. Sprawled, arm hanging off the edge. Red hair."
    n "Katarina."
    n "Two mugs. A chair at a bad angle. Tristana's money on the table, you'd guess."
    n "Whatever she'd promised herself last night, she'd collected."

    call screen katarina_room_peek

    if _return == "bt dice":

        n "A pair of dice on the corner of the table. Small. Worn smooth."

        call screen katarina_room_peek_dice

        if _return == "steal":
            show screen katarina_room_display(False)
            jump morning_day_2_steal_dice

    hide screen katarina_room_display
    jump morning_day_2_downstairs


screen katarina_room_display(show_dice=True):
    ## Non-interactive overlay: Katarina and dice visible during narration,
    ## before the player has any clickable options.
    ## Pass show_dice=False to hide the dice without removing Katarina.
    zorder 200
    add "ch kat sleeping position" xalign 0.0 yalign 0.0
    if show_dice:
        add "bt dice" at dice_hover xalign 0.0 yalign 0.0


screen katarina_room_peek():
    ## First look into Katarina's room.
    ## "Time to get out of here" is the obvious exit — lower left.
    ## The dice button sits quietly in the lower right for observant players.
    zorder 200

    add "ch kat sleeping position" xalign 0.0 yalign 0.0

    ## Subtle placement — lower right, easy to miss.
    imagebutton:
        idle "bt dice" at dice_hover
        focus_mask True
        xalign 0.0
        yalign 0.0
        action Return("bt dice")
        hover_sound "audio/sfx/hover_selectable.mp3"
        activate_sound "audio/sfx/click_selectable.mp3"

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        button:
            background None
            hover_background None
            padding (0, 0)
            action Return("leave")
            hover_sound "audio/sfx/hover_selectable.mp3"
            activate_sound "audio/sfx/click_selectable.mp3"
            fixed:
                xsize 640
                ysize 54
                add "gui/fade_choice_bar.png" xpos 0 ypos 0
                text "Time to get out of here before she notices.":
                    xalign 0.5
                    yalign 0.5
                    color "#d4c4a8"
                    hover_color "#ffffff"
                    size 26
                    font gui.choice_button_text_font
                    text_align 0.5


screen katarina_room_peek_dice():
    ## Second look — player has spotted the dice.
    ## Now two options: leave cleanly or take them.
    ## Dice are visible via katarina_room_display but no longer clickable.
    zorder 200

    add "ch kat sleeping position" xalign 0.0 yalign 0.0

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        button:
            background None
            hover_background None
            padding (0, 0)
            action Return("steal")
            hover_sound "audio/sfx/hover_selectable.mp3"
            activate_sound "audio/sfx/click_selectable.mp3"
            fixed:
                xsize 640
                ysize 54
                add "gui/fade_choice_bar.png" xpos 0 ypos 0
                text "Take the dice.":
                    xalign 0.5
                    yalign 0.5
                    color "#d4c4a8"
                    hover_color "#ffffff"
                    size 26
                    font gui.choice_button_text_font
                    text_align 0.5
        button:
            background None
            hover_background None
            padding (0, 0)
            action Return("leave")
            hover_sound "audio/sfx/hover_selectable.mp3"
            activate_sound "audio/sfx/click_selectable.mp3"
            fixed:
                xsize 640
                ysize 54
                add "gui/fade_choice_bar.png" xpos 0 ypos 0
                text "Time to get out of here before she notices.":
                    xalign 0.5
                    yalign 0.5
                    color "#d4c4a8"
                    hover_color "#ffffff"
                    size 26
                    font gui.choice_button_text_font
                    text_align 0.5


label morning_day_2_steal_dice:

    n "Your hand moves before your better judgment can catch up."
    n "Through the gap. Slow. Two fingers. The dice are heavier than they look."
    n "You ease the door back to exactly where it was. Katarina doesn't move."
    n "You hold your breath all the way to the end of the hallway."

    $ has_loaded_dice = True

    show screen system_overlay

    s "You've obtained: Loaded Dice"
    s "A pair of dice stolen from a famed Noxian assassin."
    s "Don't overuse them. Even drunks and fools can catch on when the fix is too obvious."

    call screen system_got_it

    hide screen system_overlay

    jump morning_day_2_downstairs


label morning_day_2_downstairs:

    hide screen katarina_room_display
    scene bg black with Dissolve(0.8)
    stop ambient fadeout 1.0

    n "You head downstairs."

    jump day2_tavern_loop
