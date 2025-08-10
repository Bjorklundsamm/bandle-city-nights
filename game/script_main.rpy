# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Narrator")
define b = Character("Barkeep", color="#e6810f")
define mc = Character("Main Character", color="#c8c8c8")
define s = Character("System", color="#ececec")

define unkwn = Character("???", color="#c8c8c8")

define t = Character("Tristana", color="#c8c8c8")
define p = Character("Poppy", color="#c8c8c8")
define l = Character("Lulu", color="#c8c8c8")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg black default

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    n "The sound of the leaves rushing past barely even register as you dash forward, your heart thundering in your chest as you keep your eyes focused ahead of you. Every step seems to jolt you with the force of an explosion."

    scene bg hunted with dissolve 
    
    n "It's as if you can feel yourself growing weaker with each step but you don't have any choice other than to keep moving. Moving forward, moving away, because behind you is danger... no... more than danger..."

    n "Behind you is death, it hunts you as a wolf does a doe and just like that wounded and dying deer you can feel yourself being worn down."

    n "With every beat of your heart you feel a little less alive and a little more afraid, but there is no stopping now. You just need a chance, a sign, anything to help you escape!"

    n "A light burns in the distance, if you could just reach it you could make it to safety, you could finally be free... but it's... it's just so..."

    n "You collapse, tumbling in a violent burst of leaves and dust, your breath coming in desperate and panicked gasps."

    n """
    You're... 
    
    You're... going to die here...

    You're... going to die here... Your skin grows cold, your breath ragged...

    You're... going to die here... Your skin grows cold, your breath ragged... the haunting blue eyes of your pursuer growing closer...
    """

    n "The world around you fades to black and the last thing you feel before the sweet embrace of death is the gentle touch of a small, furred hand."

    n '"Woah, hey mister! Are you alright?! Hey! Hey guys, someone-"'

    n "The words grow more distant as the world slips further away and then it is gone completely."

    jump wakingUp

label introductions:

    scene bg black default

    n "The door opens with a creak as you step into the empty hallway and begin cautiously making your way towards the sound of conversation and life."

    n "The floorboards creek and the walls seem to have a slight draft, but the smell of the food grows stronger and you can feel the hunger growing."

    n "As you round the corner the light grows brighter and the laughter louder, it's almost hard to process as a room full of people of all shapes, sizes and colors comes into view."

    scene bg tavern full with dissolve

    n "There are creatures with long pointy ears and others with long, bushy tails and others that look like animals wearing human clothes dispersed among humans of as many varieties."

    n "None of them seem to notice you, too engaged in their nightly routine to pay attention to some dirty, tired stranger."

    n "It takes you a moment to gather the courage to approach the counter, it's not as though you've never been to a bar before but the trauma of what's happened is still fresh in your mind."

    n "You take a seat at the counter and are nearly immediately greeted by a small, impish creature. Her black and white skin adorned with faint blue runes as she floats through the air in complete defiance of gravity."

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

    b "You know, most humans know better than to go out into the deep wood at night, less they're being chased that is."

    b "There was barely anything left of you when we found you out there"

    n "She drifts over to the other side of the bar filling a cup with ale and setting it in front of another patron."

    n "The other customers around you have started to take notice, casting curious glances your way, but the bartender doesn't seem worried."

    mc "What happend? Where am I?"

    n "She blinks at you in surprise"

    b 'You don\'t know? I don\'t think I\'ve ever heard of someone findin\' this place on accident...'

    n "You looked around the room, taking in the myriad of odd and colorful characters around you, most of them short enough they barely come up to your hips at full height."

    mc "This... this is Bandle City? This is where the Yordles live?"

    b "Of course it is! What, did you think we were all just a myth or somethin'? Welcome to the hidden city, stranger. Home of the small folk!"

    n "She puffs out her chest proudly and holds her head up high, her slender waist accentuating her petite figure."

    n "You look around the room, the people of the small folk, Yordles, as they were known. Most of them looked more like animals than they did people, and yet despite their size and their shape they seemed no less human than the rest of you."

    n "They talked, laughed, drank, played cards and told stories."

    b "And on that note, I've got a bit of a proposal for you. I don't know what you're about or where you're off to, but I don't think you're gonna be fit for travel any time soon."

    b "That being said there are plenty of people who need help about town. Considerin' you now owe me for that soup and one of my rooms, I'm thinkin' you outta stick around a while."

    mc "Help around town?"

    b "Mmhm, just some odd jobs here and there. I imagine for a fresh faced human like you it'll take some gettin' used to but once you get to know the folk around here I'm sure you'll settle in just fine."

    n "She's right about one thing, your whole body aches and it's a struggle to just sit upright. You don't think you could even make it a hundred yards without collapsing, and who knows if you could even make it back to the city if you tried."

    n "It's as if you were literally drained down to the point of an empty husk."

    s "You're encounter with Kindred has completely drained you of strength. Try completing around Bandle City to help regain your constitution!"

    b "You'll be able to stay here in the best lodging this side of the wildwood, The Imp's Delight!"

    b "And if you're willing to work then I can see my way clear to feedin' ya as well. And if you have any questions or want to know more about anyone you just come over to your local friendly barkeep. What do ya say, deal?"

    n "She holds out a faintly clawed hand to you, a mischievous glint in her eye."

    n "You take a moment to look around the room again, the sounds and smells and the sight of the people. You've never really spent much time around Yordles, if the tales were true most of them tended to be rather solitary creatures."

    n "But these ones seemed friendly enough... if a little boisterous."

menu:
    "Accept the deal.":
        jump gameStart

    "Go die in the forest.":
        jump gameover1

label gameStart:

    scene bg tavern empty

    show ch bartender profile default smiling

    n "You take her tiny hand in your own and shake."

    mc "I think I can manage that."

    b "Wonderful! Now, let's talk shop shall we? Unfortunately it seems like your pack got shredded to bits and I doubt there's much left."

    b "Fortunately for you, I've got an old one I wouldn't mind partin' with. I've got that set aside for you with a bit of starting cash to get you on your feet. "

    show screen backpack_intro

    s "You've unlocked the inventory system! You can access it at any time by clicking the inventory button in the top right corner of the screen."

    $ persistent.inventory_unlocked = True
    hide screen backpack_intro
    show screen inventory_button

    n "You nod in understanding as with a wink she flies to tend to her other patrons."

    hide ch bartender profile default smiling with dissolve

    n "The room is loud and lively, filled with the chatter of dozens of different voices, the clattering of silverware and the thumping of mugs against tables. You're almost started as a upbeat voice calls out from behind you."

    unkwn "Well hey there, you're a big fella!"

    show ch tristana profile with dissolve

    n "The voice rings familiar, and as you turn to take in the sight of the little blue and white furred Yordle behind you some part of you is able to sort through your hazy memories. This was the person who saved your life, and it's not hard to put together the pieces that led you here."

    mc "Ah, hey there. You're the one who saved me, right?"

    n "She flashes a toothy grin, holding a gloved hand up towards you."

    t "Yep! Another in my long list of heroic acheivements. Names Tristana, how's it going? I gotta say you're looking a lot better than when I tripped over you last night"

    mc "Yeah, I guess so. Uh... Thanks for the save, by the way, I really owe you."

    n "She grins and waves it off. You can't help but notice an odd warmth in your chest as you're overcome by her upbeat energy."

    t "Eh, don't mention it. If anything you this place was due for a fresh face, gambling with the same people over and over gets real boring real fast. Speaking of which, if you ever wanna join me I'm here just about every night over at that table in the back wall. "

    t "You should swing by for a few games, that is if you're ready to hand over all your hard earned money."

    n "She shoots you a teasing smirk and a wink before taking her drink from the bar and turning to make her way across the room. You barely even register the way your eyes linger on her tiny form."

    hide ch tristana profile with dissolve

    n """
    You had always instinctively thought of Yordles as...

    You had always instinctively thought of Yordles as... it's hard to say...
    """

    n "Is it offensive to say childish? But never having a chance to interact with one the only impression of them you were able to get back in your little village was from the tales of mischievous little tricksters, more interested in pranks and mischief than serious business."

    n "They were definitely tiny, that's much was for sure. But you felt your impressions changing, watching her figure as she crossed the room."

    n "Head maybe a bit larger compared to a humans but those big ears were actually pretty cute. And for such a little thing her arms and stomach were surprisingly toned."

    n "You couldn't help but letting your eyes drift down her shaped back, just a bit. Not to mention, after all, that perfect heart-shaped little-"

    unkwn "Hey."

    show ch poppy profile default with dissolve

    n "You start, for the second time, turning to see a pair of big blonde pigtails and a set of bright pink eyes staring at you. Another blue yordle is looking up at you, judging and weighing you with her gaze."

    n "She was a bit taller than Tristana, but not by much. What she did have though was muscle and the way she crossed her arms showed it."

    unkwn "You're a new face. My name is Poppy."

    mc "Oh, uh... Hi."

    n "Her gaze is unwavering, but there is no animosity behind it. Just a sense of purpose."

    p "I don't want to trouble you but just to make things clear, I'm the bouncer around these parts. Keep your nose out of trouble and we'll get along just fine, got it?"

    n "You nod and she seems satisfied, her stern expression relaxing and a small smile breaking across her features."

    p "Glad to hear it. Welcome to the city, I'm sure we'll be seeing each other around."

    n "Her eyes drift past you and she raises a hand to the imp at the counter before returning to her position near the door. Hopping up onto a stool she resumes her vigil, keeping a careful eye on the room."

    hide ch poppy profile default with dissolve

    n "It's odd, the situation hasn't gotten any less overwhelming but with each smile and friendly greeting the anxiety and uncertainty is fading away. These Yordles, these people are nothing like the monsters that pursued you into the deep forest. These are good people, honest and friendly."

    n "You turn back to your mug and blink in surprise to find it drained to the last drop. A tiny purple insect like creature pointing at you in an imitation of a mocking gesture as it snickers."

    unkwn "Hey! Pix! That's not nice! Sorry mister, my friend is a bit of a prankster."

    show ch lulu profile alone with dissolve

    n "A pair of bright green eyes stare up at you, innocent and curious. Swaying in the seat next to you, feet kicking playfully is another patron with purple fur and long purple hair swaying over her little red dress."

    
    unkwn "Seems like everyone is comin' around to say hi and I was starting to feel left out! My names Lulu, the GREAT sorceress supreme, ultimate magician of Bandle City."

    n "She boasts proudly, holding her chin up in a display of smug confidence. You can't help but get the giggle a bit at the declarations of might from such a little thing."

    l "Oh ho, you doubt my powers? Here check THIS out!"

    n "She swipes a gnarled wooden staff from the bar swinging it out to her side and pointing it across the room to where you see Tristana gambling among a few other patrons. After a few moments of intense focus from your newest friend Trist reaches up and scratches gently at one of her large furry ears."

    l "See? You see that?"

    mc "That was... what exactly?"

    n "She leans in, her smile dripping with a mischievous sense of accomplishment."

    l "Itchy spell..."

    mc "Right, well uhh... well done."

    l "Darn right!"

    n "She leaned back hands on her sides seemingly satisfied at your impression of her. With that she swivels on the chair hopping down with a light thud."

    l "Alright well, it's wayyyyy past my bedtime, just wanted to come say hello. I'm usually hanging around here during the day, be sure to come say hi back alright?"

    hide ch lulu profile alone with dissolve
    
    n "You nod and she smiles warmly at you before skipping off into the crowd. You let out a sigh, you can't help but feel like bedtime might be the right call."

    n "There are plenty of fresh faces around the room, maybe it would be nice to meet a few of the others. You suspect the bartender would be happy to offer a helping hand."

    s "The bar is full tonight, feel free to meet some of the other regulars since they won't always be around. If you want more information on someone you've met you can always ask the bartender. Once you're ready to move on feel free to head back to your room."
