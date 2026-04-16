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
## Shown on each new day. Randomized via a persistent shuffle so the order
## is different every playthrough but consistent within one.

init python:
    _day_card_quotes = [
        ## ── Originals ────────────────────────────────────────────────────────
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

        ## ── Size difference ──────────────────────────────────────────────────
        "She's half your size and twice your problem. That's not a complaint.",
        "You'll need to crouch. You'll need to lift. You will not need to be asked twice.",
        "The math doesn't work on paper. Work it out in practice.",
        "Don't apologize for your size. They picked you anyway. That's the whole conversation.",
        "She'll use your collarbone as a chin rest. Do not act like this is a hardship.",
        "You could wrap both hands around her waist. She will not find this alarming.",
        "The size difference means someone is always being lifted. Accept that you will be the one lifting.",
        "She fits under your chin perfectly. She's been aware of this the entire time.",
        "Everything about this is technically impractical. It's also technically irresistible.",
        "When she climbs you like you're furniture, don't try to help. Just stand there.",
        "She's going to use your shoulder for leverage. Give her the shoulder.",
        "Being held down by something a third your size requires a very specific mental adjustment.",
        "The reach differential is a feature. Work out what it opens up.",
        "You'll feel it in the morning. Good.",
        "The look on their face when they realize you're serious — that's the moment.",
        "When she wraps both hands around one of yours, try to stay calm about it.",
        "She can sit in your lap and still reach everything she's after. Don't ask how.",
        "When she stands on your foot to get level with your face, just let her.",
        "She climbed onto the table to be taller than you. The message was received.",
        "She has turned your height into a logistics advantage. Mostly for herself.",
        "Picking her up to make a point is fine. Having her immediately take charge from up there: also fine.",
        "You thought your reach would be useful. She's already past it.",
        "She will figure out the geometry. Your job is to hold still.",
        "The stacking order is: her on top. Always. This is non-negotiable and you've already accepted it.",
        "Twice your age in instinct, a third your size in patience. She will outlast you.",
        "She ran you down. You were technically faster. This will bother you for a while.",
        "The one standing on the barstool to be at eye level with you is the one in charge. Accept this.",
        "Your size advantage has not once been relevant. Make peace with this.",
        "You thought the short one would be easy to manage. How's that going.",

        ## ── Feral / beast / anthro ───────────────────────────────────────────
        "The ones raised in the Bandlewood don't know the word 'restrained.' This is not a problem.",
        "Feral isn't a warning. For some of you, it's the entire appeal.",
        "She will mark you. Scent, scratch, bite — whichever she decides. You don't get a vote.",
        "When something that hunts for fun turns that same focus on you, you'll understand the difference.",
        "The sniff before the bite is not inspection. It's appreciation.",
        "They navigate by scent. Yours has been noted and filed.",
        "Feral instinct has one setting: all the way. Adjust your schedule accordingly.",
        "The ears flatten when they're focused. You'll learn what they flatten for.",
        "She's been tracking you. Not following — tracking. Know the difference.",
        "The growl is not a warning. You'll know the warning when it comes. This is enthusiasm.",
        "Wild things don't do foreplay. They do commitment. Keep up.",
        "When something built to hunt decides you're what it wants, be very still. Then be very not still.",
        "She catalogued your scent at the bar three nights ago. You're only just catching up.",
        "The instincts don't switch off in a bedroom. If anything, they sharpen.",
        "You're slower, bigger, and completely unable to climb. They find this adorable.",
        "They pounce first and ask questions never. This is not a design flaw.",
        "The fur is not incidental. It is involved. Accept this and move forward.",
        "When she pins you with one hand, remember she could use both.",
        "The ones who move on all fours in the morning are the same ones who keep up at night.",
        "Fangs are not decorative. Neither is the way she uses them.",
        "To something raised in the wood, you're exotic. Use this information responsibly.",
        "You're the only human in her range. She has taken this as a personal project.",
        "The novelty of your species has been scientifically appreciated. Multiple times.",
        "She's never seen one of you this close before. She's making up for lost time.",
        "You're big, slow, hairless, and fascinating. Welcome to being the interesting one for once.",
        "You don't have the reflexes for this. She finds this charming and also convenient.",
        "The hands without claws were a surprise. She's been finding uses for them.",
        "The appetite here has nothing to do with the kitchen. Budget accordingly.",
        "She looked at you the way something looks at a meal it's been patient about.",
        "She's been building up to this. You were the last to know.",

        ## ── Claws / teeth / grip ─────────────────────────────────────────────
        "The claws leave lines. You'll show someone eventually. They'll want context.",
        "Grip strength scales unexpectedly in this city. You've been warned since day one.",
        "When she bites — and she will — notice she aimed carefully.",
        "What she can do with three fingers would take you all five. Don't ask for a demonstration unless you mean it.",
        "The hands are small. The grip is not. This paradox is very well-documented locally.",
        "She has claws. She keeps them. Don't suggest otherwise.",
        "Those teeth were made for something. You're starting to understand what.",
        "A claw-mark in the right place is a dedication, not a complaint.",
        "The strength is in the grip, not the size. A lesson you'll remember specifically.",
        "She could crack a walnut with that handshake. Keep this in mind going forward.",
        "The bite is the compliment. The gentle bite is the request for more.",

        ## ── Climbing / reach ─────────────────────────────────────────────────
        "She will climb you. Treat this as a compliment.",
        "When she needs something off the shelf, she'll use you as the shelf. Be useful.",
        "Don't reach down to help. She doesn't need it. She's already there.",
        "The ones too short to see over the bar have already seen everything that matters.",
        "She'll use your knee as a step, your hip as a handhold, your shoulder as a seat. Relax.",
        "When something half your height launches itself at you, catch it. This is mandatory.",
        "She got there before you and she's been waiting. Keep up.",
        "She'll wrap her legs around something of yours that she can reach. This is efficient.",
        "You'll need to hold her up for most of this. You will not complain.",
        "When she hooks her heels behind you and refuses to let go, the correct response is nothing.",

        ## ── Tail ─────────────────────────────────────────────────────────────
        "A lashing tail during conversation means something different from a lashing tail during everything else.",
        "When the tail wraps around your wrist, that is a statement of intent.",
        "The tail is a second opinion. It often disagrees with what she's saying. Trust the tail.",
        "She says she's fine. Her tail has filed a rebuttal.",
        "The tail wag is not cuteness. It is a countdown.",
        "It'll coil around things. This is not accidental. None of it is accidental.",
        "The tail position tells you more than her face will. Read the tail first.",
        "When both the tail and the ears go still, you have her complete and undivided attention.",
        "She's prehensile in ways that are not publicly documented.",

        ## ── Ears ─────────────────────────────────────────────────────────────
        "Those ears catch everything, including the parts of your voice you didn't know were audible.",
        "When both ears swivel toward you, you have her complete attention. Try not to waste it.",
        "The ears pin back right before the pounce. This is your only warning.",
        "She hears your heartbeat. She knows it changed. She has filed this information.",
        "The ears flatten for two things: anger and focus. Learn which is which.",
        "The ears know you're nervous. They've known since you walked in. She hasn't mentioned it yet.",
        "Everything you weren't saying was very loud. She heard all of it.",

        ## ── Scent / marking ──────────────────────────────────────────────────
        "You smell like something that stayed. She's decided she's fine with that.",
        "She'll smell you before she sees you. She already has.",
        "Your scent has been matched to your face, your habits, and something more specific.",
        "They mark territory. Eventually you'll understand what the territory includes.",
        "She knows exactly what you had for breakfast. She found the other thing more interesting.",
        "The nuzzle is not affection. It's inventory. Also affection.",
        "Being chosen by something feral has a permanence to it. Just so you know.",
        "She's put her scent on you. Metaphorically. And also slightly literally.",
        "Territory in this city isn't land. Adjust your understanding of what's been claimed.",
        "You've been claimed in a language you don't speak yet. You'll understand it eventually.",
        "She's decided you're hers. This was a unilateral decision. She will not be revising it.",
        "The possessiveness is not jealousy. It's taxonomy. You've been classified.",

        ## ── Sounds ───────────────────────────────────────────────────────────
        "The sounds they make are not language. They are also not nothing. Pay attention.",
        "The chirp means good. The trill means very good. The — actually, you'll know that one.",
        "They purr when comfortable. They also purr when hunting. Same muscle. Different context.",
        "The chittering isn't laughter. It's something worse and much better.",
        "When she goes quiet, that's actually louder.",
        "That sound has no phonetic equivalent in your language. This is a gap in your education.",
        "The sounds in the room next door were educational. You retain the lesson.",
        "She's making sounds that aren't in any language. You understand every single one.",

        ## ── Yordle-specific ──────────────────────────────────────────────────
        "Yordles are built different. This is not a metaphor. It is also a metaphor.",
        "Don't assume small species means small anything. The data refutes this.",
        "She has lived three times your years and has very specific ideas about what she wants.",
        "What Yordles lack in altitude they make up in grip, stamina, and intent.",
        "She's older than the city. She knows exactly what she's doing. Keep up.",
        "The ones who look young usually aren't. The ones who seem gentle usually aren't either.",
        "Compact builds concentrate things. This is physics. Also this is a personal observation.",
        "The magic is involved. That's all the explanation you're getting.",
        "She can hex things. She has decided you are a thing worth hexing. Congratulations.",
        "Bandle City runs on a different clock. What looks like patience is really anticipation.",

        ## ── Pack / social ────────────────────────────────────────────────────
        "Being accepted by a pack is not subtle. There are ceremonies. You have begun them.",
        "She introduced you to someone who matters. In Bandle City, that's a proposal.",
        "The others have been watching to see if you last. You're still here. They've noted this.",
        "Being vouched for by something feral means something specific. Find out what.",
        "The social structure here is: whoever bites first, and then everyone else.",

        ## ── Overwhelmed / in over your head ──────────────────────────────────
        "You're large enough to stop this. You're not going to.",
        "You could lift her off. The thought occurred to you. Then she did that thing.",
        "You had a plan for this evening. She had a different one. Hers was better.",
        "The one in charge in this city is rarely the biggest one in the room. You're learning that.",
        "She is very small and entirely in control of the situation. This is not a temporary condition.",
        "You thought you were making a choice. She made it three minutes before you sat down.",
        "She is extremely patient about getting exactly what she wants.",
        "You're being maneuvered. You know you're being maneuvered. You are fine with this.",
        "She's running the whole thing. You have a supporting role. You're great in it.",

        ## ── Morning after ─────────────────────────────────────────────────────
        "Whatever you planned to say this morning, lead with something other than 'that was different.'",
        "The marks are going to need a story. Make it a good one.",
        "She's gone but the evidence is thorough and well-distributed.",
        "You look like you've been somewhere specific. You have.",
        "The scratch pattern on the headboard is not from before you got here.",
        "You woke up exhausted. You are not complaining. You would not complain about this.",

        ## ── Attitude / confidence ─────────────────────────────────────────────
        "The cocky ones are cocky for documented reasons. Ask for the documentation.",
        "She said she could handle it. She was not being modest.",
        "Confidence that size is usually backed by something. Give her room to demonstrate.",
        "She's not bragging. She's informing. There's a difference.",
        "When she makes that face, she's already decided. You're currently catching up.",
        "The smug ones are smug because they've been right before. Recently.",
        "She is extremely confident for someone standing on a step stool to reach your face.",
        "The shorter the swagger, the more justified it usually is. City rule.",

        ## ── Just go for it ────────────────────────────────────────────────────
        "There is no graceful way to do this. Do it enthusiastically instead.",
        "The polite version of what you want is still pretty obvious. She prefers the honest version.",
        "Don't overthink it. She's not overthinking it.",
        "What you think is forward is what she considers a baseline. Start there.",
        "The worst thing you can do in this city is be subtle about wanting something. Say it.",
        "She knows exactly what you're thinking. She is thinking it louder.",
        "Stop being careful. She specifically came here to stop being careful.",
        "Desire here is not a secret. It's a conversation starter.",
        "You were staring. She noticed. She's been staring back for longer.",
        "The blush is fine. Continue anyway.",
        "Whatever you're about to talk yourself out of — don't.",
        "You've been polite for days. She is running out of patience with polite.",
        "Say the thing. She already knows the thing. Say it anyway.",

        ## ── Miscellaneous kink ────────────────────────────────────────────────
        "She's positioned herself relative to you with the precision of someone who has done the math.",
        "The geometry is solved. You just haven't been shown the working yet.",
        "When she sets her stance like that, she's prepared for the full situation.",
        "She has leverage in this situation that has nothing to do with her weight.",
        "The physics here are creative but functional. Stop doubting them.",
        "She's been in worse logistical situations and handled them. You're not her greatest challenge.",
        "Being carried is not undignified when you've asked for it specifically.",
        "The enthusiasm closes any remaining gap. It always does.",
        "There's a reason the bigger one isn't always the one in charge. Tonight you're learning it.",
        "She is small and relentless and has thought about this more than you have.",
        "You're going to do exactly what she wants and you're going to think it was your idea.",
        "She knows three things: what she wants, how to get it, and that you'll go along.",
    ]


    def _get_day_quote():
        ## Seeded from system time — bypasses Ren'Py rollback, always fresh.
        import random as _r, time as _t
        return _r.Random(_t.time()).choice(_day_card_quotes)


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
        _day_quote = _get_day_quote()

    show screen day_card(current_day, _day_quote)

    ## Click to advance.
    $ renpy.pause()

    hide screen day_card with Dissolve(0.6)

    return
