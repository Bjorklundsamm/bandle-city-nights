label wakingUp:
    stop music fadeout 1.0
    scene bg bedroom default with Dissolve(2.5)
    play ambient "audio/sfx/Tavern_ambience.mp3" fadein 2.0 volume 0.65

    n "Your eyes creep open as the heavy blur of a deep sleep slowly falls away."

    n """
    You

    You.

    You..

    You...

    You... are dead?

    You... are dead? Or...

    You... are dead? Or... are you alive?
    """

    n "You don't think you've ever struggled to figure that out before, but the way your head was feeling you'd be willing to put your money on dead."

    mc '"H-hello?"'

    n "Your voice calls out, raspy and weak. The air around you feels fresh, the light soft and gentle."

    mc '"Is... anyone there?"'

    n "There's no response, but outside the room the sounds of laughter and life echo out."
    n "The familiar bustle of a crowded tavern rings in your ears — a sound that's never been quite as welcoming as it is now."

    n "But more importantly, the concerns over your mortality fade as the scent of warm food tickles your nose."
    n "Your stomach growls painfully, your mouth practically watering as the rich smell of broth fills the air."

    n "It seems as though there's only one thing to do."

menu:
    "Go outside.":
        jump introductions