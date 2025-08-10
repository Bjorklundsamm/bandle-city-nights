define mc = Character("Main Character")
define n = Character("Narrator")

label wakingUp:
    scene bg bedroom default with dissolve

    n "Your eyes creep open as the black bleariness of a deep sleep falls away."

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

    n "There's no response but outside the room the sounds of laughter and life echo out. The ever familiar bustle of a crowded tavern rings in your ears, it's a sound that's never been quite as welcoming as it is now."

    n "But more importantly the concerns over the status of your mortality seem to fade away as the scent of warm food tickles your nose. Your stomach growls painfully, your mouth practically waters as the rich scent of broth fills the air."

    n "It seems as though there's only one thing to do."

menu:
    "Go outside.":
        jump introductions