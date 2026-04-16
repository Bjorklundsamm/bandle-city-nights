# narrative/day2/day2_fizz.rpy
# Fizz's Day 2 introduction and proposition.
# Kept in its own file because day2_fizz_accept contains an [EXPLICIT] block.
# Everything surrounding the explicit section is written here;
# fill in the block and jump to day2_fizz_aftermath when done.


label day2_meet_fizz:

    if fizz_explicit_done:
        n "Fizz is still propped against the wall where you left him."
        n "His trident is leaning in the crook of his elbow."
        n "His eyes are closed."
        n "His tail is moving in slow, deep arcs."
        n "He's asleep."
        n "You must have done more of a number on that little body than you thought."
        n "Best let him rest."
        return

    if met_fizz:
        show ch fizz profile default:
            xalign 0.5
            yalign 1.0
        n "He spots you before you've taken two steps."
        n "Something in his whole posture comes back online."
        f "Hey. You came back."
        f "Look — the offer still stands. Everything I said. All of it."
        f "You will not regret it. I guarantee that on my professional honor as a travel guard."
        n "He holds up the trident slightly."
        f "Which is considerable."
        hide ch fizz profile default
        return

    $ met_fizz = True
    $ persistent.fizz_met = True

    show ch fizz profile default:
        xalign 0.5
        yalign 1.0

    n "You almost miss him — he's propped against the outside wall of the tavern with his arms crossed and his trident leaning in the crook of his elbow."
    n "He sees you first. His whole posture changes in about half a second."

    f "Wait."

    n "He pushes off the wall."

    f "Wait, wait, wait."

    n "He looks at you like you just fell out of the sky."

    f """
    You're

    You're.

    You're..

    You're...

    You're... human.
    """

    mc "Last I checked."

    f "Today is my lucky - okay. Okay! Hi."

    n "He stops. Takes a breath. Remembers he has a job."

    f "My name is Fizz. I'm a travel guard."

    n "He jerks his thumb over his shoulder without looking."

    f "For that."

    mc "The pirate?"

    f "Merchant. She prefers merchant, trader, occassional opportunist. Anything that makes her sound like she's right and proper."

    n "You glance over."
    n "Miss Fortune has that kind of presence — red hair, long coat, the particular architecture of someone the universe built to make a point."
    n "You look maybe half a second longer than you mean to. Letting your glance down to... god damn!"

    n "Fizz clocks it immediately."

    f "*SIGH*"

    mc "I wasn't—"

    f "No, I know. Nobody ever is."

    n "He waves it off. Generous about it. Extremely tired."

    f "Two weeks. Every port, every supply stop, every time we walked anywhere."
    f "Every man within fifty feet just — gone. Completely cooked."
    f "Drooling. Useless. I've seen soldiers forget how to speak."

    mc "I mean—"

    f "Oh I know what she is. I'm the one who's gotta stand next to here on all these stupid trade runs."
    f "You think I don't know?"

    n "He holds both hands out in front of his chest, about a foot apart, palms in."
    n "Stares at you."

    f "You noticed her massive \"pistols\"."

    mc "You sound frustrated... or... jealous?"

    f "Jealous? No, no. It's just — observation."
    f "Like. Objectively. There are options people aren't considering."

    mc "Options."

    f "Better options, potentially. Closer options. Options that are standing right here."

    n "He says it to the middle distance. Very casual. Completely deniable."

    f "It's just, you know, when you travel with someone like that, everyone gets so..."
    f "Fixated. On the obvious thing."
    f "And nobody stops to think — what else might be available? What might feel even better?"

    mc "What might feel better than—"

    f "Tighter. Just as an example. Hypothetically."

    n "He glances off to the side. Not at you."

    f "Someone compact. Who fits better. Who you wouldn't have to be careful with."
    f "Just — hypothetically."

    mc "Are you describing yourself?"

    f "..."

    mc "Fizz."

    f "Okay yes. Obviously."

    n "He looks back. Done pretending."

    f "Let me just say this. Fish don't have a gag reflex."

    mc "...what?"

    f "No reflex. Nothing. You could use my throat as hard as you wanted and I'd just—"

    n "He opens his mouth and his tongue rolls out — long, tapered, slimy, keeps going past where it should stop."
    n "Curls at the tip."
    n "He retracts it."

    f "Do you know what this thing can do?"
    f "I can reach places. I can wrap. I have done things that made grown men cry and they meant it as a compliment."

    n "He points at you."

    f "Behind the tavern. Right now."
    f "What do you say? Lemme at em!"

    menu:
        "Lead the way.":
            jump day2_fizz_accept

        "Not... today. Thanks though.":
            jump day2_fizz_decline


label day2_fizz_accept:

    mc "Lead the way."

    n "He stares at you for half a second."
    n "Then his entire face does something fast and complicated and lands on pure, unfiltered delight."
    n "He takes your hand and starts pulling you away so quickly he leaves his trident behind."

    n "He rounds the corner into the alley without slowing down."
    n "It's narrow, quiet, shaded. Nobody around."
    n "He stops, turns, lets go of your hand."
    n "His skin is already doing something — faint patches of bioluminescence blooming along his collar and forearms."

    f "Okay. Hi."

    n "He looks up at you. The hyperactivity is gone. Something very still and very focused has replaced it."

    n "He reaches up and starts on your belt without asking, fingers already working."
    n "His voice drops to something soft and a little stunned."

    f "I have a type. I know I have a type. Tall, broad, light skin — I have dreamed about this specifically."
    f "And you just — walked out of a door. Today. My day."

    n "Belt loose. Waistband down."
    n "He goes completely still."
    n "Then his pupils eat his eyes."

    f "Tall, light skin, toned and—"

    n "He loses the sentence entirely."

    f "God damn... and PACKING!"

    n "Breathless. Like he's just been told something wonderful."
    n "Even half hard you appear to have left him speechless."
    n "Well, it wasn't the first time someone was a bit surprised about your size."

    f """
    This

    This...

    This... is going fix me.
    """
    # [GEN START]

    # [EXPLICIT START]
    n "He looks up with the sly, depraved smile of a creature who knows exactly what he wants."
    n "He puts both hands on your thighs for support, then his mouth on you — the tip of his tongue creeping out and sliding along the underside of your shaft."

    n "You suck in air."
    n "His tongue is nothing like you've felt before — longer than it should be, unnervingly mobile and strong."
    n "He wraps it around you, starts stroking, coaxing you hard with slow, wet pressure."

    n "Once you're there — breath coming fast, hips already moving in tiny twitches — he takes a deep breath through his gills and slides his lips over the head."
    n "He works his way down."
    n "And doesn't stop."

    n "You feel the back of his throat, feel him adjust, feel his lips keep moving."
    n "He stops."
    n "Not pulling back — stopped. Trembling."
    n "The cords in his neck are standing out. His gills are flaring, working overtime."
    n "His eyes are streaming, not from feeling, from sheer physical strain."
    n "His throat is fighting it — you can feel the resistance, the tissue refusing to open further."

    mc "You... you don't have to—"

    n "His hands dig into your thighs and he shoves himself forward anyway."
    n "A sound comes out of him — low, wrecked, involuntary."

    f "Gghhhnnnhh—khhk... hhnn... nng..."

    n "He keeps going."
    n "It's— it shouldn't fit. You know it doesn't."
    n "You can feel him stretching himself past any sane limit, feel his throat deform around you."
    n "Then finally — warm lips pressing flat against your stomach. His equivalent of a nose is buried in your pubic hair."
    n "Every single inch of you is down his throat."

    n "You stare down, brain misfiring."
    n "He looks up with wet, hazy eyes — a cocky little smile at the corners of his mouth, lips stretched to their limit."

    f "Mmmm?"

    n "Then he swallows."
    n "It's an intense, all-over pulse — his throat closing around you in deliberate waves, milking you with stunning, terrifying skill."
    n "You hiss, your hands fly to his head — not pushing, just holding on."
    n "He does it again. And again."
    n "Slow, agonizing, perfect."
    n "He doesn't flinch. He just keeps swallowing, coaxing out every last pulse with obscene dedication."

    n "Your eyes meet."
    n "He gives you a slow, filthy smile around your cock — then starts pulling off in desperate need of air."

    mc "Oh no you don't."

    n "You take control and slide him back down fast, past the point where he stopped, straight back to that impossible depth."
    n "He locks eyes with you, pupils blown, and moans right into your lap."
    n "Your hips snap forward, holding him there."
    n "He doesn't fight. He relaxes completely, hands clutching your thighs hard enough to bruise."
    n "You thrust."
    n "Hard."

    n "His eyes glaze over. Gills fluttering, overwhelmed."
    n "He's choking, tearing up — but he's smiling, lips stretched tight, drool starting to leak past them."
    n "He is absolutely, shamelessly, into this."
    n "You can see it in the way endless stands of precum dribble from the tip of his pointy red cock."
    n "You hit the back of his throat again and again. No slow, no build, no mercy."

    n "You feel the telltale pressure rising fast. You're getting close."
    n "He's getting close as well. Closer and closer to passing out from the lack of air."
    n "Part of you wants to be brutal and break him. Use him like a ragdoll until you finish getting what you want."
    n "It was what the little slut wanted right? Didn't he tell you to go as hard as you wanted?"
    n "You take in the sight of the little fish boy. The cocksleeve you had made him into."
    n "You gain a new found appreciation of the height difference between humans and Yordles."

    n "You feel him in a weird combination of spasming and going limp."
    n "He whimpers, eyes rolling back and losing focus."
    n "You realize with a start that he might be fading faster than you thought."
    n "He might be in serious danger here."

    n "Reluctantly you elect to pull out and finish on his face. But-"
    n "Just as you try to, as if he predicted your move, his arms wrap around your waist."
    n "You watch, stunned, whether in a final spurt of strength or some depraven form of autopilot, he locks you in a tight embrace."

    n "His mouth stays sealed to your base."
    n "You have no room to pull back. No room to maneuver."
    n "He deliberately keeps himself impaled on your cock, holding your hips against his face."
    n "Gurgling around you, moaning weakly into your skin."

    mc "F-Fizz..."
    mc "Fizz, I'm—!"

    n "You're not even all the way out when it hits."
    n "The first pulse of your orgasm shoots down his throat — and his whole body jerks."
    n "His eyes widen, and every muscle in him locks up."
    n "You're emptying straight into him — hot, thick, endless."
    n "Filling his stomach directly."
    n "And as each new rope floods his throat, Fizz shakes."
    n "Harder. Fiercer."
    n "The sensation, the warmth, the fullness — it's too much."
    n "You feel his body shudder, and watch as ropes of milky cum start spattering over of him onto the grass below."

    n "He's climaxing."
    n "His cock untouched, rigid and painting stripes on the planks — his whole body trembling in pure overstimulation."
    n "His gills flare wide, sucking in air they can't find."
    n "And through every wave of pleasure you pour into him, he's shaking. Quivering. Moaning broken sounds you can't even name."
    n "When you're done — finally, blissfully spent — you can only stare."
    n "He goes boneless all at once, sagging against you, gasping through his gills, eyes half-closed and dazed."
    n "He's sealed on you so tight you have to push his forehead to help him free with a lewd, wet pop."
    n "Thick strings of your spend trail from his swollen lips and stain his chin."
    n "He collapses back onto a patch of grass, chest heaving."
    n "Panting hard, disoriented, coughing weakly."
    n "He's literally dripping."
    n "His cock is still dribbling, and his own stomach is audibly sloshing with your load."
    n "He looks at the ceiling, utterly blissed out, breathing in gasps, tail still twitching with aftershocks."

    f "Hhhh... ah... hhhaaaa..."

    n "The wrecked little Yordle wipes his mouth with a trembling hand."
    n "Smiles like a man who's just found religion."
    n "Then coughs, wetly, turns his head, and chokes slightly before forcing it back down. No wanting to lose even a drop."

 
    # [EXPLICIT END]




    $ fizz_explicit_done = True

    jump day2_fizz_aftermath


label day2_fizz_aftermath:

    show ch fizz profile default:
        xalign 0.5
        yalign 1.0

    n "He's on the ground for a while."
    n "Not moving. Not particularly trying to."
    n "His tail does a slow, satisfied sweep through the dirt."

    f "Okay."

    n "He says it at the sky."

    f "That is the best cock I have ever had in my throat."
    f "I want that on record. Witnessed. Official."

    mc "There's nobody out here."

    f "You're a witness. You count."

    n "He props himself up on one elbow. His bioluminescence is still going — slow, idle pulses now."

    f "I need you to put that inside me sometime."
    f "Like. Actually inside. That's a scheduling note, though. Honestly I might be a little spent."

    n "A pause. He looks past you, thoughtful."

    f "I would pay serious money to watch Miss Fortune try what you just did to me."
    f "She'd choke in three seconds. I'm telling you. Three."

    mc "You did not exactly sail through it."

    f "I finished the job. That's what matters."

    n "He finally sits all the way up. Shakes his head once like he's clearing water from his ears."

    f "Listen up, anytime you need to cum, you find me. Seriously, free use."

    mc "Free use?"

    f "Whenever I'm in town just think of me as your personal fleshlight."
    f "No asking. No explaining yourself. No appointment."
    f "I will literally drop whatever I am doing. I mean that."

    n "He slowly collects himself enough to stand up, looking almost remorseful as he sees you slide your cock back into your pants."

    f "Man, sucks we're only in town today."

    n "He mutters almost to himself as he starts to return to his post in front of the tavern."
    
    f "Next time we stop by I'm gonna ride that thing until you can't walk."

    n "He heads back around the corner. His tail is high."

    hide ch fizz profile default
    return


label day2_fizz_decline:

    mc "Uhh... Not today. But... well, thanks for the offer."

    n "He goes quiet."
    n "The tail stops."

    f "Oh."

    n "A beat. He looks at you, then at the ground, then somewhere past your shoulder."

    f "Right. No, that's — yeah."

    n "He picks up his trident. Turns it over in his hands once."

    f "I just — never mind."

    n "He exhales through his nose. Perking up, clearly not the type of fish to stay down."

    f "Okay. Well, if you ever change your mind..."

    mc "Right. Gotcha."

    n "You turn awkwardly to leave from the unexpected offer. Before he catches your hand."

    f "I'm serious. Ever. Anytime. You want to cum — you come find me. That's it."
    f "Pretty girls and woman, they're fun. But man like you always needs a toy on the side."
    f "Trust me, I know these things."

    n "He says it like he's leaving you a key under a rock."
    n "With that an a wink he lets you go and heads back to his post."

    hide ch fizz profile default
    return
