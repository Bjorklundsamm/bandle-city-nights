# narrative/ui/day_card.rpy
# Day transition card — shown at the start of each new morning.
#
# Usage in any morning label:
#   $ current_day += 1
#   call show_day_card
#
# The label increments nothing itself — the caller sets current_day first
# so dev menu jumps and future scripted skips stay accurate.


## ── Quotes ───────────────────────────────────────────────────────────────────
##
## Rotate through on each new day. All are plausibly motivational if you
## squint, and something else entirely if you don't.

init python:
    _day_card_quotes = [
        "Every morning is a fresh opportunity to rise to the occasion.",
        "The early bird gets the worm. The question is what you do with it.",
        "Don't let a single day go to waste. Wring everything out of it.",
        "Another day, another chance to leave someone breathless.",
        "A hard day's work always ends in deep, satisfying relief.",
        "Make it count. The nights are long but the days are longer.",
        "Push through the resistance. The payoff is always worth it.",
        "You only get thirty-one. Use every single one.",
        "Some days you lead. Some days you follow. Either way — commit.",
        "Leave nothing on the table. Or the floor. Or wherever.",
        "The city won't explore itself. Get out there.",
        "Pace yourself. It's a long month and you'll need your stamina.",
        "Do the thing you've been putting off. You'll feel much better after.",
        "A little effort goes a long way. A lot of effort goes further.",
        "The best experiences rarely happen indoors. Mostly.",
        "Don't be shy. Everyone's waiting for someone to make the first move.",
        "Today could be the day everything comes together. Or comes apart. Either's interesting.",
        "Breathe. Stretch. Go find something worth doing.",
        "A good day starts with intention and ends with exhaustion.",
        "You came this far. Might as well see how deep it goes.",
        "The only bad move is no move at all.",
        "Some doors only open if you knock. Some open if you just lean on them.",
        "Whatever you're after — it's closer than you think.",
        "Stay hungry. Stay curious. Stay hydrated.",
        "Make someone's day. It costs nothing and pays out endlessly.",
        "The city has a lot to offer. Most of it you haven't found yet.",
        "Every day is a gift. Unwrap it with enthusiasm.",
        "Fortune favors the bold. And the bold tend to have more fun.",
        "Don't overthink it. Just go.",
        "Last few days. Make them memorable.",
        "Final day. No regrets. Well — the good kind of regrets.",
    ]


## ── Screen ───────────────────────────────────────────────────────────────────

screen day_card(day, quote):
    zorder 900
    modal True

    ## Full black background — fades in via the screen's own ATL.
    add Solid("#000000"):
        alpha 0.0
        linear 0.6 alpha 1.0

    ## Content fades in slightly after the background.
    vbox:
        xalign 0.5
        yalign 0.44
        spacing 28
        alpha 0.0
        linear 0.8 alpha 1.0

        ## "Day X / 31"
        text "Day [day] / 31":
            xalign 0.5
            color "#e8e0d0"
            size 72
            font gui.name_text_font

        ## Days remaining
        text "[31 - day] days remaining":
            xalign 0.5
            color "#a09070"
            size 28
            font gui.name_text_font

        ## Divider
        add Solid("#a0907044") xsize 320 ysize 1 xalign 0.5

        ## Quote
        text "[quote]":
            xalign 0.5
            text_align 0.5
            color "#c8b88088"
            size 22
            font gui.name_text_font
            xmaximum 640


## ── Label ────────────────────────────────────────────────────────────────────

label show_day_card:

    python:
        _day_quote = _day_card_quotes[(current_day - 1) % len(_day_card_quotes)]

    show screen day_card(current_day, _day_quote)

    ## Hold long enough to read the quote comfortably.
    $ renpy.pause(3.2, hard=True)

    hide screen day_card with Dissolve(0.6)

    return
