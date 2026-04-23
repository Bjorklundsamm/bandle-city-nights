################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")
    hover_sound "audio/sfx/hover_selectable.mp3"
    activate_sound "audio/sfx/click_selectable.mp3"

style patron_button is button:
    hover_sound None
    activate_sound None
    padding (0, 0, 0, 0)
    background None

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Solid("#c8a87acc")
    right_bar Solid("#3a302899")

style vbar:
    xsize gui.bar_size
    top_bar Solid("#3a302899")
    bottom_bar Solid("#c8a87acc")

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Solid("#3a302866")
    thumb Frame(Solid("#7a6a50cc"), gui.scrollbar_borders)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Solid("#3a302866")
    thumb Frame(Solid("#7a6a50cc"), gui.vscrollbar_borders)

style slider:
    ysize gui.slider_size
    left_bar Solid("#c8a87acc")
    right_bar Solid("#3a302899")
    thumb Frame(Solid("#c8a87a"), Borders(4, 4, 4, 4))

style vslider:
    xsize gui.slider_size
    top_bar Solid("#3a302899")
    bottom_bar Solid("#c8a87acc")
    thumb Frame(Solid("#c8a87a"), Borders(4, 4, 4, 4))


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################



## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    zorder 260

    if who is not None or (what is not None and what != ""):
        window:
            id "window"

            if who is not None:

                window:
                    id "namebox"
                    style "namebox"
                    text who id "who"

            text what id "what"

            ## Emotion icon — left side of textbox, set via emotion_icon variable.
            if emotion_icon is not None and not renpy.variant("small"):
                if renpy.has_image(emotion_icon):
                    add emotion_icon at emotion_icon_pos
                else:
                    frame:
                        xanchor 0.0
                        yanchor 0.5
                        xpos 240
                        ypos 105
                        xsize 240
                        ysize 50
                        background Solid("#ff6b3530")
                        foreground Frame(Solid("#ff6b3570"), Borders(1, 1, 1, 1))
                        padding (6, 4)
                        text "[emotion_icon]":
                            xalign 0.5
                            yalign 0.5
                            color "#ff6b35dd"
                            size 12
                            font gui.name_text_font
                            text_align 0.5

    else:
        ## No content — still render the required ids so Ren'Py internals don't break.
        window at Transform(alpha=0.0):
            id "window"
            text "" id "what"

    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Transform("gui/textbox.png", xalign=0.5, yalign=0.0, alpha=0.75)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize 305
    ypos gui.name_ypos
    ysize 40

    background None
    padding (0, 0, 0, 0)

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign 0.5
    yalign 0.5
    text_align 0.5
    color "#100b09"

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xanchor 0.5
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    textalign 0.5
    layout "greedy"
    adjust_spacing False
    color "#7c7e79"

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")
    color "#7c7e79"

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width
    color "#7c7e79"


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    vbox:
        xalign 0.5
        yalign 0.5
        spacing gui.choice_spacing

        for i in items:
            button:
                background None
                hover_background None
                padding (0, 0)
                action i.action
                hover_sound "audio/sfx/hover_selectable.mp3"
                activate_sound "audio/sfx/click_selectable.mp3"
                fixed:
                    xsize 640
                    ysize 54
                    add "gui/fade_choice_bar.png" xpos 0 ypos 0
                    text i.caption:
                        xalign 0.5
                        yalign 0.5
                        color "#d4c4a8"
                        hover_color "#ffffff"
                        size 26
                        font gui.choice_button_text_font
                        text_align 0.5


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            # textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            # textbutton _("Q.Save") action QuickSave()
            # textbutton _("Q.Load") action QuickLoad()
            textbutton _("Menu") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")
    config.overlay_screens.append("constitution_hud")
    config.overlay_screens.append("energy_hud")
    config.overlay_screens.append("journal_button")

default quick_menu = True


## System announcement overlay #################################################
##
## Dark veil shown behind system message textboxes.
## The say screen (zorder 260), hearts (overlay layer), and backpack (zorder 300)
## all render above this (zorder 249) so they remain visible.
## Show/hide this in the script around any s "..." announcement line.

screen system_overlay():
    zorder 249
    add Solid("#000000c0")


## System "Got it." button #####################################################
##
## A clickable button shown at the top of the screen during system announcements.
## Use `call screen system_got_it` in the script — it returns immediately when
## clicked so the script can then hide the overlay and continue.
## zorder 310 places it above the overlay (249) and the say screen (260).

## fade_choice_bar — transparent→dark→transparent horizontal bar.
## Generated at init time as a PNG using pure Python (struct + zlib).
## Written to game/gui/fade_choice_bar.png so Ren'Py loads it normally.
## The bar is 640×54px; text is layered on top inside a fixed.

init python:
    import struct, zlib, os

    def _write_png(path, width, height, rows_rgba):
        """Write a minimal RGBA PNG to disk."""
        def chunk(tag, data):
            c = tag + data
            return struct.pack(">I", len(data)) + c + struct.pack(">I", zlib.crc32(c) & 0xFFFFFFFF)

        raw = b""
        for row in rows_rgba:
            raw += b"\x00" + bytes(row)

        png = (
            b"\x89PNG\r\n\x1a\n"
            + chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 6, 0, 0, 0))
            + chunk(b"IDAT", zlib.compress(raw, 9))
            + chunk(b"IEND", b"")
        )
        with open(path, "wb") as f:
            f.write(png)

    def _make_fade_bar_png(path, width=640, height=54,
                           mid_r=0x1a, mid_g=0x1a, mid_b=0x1a, mid_a=0xcc,
                           fade_w=180):
        rows = []
        for _y in range(height):
            row = []
            for x in range(width):
                if x < fade_w:
                    t = x / float(fade_w)
                elif x > width - fade_w:
                    t = (width - x) / float(fade_w)
                else:
                    t = 1.0
                a = int(mid_a * t)
                row += [mid_r, mid_g, mid_b, a]
            rows.append(row)
        _write_png(path, width, height, rows)

    _bar_path  = os.path.join(renpy.config.gamedir, "gui", "fade_choice_bar.png")
    _bar_path2 = os.path.join(renpy.config.gamedir, "gui", "fade_choice_bar_hover.png")
    _make_fade_bar_png(_bar_path,  mid_r=0x1a, mid_g=0x1a, mid_b=0x1a, mid_a=0xcc)
    _make_fade_bar_png(_bar_path2, mid_r=0x2e, mid_g=0x2e, mid_b=0x2e, mid_a=0xcc)


screen system_got_it():
    zorder 310
    modal True
    button:
        xalign 0.5
        yalign 0.5
        background None
        hover_background None
        padding (0, 0)
        action [Function(renpy.block_rollback), Return()]
        hover_sound "audio/sfx/hover_selectable.mp3"
        activate_sound "audio/sfx/click_selectable.mp3"
        fixed:
            xsize 640
            ysize 54
            add "gui/fade_choice_bar.png" xpos 0 ypos 0
            text "Got it.":
                xalign 0.5
                yalign 0.5
                color "#d4c4a8"
                hover_color "#ffffff"
                size 26
                font gui.number_font


## Announcement arrows #########################################################
##
## Off-white bobbing arrows shown during system announcements to highlight
## newly revealed UI elements. Adjust xpos/ypos if heart or backpack size changes.
##
## Constitution arrow — points left toward the hearts in the top-left corner.
## Backpack arrow — points right toward the backpack icon in the top-right corner.
## Journal arrow — points right toward the journal button below the backpack.

## Position + bob baked into the transform so no screen-level container is needed,
## which avoids any inherited box styling on the arrow character.

transform const_arrow_anim:
    ## Sits to the right of the hearts row, bobs left toward them.
    ## ypos 52 = center of the hearts row (xpos 20, ypos 20, hearts ~64px tall at zoom=0.5).
    xpos 395 ypos 52 yanchor 0.5 xoffset 0
    linear 0.45 xoffset -20
    linear 0.45 xoffset 0
    repeat

transform pack_arrow_anim:
    ## Sits to the left of the backpack icon, bobs right toward it.
    ## ypos 52 = center of the backpack icon (xalign 0.99, yalign 0.02, ~64px tall at zoom=0.5).
    xpos 1745 ypos 52 yanchor 0.5 xoffset 0
    linear 0.45 xoffset 20
    linear 0.45 xoffset 0
    repeat

transform journal_arrow_anim:
    ## Sits to the left of the journal button, bobs right toward it.
    ## ypos 134 = center of the journal icon (xalign 0.99, yalign 0.10, ~64px tall at zoom=0.5).
    xpos 1745 ypos 134 yanchor 0.5 xoffset 0
    linear 0.45 xoffset 20
    linear 0.45 xoffset 0
    repeat

transform energy_arrow_anim:
    ## Sits to the right of the energy display, bobs left toward it.
    xpos 90 ypos 90 yanchor 0.5 xoffset 0
    linear 0.45 xoffset -20
    linear 0.45 xoffset 0
    repeat

## Navigation arrow hover bounces — used by travel buttons in hub screens.

transform nav_arrow_bounce:
    ## Vertical bob for down-pointing arrows (rotate=90).
    yoffset 0
    linear 0.3 yoffset 7
    linear 0.3 yoffset 0
    repeat

transform nav_arrow_bounce_diag:
    ## Down-left bob for diagonal arrows (rotate=135).
    xoffset 0 yoffset 0
    linear 0.3 xoffset -5 yoffset 5
    linear 0.3 xoffset 0 yoffset 0
    repeat

transform emotion_icon_pos:
    ## Positions the emotion icon in the bottom-left of the textbox.
    zoom 0.375
    alpha 0.6
    xanchor 0.0
    yanchor 0.5
    xpos 240
    ypos 105

screen constitution_arrow():
    zorder 310
    add Transform("pointer arrow", xzoom=-1.0, zoom=0.5, alpha=0.6) at const_arrow_anim

screen backpack_arrow():
    zorder 310
    add Transform("pointer arrow", zoom=0.5, alpha=0.6) at pack_arrow_anim

screen journal_arrow():
    zorder 310
    add Transform("pointer arrow", zoom=0.5, alpha=0.6) at journal_arrow_anim

screen energy_arrow():
    zorder 310
    add Transform("pointer arrow", xzoom=-1.0, zoom=0.5, alpha=0.6) at energy_arrow_anim

screen energy_intro():
    ## Preview of the energy display shown during the system announcement.
    zorder 300
    hbox:
        xpos 20
        ypos 90
        spacing 2
        for i in range(3):
            if i < energy:
                add Transform("bt energy full", zoom=0.175)
            else:
                add Transform("bt energy empty", zoom=0.175)


## Constitution HUD ############################################################
##
## Five hearts displayed in the top-left. Each heart has 5 sections (25 total).
## constitution tracks the total filled sections (starts at 1).
## Formula per heart i:  min(max(constitution - i*5, 0), 5)
##
## To gain a constitution point:  $ constitution += 1
## Images live at:  game/gui/hud/Heart - N.png  (N = 0..5)
## Adjust zoom (currently 0.5) here if hearts appear too large or small.

screen constitution_hud():
    zorder 260
    ## Hidden during game-menu screens (quick_menu is False there).
    if constitution_hud_visible and quick_menu:
        hbox:
            xpos 20
            ypos 20
            spacing 6
            for i in range(5):
                add Transform(
                    "gui/hud/Heart - %d.png" % min(max(constitution - i * 5, 0), 5),
                    zoom=0.5
                )

screen energy_hud():
    zorder 260
    if energy_hud_visible and quick_menu:
        hbox:
            xpos 20
            ypos 90
            spacing 2
            for i in range(3):
                if i < energy:
                    add Transform("bt energy full", zoom=0.175)
                else:
                    add Transform("bt energy empty", zoom=0.175)

## Barkeep: ask about someone ################################################
##
## Paginated name selection screen. Called from barkeep_ask_about_page.
## _slice  — list of (display_name, affection, label) for this page
## _page   — current page index (0-based)
## _pages  — total number of pages
##
## Returns: label name string, "prev", "next", or "back"

screen barkeep_name_select(_slice, _page, _pages):
    modal True
    zorder 200

    vbox:
        xalign 0.5
        yalign 0.5
        spacing gui.choice_spacing

        for _name, _aff, _label in _slice:
            button:
                background None
                hover_background None
                padding (0, 0)
                action Return(_label)
                hover_sound "audio/sfx/hover_selectable.mp3"
                activate_sound "audio/sfx/click_selectable.mp3"
                fixed:
                    xsize 640
                    ysize 54
                    add "gui/fade_choice_bar.png" xpos 0 ypos 0
                    text "[_name]":
                        xalign 0.5
                        yalign 0.5
                        color "#d4c4a8"
                        hover_color "#ffffff"
                        size 26
                        font gui.choice_button_text_font
                        text_align 0.5

        null height 4

        hbox:
            xalign 0.5
            spacing gui.choice_spacing

            if _page > 0:
                button:
                    background None
                    hover_background None
                    padding (0, 0)
                    action Return("prev")
                    hover_sound "audio/sfx/hover_selectable.mp3"
                    activate_sound "audio/sfx/click_selectable.mp3"
                    fixed:
                        xsize 640
                        ysize 54
                        add "gui/fade_choice_bar.png" xpos 0 ypos 0
                        text "← Previous":
                            xalign 0.5
                            yalign 0.5
                            color "#d4c4a8"
                            hover_color "#ffffff"
                            size 26
                            font gui.choice_button_text_font
                            text_align 0.5

            button:
                background None
                hover_background None
                padding (0, 0)
                action Return("back")
                hover_sound "audio/sfx/hover_selectable.mp3"
                activate_sound "audio/sfx/click_selectable.mp3"
                fixed:
                    xsize 640
                    ysize 54
                    add "gui/fade_choice_bar.png" xpos 0 ypos 0
                    text "Never mind":
                        xalign 0.5
                        yalign 0.5
                        color "#d4c4a8"
                        hover_color "#ffffff"
                        size 26
                        font gui.choice_button_text_font
                        text_align 0.5

            if _page < _pages - 1:
                button:
                    background None
                    hover_background None
                    padding (0, 0)
                    action Return("next")
                    hover_sound "audio/sfx/hover_selectable.mp3"
                    activate_sound "audio/sfx/click_selectable.mp3"
                    fixed:
                        xsize 640
                        ysize 54
                        add "gui/fade_choice_bar.png" xpos 0 ypos 0
                        text "More →":
                            xalign 0.5
                            yalign 0.5
                            color "#d4c4a8"
                            hover_color "#ffffff"
                            size 26
                            font gui.choice_button_text_font
                            text_align 0.5


style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")
    hover_sound "audio/sfx/hover_selectable.mp3"
    activate_sound "audio/sfx/click_selectable.mp3"

style quick_button_text:
    properties gui.text_properties("quick_button")


## Tavern Hub screen ###########################################################
##
## Interactive tavern view shown during free-roam nights. The scene background
## (bg tavern empty) is set in the label before calling this screen.
##
## Position images are 1920x1088 but the viewport is 1920x1080.
## patron_zoom handles both centering and the hover effect: each button gets its
## own instance of the transform, so patrons animate independently and the zoom
## always resets cleanly on blur (fixes the "permanently zoomed" caching bug
## that occurred with paired idle/hover Transform objects sharing the same image).
##
## Draw order matters for overlap: elements declared earlier are drawn first
## (further back). Ezreal is declared before Ahri so Ahri renders on top.
##
## Barkeep and Poppy are unconditional; all others are guarded by their flag.

transform patron_zoom:
    xanchor 0.5 yanchor 0.5 xpos 960 ypos 535
    zoom 1.0
    on hover:
        linear 0.15 zoom 1.005
    on idle:
        linear 0.15 zoom 1.0

transform dice_hover:
    alpha 0.65
    on hover:
        linear 0.1 alpha 1.0
    on idle:
        linear 0.1 alpha 0.65

screen tavern_hub():
    zorder 1

    ## ── Barkeep (always present) ─────────────────────────────────────────────
    button:
        style "patron_button"
        focus_mask True
        xsize 1920
        ysize 1088
        action Return("barkeep")
        add "ch barkeep tavern position" at patron_zoom

    ## ── Poppy — bouncer, always at the door ──────────────────────────────────
    button:
        style "patron_button"
        focus_mask True
        xsize 1920
        ysize 1088
        action Return("poppy")
        add "ch poppy tavern position" at patron_zoom

    ## ── Tristana ─────────────────────────────────────────────────────────────
    ## (image is named "ch tristana tavern" — no "position" suffix)
    if tristana_in_tavern:
        button:
            style "patron_button"
            focus_mask True
            xsize 1920
            ysize 1088
            action Return("tristana")
            add "ch tristana tavern" at patron_zoom

    ## ── Vex ──────────────────────────────────────────────────────────────────
    if vex_in_tavern:
        button:
            style "patron_button"
            focus_mask True
            xsize 1920
            ysize 1088
            action Return("vex")
            add "ch vex tavern position" at patron_zoom

    ## ── Katarina ─────────────────────────────────────────────────────────────
    if katarina_in_tavern:
        button:
            style "patron_button"
            focus_mask True
            xsize 1920
            ysize 1088
            action Return("katarina")
            add "ch katarina tavern position" at patron_zoom

    ## ── Ezreal (behind Ahri — declared first) ────────────────────────────────
    if ezreal_in_tavern:
        button:
            style "patron_button"
            focus_mask True
            xsize 1920
            ysize 1088
            action Return("ezreal")
            add "ch ezreal tavern position" at patron_zoom

    ## ── Ahri (in front of Ezreal — declared after) ───────────────────────────
    if ahri_in_tavern:
        button:
            style "patron_button"
            focus_mask True
            xsize 1920
            ysize 1088
            action Return("ahri")
            add "ch ahri tavern position" at patron_zoom

    ## ── Nidalee & Neeko (shared position image) ──────────────────────────────
    if nidalee_neeko_in_tavern:
        button:
            style "patron_button"
            focus_mask True
            xsize 1920
            ysize 1088
            action Return("nidalee_neeko")
            add "ch nidalee and neeko tavern position" at patron_zoom

    ## ── Jinx ─────────────────────────────────────────────────────────────────
    if jinx_in_tavern:
        button:
            style "patron_button"
            focus_mask True
            xsize 1920
            ysize 1088
            action Return("jinx")
            add "ch jinx tavern position" at patron_zoom

    ## ── Leave button — diagonal arrow, lower-left corner ────────────────────
    button:
        xalign 0.0
        yalign 1.0
        background None
        hover_background Frame("gui/fade_choice_bar.png", 80, 0)
        padding (14, 8)
        action [Function(renpy.block_rollback), Return("leave")]
        hbox:
            spacing 10
            yalign 0.5
            add Transform("pointer arrow", zoom=0.63, rotate=135, alpha=0.6) yalign 0.5
            text "Return to your room":
                size 22
                color "#d4c4a800"
                hover_color "#d4c4a8ee"


## Journal Button ##############################################################
##
## Displayed below the backpack in the top-right corner.
## The journal tracks relationships, stats, and days elapsed.
## Unlocked alongside the journal system announcement in gameStart.

screen journal_button():
    zorder 260
    if journal_unlocked and quick_menu:
        imagebutton:
            xalign 0.99
            yalign 0.10
            idle Transform("bt journal", zoom=0.5, alpha=0.5)
            hover Transform("bt journal", zoom=0.56, alpha=1.0)
            hover_sound "audio/sfx/hover_selectable.mp3"
            activate_sound "audio/sfx/click_selectable.mp3"
            action Show("journal_screen")


## Journal intro preview — shown during the system announcement so the player
## can see the button while it's being described.
screen journal_intro():
    zorder 300
    add Transform("bt journal", zoom=0.5) xalign 0.99 yalign 0.10


## Journal Screen ##############################################################
##
## Full overlay showing:
##   • Day tracker (Day X / 31)
##   • Stats: Constitution, Strength, Charisma, Intellect
##   • People — silhouette (?) if not met, name + affection hearts if met
##
## Characters not in the tavern tonight: Kindred, Lilia, Miss Fortune, Fizz, Morgana.
## All 5 start unmet so they show as question marks.

init python:
    ## All characters tracked in the journal.
    ## Each entry: (internal_key, display_name, met_flag_name, affection_var_name)
    journal_characters = [
        ## Tavern regulars
        ("barkeep",       "Barkeep",       "met_barkeep",        "affection_barkeep"),
        ("tristana",      "Tristana",      "met_tristana",       "affection_tristana"),
        ("poppy",         "Poppy",         "met_poppy",          "affection_poppy"),
        ("lulu",          "Lulu",          "met_lulu",           "affection_lulu"),
        ("vex",           "Vex",           "met_vex",            "affection_vex"),
        ("katarina",      "Katarina",      "met_katarina",       "affection_katarina"),
        ("ahri",          "Ahri",          "met_ahri",           "affection_ahri"),
        ("ezreal",        "Ezreal",        "met_ezreal",         "affection_ezreal"),
        ("nidalee",       "Nidalee",       "met_nidalee_neeko",  "affection_nidalee"),
        ("neeko",         "Neeko",         "met_nidalee_neeko",  "affection_neeko"),
        ("jinx",          "Jinx",          "met_jinx",           "affection_jinx"),
        ## Not in tavern tonight
        ("kindred",       "Kindred",       "met_kindred",        "affection_kindred"),
        ("lilia",         "Lilia",         "met_lilia",          "affection_lilia"),
        ("miss_fortune",  "Miss Fortune",  "met_miss_fortune",   "affection_miss_fortune"),
        ("fizz",          "Fizz",          "met_fizz",           "affection_fizz"),
        ("morgana",       "Morgana",       "met_morgana",        "affection_morgana"),
    ]

## All defaults (affection, met flags, current_day) are in narrative/defines.rpy.

screen journal_screen():
    modal True
    zorder 500

    ## Full-screen dim — click outside to close
    button:
        xfill True
        yfill True
        background Solid("#22222299")
        action Hide("journal_screen")

    ## Main journal panel
    frame:
        xalign 0.5
        yalign 0.5
        xsize 960
        ysize 680
        background Solid("#1a1a1acc")
        padding (40, 36, 40, 36)

        vbox:
            spacing 18

            ## ── Title + day ──────────────────────────────────────────────────
            hbox:
                xfill True
                text "Journal":
                    xalign 0.0
                    color "#e8e0d0"
                    size 46
                    font gui.name_text_font
                text "Day [current_day] / 31":
                    xalign 1.0
                    color "#a09880"
                    size 26
                    yalign 0.7
                    font gui.number_font

            ## ── Stats ────────────────────────────────────────────────────────
            frame:
                background Solid("#ffffff11")
                padding (16, 12)
                xfill True
                vbox:
                    spacing 6
                    text "Stats":
                        color "#c8b89a"
                        size 22
                        font gui.name_text_font
                    grid 2 2:
                        xfill True
                        spacing 4
                        text "Constitution  [constitution] / 25":
                            color "#e8e0d0"
                            size 19
                        text "Strength  [strength] / 10":
                            color "#e8e0d0"
                            size 19
                        text "Charisma  [charisma] / 10":
                            color "#e8e0d0"
                            size 19
                        text "Intellect  [intellect] / 10":
                            color "#e8e0d0"
                            size 19

            ## ── People ───────────────────────────────────────────────────────
            text "People":
                color "#c8b89a"
                size 22
                font gui.name_text_font

            viewport:
                xfill True
                ysize 340
                scrollbars "vertical"
                mousewheel True
                vbox:
                    spacing 0
                    for key, display_name, met_flag, affection_var in journal_characters:
                        python:
                            _met = getattr(store, met_flag, False)
                            _hearts = getattr(store, affection_var, 0)
                        fixed:
                            xfill True
                            ysize 38
                            ## Name at xpos 0 — length doesn't affect anything else.
                            if _met:
                                text "[display_name]":
                                    xpos 0
                                    yalign 0.5
                                    color "#e8e0d0"
                                    size 20
                            else:
                                text "???":
                                    xpos 0
                                    yalign 0.5
                                    color "#555555"
                                    size 20
                            ## Hearts pinned to xpos 200 — always the same column.
                            if _met:
                                hbox:
                                    xpos 200
                                    yalign 0.5
                                    spacing 4
                                    for h in range(5):
                                        if h < _hearts:
                                            add Transform("journal heart full", zoom=0.12) yalign 0.5
                                        else:
                                            add Transform("journal heart empty", zoom=0.12) yalign 0.5
                        ## Thin separator between entries
                        frame:
                            background Solid("#ffffff18")
                            xfill True
                            ysize 1
                            padding (0, 0, 0, 0)

    ## Close button
    textbutton "✕":
        xalign 0.97
        yalign 0.03
        action Hide("journal_screen")
        text_color "#e8e0d0"
        text_hover_color "#ffffff"
        text_size 36


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing 4

        if main_menu:

            textbutton _("New Game") action Start()

        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Options") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            null height 28

            textbutton _("Main Menu") action MainMenu()

        if renpy.variant("pc"):

            null height 28

            textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    background None
    hover_background Solid("#c8a87a1a")
    padding (14, 8, 14, 8)
    hover_sound "audio/sfx/hover_selectable.mp3"
    activate_sound "audio/sfx/click_selectable.mp3"

style navigation_button_text:
    font gui.interface_text_font
    size 42
    color "#c8b89a"
    hover_color "#f0e8d8"
    selected_color "#c8a87a"
    insensitive_color "#6a5a4a"


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu
    
    add "bg title tavern default"
    add "sc title default" align (0.85, 0.5)
    add "bt title sticker" xpos 0.85 ypos 0.9 anchor (0.5, 0.5)

    ## This empty frame darkens the main menu.
    frame:
        style "main_menu_frame"

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

# style main_menu_frame:
#     xsize 420
#     yfill True

#     background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid".
## This screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background Solid("#1a1510e6")

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()
                    key "save_page_prev" action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    ## range(1, 10) gives the numbers from 1 to 9.
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()
                    key "save_page_next" action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Upload Sync"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Download Sync"):
                            action DownloadSync()
                            xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")


## Options screen ##############################################################
##
## Player settings: display, gameplay toggles, and audio volumes.

screen preferences():

    tag menu

    use game_menu(_("Options"), scroll="viewport"):

        vbox:
            xfill True
            spacing 0

            ## ── Display ───────────────────────────────────────────────────
            if renpy.variant("pc") or renpy.variant("web"):

                text _("Display"):
                    style "pref_section_header"

                frame:
                    style "pref_section_rule"

                hbox:
                    style_prefix "radio"
                    spacing 0
                    textbutton _("Window") action Preference("display", "window")
                    textbutton _("Fullscreen") action Preference("display", "fullscreen")

                null height 36

            ## ── Gameplay ──────────────────────────────────────────────────
            text _("Gameplay"):
                style "pref_section_header"

            frame:
                style "pref_section_rule"

            hbox:
                style_prefix "check"
                spacing 0
                vbox:
                    xsize 520
                    textbutton _("Skip Unseen Text") action Preference("skip", "toggle")
                    textbutton _("Skip After Choices") action Preference("after choices", "toggle")
                    textbutton _("Disable Transitions") action InvertSelected(Preference("transitions", "toggle"))

            null height 28

            hbox:
                spacing 80

                vbox:
                    xsize 580
                    text _("Text Speed"):
                        style "pref_slider_label"
                    bar value Preference("text speed"):
                        xsize 560

                vbox:
                    xsize 580
                    text _("Auto-Forward Speed"):
                        style "pref_slider_label"
                    bar value Preference("auto-forward time"):
                        xsize 560

            null height 48

            ## ── Audio ─────────────────────────────────────────────────────
            text _("Audio"):
                style "pref_section_header"

            frame:
                style "pref_section_rule"

            hbox:
                spacing 80

                if config.has_music:
                    vbox:
                        xsize 580
                        text _("Music"):
                            style "pref_slider_label"
                        bar value Preference("music volume"):
                            xsize 560

                if config.has_sound:
                    vbox:
                        xsize 580
                        text _("Sound Effects"):
                            style "pref_slider_label"
                        bar value Preference("sound volume"):
                            xsize 560

            if config.has_voice:
                null height 24
                hbox:
                    spacing 80
                    vbox:
                        xsize 580
                        text _("Voice"):
                            style "pref_slider_label"
                        bar value Preference("voice volume"):
                            xsize 560

            if config.has_music or config.has_sound or config.has_voice:
                null height 28
                hbox:
                    style_prefix "check"
                    spacing 0
                    textbutton _("Mute All") action Preference("all mute", "toggle")

            null height 48


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")
    font gui.interface_text_font
    color "#c8b89a"
    hover_color "#f0e8d8"
    selected_color "#c8a87a"
    size 26

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")
    font gui.interface_text_font
    color "#c8b89a"
    hover_color "#f0e8d8"
    selected_color "#c8a87a"
    size 26

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675

## Section headers and rules for the Options screen

style pref_section_header is gui_text:
    font gui.interface_text_font
    color "#c8a87a"
    size 26
    top_margin 16
    bottom_margin 8

style pref_section_rule is frame:
    background Solid("#c8a87a55")
    xfill True
    ysize 1
    padding (0, 0, 0, 0)
    bottom_margin 20

style pref_slider_label is gui_text:
    font gui.interface_text_font
    color "#a09880"
    size 20
    top_margin 10
    bottom_margin 6


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide, B/Right Button")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Bubble screen ###############################################################
##
## The bubble screen is used to display dialogue to the player when using speech
## bubbles. The bubble screen takes the same parameters as the say screen, must
## create a displayable with the id of "what", and can create displayables with
## the "namebox", "who", and "window" ids.
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900


################################################################################
## Placeholder asset system
##
## Used wherever a real asset (bg, ch sprite, bt button) doesn't exist yet.
## ph_bg        — full-screen background stand-in (dark slate + label)
## ph_sprite    — character sprite stand-in (tall outlined box + label)
## ph_button    — interactive button stand-in (small outlined box + label)
##
## Usage in script:
##   call screen ph_bg("bg patron room")
##   call screen ph_sprite("ch katarina sleeping")
##   show screen ph_button("bt dice", 0.72, 0.55)
################################################################################

screen ph_bg(label="[ MISSING BG ]"):
    ## Full-screen dark fill so the scene isn't blank.
    zorder 1
    add Solid("#1a1e24")
    frame:
        xfill True
        yfill True
        background None
        text "[label]":
            xalign 0.5
            yalign 0.5
            color "#ff6b3580"
            size 28
            font gui.name_text_font


screen ph_sprite(label="[ MISSING SPRITE ]", xalign=0.5, yalign=1.0):
    ## Tall outlined box standing in for a character sprite.
    zorder 50
    frame:
        xalign xalign
        yalign yalign
        xsize 280
        ysize 520
        background Solid("#ff6b3518")
        foreground Frame(Solid("#ff6b3560"), Borders(2, 2, 2, 2))
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 12
            text "[[ ART NEEDED ]]":
                xalign 0.5
                color "#ff6b35cc"
                size 18
                font gui.name_text_font
            text "[label]":
                xalign 0.5
                color "#ff6b3599"
                size 14
                font gui.name_text_font


screen ph_button(label="[ MISSING BTN ]", xalign=0.5, yalign=0.5):
    ## Small clickable outlined box standing in for a button/item sprite.
    ## Returns label string on click so the caller can check _return.
    zorder 200
    frame:
        xalign xalign
        yalign yalign
        xsize 120
        ysize 80
        background Solid("#f5c84218")
        foreground Frame(Solid("#f5c84280"), Borders(2, 2, 2, 2))
        button:
            xfill True
            yfill True
            background None
            hover_background Solid("#f5c84230")
            hover_sound "audio/sfx/hover_selectable.mp3"
            activate_sound "audio/sfx/click_selectable.mp3"
            action Return(label)
            text "[label]":
                xalign 0.5
                yalign 0.5
                color "#f5c842cc"
                size 13
                font gui.name_text_font
