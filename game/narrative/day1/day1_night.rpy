# narrative/day1/day1_night.rpy
# Tutorial night tavern free-roam: the loop, night-end sleep sequence,
# and all first-meeting character interaction labels.
#
# The barkeep_ask_about system and barkeep_overview_* labels live in
# narrative/tavern/barkeep_system.rpy — call them from here, don't duplicate.


## ── Tutorial night loop ──────────────────────────────────────────────────────

label tavern_tutorial_loop:

    scene bg tavern empty
    show screen inventory_button
    $ _tavern_running = True

    while _tavern_running:
        window hide
        call screen tavern_hub
        window show

        if _return == "leave":
            $ _tavern_running = False

        elif _return == "barkeep":
            call tavern_tutorial_barkeep

        elif _return == "poppy":
            call tavern_tutorial_poppy

        elif _return == "tristana":
            call tavern_tutorial_tristana

        elif _return == "vex":
            call tavern_tutorial_vex

        elif _return == "katarina":
            call tavern_tutorial_katarina

        elif _return == "ahri":
            call tavern_tutorial_ahri

        elif _return == "ezreal":
            call tavern_tutorial_ezreal

        elif _return == "nidalee_neeko":
            call tavern_tutorial_nidalee_neeko

        elif _return == "jinx":
            call tavern_tutorial_jinx

    jump tavern_night_end


## ── Night end ────────────────────────────────────────────────────────────────

label tavern_night_end:

    menu:
        "Call it a night.":
            $ renpy.block_rollback()
        "Actually, head back in.":
            jump tavern_tutorial_loop

    scene bg black with dissolve
    stop music fadeout 2.0

    n "You make your way back through the inn, the noise of the tavern softening behind you with each step up the stairs."
    n "The hallway is quiet. A single lamp flickers at the far end, throwing long shadows across the floorboards."

    scene bg bedroom default with Dissolve(1.5)
    play ambient "audio/sfx/Tavern_ambience.mp3" fadein 2.0 volume 0.3

    n "The room is exactly as you left it — small, simple, nothing that didn't have a purpose."
    n "You don't bother with anything. No boots, no belt. You sit on the edge of the bed and that's about all it takes."

    n "Your eyes are already closing before your head hits the pillow."
    n "You're not even sure you finished the thought you were having."

    n "The weight of the day — all of it, the chase, the fall, the barkeep, the faces, the noise — pulls you under like a current."
    n "And you're gone."

    scene bg black with Dissolve(1.2)

    n "..."

    n "You don't know what time it is when the sound reaches you."
    n "Your body knows before your brain does — something pulls you half-awake, every nerve already braced."
    n "Last night is still in your muscles. The dark, the running, whatever was behind you."
    n "For one bad second you are certain someone is being hurt."

    n "You lie still and listen."

    n "It's coming from close. Next room, maybe. The walls here aren't thick."
    n "There's rhythm to it. Something being taken and not entirely given."
    n "A voice — low, controlled, with the patience of someone who has all night and knows it."
    n "And another — shorter sounds, cut off, like breath that keeps getting interrupted."

    n "It does't sound gentle."
    n "Not something that pauses to ask."

    n "You can't hear enough to be sure of anything except that one of them is in charge and the other one is not, and whoever the victim is..."
    n "...isn't exactly hating it."

    n "You lie there a moment more before sleep creeps back in."
    n "Then the warmth closes back over you and you let it."

    jump morning_day_2


## ── Barkeep ──────────────────────────────────────────────────────────────────

label tavern_tutorial_barkeep:

    show ch bartender profile default smiling with dissolve

    b "What can I do for you?"

    menu:
        "I wanted to ask about someone.":
            call barkeep_ask_about
        "Just checking in.":
            b "Well. You know where to find me."

    hide ch bartender profile default smiling with dissolve
    return


## ── Poppy ────────────────────────────────────────────────────────────────────

label tavern_tutorial_poppy:

    # Poppy was introduced at the bar in gameStart. She's on duty tonight.
    n "Poppy gives you a brief nod as your eyes meet. She's still watching the room."
    n "You leave her to it."
    return


## ── Tristana ─────────────────────────────────────────────────────────────────

label tavern_tutorial_tristana:

    # Met in gameStart — she's deep in Katarina's dice trap tonight.
    n "Tristana is hunched over the table, jaw set, staring at the dice like she can change the outcome through sheer force of will."
    n "The pile in front of her is not encouraging. You decide to leave her to it."
    return


## ── Vex ──────────────────────────────────────────────────────────────────────

label tavern_tutorial_vex:

    if met_vex:
        n "Vex hasn't moved. A fresh mug has joined the collection. You decide to leave her to it."
        return

    $ met_vex = True

    show ch vex profile default with dissolve

    n "Tucked into the corner booth as far from the noise as it's possible to get, a grey-furred girl sits alone."
    n "In front of her is a graveyard of empty mugs — four, maybe five — arranged with the passive inevitability of someone who has been here a while."
    n "She's working on another, baggy hoodie pulled up around her ears, staring at nothing."
    n "A small shadow flickers at her shoulder — something between a cat and a smudge of ink — watching you approach."

    $ emotion_icon = "ch vex icon annoyed"
    vx "Don't."

    n "She says it before you've even opened your mouth."

    mc "I didn't—"

    vx "Whatever it was going to be. Don't."

    n "The shadow flickers. You get the distinct impression it finds this amusing even if she doesn't."

    menu:
        "Fair enough. Just saying hi.":
            mc "Fair enough. Just saying hi."
            vx "Hi."
            n "A pause. She doesn't look at you."
            vx "There. Now you've said it. You can go."

        "Rough night?":
            mc "Rough night?"
            vx "Every night."
            vx "This one in particular is loud. And bright. And there are too many people."
            mc "Then why come to a bar?"
            vx "..."
            n "She doesn't answer. The shadow slinks over and sits directly in front of you, staring."

        "Is your shadow... alive?":
            mc "Is your shadow alive?"
            n "For the first time she looks at you — a slow, flat assessment."
            $ emotion_icon = "ch vex icon grin"
            vx "What do you think?"
            mc "I think it is."
            vx "Then you're smarter than most people who talk to me."
            n "Shadow tilts its head. She looks back at the middle distance."
            $ emotion_icon = "ch vex icon annoyed"
            vx "Don't make it weird."

    n "She pulls her cloak a little tighter and resumes staring at nothing."
    n "Conversation clearly over. You're not sure whether that counted as a good first impression, but somehow you doubt she gives those out."

    hide ch vex profile default with dissolve
    $ emotion_icon = None
    return


## ── Katarina ─────────────────────────────────────────────────────────────────

label tavern_tutorial_katarina:

    if met_katarina:
        n "Katarina has a fresh victim across the table. The poor thing doesn't know it yet. Best not to interrupt."
        return

    $ met_katarina = True

    show ch katarina profile default with dissolve

    n "You find her at the back table — the kind of woman who makes a room rearrange itself around her without asking."
    n "Red hair, a soldier's posture, and the loose, unhurried ease of someone who has never once been caught off guard."
    n "She's at the dice table. Tristana sits across from her, brow furrowed, studying the table like the numbers might change if she looks hard enough."
    n "Katarina is winning. You can tell by the way everyone else keeps glancing at each other."

    n "As you approach she catches you in her periphery. She lets the silence sit for a moment, then speaks — low, easy, not loud enough to carry."

    $ emotion_icon = "ch katarina icon bored"
    k "You've been standing there for a few seconds."

    mc "Sorry, I—"

    k "Don't apologize. It's tedious."

    n "She leans back in her chair, looking you over the way you'd appraise something that might be useful."

    k "You're the one who washed up in the deep wood last night, yeah?"
    k "The barkeep's newest little charity case."

    mc "Something like that."

    k "Mm."

    n "She picks up the dice, rolls them without looking down, and sets them back. Tristana mutters something under her breath."

    k "I'll be honest with you. I don't love the idea of a new hunter moving through my grounds."
    k "There's no shortage of interesting prey. The trouble is I'm never quite... satisfied."

    n "She finally looks at you directly — a calm, complete assessment."

    k "We'll see if you're worth the competition."

    n "She keeps her voice level, unhurried — just two people making conversation while Tristana stares at the dice."

    $ emotion_icon = "ch katarina icon horny"
    k "She's spoken for tonight, by the way. I've put a lot of work into this table."
    k "By the time we're done she'll owe me enough that I'll be collecting on it for quite a while."
    k "In whatever form I see fit. For as long as I like."
    n "The way she says it leaves very little to the imagination."
    k "I'd hate for anything to distract her before we've had a chance to settle up."

    n "She says it pleasantly. Like she's doing you a favor."

    $ emotion_icon = "ch katarina icon bored"
    k "Sit if you want. But I don't go easy on anyone at this table."

    menu:
        "Maybe another time.":
            mc "I'll pass tonight. Just wanted to say hello."
            k "Wise."
            n "She says it like she means it as a compliment."
            k "Another time, then."

        "I'll keep that in mind.":
            mc "I'll keep that in mind."
            n "The faintest smile. Not warm exactly, but real."
            $ emotion_icon = "ch katarina icon smile"
            k "Good answer."
            n "She glances back at the dice, signaling that's about all the welcome you're going to get."
            n "Somehow it still feels like passing a test."

    hide ch katarina profile default with dissolve
    $ emotion_icon = None
    return


## ── Ahri ─────────────────────────────────────────────────────────────────────

label tavern_tutorial_ahri:

    if met_ahri:
        n "Ahri is still at her table, watching the room. Her tails shift slowly as your gaze passes over her."
        n "She doesn't look back — but somehow you're certain she noticed."
        return

    $ met_ahri = True

    show ch ahri profile default with dissolve

    n "There's a moment where the noise of the room just — stops registering."
    n "She's seated at a table in the middle of it all, nine white tails fanned out behind her like something out of a painting."
    n "Half the room is pretending not to look at her. The other half has given up pretending."
    n "She has a small glass of something amber and the patient, unhurried quality of someone who has never needed to compete for attention in her life."
    n "Not inattentive — the opposite. Nothing in her eyeline is escaping her."

    n "When your gaze meets hers she doesn't look away. She just waits to see what you'll do with the eye contact."

    n "Two small blue-gold embers drift from her fingertips and dissolve before they reach the table."

    $ emotion_icon = "ch ahri icon default"
    a "You're the one they found out there last night, all mangled up by something wild and angry."

    n "It isn't a question."

    mc "Word travels fast."

    a "I was there when they brought you in. You were in poor condition."

    n "She tilts her head slightly."

    a "You're doing better than I expected."

    n "The nine tails behind her shift — a slow, thoughtful motion, like something checking its own impressions."

    mc "Should I be flattered?"

    $ emotion_icon = "ch ahri icon default"
    a "Probably not. I expected very little."

    n "She says it with something that might be a smile."

    n "Then her eyes drift — not away from you, but through you, like she's reading something written underneath."
    n "Her nostrils flicker almost imperceptibly. The tails slow."

    $ emotion_icon = "ch ahri icon default"
    a "You smell like the city. Roads. Iron. Other people's fires."

    n "She considers that for a moment."

    $ emotion_icon = "ch ahri icon default"
    a "Nothing wrong with it. It's just... ordinary. I've read that story before."
    a "Come back when you've spent some time out here. When the wood is in you a little."
    a "When you smell like something that's touched this world and let it touch back."

    n "She tilts her glass, watching the amber catch the light."

    a "That version of you will be much more interesting."

    n "She turns her attention back to the room — not dismissive exactly, just done."
    n "The tails settle. You get the sense she's still aware of exactly where you are."

    hide ch ahri profile default with dissolve
    $ emotion_icon = None
    return


## ── Ezreal ───────────────────────────────────────────────────────────────────

label tavern_tutorial_ezreal:

    if met_ezreal:
        n "Ezreal has migrated to a bigger audience. He catches your eye and gives a quick nod — clearly mid-performance. You'll catch him another time."
        return

    $ met_ezreal = True

    show ch ezreal profile default with dissolve

    n "You hear him before you see him."

    $ emotion_icon = "ch ezreal icon smile"
    ez "— no, no, the real problem was the trap was already sprung, right? So I had about two seconds to decide."
    ez "Most people freeze. I ran the numbers, flipped the panel, and just — gone. Completely clean."

    n "He's leaning back in his chair with the posture of someone who has told this story before and knows exactly where the good parts are."
    n "As you approach, he pivots to include you with the ease of someone who is very used to audiences."

    ez "New guy! Pull up a chair, I was just getting to the good part."

    mc "What's the story?"

    ez "Oh, just a little thing I got up to in the Shuriman ruins last season. Totally routine, except for the part where it wasn't."

    n "He grins."

    ez "Ezreal. Explorer, treasure hunter, occasional legend. You're [player_name], right? Barkeep mentioned you."

    mc "News really does travel fast in this city."

    ez "Small place. Big ears. Literally, in most cases."

    n "He taps one of his own ears for emphasis."

    menu:
        "What were you doing in Shurima?":
            mc "What were you doing in Shurima?"
            ez "Recovering an artifact that three separate academic institutions said was unrecoverable."
            ez "They were wrong. Obviously."
            $ emotion_icon = "ch ezreal icon smile"
            ez "No luck. All skill."

        "You said 'occasional legend'?":
            mc "Occasional legend?"
            $ emotion_icon = "ch ezreal icon smile"
            ez "I'm being modest. It's a new thing I'm trying."

        "I'll let you get back to your story.":
            mc "Don't let me interrupt."
            $ emotion_icon = "ch ezreal icon smile"
            ez "You're not interrupting, you're improving the audience-to-story ratio."
            ez "Sit down, this next part is genuinely impressive."

    n "You can't quite tell where the performance ends and the actual person starts."
    n "You suspect he might not know either."

    hide ch ezreal profile default with dissolve
    $ emotion_icon = None
    return


## ── Nidalee & Neeko ──────────────────────────────────────────────────────────

label tavern_tutorial_nidalee_neeko:

    if met_nidalee_neeko:
        n "Neeko is gesturing at something only she can see. Nidalee is nodding slowly. You leave them to it."
        return

    $ met_nidalee_neeko = True

    # All three images share the "ch" tag — showing one auto-replaces the other.

    show ch neeko and nidalee profile with dissolve
    n "You hear them before you reach the table."

    $ emotion_icon = "ch nidalee icon default"
    show ch nidalee profile default with Dissolve(0.15)
    ni "You said you weren't going to do it again."

    $ emotion_icon = "ch neeko icon default"
    show ch neeko profile default with Dissolve(0.15)
    neo "Neeko did not agree to that. Nidalee said it. Neeko was quiet."

    $ emotion_icon = "ch nidalee icon default"
    show ch nidalee profile default with Dissolve(0.15)
    ni "Quiet is agreement."

    $ emotion_icon = "ch neeko icon default"
    show ch neeko profile default with Dissolve(0.15)
    neo "Quiet is quiet. They are not the same thing."

    show ch neeko and nidalee profile with Dissolve(0.15)
    n "The taller one has the posture of someone who hunts for a living — still, coiled, zero wasted energy."
    n "The shorter one has scales along her jaw and eyes that are doing several things at once, including noticing you."

    $ emotion_icon = "ch neeko icon default"
    show ch neeko profile default with Dissolve(0.15)
    neo "Oh."

    show ch neeko and nidalee profile with Dissolve(0.15)
    n "Neeko looks at you the way you'd look at something you weren't expecting but are immediately glad exists."

    $ emotion_icon = "ch neeko icon default"
    show ch neeko profile default with Dissolve(0.15)
    neo "Nidalee. There is a human."

    $ emotion_icon = "ch nidalee icon default"
    show ch nidalee profile default with Dissolve(0.15)
    ni "I know."

    show ch neeko and nidalee profile with Dissolve(0.15)
    n "She doesn't look at you yet. Still watching Neeko."

    $ emotion_icon = "ch neeko icon default"
    show ch neeko profile default with Dissolve(0.15)
    neo "Neeko thinks you should tell the human what we are arguing about."
    neo "So that they can decide for themselves."

    $ emotion_icon = "ch nidalee icon default"
    show ch nidalee profile default with Dissolve(0.15)
    ni "We're not doing that."

    $ emotion_icon = "ch neeko icon default"
    show ch neeko profile default with Dissolve(0.15)
    neo "Neeko is doing it."

    show ch neeko and nidalee profile with Dissolve(0.15)
    n "She turns to you fully, earnest and completely without embarrassment."

    $ emotion_icon = "ch neeko icon default"
    show ch neeko profile default with Dissolve(0.15)
    neo "Nidalee believes that Neeko belongs to her. Like territory."
    neo "Neeko believes Nidalee is wrong. But also correct. It is complicated."
    neo "You are [player_name], yes? The one from the forest?"

    show ch neeko and nidalee profile with Dissolve(0.15)
    mc "That's me."

    show ch neeko profile default with Dissolve(0.15)
    neo "Good. Neeko thinks you should weigh in."

    show ch neeko and nidalee profile with Dissolve(0.15)
    n "Nidalee finally looks at you. It's a slow, complete assessment — the kind that takes inventory."

    $ emotion_icon = "ch nidalee icon default"
    show ch nidalee profile default with Dissolve(0.15)
    ni "Don't."

    $ emotion_icon = "ch neeko icon default"
    show ch neeko profile default with Dissolve(0.15)
    neo "Nidalee."

    $ emotion_icon = "ch nidalee icon default"
    show ch nidalee profile default with Dissolve(0.15)
    ni "He doesn't need to be part of this."

    $ emotion_icon = "ch neeko icon default"
    show ch neeko profile default with Dissolve(0.15)
    neo "Neeko disagrees. Neeko thinks outside perspective is useful."

    show ch neeko and nidalee profile with Dissolve(0.15)
    n "A silence. Nidalee holds it the way someone holds a weapon they've decided not to use yet."

    $ emotion_icon = "ch nidalee icon default"
    show ch nidalee profile default with Dissolve(0.15)
    ni "You smell like the deep wood. Whatever came for you out there didn't finish the job."

    show ch neeko and nidalee profile with Dissolve(0.15)
    n "She says it like it's a fact worth filing."

    $ emotion_icon = "ch nidalee icon default"
    show ch nidalee profile default with Dissolve(0.15)
    ni "Stay out of things that aren't yours."

    show ch neeko and nidalee profile with Dissolve(0.15)
    n "It's not entirely clear if she's talking to you or to Neeko."
    n "Neeko, for her part, gives you an apologetic look — the kind that says this is a normal Tuesday."

    $ emotion_icon = "ch neeko icon default"
    show ch neeko profile default with Dissolve(0.15)
    neo "Neeko is sorry about her. She is like this."
    neo "You can come find Neeko again later. When she is less territorial."

    show ch neeko and nidalee profile with Dissolve(0.15)
    n "Nidalee says nothing. She picks up her cup, drinks, and resumes watching the room."
    n "You get the sense the argument isn't over. It's just been set down somewhere they'll pick it up again later."

    hide ch neeko and nidalee profile with dissolve
    $ emotion_icon = None
    return


## ── Jinx ─────────────────────────────────────────────────────────────────────

label tavern_tutorial_jinx:

    if met_jinx:
        n "Jinx is cross-legged on a table in the corner, disassembling something. You decide not to startle her — you'll find her again later."
        return

    $ met_jinx = True

    show ch jinx profile default with dissolve

    n "She finds you before you find her."

    $ emotion_icon = "ch jinx icon crazy"
    j "Hey. Hey, you. Big guy."

    n "A blue-haired girl is leaning backwards off a barstool, pigtails nearly touching the floor, pointing at you upside-down."
    n "There is a rocket launcher on the stool next to her that she is apparently on a first-name basis with."

    j "You're the one who got dragged out of the deep wood half-dead, right? Right."
    j "Okay but what was chasing you."

    mc "I'm not entirely sure."

    j "Okay but what did it look like."

    mc "I didn't get a great look at it."

    j "Okay but—"

    n "She rights herself, dropping back upright with zero apparent effort, and stares at you."

    $ emotion_icon = "ch jinx icon smile"
    j "You have to give me something. I've been thinking about this since last night."

    n "She seems genuinely aggrieved. Like you've personally inconvenienced her by not having better information about your own near-death experience."

    menu:
        "Big. Blue eyes. Fast.":
            mc "Big. Blue eyes. Fast."
            $ emotion_icon = "ch jinx icon crazy"
            j "Okay, okay. Blue eyes."
            n "She points at you."
            j "That's something. Fishbones, blue eyes."
            n "She appears to be consulting the rocket launcher."
            j "He says that doesn't narrow it down. He's wrong but I'm not going to tell him that."

        "I'd rather not think about it.":
            mc "I'd rather not think about it, honestly."
            $ emotion_icon = "ch jinx icon smile"
            j "Ugh. Fair. Fine."
            n "She says 'fine' the way someone says it when it is not fine."
            j "I'm putting 'big and scary' in my notes."

    $ emotion_icon = "ch jinx icon crazy"
    j "I'm Jinx, by the way. And this is Fishbones."

    n "She pats the rocket launcher. It does not respond. She seems satisfied anyway."

    j "Don't be weird about him. Everyone's weird about him."

    mc "I'm not being weird."

    j "You're a little weird."
    j "It's fine, I like weird. Normal people are exhausting, right?"

    n "She squints at you with the focused assessment of someone running a rapid threat evaluation."

    j "You're going to be around for a while, yeah? Barkeep's got you set up?"

    mc "That's the plan."

    $ emotion_icon = "ch jinx icon crazy"
    j "Good. Come find me if anything explodes."
    j "Actually come find me anyway. Things are more likely to explode if I'm involved."

    n "She grins, and for a half-second it's brighter than it should be — the kind of smile that arrives too fast and means too much."
    n "Then she's already turning away, picking up a component from the table and turning it over in her fingers."
    n "Conversation over. You've been filed somewhere."

    hide ch jinx profile default with dissolve
    $ emotion_icon = None
    return
