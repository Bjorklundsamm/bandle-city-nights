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
        "You'd be surprised what fits where, if everyone involved is enthusiastic enough.",
        "The claws are part of it. Don't ask them to hold back on your account.",
        "Small doesn't mean gentle. It means concentrated.",
        "The bite marks will fade. The memory won't.",
        "Go slow at first. Then don't.",
        "Something half your size wanting all of you is its own kind of flattering.",
        "The ones raised wild don't ask permission. They just take. Keep up.",
        "Fur is warmer than you expect. So is everything else.",
        "She'll scratch. That's not a warning — it's a review.",
        "The gap is significant. Close it anyway. That's the whole point.",
        "They were feral long before they were charming. Some nights, only one of those shows.",
        "When something that small looks up at you like that, you stop thinking about the logistics.",
        "A tail that lashes isn't angry. Learn to read the difference.",
        "The sounds they make aren't something you'll find a word for. That's fine.",
        "She will fit. She always fits. Don't make it weird by mentioning it.",
        "Teeth are a love language here. Adjust your expectations accordingly.",
        "The ones built low to the ground have the strongest grip. You'll understand soon.",
        "Don't go easy. They don't want easy. They want to feel it.",
        "The instinct is older than language. Stop using language and just follow it.",
        "Small hands know exactly what they're doing. Stop being surprised.",
        "When something feral decides you're worth keeping around, you'll know. You'll have marks.",
        "Half your height doesn't mean half anything else.",
        "They purr. They also bite. Same situation, sometimes simultaneously.",
        "The claws retract when they want to. They'll let you know when they want to.",
        "She doesn't need your help reaching. She'll climb if she wants to.",
        "The ones with ears that move are listening to more than your words. Mind your breathing.",
        "Going soft gets you nothing here. That goes for attitude as much as anything.",
        "What you think is too much is usually exactly enough.",
        "They don't do careful. They do thorough. There's a difference.",
        "You're almost out of time. Stop being polite about what you want.",
        "Last day. The ones worth remembering were never the ones you were cautious with.",
    ]


## ── Screen ───────────────────────────────────────────────────────────────────

screen day_card(day, quote):
    zorder 900

    ## Full black background — fades in via the screen's own ATL.
    add Solid("#000000") at transform:
        alpha 0.0
        linear 0.6 alpha 1.0

    ## Content fades in slightly after the background.
    vbox:
        at transform:
            alpha 0.0
            linear 0.8 alpha 1.0
        xalign 0.5
        yalign 0.44
        spacing 28

        ## "Day X / 31"
        text "Day [day] / 31":
            xalign 0.5
            color "#e8e0d0"
            size 72
            font gui.number_font

        ## Days remaining
        text "[31 - day + 1] days remaining":
            xalign 0.5
            color "#a09070"
            size 28
            font gui.number_font

        ## Divider
        add Solid("#a0907044") xsize 320 ysize 1 xalign 0.5

        ## Quote
        text "[quote]":
            xalign 0.5
            text_align 0.5
            color "#c8b88088"
            size 22
            font gui.number_font
            xmaximum 1760


## ── Label ────────────────────────────────────────────────────────────────────

label show_day_card:

    python:
        _day_quote = _day_card_quotes[(current_day - 1) % len(_day_card_quotes)]

    show screen day_card(current_day, _day_quote)

    ## Click to advance.
    $ renpy.pause()

    hide screen day_card with Dissolve(0.6)

    return
