# narrative/day2/day2_rumble.rpy
# Rumble's Robo-Workshop — parts sorter minigame.
# Click a loose part to select it (yellow), then click the correct bin to sort it.
# A new part spawns every 2s. Chaos meter = parts on screen; hit 8 = game over.
# Rewards scale with total sorted count.


## ── Python logic ─────────────────────────────────────────────────────────────

init python:

    _rumble_state = {
        "parts":       [],
        "sorted":      0,
        "selected_id": None,
        "game_over":   False,
        "next_id":     0,
    }

    def rumble_init():
        _rumble_state["parts"]       = []
        _rumble_state["sorted"]      = 0
        _rumble_state["selected_id"] = None
        _rumble_state["game_over"]   = False
        _rumble_state["next_id"]     = 0

    def rumble_spawn():
        """Spawn one part. If chaos hits 8, end the screen via end_interaction."""
        import random
        s = _rumble_state
        if s["game_over"]:
            return
        s["next_id"] += 1
        s["parts"].append({
            "id":   s["next_id"],
            "type": random.choice(["bolt", "gear", "wire", "plate"]),
            "x":    random.randint(80, 1750),
            "y":    random.randint(80, 560),
        })
        if len(s["parts"]) >= 8:
            s["game_over"] = True
            renpy.end_interaction("done")
        else:
            renpy.restart_interaction()

    def rumble_select(part_id):
        _rumble_state["selected_id"] = part_id
        renpy.restart_interaction()

    def rumble_sort(bin_type):
        s = _rumble_state
        sel_id = s["selected_id"]
        if sel_id is None:
            return
        part = next((p for p in s["parts"] if p["id"] == sel_id), None)
        if part is None:
            s["selected_id"] = None
            renpy.restart_interaction()
            return
        if part["type"] == bin_type:
            s["parts"].remove(part)
            s["sorted"] += 1
        s["selected_id"] = None
        renpy.restart_interaction()


## ── Screen ───────────────────────────────────────────────────────────────────

screen rumble_game():
    modal True
    zorder 100

    python:
        _rparts = _rumble_state["parts"]
        _rsel   = _rumble_state["selected_id"]
        _rsort  = _rumble_state["sorted"]

    # HUD
    text "Loose: [len(_rparts)]/8     Sorted: [_rsort]" xpos 20 ypos 14 size 26 color "#ffffff" outlines [(2, "#000000", 0, 0)]

    # Loose parts scattered across screen
    for p in _rparts:
        textbutton p["type"][0].upper():
            xpos p["x"]
            ypos p["y"]
            xsize 56
            ysize 56
            text_xalign 0.5
            text_yalign 0.5
            text_size 30
            text_color ("#ffff00" if p["id"] == _rsel else "#cccccc")
            action Function(rumble_select, p["id"])

    # Bins — bottom strip
    hbox:
        xalign 0.5
        yalign 0.96
        spacing 12
        for _bin in ["bolt", "gear", "wire", "plate"]:
            textbutton "[ " + _bin.upper() + " ]":
                xsize 180
                ysize 58
                text_xalign 0.5
                text_yalign 0.5
                text_size 22
                action Function(rumble_sort, _bin)

    # Spawn timer
    timer 2.0 repeat True action Function(rumble_spawn)


## ── Label ────────────────────────────────────────────────────────────────────

label loc_roboshop:

    $ energy -= 1
    $ renpy.block_rollback()

    python:
        rumble_init()
        rumble_spawn()  # seed one part before the screen opens

    scene bg black  # placeholder — bg rumble workshop interior
    n "[[Rumble's Workshop — bg placeholder]"
    # TODO: Rumble intro dialogue

    call screen rumble_game()

    python:
        _rscore = _rumble_state["sorted"]

    show screen system_overlay

    if _rscore >= 20:
        s "Workshop back under control. Sorted: [_rscore] parts."
        s "Strength +2   Charisma +2   Intellect +2   Gold +50"
        $ strength  += 2
        $ charisma  += 2
        $ intellect += 2
        $ gold      += 50
    elif _rscore >= 10:
        s "Held together. Sorted: [_rscore] parts."
        s "Strength +1   Charisma +1   Intellect +1   Gold +50"
        $ strength  += 1
        $ charisma  += 1
        $ intellect += 1
        $ gold      += 50
    else:
        s "Workshop overwhelmed. Sorted: [_rscore] parts."
        s "Intellect +1   Gold +25"
        $ intellect += 1
        $ gold      += 25

    call screen system_got_it
    hide screen system_overlay

    $ persistent.rumble_visits += 1

    return
