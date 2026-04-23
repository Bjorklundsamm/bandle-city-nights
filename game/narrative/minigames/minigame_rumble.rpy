# minigames/minigame_rumble.rpy
# Rumble's Robo-Workshop — Parts Sorter
#
# Normal mode: 4 bin types (Bolt, Nut, Gear, Wheel), chaos threshold 8, target 10-20+ parts.
# Hard mode:   5 bin types (Bolt, Nut, Wheel, Gear Large, Gear Small), chaos threshold 5.
#              Hard mode distinguishes gear sizes — Gear Large and Gear Small are separate bins.
#
# Rewards
#   Normal 20+ parts: +2 STR, +2 CHA, +2 INT, +50g
#   Normal 10–19:     +1 STR, +1 CHA, +1 INT, +50g
#   Normal <10:       +1 INT, +25g
#   Hard 20+ parts:   +3 STR, +3 CHA, +3 INT, +75g
#   Hard 10–19:       +1 STR, +1 CHA, +1 INT, +50g
#   Hard <10:         +1 INT, +25g
#
# Hard mode unlocked: persistent.rumble_hard_unlocked after first normal 10+ pass.

init python:

    RUMBLE_BINS_NORMAL = ["Bolt", "Nut", "Gear", "Wheel"]
    RUMBLE_BINS_HARD   = ["Bolt", "Nut", "Wheel", "Gear Large", "Gear Small"]

    RUMBLE_CHAOS_NORMAL = 8
    RUMBLE_CHAOS_HARD   = 5

    RUMBLE_PART_IMAGES = {
        "Bolt":       "bt bolt.png",
        "Nut":        "bt nut.png",
        "Gear":       "bt gear medium.png",
        "Wheel":      "bt wheel.png",
        "Gear Large": "bt gear large.png",
        "Gear Small": "bt gear small.png",
    }

    class _RumbleState:
        def __init__(self, hard_mode=False):
            self.hard_mode    = hard_mode
            self.bins         = RUMBLE_BINS_HARD if hard_mode else RUMBLE_BINS_NORMAL
            self.chaos_max    = RUMBLE_CHAOS_HARD if hard_mode else RUMBLE_CHAOS_NORMAL
            self.sorted       = 0
            self.chaos        = 0
            self.active_parts = []  # list of {"id": int, "type": str, "x": float, "y": float}
            self.next_id      = 0
            self.game_over    = False
            self.half_warned  = False

        def spawn_part(self):
            import random
            pid = self.next_id
            self.next_id += 1
            ptype = random.choice(self.bins)
            x = random.uniform(0.1, 0.85)
            y = random.uniform(0.15, 0.7)
            self.active_parts.append({"id": pid, "type": ptype, "x": x, "y": y})
            self.chaos = len(self.active_parts)

        def drop_part(self, pid, bin_name):
            """Returns True if correct bin, False if wrong."""
            for part in self.active_parts:
                if part["id"] == pid:
                    correct = (part["type"] == bin_name)
                    if correct:
                        self.active_parts.remove(part)
                        self.sorted += 1
                        self.chaos = len(self.active_parts)
                    return correct
            return False

        def check_chaos(self):
            if self.chaos >= self.chaos_max:
                self.game_over = True
            if self.chaos >= self.chaos_max // 2 and not self.half_warned:
                self.half_warned = True
                return "half"
            return None

    _rumble_state = None


screen rumble_workshop(state):
    style_prefix "rumble"

    frame:
        xalign 0.02
        yalign 0.1
        padding (10, 8)
        vbox:
            text "CHAOS" style "rumble_label"
            bar:
                value state.chaos
                range state.chaos_max
                xsize 120
                ysize 20
            text "[state.chaos]/[state.chaos_max]" style "rumble_label"

    frame:
        xalign 0.02
        yalign 0.02
        padding (10, 8)
        text "Sorted: [state.sorted]" style "rumble_label"

    # Active parts — draggable
    for part in state.active_parts:
        frame:
            xpos part["x"]
            ypos part["y"]
            xanchor 0.5
            yanchor 0.5
            padding (4, 4)
            imagebutton:
                idle  RUMBLE_PART_IMAGES.get(part["type"], "bt bolt.png")
                hover RUMBLE_PART_IMAGES.get(part["type"], "bt bolt.png")
                action NullAction()
                xsize 64
                ysize 64

    # Bins along the bottom
    hbox:
        xalign 0.5
        yalign 0.95
        spacing 16
        for bin_name in state.bins:
            vbox:
                spacing 4
                frame:
                    xsize 80
                    ysize 70
                    background "#3a2010"
                text bin_name xalign 0.5 style "rumble_bin_label"

style rumble_label:
    color "#e8c87a"
    size 20
    bold True

style rumble_bin_label:
    color "#c8c8c8"
    size 16


## ── Note on Rumble's drag mechanic ──────────────────────────────────────────
## Full Ren'Py Drag/DragGroup implementation requires the native Drag screen
## language component. The screen above shows a simplified static layout.
## The full Drag implementation is in the label via Python + renpy.call_screen.


label rumble_job:
    $ energy -= 1
    $ persistent.rumble_visits += 1

    scene bg rumbles roboshop
    show ch rumble roboshop position

    if persistent.rumble_visits == 1:
        ru "..."
        ru "Grab the parts off the bench. Sort them. Don't touch Tristy."
    else:
        ru "You're back. Good. Roboshop's a disaster again."

    $ _rumble_state = _RumbleState(hard_mode=False)
    $ _rumble_done = False
    $ _rumble_warned = False

    $ _rumble_state.spawn_part()
    $ _rumble_state.spawn_part()
    $ _rumble_state.spawn_part()

    $ _rumble_rounds = 0
    while _rumble_rounds < 30 and not _rumble_state.game_over:
        call screen rumble_workshop(_rumble_state)

        if defined("_rumble_drop_result"):
            $ _sig = _rumble_state.check_chaos()
            if _sig == "half" and not _rumble_warned:
                $ _rumble_warned = True
                show ch rumble roboshop position
                ru "Getting messy in here..."
            if _rumble_state.game_over:
                $ _rumble_rounds = 999

        $ _rumble_state.spawn_part()
        $ _rumble_rounds += 1
        $ renpy.pause(0.1)

    jump rumble_resolve

label rumble_job_hard:
    $ energy -= 1
    $ persistent.rumble_visits += 1

    scene bg rumbles roboshop
    show ch rumble roboshop position

    ru "Hard mode. Five bins. You'll fail."
    ru "Prove me wrong."

    $ _rumble_state = _RumbleState(hard_mode=True)
    $ _rumble_done = False
    $ _rumble_warned = False

    $ _rumble_state.spawn_part()
    $ _rumble_state.spawn_part()
    $ _rumble_state.spawn_part()

    $ _rumble_rounds = 0
    while _rumble_rounds < 30 and not _rumble_state.game_over:
        call screen rumble_workshop(_rumble_state)

        if defined("_rumble_drop_result"):
            $ _sig = _rumble_state.check_chaos()
            if _sig == "half" and not _rumble_warned:
                $ _rumble_warned = True
                show ch rumble roboshop position
                ru "Four loose parts. You're already behind."
            if _rumble_state.game_over:
                $ _rumble_rounds = 999

        $ _rumble_state.spawn_part()
        $ _rumble_rounds += 1
        $ renpy.pause(0.1)

    jump rumble_resolve_hard

label rumble_resolve:
    $ _sorted = _rumble_state.sorted
    if _sorted >= 20:
        show ch rumble roboshop position
        ru "..."
        ru "Hm."
        $ strength  += 2
        $ charisma  += 2
        $ intellect += 2
        $ gold      += 50
        $ persistent.rumble_hard_unlocked = True
        if _sorted > persistent.rumble_best:
            $ persistent.rumble_best = _sorted
            ru "Personal best. Don't get used to it."
        show screen system_overlay
        s "Strength +2. Charisma +2. Intellect +2. [50]g earned."
        hide screen system_overlay
    elif _sorted >= 10:
        show ch rumble roboshop position
        ru "Passable."
        $ strength  += 1
        $ charisma  += 1
        $ intellect += 1
        $ gold      += 50
        $ persistent.rumble_hard_unlocked = True
        show screen system_overlay
        s "Strength +1. Charisma +1. Intellect +1. [50]g earned."
        hide screen system_overlay
    else:
        show ch rumble roboshop position
        ru "Disappointing."
        $ intellect += 1
        $ gold      += 25
        show screen system_overlay
        s "Intellect +1. [25]g earned."
        hide screen system_overlay
    return

label rumble_resolve_hard:
    $ _sorted = _rumble_state.sorted
    if _sorted >= 20:
        show ch rumble roboshop position
        ru "..."
        n "Rumble almost looks up. Not quite."
        $ strength  += 3
        $ charisma  += 3
        $ intellect += 3
        $ gold      += 75
        if _sorted > persistent.rumble_best:
            $ persistent.rumble_best = _sorted
            ru "New record. Still not enough to run the press."
        show screen system_overlay
        s "Strength +3. Charisma +3. Intellect +3. [75]g earned."
        hide screen system_overlay
    elif _sorted >= 10:
        show ch rumble roboshop position
        ru "Made a dent."
        $ strength  += 1
        $ charisma  += 1
        $ intellect += 1
        $ gold      += 50
        show screen system_overlay
        s "Strength +1. Charisma +1. Intellect +1. [50]g earned."
        hide screen system_overlay
    else:
        show ch rumble roboshop position
        ru "Five bins and you couldn't manage ten. Go home."
        $ intellect += 1
        $ gold      += 25
        show screen system_overlay
        s "Intellect +1. [25]g earned."
        hide screen system_overlay
    return
