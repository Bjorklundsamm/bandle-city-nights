# minigames/jobs_hub.rpy
# Town job hub — available from Day 3.
# Displays 5 job buttons with energy cost indicator.
# When energy = 0, buttons are greyed out.

## ── Hub screen ────────────────────────────────────────────────────────────────

screen jobs_hub():
    tag menu
    style_prefix "jobs"

    add "bg town jobs district"

    # Energy HUD
    frame:
        xalign 0.02
        yalign 0.02
        padding (14, 10)
        hbox:
            spacing 8
            text "Energy:" style "jobs_label"
            for i in range(3):
                if i < persistent.energy:
                    add "bt energy full.png" xsize 28 ysize 28
                else:
                    add "bt energy empty.png" xsize 28 ysize 28

    # Gold HUD
    frame:
        xalign 0.98
        yalign 0.02
        padding (14, 10)
        text "[persistent.gold]g" style "jobs_label" xalign 1.0

    # Job buttons — 5 stacked vertically, centered
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 14

        # Corki
        frame:
            padding (12, 8)
            background ("#3a2a00" if persistent.energy > 0 else "#1a1a1a")
            hbox:
                spacing 12
                add "bt job corki.png" xsize 48 ysize 48
                vbox:
                    yalign 0.5
                    text "Corki's Auto-Repair" style "jobs_title"
                    text "Pipe puzzle — STR, CHA, Gold" style "jobs_sub"
                    if persistent.corki_hard_unlocked:
                        text "[hard_badge()]" style "jobs_hard"
                if persistent.energy > 0:
                    textbutton "Work (1 energy)" action Jump("corki_hub_choice") style "jobs_btn"
                else:
                    textbutton "Too tired" action NullAction() style "jobs_btn_grey"

        # Rumble
        frame:
            padding (12, 8)
            background ("#3a2a00" if persistent.energy > 0 else "#1a1a1a")
            hbox:
                spacing 12
                add "bt job rumble.png" xsize 48 ysize 48
                vbox:
                    yalign 0.5
                    text "Rumble's Robo-Workshop" style "jobs_title"
                    text "Parts sorter — STR, CHA, INT, Gold" style "jobs_sub"
                    if persistent.rumble_hard_unlocked:
                        text "[hard_badge()]" style "jobs_hard"
                if persistent.energy > 0:
                    textbutton "Work (1 energy)" action Jump("rumble_hub_choice") style "jobs_btn"
                else:
                    textbutton "Too tired" action NullAction() style "jobs_btn_grey"

        # Morgana
        frame:
            padding (12, 8)
            background ("#3a2a00" if persistent.energy > 0 else "#1a1a1a")
            hbox:
                spacing 12
                add "bt job morgana.png" xsize 48 ysize 48
                vbox:
                    yalign 0.5
                    text "Morgana's Kitchen" style "jobs_title"
                    text "Recipe memory — INT, Gold" style "jobs_sub"
                    if persistent.morgana_hard_unlocked:
                        text "[hard_badge()]" style "jobs_hard"
                if persistent.energy > 0:
                    textbutton "Work (1 energy)" action Jump("morgana_hub_choice") style "jobs_btn"
                else:
                    textbutton "Too tired" action NullAction() style "jobs_btn_grey"

        # Teemo
        frame:
            padding (12, 8)
            background ("#3a2a00" if persistent.energy > 0 else "#1a1a1a")
            hbox:
                spacing 12
                add "bt job teemo.png" xsize 48 ysize 48
                vbox:
                    yalign 0.5
                    text "Teemo's Scout Training" style "jobs_title"
                    text "Timed decisions — STR, INT" style "jobs_sub"
                    if persistent.teemo_hard_unlocked:
                        text "[hard_badge()]" style "jobs_hard"
                if persistent.energy > 0:
                    textbutton "Work (1 energy)" action Jump("teemo_hub_choice") style "jobs_btn"
                else:
                    textbutton "Too tired" action NullAction() style "jobs_btn_grey"

        # Ezreal
        frame:
            padding (12, 8)
            background ("#3a2a00" if persistent.energy > 0 else "#1a1a1a")
            hbox:
                spacing 12
                add "bt job ezreal.png" xsize 48 ysize 48
                vbox:
                    yalign 0.5
                    text "Ezreal's Target Practice" style "jobs_title"
                    text "Click targets — STR" style "jobs_sub"
                    if persistent.ezreal_hard_unlocked:
                        text "[hard_badge()]" style "jobs_hard"
                if persistent.energy > 0:
                    textbutton "Work (1 energy)" action Jump("ezreal_hub_choice") style "jobs_btn"
                else:
                    textbutton "Too tired" action NullAction() style "jobs_btn_grey"

    # Leave button
    textbutton "Head to town" action Jump("day_hub_return") xalign 0.5 yalign 0.95 style "jobs_leave"

style jobs_label:
    color "#e8c87a"
    size 20
    bold True

style jobs_title:
    color "#ffffff"
    size 20
    bold True

style jobs_sub:
    color "#a0a0a0"
    size 16

style jobs_hard:
    color "#e8a020"
    size 14

style jobs_btn:
    color "#e8c87a"
    size 18

style jobs_btn_grey:
    color "#606060"
    size 18

style jobs_leave:
    color "#c0c0c0"
    size 18

init python:
    def hard_badge():
        return "★ HARD MODE UNLOCKED"


## ── Hub routing labels ────────────────────────────────────────────────────────

label jobs_hub_open:
    call screen jobs_hub()
    return

label corki_hub_choice:
    if persistent.corki_hard_unlocked:
        menu:
            "Normal mode (Pipe Puzzle 5×5)":
                call corki_job
            "Hard mode ★ (Pipe Puzzle 7×7, two circuits)":
                call corki_job_hard
    else:
        call corki_job
    jump jobs_hub_open

label rumble_hub_choice:
    if persistent.rumble_hard_unlocked:
        menu:
            "Normal mode (4 bins, 8-part chaos limit)":
                call rumble_job
            "Hard mode ★ (5 bins, 5-part chaos limit)":
                call rumble_job_hard
    else:
        call rumble_job
    jump jobs_hub_open

label morgana_hub_choice:
    if persistent.morgana_hard_unlocked:
        menu:
            "Normal mode (Recipe Memory)":
                call morgana_job
            "Hard mode ★ (Longer sequence, zero corrections)":
                call morgana_job_hard
    else:
        call morgana_job
    jump jobs_hub_open

label teemo_hub_choice:
    if persistent.teemo_hard_unlocked:
        menu:
            "Normal mode (6 checkpoints)":
                call teemo_job
            "Hard mode ★ (6 checkpoints, 3-option forks, trap decisions)":
                call teemo_job_hard
    else:
        call teemo_job
    jump jobs_hub_open

label ezreal_hub_choice:
    if persistent.ezreal_hard_unlocked:
        menu:
            "Normal mode (10 targets)":
                call ezreal_job
            "Hard mode ★ (15 targets, 1s window, decoys)":
                call ezreal_job_hard
    else:
        call ezreal_job
    jump jobs_hub_open

label day_hub_return:
    return
