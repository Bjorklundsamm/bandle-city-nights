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
        n "His tail gives him away."
        hide screen ph_sprite
        return

    $ met_fizz = True
    $ persistent.fizz_met = True

    # MISSING: ch fizz profile default — small, bright-eyed, aquatic Yordle.
    # Barely-contained excited energy. Trident propped nearby.
    show screen ph_sprite("ch fizz profile default", xalign=0.5, yalign=1.0)

    n "You almost miss him — he's leaning against the tavern wall, half behind a barrel, arms crossed."
    n "He spots you first and immediately stands up a little too straight."

    f "Oh. Oh! You're — you're the human. The new one."

    mc "That's me."

    f "I knew there was a human but I didn't think you'd be — I mean, I knew humans were tall but you're—"

    n "He gestures at you. All of you. Helplessly."

    f "...really tall."

    n "He closes his mouth. Seems to remember he has a job."

    f "Fizz. I'm a travel guard. For her."

    n "He jerks his thumb toward where Miss Fortune is standing without looking."

    mc "The pirate?"

    f "Merchant. She prefers merchant. The pistols are for commerce."

    n "You glance over. Miss Fortune has that effect — the red hair, the coat, the way she's built like the universe was making a point."
    n "Fizz watches you look. His face goes flat."

    f "Yeah."

    mc "She's—"

    f "Enormous, I know."

    n "He holds both hands out in front of his chest, palms facing inward, a good foot apart."
    n "He stares at you."

    f "The tits get everyone. Every single man, every single time."
    f "I have been standing next to those tits for three days."
    f "Three. Days."

    mc "That sounds—"

    f "I can describe every cobblestone in this city because I have been staring at the ground trying to look professional."
    f "She doesn't even notice. She just stands there being... aggressively shaped."
    f "And every cock in a hundred feet points directly at her and completely forgets I exist."

    n "He looks at you. Actually at you, this time — the set of your shoulders, lower."
    n "His expression changes. The frustration doesn't leave but something else sharpens behind it."

    f "And then you walk out that door."

    n "He tilts his head. His tail flicks once."

    f "You've got the build. The hands."

    n "His eyes drop. Stay there. He doesn't pretend he isn't looking."

    f "And you are packing."

    mc "Excuse me?"

    f "Your cock. You're hung. I can tell."
    f "Three days of nothing and you walk out with that."

    n "He says it with the flat energy of a man who has endured a great deal and deserves this."

    f "Do you want to go behind the tavern."

    n "Not a question. A proposal."

    f "I have been waiting three days to get my mouth around something worth the wait."

    menu:
        "Lead the way.":
            jump day2_fizz_accept

        "Not today.":
            jump day2_fizz_decline


label day2_fizz_accept:

    mc "Lead the way."

    n "Fizz blinks. Then his entire face rearranges into something much brighter."

    f "Okay. Yes. Around the back."
    f "There's a spot. Good spot. I know it very well."

    n "He is already moving, trident tucked under his arm, tail going absolutely berserk."
    n "He is not playing it cool. He has stopped trying."


    # [GEN START]

    # [EXPLICIT START]
    n "Behind the tavern, there's an alley. Fizz turns and hits you with the most impatient look you have ever seen."
    n "Then he gestures impatiently at your trousers."

    f "Out."

    n "You could be offended, but he's vibrating with eagerness and his skin is starting to glow in patches."
    n "You undo your belt. The moment your waistband clears your hips, Fizz's pupils blow wide."

    f "Oh, fuck yes."

    n "His hand is already out. He doesn't touch. His fingers just hover, an inch from your shaft, almost shaking."

    f "This is why I travel with her."
    f "All the men who try to impress her. Like there's a cock shortage in Bilgewater or something."
    f "But they all want her, so when one of them finally looks my way..."
    f "It's not this."

    n "He moves his hand closer. His fingertips brush your length and he makes a noise that should be illegal."

    f "You feel heavy. I love it."
    f "Can I put it in my mouth now."
    f "Please let me put it in my mouth. I'll be really good at it."

    mc "You don't need to ask twice."

    n "Fizz's mouth is on you before you finish the sentence."
    n "And he is just as good as he thinks he is."
    n "His tongue is long and textured. He knows how to use it. He swallows you down like he's been starving for weeks and you are the first meal he's seen."
    n "His hands are on your thighs, nails pricking just enough to keep you anchored in the moment."
    n "You thread your fingers through his hair — cool and damp, smells like the ocean — and he groans."
    n "The sound vibrates right up your spine."

    f "Don't hold back."
    n "He pulls back just enough to say it, then goes right back to work, one hand working your base while his mouth takes the rest."
    n "There's no hesitation. No teasing. Just pure, focused enthusiasm."
    n "He wants this. He wants you."
    n "It doesn't take long. Not with that mouth on you."
    n "You tighten your grip on his hair, warn him — he doubles down."
    n "When you come, he doesn't spill a drop."
    n "He pulls back, lips swollen, eyes heavy-lidded, and licks them slow."

    f "Fuck."

    mc "Language."

    f "I meant it as a compliment."
    f "You taste good. Salty. I like it."
    f "Thank you. That was... thank you."

    n "He tucks himself back in his shorts with a dreamy look on his
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

    mc "Not today."

    n "He takes it well. Holds up both hands."

    f "Valid. Completely valid."

    n "A pause. His tail flicks."

    f "You know what free use is?"

    mc "I have a general sense."

    f "Open offer. No appointment. No asking."
    f "Any time you want your cock sucked, you come find me."
    f "I'm not joking. I'll drop whatever I'm doing."

    n "He says it with the same energy he'd use to give you directions to the market."

    f "Literally anything."
    f "I mean it."

    n "He picks up his trident and pushes off the wall."
    n "Completely casual. As if this was a perfectly normal thing to say to someone you met thirty seconds ago."
    n "His tail is wagging."

    hide screen ph_sprite
    return
