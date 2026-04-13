# script_tavern.rpy
# Tavern free-roam system. The player browses the tavern by clicking character
# position images. Each character has a stub interaction label below — fill them
# in as writing progresses. After all desired interactions, the player hits
# "Head to bed" to end the night.


## ── Transforms ───────────────────────────────────────────────────────────────
## Used to position two characters side by side during duo interactions.

transform duo_left:
    xalign 0.28
    yalign 1.0

transform duo_right:
    xalign 0.72
    yalign 1.0


## ── Tutorial night tavern loop ───────────────────────────────────────────────
##
## Called via `jump tavern_tutorial_loop` from gameStart in script_main.rpy.
## Sets the scene, hides the textbox while the hub screen is active, then
## dispatches to the appropriate interaction label based on what was clicked.
## After each interaction the loop restores the tavern view and repeats.

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

    scene bg black with dissolve
    stop music fadeout 2.0

    n "You make your way back through the inn and up to the small room the barkeep set aside for you."
    n "It's nothing fancy, but after what you've been through, a bed feels like a luxury."

    n "You lie back and close your eyes, and for the first time in what feels like forever, you sleep without fear."

    # TODO: jump to next day's label when written
    return


## ── Interaction labels ───────────────────────────────────────────────────────
##
## Tutorial night — first meetings only. Each label checks the met_* flag:
## if already met (or dialogue exhausted), the narrator gives a short reason
## to check back later and returns immediately. Otherwise the intro plays,
## sets the flag, then returns.
##
## Keep scene state clean: hide any profile sprites before returning.


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


## ── Barkeep: ask about someone ───────────────────────────────────────────────
##
## Builds a list of met characters, displays them paginated (4 per page),
## and dispatches to the appropriate overview label based on affection level.
## Called from any barkeep interaction label.

label barkeep_ask_about:

    python:
        ## Build list of (display_name, affection_var, overview_label) for met characters.
        _barkeep_roster = []
        if met_tristana:
            _barkeep_roster.append(("Tristana",     affection_tristana,  "barkeep_overview_tristana"))
        if met_poppy:
            _barkeep_roster.append(("Poppy",        affection_poppy,     "barkeep_overview_poppy"))
        if met_lulu:
            _barkeep_roster.append(("Lulu",         affection_lulu,      "barkeep_overview_lulu"))
        if met_vex:
            _barkeep_roster.append(("Vex",          affection_vex,       "barkeep_overview_vex"))
        if met_katarina:
            _barkeep_roster.append(("Katarina",     affection_katarina,  "barkeep_overview_katarina"))
        if met_ahri:
            _barkeep_roster.append(("Ahri",         affection_ahri,      "barkeep_overview_ahri"))
        if met_ezreal:
            _barkeep_roster.append(("Ezreal",       affection_ezreal,    "barkeep_overview_ezreal"))
        if met_nidalee_neeko:
            _barkeep_roster.append(("Nidalee",      affection_nidalee,   "barkeep_overview_nidalee"))
            _barkeep_roster.append(("Neeko",        affection_neeko,     "barkeep_overview_neeko"))
        if met_jinx:
            _barkeep_roster.append(("Jinx",         affection_jinx,      "barkeep_overview_jinx"))

    if not _barkeep_roster:
        b "You haven't spoken to anyone yet. Get out there first."
        return

    b "Who did you have in mind?"

    $ _barkeep_page = 0
    $ _barkeep_per_page = 4

    label barkeep_ask_about_page:

        python:
            _barkeep_total = len(_barkeep_roster)
            _barkeep_pages = (_barkeep_total + _barkeep_per_page - 1) // _barkeep_per_page
            _barkeep_start = _barkeep_page * _barkeep_per_page
            _barkeep_slice = _barkeep_roster[_barkeep_start:_barkeep_start + _barkeep_per_page]

        call screen barkeep_name_select(_barkeep_slice, _barkeep_page, _barkeep_pages)

        if _return == "prev":
            $ _barkeep_page -= 1
            jump barkeep_ask_about_page
        elif _return == "next":
            $ _barkeep_page += 1
            jump barkeep_ask_about_page
        elif _return == "back":
            return
        else:
            ## _return is the overview label name
            call expression _return
            b "Anyone else you wanted to ask about?"
            jump barkeep_ask_about_page


## ── Barkeep overview labels ───────────────────────────────────────────────────
##
## One label per character. Each checks affection level and delivers
## an appropriate overview + hint. Affection tiers: 0, 1-2, 3-4, 5+.
## Lines can be revisited freely — Midna's read updates as affection grows.

label barkeep_overview_tristana:
    if affection_tristana >= 5:
        b "Tristana? She's taken a shine to you, that much is clear."
        b "Keep showing up. She respects people who don't fold."
    elif affection_tristana >= 3:
        b "She likes you well enough. The trick with Tristana is matching her energy."
        b "She doesn't have much patience for hesitation."
    elif affection_tristana >= 1:
        b "She's noticed you exist, which is a start."
        b "Join her at the table sometime. Win or lose, she'll remember you better for it."
    else:
        b "Tristana. Gunner. Here most nights, losing most nights, refusing to acknowledge either."
        b "She responds well to a dare. Badly to being ignored."
    return

label barkeep_overview_poppy:
    if affection_poppy >= 5:
        b "Poppy's got her eye on you — in the good way. That doesn't happen easily."
        b "Just keep doing what you're doing."
    elif affection_poppy >= 3:
        b "She's warming up to you. Slowly. That's fast by her standards."
        b "She responds well to people who take the work seriously. Whatever work that is."
    elif affection_poppy >= 1:
        b "You've made an impression. She mentioned you, which she doesn't do."
        b "Don't push. Let her come to you on her own terms."
    else:
        b "Poppy keeps this place from falling apart. She's been doing it longer than I've known her."
        b "She's not unfriendly — she's just not warm on first contact. Give it time."
    return

label barkeep_overview_lulu:
    if affection_lulu >= 5:
        b "Lulu has decided you're interesting. That means Pix has too."
        b "They'll find you. They always do when they've decided."
    elif affection_lulu >= 3:
        b "She's been watching you. Pix too. Take that as the compliment it is."
        b "She opens up in her own time, in her own order. Just follow where she leads."
    elif affection_lulu >= 1:
        b "She's curious about you. With Lulu that's most of the work already done."
        b "Find her during the day. She's more herself away from the evening crowd."
    else:
        b "Lulu. She's been around longer than she looks, and she looks at things the rest of us miss."
        b "Don't try to make sense of everything she says. Just listen to the parts that land."
    return

label barkeep_overview_vex:
    if affection_vex >= 5:
        b "I don't know what you did, but Vex is... different around you."
        b "Don't make a thing of it. She'll close back up if you do."
    elif affection_vex >= 3:
        b "She's stopped making it obvious she wants you to leave. Progress."
        b "Keep showing up. Consistency matters more to her than charm."
    elif affection_vex >= 1:
        b "She hasn't run you off yet. That's more than most people get."
        b "Shadow's the tell — watch it, not her face."
    else:
        b "Vex. Corner booth, far end. Drinks more than she should and talks less than she could."
        b "She's not as indifferent as she looks. Shadow gives her away."
    return

label barkeep_overview_katarina:
    if affection_katarina >= 5:
        b "Katarina's invested. I wouldn't know what to do with that information if I were you."
        b "Whatever you're doing — carefully keep doing it."
    elif affection_katarina >= 3:
        b "She's watching you differently than she watches everyone else."
        b "She doesn't do things without a reason. Figure out what she wants and decide if you want to give it."
    elif affection_katarina >= 1:
        b "You passed her first assessment. She has several more."
        b "Don't try to charm her. She's had better try and fail. Just be direct."
    else:
        b "Katarina. Noxian. Dangerous in ways I'm not going to enumerate."
        b "She comes here to relax, which apparently involves taking everyone's money. Don't play her at dice."
    return

label barkeep_overview_ahri:
    if affection_ahri >= 5:
        b "Ahri's decided something about you. I don't know what, but her tails don't lie."
        b "Whatever she offers, go in with your eyes open."
    elif affection_ahri >= 3:
        b "She's started staying longer when you're here. She thinks I haven't noticed."
        b "She'll come to you when she's ready. Don't rush it."
    elif affection_ahri >= 1:
        b "She's filed you somewhere interesting. That's a start."
        b "Spend time in the city. The more this place gets into you, the more she'll find worth looking at."
    else:
        b "Ahri passes through when she needs something from the wood's edge. She's not a regular."
        b "She reads people. Literally, near as I can tell. Don't try to perform anything — she'll see through it."
    return

label barkeep_overview_ezreal:
    if affection_ezreal >= 5:
        b "Ezreal's dropped the performance around you. That's rare."
        b "He'll never say it directly. Just notice when the stories get quieter."
    elif affection_ezreal >= 3:
        b "He's started telling you the real versions instead of the good ones."
        b "Ask him about Shurima sometime. The answer he gives you will tell you a lot."
    elif affection_ezreal >= 1:
        b "He likes you. He likes most people, but he likes you slightly differently."
        b "Find something to challenge him on. He doesn't respect people who don't push back."
    else:
        b "Ezreal. Explorer, treasure hunter, chronic storyteller."
        b "Half of what he says is true and the other half is what he wished happened. Usually in that order."
    return

label barkeep_overview_nidalee:
    if affection_nidalee >= 5:
        b "Nidalee trusts you. I'm not sure she knows that yet."
        b "Don't give her a reason to reconsider."
    elif affection_nidalee >= 3:
        b "She's stopped tracking you as a variable and started tracking you as a presence."
        b "That's significant, coming from her."
    elif affection_nidalee >= 1:
        b "She's classified you as something other than background noise. That's the first step."
        b "Don't be unpredictable around her. She doesn't like what she can't read."
    else:
        b "Nidalee. She came from the deep wood and never fully left it."
        b "She communicates in assessments, not pleasantries. Don't take it personally."
    return

label barkeep_overview_neeko:
    if affection_neeko >= 5:
        b "Neeko's added you to her internal tribe. In her terms, that's everything."
        b "She'll be you sometimes, when she's thinking about you. It's a compliment."
    elif affection_neeko >= 3:
        b "She's been watching your sho'ma — your essence, near as I can translate it."
        b "Let her be curious. She opens up fast once she decides she trusts someone."
    elif affection_neeko >= 1:
        b "She's interested. With Neeko, interested is most of the distance."
        b "Answer her questions directly, even the strange ones. Especially the strange ones."
    else:
        b "Neeko. She's the last of her kind, though she doesn't dwell on it the way you'd expect."
        b "She shapeshifts — not for disguise, just out of curiosity. Don't be startled."
    return

label barkeep_overview_jinx:
    if affection_jinx >= 5:
        b "Jinx has put you in the category of people she keeps track of. That's not nothing."
        b "She'll remember things you said months ago. She always does, with people who matter."
    elif affection_jinx >= 3:
        b "She's started including you in the Fishbones conversations. Take that seriously."
        b "She doesn't let many people into that."
    elif affection_jinx >= 1:
        b "She's decided you're interesting. You've got maybe a few minutes before she tests that conclusion."
        b "Don't be boring. She has a very low tolerance for boring."
    else:
        b "Jinx. Blue hair, large weapon, very specific relationship with said weapon."
        b "She's not dangerous. Mostly. Just... keep your distance from anything she's pointing Fishbones at."
    return


label tavern_tutorial_poppy:

    ## Poppy was properly introduced at the bar in gameStart.
    ## She's on duty — a nod is all you're getting tonight.
    n "Poppy gives you a brief nod as your eyes meet. She's still watching the room."
    n "You leave her to it."
    return


label tavern_tutorial_tristana:

    ## Met properly at the bar in gameStart — met_tristana is set to 2 there.
    ## On tutorial night she's deep in Katarina's trap and not free to chat.
    n "Tristana is hunched over the table, jaw set, staring at the dice like she can change the outcome through sheer force of will."
    n "The pile in front of her is not encouraging. You decide to leave her to it."
    return


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
            n "She says it so flatly you can't tell if it's a joke."
            vx "This one in particular is loud. And bright. And there are too many people."
            mc "Then why come to a bar?"
            vx "..."
            n "She doesn't answer. The shadow slinks over and sits directly in front of you, staring."

        "Is your shadow... alive?":
            mc "Is your shadow alive?"
            n "For the first time she looks at you — a slow, flat assessment."
            vx "What do you think?"
            mc "I think it is."
            vx "Then you're smarter than most people who talk to me."
            n "Shadow tilts its head. She looks back at the middle distance."
            vx "Don't make it weird."

    n "She pulls her cloak a little tighter and resumes staring at nothing."
    n "Conversation clearly over. You're not sure whether that counted as a good first impression, but somehow you doubt she gives those out."

    hide ch vex profile default with dissolve
    return


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

    k "She's spoken for tonight, by the way. I've put a lot of work into this table."
    k "By the time we're done she'll owe me enough that I'll be collecting on it for quite a while."
    k "In whatever form I see fit. For as long as I like."
    n "The way she says it leaves very little to the imagination."
    k "I'd hate for anything to distract her before we've had a chance to settle up."

    n "She says it pleasantly. Like she's doing you a favor."

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
            k "Good answer."
            n "She glances back at the dice, signaling that's about all the welcome you're going to get."
            n "Somehow it still feels like passing a test."

    hide ch katarina profile default with dissolve
    return


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

    a "You're the one they found in the wood."

    n "It isn't a question."

    mc "Word travels fast."

    a "I was there when they brought you in. You were in poor condition."

    n "She tilts her head slightly."

    a "You're doing better than I expected."

    n "The nine tails behind her shift — a slow, thoughtful motion, like something checking its own impressions."

    mc "Should I be flattered?"

    a "Probably not. I expected very little."

    n "She says it with something that might be a smile."

    n "Then her eyes drift — not away from you, but through you, like she's reading something written underneath."
    n "Her nostrils flicker almost imperceptibly. The tails slow."

    a "You smell like the city. Roads. Iron. Other people's fires."

    n "She considers that for a moment."

    a "Nothing wrong with it. It's just... ordinary. I've read that story before."
    a "Come back when you've spent some time out here. When the wood is in you a little."
    a "When you smell like something that's touched this world and let it touch back."

    n "She tilts her glass, watching the amber catch the light."

    a "That version of you will be much more interesting."

    n "She turns her attention back to the room — not dismissive exactly, just done."
    n "The tails settle. You get the sense she's still aware of exactly where you are."

    hide ch ahri profile default with dissolve
    return


label tavern_tutorial_ezreal:

    if met_ezreal:
        n "Ezreal has migrated to a bigger audience. He catches your eye and gives a quick nod — clearly mid-performance. You'll catch him another time."
        return

    $ met_ezreal = True

    show ch ezreal profile default with dissolve

    n "You hear him before you see him."

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
            n "He says it with total sincerity, like he's correcting a minor error in a ledger."
            ez "No luck. All skill."

        "You said 'occasional legend'?":
            mc "Occasional legend?"
            ez "I'm being modest. It's a new thing I'm trying."
            n "He doesn't look like he's tried it very long."

        "I'll let you get back to your story.":
            mc "Don't let me interrupt."
            ez "You're not interrupting, you're improving the audience-to-story ratio."
            ez "Sit down, this next part is genuinely impressive."

    n "You can't quite tell where the performance ends and the actual person starts."
    n "You suspect he might not know either."

    hide ch ezreal profile default with dissolve
    return


label tavern_tutorial_nidalee_neeko:

    if met_nidalee_neeko:
        n "Neeko is gesturing at something only she can see. Nidalee is nodding slowly. You leave them to it."
        return

    $ met_nidalee_neeko = True

    show ch nidalee profile default at duo_left
    show ch neeko profile default at duo_right
    with dissolve

    n "You hear them before you reach the table."

    ni "You said you weren't going to do it again."

    neo "Neeko did not agree to that. Nidalee said it. Neeko was quiet."

    ni "Quiet is agreement."

    neo "Quiet is quiet. They are not the same thing."

    n "The taller one has the posture of someone who hunts for a living — still, coiled, zero wasted energy."
    n "The shorter one has scales along her jaw and eyes that are doing several things at once, including noticing you."

    neo "Oh."

    n "Neeko looks at you the way you'd look at something you weren't expecting but are immediately glad exists."

    neo "Nidalee. There is a human."

    ni "I know."

    n "She doesn't look at you yet. Still watching Neeko."

    neo "Neeko thinks you should tell the human what we are arguing about."
    neo "So that they can decide for themselves."

    ni "We're not doing that."

    neo "Neeko is doing it."

    n "She turns to you fully, earnest and completely without embarrassment."

    neo "Nidalee believes that Neeko belongs to her. Like territory."
    neo "Neeko believes Nidalee is wrong. But also correct. It is complicated."
    neo "You are [player_name], yes? The one from the forest?"

    mc "That's me."

    neo "Good. Neeko thinks you should weigh in."

    n "Nidalee finally looks at you. It's a slow, complete assessment — the kind that takes inventory."

    ni "Don't."

    neo "Nidalee."

    ni "He doesn't need to be part of this."

    neo "Neeko disagrees. Neeko thinks outside perspective is useful."

    n "A silence. Nidalee holds it the way someone holds a weapon they've decided not to use yet."

    ni "You smell like the deep wood. Whatever came for you out there didn't finish the job."

    n "She says it like it's a fact worth filing."

    ni "Stay out of things that aren't yours."

    n "It's not entirely clear if she's talking to you or to Neeko."
    n "Neeko, for her part, gives you an apologetic look — the kind that says this is a normal Tuesday."

    neo "Neeko is sorry about her. She is like this."
    neo "You can come find Neeko again later. When she is less territorial."

    n "Nidalee says nothing. She picks up her cup, drinks, and resumes watching the room."
    n "You get the sense the argument isn't over. It's just been set down somewhere they'll pick it up again later."

    hide ch nidalee profile default
    hide ch neeko profile default
    with dissolve
    return


label tavern_tutorial_jinx:

    if met_jinx:
        n "Jinx is cross-legged on a table in the corner, disassembling something. You decide not to startle her — you'll find her again later."
        return

    $ met_jinx = True

    show ch jinx profile default with dissolve

    n "She finds you before you find her."

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

    j "You have to give me something. I've been thinking about this since last night."

    n "She seems genuinely aggrieved. Like you've personally inconvenienced her by not having better information about your own near-death experience."

    menu:
        "Big. Blue eyes. Fast.":
            mc "Big. Blue eyes. Fast."
            j "Okay, okay. Blue eyes."
            n "She points at you."
            j "That's something. Fishbones, blue eyes."
            n "She appears to be consulting the rocket launcher."
            j "He says that doesn't narrow it down. He's wrong but I'm not going to tell him that."

        "I'd rather not think about it.":
            mc "I'd rather not think about it, honestly."
            j "Ugh. Fair. Fine."
            n "She says 'fine' the way someone says it when it is not fine."
            j "I'm putting 'big and scary' in my notes."

    j "I'm Jinx, by the way. And this is Fishbones."

    n "She pats the rocket launcher. It does not respond. She seems satisfied anyway."

    j "Don't be weird about him. Everyone's weird about him."

    mc "I'm not being weird."

    j "You're a little weird."
    j "It's fine, I like weird. Normal people are exhausting, right?"

    n "She squints at you with the focused assessment of someone running a rapid threat evaluation."

    j "You're going to be around for a while, yeah? Barkeep's got you set up?"

    mc "That's the plan."

    j "Good. Come find me if anything explodes."
    j "Actually come find me anyway. Things are more likely to explode if I'm involved."

    n "She grins, and for a half-second it's brighter than it should be — the kind of smile that arrives too fast and means too much."
    n "Then she's already turning away, picking up a component from the table and turning it over in her fingers."
    n "Conversation over. You've been filed somewhere."

    hide ch jinx profile default with dissolve
    return
