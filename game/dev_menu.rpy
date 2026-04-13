# dev_menu.rpy
# Developer overlay — tiny dot in top-right corner opens a debug panel.
# Always registered as an overlay screen so it's available everywhere in-game.
# To disable entirely: comment out the config.overlay_screens line below.

init python:
    config.overlay_screens.append("dev_dot")


## ── Dev dot ──────────────────────────────────────────────────────────────────
## A tiny, barely-visible dot in the top-right corner. Click to open the menu.

screen dev_dot():
    zorder 9999
    button:
        xalign 1.0
        yalign 0.0
        xoffset -6
        yoffset 6
        background Solid("#ffffff22")
        hover_background Solid("#ffffff88")
        padding (5, 5)
        action Show("dev_menu")
        text "·":
            size 14
            color "#ffffff55"
            hover_color "#ffffffff"


## ── Dev menu ─────────────────────────────────────────────────────────────────

screen dev_menu():
    zorder 10000
    modal True

    add Solid("#000000cc")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 860
        ymaximum 900
        background Frame(Solid("#111118"), 0, 0)
        padding (30, 24)

        vbox:
            spacing 0

            ## Header
            hbox:
                xfill True
                text "DEV MENU":
                    size 18
                    color "#aaaaff"
                    xalign 0.0
                textbutton "✕ close":
                    text_size 14
                    text_color "#888888"
                    text_hover_color "#ffffff"
                    xalign 1.0
                    action Hide("dev_menu")

            null height 16

            ## ── Variable state ───────────────────────────────────────────────
            text "VARIABLES":
                size 13
                color "#666688"

            null height 8

            viewport:
                ysize 260
                scrollbars "vertical"
                mousewheel True
                vbox:
                    spacing 3
                    python:
                        dev_vars = [
                            ## Stats
                            ("persistent.constitution",   persistent.constitution),
                            ("persistent.strength",       persistent.strength),
                            ("persistent.charisma",       persistent.charisma),
                            ("persistent.intellect",      persistent.intellect),
                            ## Misc persistent
                            ("persistent.fizz_met",       persistent.fizz_met),
                            ## Session flags
                            ("player_name",               player_name),
                            ("current_day",               current_day),
                            ("constitution_hud_visible",  constitution_hud_visible),
                            ("inventory_unlocked",        inventory_unlocked),
                            ("journal_unlocked",          journal_unlocked),
                            ## Met flags
                            ("met_barkeep",               met_barkeep),
                            ("met_tristana",              met_tristana),
                            ("met_poppy",                 met_poppy),
                            ("met_lulu",                  met_lulu),
                            ("met_vex",                   met_vex),
                            ("met_katarina",              met_katarina),
                            ("met_ahri",                  met_ahri),
                            ("met_ezreal",                met_ezreal),
                            ("met_nidalee_neeko",         met_nidalee_neeko),
                            ("met_jinx",                  met_jinx),
                            ("met_kindred",               met_kindred),
                            ("met_lilia",                 met_lilia),
                            ("met_miss_fortune",          met_miss_fortune),
                            ("met_morgana",               met_morgana),
                            ## Tavern presence
                            ("tristana_in_tavern",        tristana_in_tavern),
                            ("vex_in_tavern",             vex_in_tavern),
                            ("katarina_in_tavern",        katarina_in_tavern),
                            ("ahri_in_tavern",            ahri_in_tavern),
                            ("ezreal_in_tavern",          ezreal_in_tavern),
                            ("nidalee_neeko_in_tavern",   nidalee_neeko_in_tavern),
                            ("jinx_in_tavern",            jinx_in_tavern),
                        ]
                    for dev_name, dev_val in dev_vars:
                        $ dev_color = "#00ff88" if dev_val == True else ("#ff6666" if dev_val == False else "#ffdd88")
                        hbox:
                            spacing 10
                            text "[dev_name]":
                                size 13
                                color "#aaaaaa"
                                xminimum 320
                            text "[dev_val!r]":
                                size 13
                                color dev_color

            null height 18

            ## ── Stat adjusters ───────────────────────────────────────────────
            text "STATS":
                size 13
                color "#666688"

            null height 8

            grid 4 1:
                spacing 8
                xfill True

                ## Constitution (1–25)
                frame:
                    background Solid("#ffffff0a")
                    padding (8, 6)
                    vbox:
                        spacing 4
                        text "Constitution":
                            size 12
                            color "#aaaaaa"
                            xalign 0.5
                        hbox:
                            spacing 6
                            xalign 0.5
                            textbutton "−":
                                text_size 16
                                text_color "#ff8888"
                                text_hover_color "#ffffff"
                                padding (8, 2)
                                action If(persistent.constitution > 1,
                                    SetField(persistent, "constitution", persistent.constitution - 1))
                            text "[persistent.constitution]":
                                size 15
                                color "#ffdd88"
                                xalign 0.5
                                yalign 0.5
                            textbutton "+":
                                text_size 16
                                text_color "#88ff88"
                                text_hover_color "#ffffff"
                                padding (8, 2)
                                action If(persistent.constitution < 25,
                                    SetField(persistent, "constitution", persistent.constitution + 1))

                ## Strength (1–10)
                frame:
                    background Solid("#ffffff0a")
                    padding (8, 6)
                    vbox:
                        spacing 4
                        text "Strength":
                            size 12
                            color "#aaaaaa"
                            xalign 0.5
                        hbox:
                            spacing 6
                            xalign 0.5
                            textbutton "−":
                                text_size 16
                                text_color "#ff8888"
                                text_hover_color "#ffffff"
                                padding (8, 2)
                                action If(persistent.strength > 1,
                                    SetField(persistent, "strength", persistent.strength - 1))
                            text "[persistent.strength]":
                                size 15
                                color "#ffdd88"
                                xalign 0.5
                                yalign 0.5
                            textbutton "+":
                                text_size 16
                                text_color "#88ff88"
                                text_hover_color "#ffffff"
                                padding (8, 2)
                                action If(persistent.strength < 10,
                                    SetField(persistent, "strength", persistent.strength + 1))

                ## Charisma (1–10)
                frame:
                    background Solid("#ffffff0a")
                    padding (8, 6)
                    vbox:
                        spacing 4
                        text "Charisma":
                            size 12
                            color "#aaaaaa"
                            xalign 0.5
                        hbox:
                            spacing 6
                            xalign 0.5
                            textbutton "−":
                                text_size 16
                                text_color "#ff8888"
                                text_hover_color "#ffffff"
                                padding (8, 2)
                                action If(persistent.charisma > 1,
                                    SetField(persistent, "charisma", persistent.charisma - 1))
                            text "[persistent.charisma]":
                                size 15
                                color "#ffdd88"
                                xalign 0.5
                                yalign 0.5
                            textbutton "+":
                                text_size 16
                                text_color "#88ff88"
                                text_hover_color "#ffffff"
                                padding (8, 2)
                                action If(persistent.charisma < 10,
                                    SetField(persistent, "charisma", persistent.charisma + 1))

                ## Intellect (1–10)
                frame:
                    background Solid("#ffffff0a")
                    padding (8, 6)
                    vbox:
                        spacing 4
                        text "Intellect":
                            size 12
                            color "#aaaaaa"
                            xalign 0.5
                        hbox:
                            spacing 6
                            xalign 0.5
                            textbutton "−":
                                text_size 16
                                text_color "#ff8888"
                                text_hover_color "#ffffff"
                                padding (8, 2)
                                action If(persistent.intellect > 1,
                                    SetField(persistent, "intellect", persistent.intellect - 1))
                            text "[persistent.intellect]":
                                size 15
                                color "#ffdd88"
                                xalign 0.5
                                yalign 0.5
                            textbutton "+":
                                text_size 16
                                text_color "#88ff88"
                                text_hover_color "#ffffff"
                                padding (8, 2)
                                action If(persistent.intellect < 10,
                                    SetField(persistent, "intellect", persistent.intellect + 1))

            null height 12

            ## Day adjuster
            hbox:
                spacing 10
                yalign 0.5
                text "Day:":
                    size 13
                    color "#aaaaaa"
                    yalign 0.5
                textbutton "−":
                    text_size 15
                    text_color "#ff8888"
                    text_hover_color "#ffffff"
                    padding (6, 2)
                    action If(current_day > 1, SetVariable("current_day", current_day - 1))
                text "[current_day] / 31":
                    size 14
                    color "#ffdd88"
                    yalign 0.5
                textbutton "+":
                    text_size 15
                    text_color "#88ff88"
                    text_hover_color "#ffffff"
                    padding (6, 2)
                    action If(current_day < 31, SetVariable("current_day", current_day + 1))

            null height 18

            ## ── Toggle flags ─────────────────────────────────────────────────
            text "TOGGLE FLAGS":
                size 13
                color "#666688"

            null height 8

            ## Unlocks
            grid 3 1:
                spacing 6
                xfill True
                textbutton "constitution_hud_visible":
                    text_size 12
                    action ToggleVariable("constitution_hud_visible")
                textbutton "inventory_unlocked":
                    text_size 12
                    action ToggleVariable("inventory_unlocked")
                textbutton "journal_unlocked":
                    text_size 12
                    action ToggleVariable("journal_unlocked")

            null height 6

            ## Met flags — all characters
            grid 4 4:
                spacing 6
                xfill True

                textbutton "met_barkeep":
                    text_size 12
                    action ToggleVariable("met_barkeep")
                textbutton "met_tristana":
                    text_size 12
                    action ToggleVariable("met_tristana")
                textbutton "met_poppy":
                    text_size 12
                    action ToggleVariable("met_poppy")
                textbutton "met_lulu":
                    text_size 12
                    action ToggleVariable("met_lulu")
                textbutton "met_vex":
                    text_size 12
                    action ToggleVariable("met_vex")
                textbutton "met_katarina":
                    text_size 12
                    action ToggleVariable("met_katarina")
                textbutton "met_ahri":
                    text_size 12
                    action ToggleVariable("met_ahri")
                textbutton "met_ezreal":
                    text_size 12
                    action ToggleVariable("met_ezreal")
                textbutton "met_nidalee_neeko":
                    text_size 12
                    action ToggleVariable("met_nidalee_neeko")
                textbutton "met_jinx":
                    text_size 12
                    action ToggleVariable("met_jinx")
                textbutton "met_kindred":
                    text_size 12
                    action ToggleVariable("met_kindred")
                textbutton "met_lilia":
                    text_size 12
                    action ToggleVariable("met_lilia")
                textbutton "met_miss_fortune":
                    text_size 12
                    action ToggleVariable("met_miss_fortune")
                textbutton "met_morgana":
                    text_size 12
                    action ToggleVariable("met_morgana")
                textbutton "— ":
                    text_size 12
                    sensitive False
                textbutton "— ":
                    text_size 12
                    sensitive False

            null height 6

            ## Tavern presence
            grid 4 2:
                spacing 6
                xfill True

                textbutton "tristana_in_tavern":
                    text_size 12
                    action ToggleVariable("tristana_in_tavern")
                textbutton "vex_in_tavern":
                    text_size 12
                    action ToggleVariable("vex_in_tavern")
                textbutton "katarina_in_tavern":
                    text_size 12
                    action ToggleVariable("katarina_in_tavern")
                textbutton "ahri_in_tavern":
                    text_size 12
                    action ToggleVariable("ahri_in_tavern")
                textbutton "ezreal_in_tavern":
                    text_size 12
                    action ToggleVariable("ezreal_in_tavern")
                textbutton "nidalee_neeko_in_tavern":
                    text_size 12
                    action ToggleVariable("nidalee_neeko_in_tavern")
                textbutton "jinx_in_tavern":
                    text_size 12
                    action ToggleVariable("jinx_in_tavern")
                textbutton "— ":
                    text_size 12
                    sensitive False

            null height 18

            ## ── Jump to scene ─────────────────────────────────────────────────
            text "JUMP TO SCENE":
                size 13
                color "#666688"

            null height 8

            grid 4 2:
                spacing 8
                xfill True

                textbutton "start":
                    text_size 13
                    action [Hide("dev_menu"), Jump("start")]
                textbutton "wakingUp":
                    text_size 13
                    action [Hide("dev_menu"), Jump("wakingUp")]
                textbutton "introductions":
                    text_size 13
                    action [Hide("dev_menu"), Jump("introductions")]
                textbutton "gameStart":
                    text_size 13
                    action [Hide("dev_menu"), Jump("gameStart")]
                textbutton "tavern loop":
                    text_size 13
                    action [Hide("dev_menu"), Jump("tavern_tutorial_loop")]
                textbutton "tavern night end":
                    text_size 13
                    action [Hide("dev_menu"), Jump("tavern_night_end")]
                textbutton "gameover1":
                    text_size 13
                    action [Hide("dev_menu"), Jump("gameover1")]
                textbutton "— ":
                    text_size 13
                    sensitive False
