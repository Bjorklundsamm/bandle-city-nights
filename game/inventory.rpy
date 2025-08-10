# Inventory system for Bandle City Nights

# Initialize inventory variables
default persistent.inventory_unlocked = False

# Transform for backpack animation - large center to small top right
transform backpack_intro_animation:
    xalign 0.5
    yalign 0.5
    zoom 2.0
    alpha 1.0
    pause 3.0
    parallel:
        linear 1.5 xalign 0.95
        linear 1.5 yalign 0.05
    parallel:
        linear 1.5 zoom 0.5

# Screen for the backpack introduction animation
screen backpack_intro():
    zorder 300
    add "bt backpack" at backpack_intro_animation

# Screen for the persistent inventory button
screen inventory_button():
    zorder 200
    if persistent.inventory_unlocked:
        imagebutton:
            xalign 0.95
            yalign 0.05
            idle "bt backpack"
            hover "bt backpack"
            action NullAction()
            zoom 0.5
