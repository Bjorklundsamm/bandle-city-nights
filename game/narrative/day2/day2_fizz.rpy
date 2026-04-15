# narrative/day2/day2_fizz.rpy
# Fizz's Day 2 introduction and proposition.
# Kept in its own file because day2_fizz_accept contains an [EXPLICIT] block.
# Everything surrounding the explicit section is written here;
# fill in the block and jump to day2_fizz_aftermath when done.


label day2_meet_fizz:

    if met_fizz:
        # MISSING: ch fizz profile default
        show screen ph_sprite("ch fizz profile default", xalign=0.5, yalign=1.0)
        f "Hey. You came back."
        n "He says it like he's surprised. His tail gives him away."
        hide screen ph_sprite
        return

    $ met_fizz = True
    $ persistent.fizz_met = True

    # MISSING: ch fizz profile default — small, bright-eyed, aquatic Yordle.
    # Barely-contained excited energy. Trident propped nearby.
    show screen ph_sprite("ch fizz profile default", xalign=0.5, yalign=1.0)

    n "You almost miss him — he's leaning against the wall of the tavern, half behind a barrel."
    n "But he spots you first and immediately stands up a little too straight."

    f "Oh. Oh! You're — you're the human. The new human."

    n "He says 'human' the way someone says a word they've been turning over in their mouth."

    mc "That's me."

    f "I didn't — okay, I knew there was a human but I didn't think I'd run into you outside."
    f "I'm Fizz. I work for Katarina."

    mc "Her bodyguard?"

    f "Yeah! Well. Sort of. She says bodyguard, I say I keep an eye on things for her."
    f "It's the same thing. She just doesn't like me saying bodyguard because she thinks it implies she needs protecting."

    n "He glances around reflexively, as though Katarina might be nearby."
    n "She isn't."

    f "She doesn't need protecting. I'm more like... a very small very mobile asset."

    mc "Sure."

    f "You've met her, right? She mentioned a new human was in town."

    mc "Yeah. Last night."

    f "What did you think?"

    mc "She's intense."

    f "She's incredible."
    n "He says it with complete sincerity and then seems to realize that wasn't what you meant."
    f "I mean — yeah. Intense. That too."

    n "He fidgets with the trident he's been half-hiding behind him."

    f "So — you're from the mainland? A city?"

    mc "Something like that."

    f "I've always wanted to go to the mainland."
    f "Well. More specifically I've always wanted to meet more humans."
    n "A beat."
    f "I just think humans are really interesting."

    mc "We're not that remarkable."

    f "No, you are. You really are."
    f "The — the proportions are just very. You know."
    n "He gestures vaguely at your general person."
    f "Impressive."

    n "There's a pause. He seems to be deciding something."

    f "Okay I'm going to be honest."
    f "I have a type."

    mc "Okay."

    f "Tall. Pale. Kind of the whole — prince charming thing. You know."
    f "The jaw. The shoulders."
    f "And, um."

    n "He glances down briefly and then back up at you with an expression of profound restraint."

    f "The, uh. Everything else."

    mc "Are you flirting with me?"

    f "I'm complimenting you. There's a difference."
    f "Flirting would be if I told you I haven't stopped thinking about certain things since I saw you come out of the tavern this morning."

    n "A beat."

    f "Okay that might have been flirting."

    n "He tugs one ear with an expression that suggests the line between 'telling you something' and 'asking you something' is getting harder to find."

    f "I guess what I'm wondering is whether you're — you know. Open."

    mc "Open to what, exactly?"

    n "He gives up on the approach."

    f "Do you want to go behind the tavern and let me suck your cock."

    n "He says it completely flat. Then immediately:"

    f "That came out more direct than I intended."

    menu:
        "Yeah, alright.":
            jump day2_fizz_accept

        "No thanks.":
            jump day2_fizz_decline


label day2_fizz_accept:

    mc "Yeah. Alright."

    n "Fizz blinks. Then his whole face rearranges into something much brighter."

    f "Okay. Cool. Yeah. Okay."
    f "Around the back. There's a — there's a spot. I know the spot."

    n "He is already moving, trident in hand, tail flicking with a speed that suggests 'casual' is no longer in play."

    # This is pushing past what I'll write directly. I've drafted through the lead-up above.
    # Author the explicit section yourself, wrap it in the markers below,
    # then jump continues to day2_fizz_aftermath.

    # [EXPLICIT START]

    # [EXPLICIT END]

    jump day2_fizz_aftermath


label day2_fizz_aftermath:

    # MISSING: ch fizz profile default — same sprite, now looking thoroughly
    # satisfied. Still trying to play it cool. Failing slightly.
    show screen ph_sprite("ch fizz profile default", xalign=0.5, yalign=1.0)

    n "Fizz leans back against the tavern wall, catching his breath."
    n "His tail is doing something complicated that you think might be the Yordle equivalent of a victory lap."

    f "So."

    mc "So."

    f "You're welcome to do that again."
    f "Like. Whenever."
    f "That's a standing offer. Very open-ended. No appointment needed."

    n "He picks up his trident from where it's leaning and tries to look like he wasn't just kneeling behind a tavern."

    f "I'll be around."

    hide screen ph_sprite
    return


label day2_fizz_decline:

    mc "I'm going to pass."

    f "Oh — yeah, no, totally."
    n "He holds up both hands."
    f "That's fine. That's completely fine."

    n "A pause. He tilts his head."

    f "Do you know what free use is?"

    mc "I have a general sense."

    f "I'm just saying — the offer stands. Permanently."
    f "You never have to ask. You never have to think about it in advance."
    f "If you ever want to — for any reason, at any time, literally any time — I'm available."
    f "You don't even have to say anything. You can just — show up."

    n "He says it with the same matter-of-fact energy he'd use to give you directions."

    f "Just come find me."
    f "I'll know what it's about."

    n "He picks up his trident, gives you a small nod, and pushes off the wall."
    n "Completely casual. As though that was a perfectly ordinary thing to say."
    n "His tail, however, is wagging."

    hide screen ph_sprite
    return
