# Inventory system for Bandle City Nights

## inventory_unlocked default is in narrative/defines.rpy.

transform inventory_button_zoom:
    zoom 0.5

# Screen for the backpack introduction — shown during the system announcement.
# No animation: appears immediately at its final resting position.
screen backpack_intro():
    zorder 300
    add Transform("bt backpack", zoom=0.5) xalign 0.99 yalign 0.02

# Screen for the persistent inventory button.
# Hidden during game-menu screens (quick_menu is False there).
screen inventory_button():
    zorder 260
    if inventory_unlocked and quick_menu:
        imagebutton:
            xalign 0.99
            yalign 0.02
            idle Transform("bt backpack", zoom=0.5, alpha=0.5)
            hover Transform("bt backpack", zoom=0.56, alpha=1.0)
            hover_sound "audio/sfx/hover_selectable.mp3"
            activate_sound "audio/sfx/click_selectable.mp3"
            action Show("inventory_screen")

# Placeholder inventory screen.
# Semi-translucent dark gray, click outside the box or press X to close.
screen inventory_screen():
    modal True
    zorder 500

    # Full-screen dim — clicking anywhere here closes the screen
    button:
        xfill True
        yfill True
        background Solid("#22222299")
        action Hide("inventory_screen")

    # Center panel
    frame:
        xalign 0.5
        yalign 0.5
        xsize 900
        ysize 600
        background Solid("#1a1a1acc")
        padding (40, 40, 40, 40)

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20

            text "Inventory":
                xalign 0.5
                color "#e8e0d0"
                size 52
                font gui.name_text_font

            text "[persistent.gold]g":
                xalign 0.5
                color "#e8c87a"
                size 30
                font gui.name_text_font

    # Close button — sits above the frame in z-order (declared last)
    textbutton "✕":
        xalign 0.97
        yalign 0.03
        action Hide("inventory_screen")
        text_color "#e8e0d0"
        text_hover_color "#ffffff"
        text_size 36
