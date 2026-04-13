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

    n "You take a seat at the counter and are almost immediately greeted by a small, impish creature."
    n "Her black and white skin is adorned with faint blue runes as she floats through the air in complete defiance of gravity."

    scene bg tavern empty
    
    show ch bartender profile default smiling with dissolve

    n "She grins at you, a single sharp fang distinct among her smile."

    b "Well, well, look who\'s finally up, I thought we lost you for sure!"

    n "Her tone is light and teasing, an air of confidence about her that makes you feel a little more at ease as you struggle to find the words."

    mc "I-"

    n "You start, but a rough cough catches you off guard. The Imp frowns sympathetically and pushes a mug of steaming broth towards you."

    b "Take this, you look like you need it."

    n "The smell alone makes your stomach rumble and as soon as the cup is in your hands you start greedily gulping down the hot, delicious soup."

    n "It's salty and rich, filled with vegetables and meat. The kind of meal that warms you up from the inside out and fills you with energy."

    b "You know, most humans know better than to go out into the deep wood at night, unless they're bein' chased, that is."

    b "You're lucky they found you when they did — when we found you out there, there was barely anything left of you."

    n "She drifts over to the other side of the bar filling a cup with ale and setting it in front of another patron."

    n "The other customers around you have started to take notice, casting curious glances your way, but the bartender doesn't seem worried."

    mc "What happened? Where am I?"

    n "She blinks at you in surprise."

    b 'You don\'t know? I don\'t think I\'ve ever heard of someone findin\' this place by accident...'

    n "You look around the room, taking in the myriad of odd and colorful characters."
    n "Most of them are short enough that they barely come up to your hips at full height."

    mc "This... this is Bandle City? This is where the Yordles live?"

    b "Of course it is! What, did you think we were all just a myth or somethin'? Welcome to the hidden city, stranger. Home of the small folk!"

    n "She puffs out her chest proudly and holds her head up high, despite your fatigue your simple male brain can't help but sneak a quick glance at her slender figure."

    n "You look around the room at the Yordles — the small folk. Most of them look more like animals than people."
    n "And yet despite their size and shape, they seem no less human than the rest of you."

    n "They talked, laughed, drank, played cards and told stories."

    b "And on that note, I've got a bit of a proposal for you."
    b "I don't know what you're about or where you're off to, but I don't think you're gonna be fit for travel any time soon."

    b "That being said, there are plenty of people who need help about town."
    b "Considerin' you now owe me for that soup and one of my rooms, I'm thinkin' you outta stick around a while."

    mc "Help around town?"

    b "Mmhm, just some odd jobs here and there. For a fresh-faced human like you it'll take some gettin' used to."
    b "But once you get to know the folk around here, I'm sure you'll settle in just fine."

    n "She's right about one thing — your whole body aches and it's a struggle to just sit upright."
    n "You don't think you could make it a hundred yards without collapsing, let alone all the way back to the city."

    n "You feel like you've been drained to an empty husk."

    show screen system_overlay
    $ constitution_hud_visible = True
    show screen constitution_arrow
    s "Your encounter with Kindred has completely drained you of strength. Try completing tasks around Bandle City to help regain your constitution!"

    menu:
        "Got it.":
            pass

    hide screen constitution_arrow
    hide screen system_overlay

    $ renpy.block_rollback()

    b "You'll be able to stay here in the best lodging this side of the wildwood, The Imp's Delight!"

    b "And if you're willing to work then I can see my way clear to feedin' ya as well."
    b "If you have any questions or want to know more about anyone around here, you just come over to your local friendly barkeep. What do ya say, deal?"

    n "She holds out a faintly clawed hand to you, a mischievous glint in her eye."

    n "You take a moment to look around the room again, drinking in the sounds, the smells, and the sight of it all."
    n "You've never spent much time around Yordles. If the tales were true, most of them tended to be rather solitary creatures."

    n "But these ones seemed friendly enough... if a little boisterous."

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

    n "You take her tiny hand in your own and shake."

    mc "I think I can manage that."

    b "Wonderful! Now, let's talk shop shall we? Unfortunately it seems like your pack got shredded to bits and I doubt there's much left."

    b "Fortunately for you, I've got an old one I wouldn't mind partin' with."
    b "I've got that set aside for you with a bit of starting cash to get you on your feet."

    show screen system_overlay
    show screen backpack_intro
    show screen backpack_arrow

    s "You've unlocked the inventory system! You can access it at any time by clicking the inventory button in the top right corner of the screen."

    menu:
        "Got it.":
            pass

    $ inventory_unlocked = True
    hide screen backpack_arrow
    hide screen backpack_intro
    hide screen system_overlay

    $ renpy.block_rollback()
    show screen inventory_button

    n "You nod in understanding as with a wink she flies to tend to her other patrons."

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
    n "A tiny purple insect-like creature points at you in a mocking gesture as it snickers."

    unkwn "Hey! Pix! That's not nice! Sorry mister, my friend is a bit of a prankster."

    show ch lulu profile default with dissolve

    n "A pair of bright green eyes stare up at you, innocent and curious."
    n "Swaying in the seat next to you, feet kicking playfully, is another patron — purple fur and long hair cascading over a little red dress."

    
    unkwn "Seems like everyone is comin' around to say hi and I was starting to feel left out!"
    unkwn "My name's Lulu, the GREAT sorceress supreme, ultimate magician of Bandle City."

    l "[player_name], huh? Funny sounding name! Humans are always soooo weird like that."

    n "She boasts proudly, holding her chin up in a display of smug confidence. You can't help but giggle a little at the declarations of might from such a tiny thing."

    l "Oh ho, you doubt my powers? Here check THIS out!"

    n "She swipes a gnarled wooden staff from the bar, swinging it out to her side and pointing it across the room toward Tristana, who's gambling with a few other patrons."
    n "After a few moments of intense concentration, Trist reaches up and scratches gently at one of her large furry ears."

    l "See? You see that?"

    mc "That was... what exactly?"

    n "She leans in, her smile dripping with a mischievous sense of accomplishment."

    l "Itchy spell..."

    mc "Right, well uhh... well done."

    l "Darn right!"

    n "She leans back, hands on her sides, seemingly satisfied with your impression of her. With that she swivels on the chair and hops down with a light thud."

    l "Alright well, it's wayyyyy past my bedtime, just wanted to come say hello. I'm usually hanging around here during the day, be sure to come say hi back alright?"

    hide ch lulu profile default with dissolve
    
    n "You nod and she smiles warmly at you before skipping off into the crowd. You let out a sigh, you can't help but feel like bedtime might be the right call."

    n "There are plenty of fresh faces around the room, maybe it would be nice to meet a few of the others. You suspect the bartender would be happy to offer a helping hand."

    show screen system_overlay
    s "The bar is full tonight — feel free to meet some of the other regulars, since they won't always be around."
    s "For more information on anyone you've met, ask the bartender. When you're ready to move on, head back to your room."

    menu:
        "Got it.":
            pass

    hide screen system_overlay

    jump tavern_tutorial_loop
