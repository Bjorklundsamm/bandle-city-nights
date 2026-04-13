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


## ── Interaction stubs ────────────────────────────────────────────────────────
##
## Each label should show the relevant profile/tavern sprite, run its dialogue,
## then `return` to drop back into the loop. Keep scene state clean:
## restore bg tavern empty and hide profile sprites before returning if you
## change them inside the interaction.


label tavern_tutorial_barkeep:

    show ch bartender profile default smiling with dissolve
    b "I can't wait to be your cocksleeve, but I'm still in development!"
    hide ch bartender profile default smiling with dissolve
    return


label tavern_tutorial_poppy:

    show ch poppy profile default with dissolve
    p "I can't wait to be your cocksleeve, but I'm still in development!"
    hide ch poppy profile default with dissolve
    return


label tavern_tutorial_tristana:

    show ch tristana profile default with dissolve
    t "I can't wait to be your cocksleeve, but I'm still in development!"
    hide ch tristana profile default with dissolve
    return


label tavern_tutorial_vex:

    show ch vex profile default with dissolve
    vx "I can't wait to be your cocksleeve, but I'm still in development!"
    hide ch vex profile default with dissolve
    return


label tavern_tutorial_katarina:

    show ch katarina profile default with dissolve
    k "I can't wait to be your cocksleeve, but I'm still in development!"
    hide ch katarina profile default with dissolve
    return


label tavern_tutorial_ahri:

    show ch ahri profile default with dissolve
    a "I can't wait to be your cocksleeve, but I'm still in development!"
    hide ch ahri profile default with dissolve
    return


label tavern_tutorial_ezreal:

    show ch ezreal profile default with dissolve
    ez "I can't wait to be your cocksleeve, but I'm still in development!"
    hide ch ezreal profile default with dissolve
    return


label tavern_tutorial_nidalee_neeko:

    show ch nidalee profile default at duo_left
    show ch neeko profile default at duo_right
    with dissolve

    ni "I can't wait to be your cocksleeve, but I'm still in development!"
    neo "I can't wait to be your cocksleeve, but I'm still in development!"

    hide ch nidalee profile default
    hide ch neeko profile default
    with dissolve
    return


label tavern_tutorial_jinx:

    show ch jinx profile default with dissolve
    j "I can't wait to be your cocksleeve, but I'm still in development!"
    hide ch jinx profile default with dissolve
    return
