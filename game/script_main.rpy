# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Narrator")
define b = Character("Barkeep")
define mc = Character("[player_name]")
define s = Character("System")

define unkwn = Character("???")

define t = Character("Tristana")
define p = Character("Poppy")
define l = Character("Lulu")
define f = Character("Fizz")
define vx = Character("Vex")
define k = Character("Katarina")
define a = Character("Ahri")
define ez = Character("Ezreal")
define neo = Character("Neeko")
define ni = Character("Nidalee")
define j = Character("Jinx")

default persistent.fizz_met = False
default persistent.constitution = 1
default persistent.strength = 1
default persistent.charisma = 1
default persistent.intellect = 1
default constitution_hud_visible = False
default player_name = "Stranger"

# Tavern presence flags — set each night before entering the tavern loop.
# All True for the tutorial night; adjust per future night scripts.
# Barkeep and Poppy are unconditional in the screen — no flags needed.
default tristana_in_tavern = True
default vex_in_tavern = True
default katarina_in_tavern = True
default ahri_in_tavern = True
default ezreal_in_tavern = True
default nidalee_neeko_in_tavern = True
default jinx_in_tavern = True

# First-meeting flags for tutorial night introductions.
# Tristana and Poppy are already met via the gameStart sequence.
# met_tristana uses an integer — 1 = met in gameStart, 2+ = tavern scene done.
default met_tristana = 1
default met_poppy = True
default met_vex = False
default met_katarina = False
default met_ahri = False
default met_ezreal = False
default met_nidalee_neeko = False
default met_jinx = False
default met_barkeep = True


# The game starts here.

label start:

    stop music fadeout 1.5

    scene bg black default

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    n "The sound of the leaves rushing past barely even registers as you dash forward, your heart thundering in your chest."
    n "Every step seems to jolt you with the force of an explosion, your eyes fixed desperately on what lies ahead."

    scene bg hunted with dissolve
    play sound "audio/sfx/forest_running.mp3" loop

    n "It's as if you can feel yourself growing weaker with each step, but you don't have any choice other than to keep moving."
    n "Moving forward, moving away... because behind you is danger. No... more than danger..."

    n "Behind you is death. It hunts you as a wolf hunts a doe, and just like that wounded deer you can feel yourself being worn down."

    n "With every beat of your heart you feel a little less alive and a little more afraid, but there is no stopping now."
    n "You just need a chance — a sign, anything — to help you escape!"

    n "A light burns in the distance. If you could just reach it you could make it to safety, finally be free..."
    n "But it's... it's just so..."

    stop sound
    play sound "audio/sfx/body_fall.mp3"
    with hpunch

    n "You collapse, tumbling in a violent burst of leaves and dust, your breath coming in desperate and panicked gasps."

    n """
    You're... 
    
    You're... going to die here...
    """
    
    n """
     Your skin grows cold, your breath ragged... The haunting blue eyes of your pursuer growing closer...
    """

    n "The world around you fades to black and the last thing you feel before the sweet embrace of death is the gentle touch of a small, furred hand."

    n '"Woah, hey mister! Are you alright?! Hey! Hey guys, someone-"'

    n "The words grow more distant as the world slips further away and then it is gone completely."

    jump wakingUp

label introductions:

    scene bg black default

    n "The door opens with a creak as you step into the empty hallway and begin cautiously making your way towards the sound of conversation and life."

    n "The floorboards creak and the walls seem to have a slight draft, but the smell of the food grows stronger and you can feel the hunger growing."

    n "As you round the corner the light grows brighter and the laughter louder, a room full of people of all shapes, sizes, and colors coming into view."

    scene bg tavern full with dissolve
    play music "audio/music/impish_delight.mp3" fadein 2.0

    n "There are creatures with long pointy ears, others with long bushy tails, and some that look like animals wearing human clothes."
    n "They're scattered among humans of every variety imaginable."

    n "None of them seem to notice you, too engaged in their nightly routine to pay attention to some dirty, tired stranger."

    n "It takes you a moment to gather the courage to approach the counter."
    n "It's not as though you've never been to a bar before, but the trauma of what's happened is still fresh in your mind."

    n "You take a seat at the counter and are almost immediately greeted by a small creature behind the bar."
    n "Dark fur marked with swirling patterns that seem to absorb the light rather than catch it, hood up despite the warmth of the room."
    n "She's floating — drifting with the idle ease of someone who stopped finding that remarkable a long time ago."

    scene bg tavern empty

    show ch bartender profile default smiling with dissolve

    n "A single amber eye finds you from beneath the hood, the rest of her face mostly shadow."
    n "She looks at you the way someone looks at a ledger entry they already know the sum of."

    b "Well. You didn't die. That's better than I expected, frankly."

    n "She sets a mug of steaming broth on the counter in front of you without being asked."

    b "Drink that before you try to speak. You look like you need it more than words right now."

    n "You don't argue. The smell alone makes your stomach lurch with hunger and as soon as the cup is in your hands you're gulping it down — salty, rich, hot all the way through."

    b "Most humans who find their way into the deep wood at night are running from something. You were in poor enough shape that I didn't ask."
    b "You're lucky the ones who found you have better instincts than sense. There wasn't much left of you."

    n "She drifts to the other end of the bar, refills a cup without looking, sets it down in exactly the right place, and drifts back."
    n "The other patrons have begun to notice you. She doesn't seem concerned."

    mc "What happened? Where am I?"

    b "You collapsed at the edge of the Bandlewood. Someone brought you in. I gave you a room."
    b "You've been out the better part of a day."

    n "She says it plainly, like she's reading a weather report."

    n "You look around the room — the pointed ears, the tails, the sheer variety of creatures occupying a perfectly ordinary-looking tavern."
    n "Most of them barely come up to your hips."

    mc "This is Bandle City."

    b "It is. Home of the Yordles, the small folk, the hidden city — whichever version you heard growing up."
    b "I take it you didn't come here on purpose."

    mc "Not exactly."

    b "Mm."

    n "She studies you for a moment with that precise, unhurried attention."
    n "You realize you're staring. You can't quite help it."
    n "You've heard stories your whole life — most humans have — but stories don't prepare you for a room full of them."
    n "Tails and ears and fur and things that float and glow and move in ways that have no business being as casual as they are."
    n "And yet every single one of them is just... living. Drinking, arguing, laughing."
    n "Creatures out of myth, completely unbothered by being mythical."

    b "Well. Since you're here and you're upright, I have a proposal."
    b "You owe me for the room and the broth. Your body is in no condition to settle that debt by leaving — you wouldn't make it past the treeline."
    b "As it happens, there are people in this city who need help. Odd jobs. Nothing that requires being in one piece."
    b "Work off what you owe, get back on your feet. A month should cover it."
    b "After that, the debt is clear and you do what you like."

    mc "And if I say no?"

    b "Then you leave now and that's your business."
    n "She says it without any particular weight, which somehow makes it land heavier."
    b "I'd put good coin on you not making it to morning, but I've been wrong before."

    mc "What kind of help?"

    b "The kind that needs doing, as I said. The folk have short arms and shorter patience for things outside their routine."
    b "Come to me when you need context. I know everyone in this room and most of what they haven't said out loud."

    n "She's not wrong. Every part of you aches, and you haven't even tried to stand yet."
    n "You feel hollowed out — like whatever was chasing you took something even after it stopped."

    show screen system_overlay
    $ constitution_hud_visible = True
    show screen constitution_arrow
    s "Your encounter with Kindred has completely drained you of strength. Try completing tasks around Bandle City to help regain your constitution!"

    call screen system_got_it

    hide screen constitution_arrow
    hide screen system_overlay

    $ renpy.block_rollback()

    b "The inn is called The Imp's Delight, since you'll be sleeping here. Best lodging this side of the Bandlewood, though I'll admit the competition isn't fierce."
    b "Food included if you're working. If you have questions — about the city, the folk, any of it — you know where I am."

    n "She holds out a small, dark-furred hand. The markings on her wrist catch your eye — you swear they're shifting, drifting ever so slightly, like something alive beneath the fur."
    b "Do we have an arrangement?"

    n "You look around the room. The noise and warmth of it. The absolute strangeness."
    n "You've never spent much time around Yordles — the stories painted them as solitary, mischievous, not particularly interested in humans."
    n "These ones seem different. Loud, maybe. But not unwelcoming."

menu:
    "Accept the deal.":
        $ renpy.block_rollback()
        jump gameStart

    "Go die in the forest.":
        $ renpy.block_rollback()
        jump gameover1

label gameStart:

    scene bg tavern empty

    show ch bartender profile default smiling

    n "You take her hand. It's smaller than yours, and cooler."

    mc "I think I can manage that."

    b "Good. I thought you might."
    b "Now — your pack didn't survive whatever happened out there. I wouldn't bother looking for it."
    b "I have an old one. Nothing impressive, but functional. There's a small amount of coin with it — enough to get started."

    show screen system_overlay
    show screen backpack_intro
    show screen backpack_arrow

    s "You've unlocked the inventory system! You can access it at any time by clicking the inventory button in the top right corner of the screen."

    call screen system_got_it

    $ inventory_unlocked = True
    hide screen backpack_arrow
    hide screen backpack_intro
    hide screen system_overlay

    $ renpy.block_rollback()
    show screen inventory_button

    n "She gives you one more brief, assessing look — satisfied, or close enough — and drifts back to her end of the bar."

    hide ch bartender profile default smiling with dissolve

    n "The room is loud and lively, filled with chatter, the clattering of silverware, and the thumping of mugs against tables."
    n "You're almost startled as an upbeat voice calls out from behind you."

    unkwn "Well hey there, you're a big fella!"

    show ch tristana profile with dissolve

    n "The voice rings familiar. As you turn, some part of you manages to sort through your hazy memories."
    n "This was the one who saved your life — it's not hard to piece together what must have happened."

    mc "Ah, hey there. You're the one who saved me, right?"

    n "She flashes a toothy grin, holding a gloved hand up towards you."

    t "Yep! Another in my long list of heroic achievements. Name's Tristana, how's it going?"
    t "I gotta say you're looking a lot better than when I tripped over you last night."

    mc "Yeah, I guess so. Uh... Thanks for the save, by the way, I really owe you."

    t "Don't even sweat it! Didn't catch your name though."

    $ player_name = renpy.input("Your name is...?", default="", length=24).strip() or "Stranger"

    mc "It's [player_name]."

    t "[player_name]! Ha, I like it. Alright then, [player_name] — consider the debt paid."

    n "She grins and waves it off. You can't help but notice an odd warmth in your chest as you're overcome by her upbeat energy."

    t "If anything, this place was due for a fresh face — gambling with the same people over and over gets old fast."
    t "If you ever wanna join me, I'm here just about every night at that table in the back."

    t "You should swing by for a few games, that is if you're ready to hand over all your hard earned money."

    n "She shoots you a teasing smirk and a wink before taking her drink from the bar and making her way across the room."
    n "You barely even register the way your eyes linger on her tiny form."

    $ met_tristana = 2

    hide ch tristana profile with dissolve

    n """
    You had always instinctively thought of Yordles as

    You had always instinctively thought of Yordles as.

    You had always instinctively thought of Yordles as..

    You had always instinctively thought of Yordles as...

    You had always instinctively thought of Yordles as... it's hard to say...
    """

    n "Is it offensive to say childish? Never having met one before, the only impression you had back home was from tales of mischievous little tricksters."
    n "More interested in pranks and mischief than anything serious."

    n "They were definitely tiny, that much was for sure. But you felt your impressions changing, watching her figure as she crossed the room."

    n "Head maybe a bit larger compared to a human's, but those big ears were actually pretty cute."
    n "And for such a little thing, her arms and stomach were surprisingly toned."

    n "You couldn't help but let your eyes drift down her shapely back, just a bit. Not to mention, after all, that perfect heart-shaped little—"

    unkwn "Hey."

    show ch poppy profile default with dissolve

    n "You start, for the second time, turning to see a pair of big blonde pigtails and a set of bright pink eyes."
    n "Another blue Yordle is looking up at you, quietly judging and weighing you with her gaze."

    n "She was a bit taller than Tristana, but not by much. What she did have though was muscle and the way she crossed her arms showed it."

    unkwn "You're a new face. My name is Poppy."

    mc "Oh, uh... Hi."

    n "Her gaze is unwavering, but there is no animosity behind it. Just a sense of purpose."

    p "I don't want to trouble you but just to make things clear, I'm the bouncer around these parts. Keep your nose out of trouble and we'll get along just fine, got it?"

    n "You nod and she seems satisfied, her stern expression relaxing and a small smile breaking across her features."

    p "Glad to hear it. I overheard you mention your name was [player_name] — welcome to the city. I'm sure we'll be seeing each other around."

    n "Her eyes drift past you and she raises a hand to the Imp at the counter before returning to her position near the door."
    n "Hopping up onto a stool, she resumes her vigil, keepng a careful eye on the room."

    hide ch poppy profile default with dissolve

    n "It's odd — the situation hasn't gotten any less overwhelming, but with each smile and greeting the anxiety is slowly fading."
    n "These Yordles, these people, are nothing like the monsters that pursued you into the forest. They're good people."

    n "You turn back to your mug and blink in surprise to find it drained to the last drop."
    n "A tiny creature — purple, vaguely insect-shaped, with an expression of deep personal satisfaction — is pointing at you and snickering."

    unkwn "Pix! We talked about this."

    show ch lulu profile default with dissolve

    n "Swaying in the seat next to you is another patron — purple fur, long hair, a little red dress, feet that don't quite reach the floor."
    n "She's looking at you with bright green eyes and an air of someone who has been waiting patiently for exactly this moment."

    l "He does that to people he finds interesting. You should feel good about it."
    l "My name's Lulu. The great sorceress supreme, ultimate magician of Bandle City. It's official."

    n "She says 'official' with the certainty of someone who filed the paperwork herself."

    l "[player_name], huh? That's a good name. It has weight to it. Pix noticed you first, by the way — he's been watching since they brought you in."

    n "The little creature — Pix — glances away with theatrical innocence."

    mc "He's been watching me?"

    l "He watches everyone. But he watched you longer, which means something."

    n "She says it like this settles the matter completely."

    l "Oh! Speaking of which—"

    n "She snatches a gnarled wooden staff from the bar and swings it toward Tristana's table across the room."
    n "After a moment of intense, furrowed concentration, Trist reaches up and scratches slowly at one of her large furry ears."

    l "See that?"

    mc "What did you just do?"

    n "She leans in. Delighted."

    l "Itchy spell."

    mc "...well done."

    l "Thank you. I've been practicing."

    n "She leans back with her hands on her sides, thoroughly satisfied. Then, as if a different thought entirely has arrived, she hops down from the stool with a light thud."

    l "It's past my bedtime by about three hours. I just wanted to come say hello while you were still awake enough to remember it."
    l "I'm usually around during the day. Come find me. Or Pix will find you, which is the same thing."

    hide ch lulu profile default with dissolve

    n "She gives you one last smile — warm, genuine, slightly like she knows something you don't — and skips off into the crowd."
    n "You let out a slow breath. Bedtime is starting to sound reasonable."

    n "There are plenty of fresh faces around the room. She said to come find her if you had questions — but for now, maybe it's worth seeing who else is here."

    show screen system_overlay
    show screen journal_intro
    show screen journal_arrow

    s "You've unlocked the journal! Press J in the top right corner to open it at any time."
    s "Your journal tracks your relationships with the townsfolk and your path to recovery."
    s "There are plenty of people to meet around the city — get out there and introduce yourself."
    s "You have 30 days left to recover and explore the city. Make them count."

    call screen system_got_it

    $ journal_unlocked = True
    hide screen journal_arrow
    hide screen journal_intro
    hide screen system_overlay

    show screen system_overlay

    s "The bar is full tonight — feel free to meet some of the other regulars, since they won't always be around."
    s "For more information on anyone you've met, ask the bartender. When you're ready to move on, head back to your room."

    call screen system_got_it

    hide screen system_overlay

    jump tavern_tutorial_loop
