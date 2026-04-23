# minigames/minigame_ezreal.rpy
# Ezreal's Target Practice — Click Targets
#
# Normal mode: 10 targets, 1.5s window, no decoys.
# Hard mode:   15 targets, 1.0s window, 3 decoys (rotated 45° visually; subtract hit if clicked).
#
# All hits build the consecutive streak. After 5 in a row Ezreal stops commentary.
#
# Rewards
#   Normal 80%+:   +5 STR
#   Normal 50–79%: +3 STR
#   Normal <50%:   +1 STR
#   Hard 80%+:     +7 STR  → triggers ezreal_shower_scene (if STR >= 30)
#   Hard 50–79%:   +3 STR
#   Hard <50%:     +1 STR
#
# Hard mode unlocked: persistent.ezreal_hard_unlocked after first 80%+ normal run.

init python:

    class _EzrealState:
        def __init__(self, hard_mode=False):
            self.hard_mode    = hard_mode
            self.total        = 15 if hard_mode else 10
            self.shrink_time  = 1.0 if hard_mode else 1.5
            self.hits         = 0
            self.misses       = 0
            self.decoy_ids    = set()
            self.hit_streak   = 0
            self.max_streak   = 0
            self.current      = 0
            self.silenced     = False  # Ezreal stops trash-talking at 5-streak

        def accuracy(self):
            if self.total == 0:
                return 0
            return int((self.hits / self.total) * 100)

        def record_hit(self):
            self.hits += 1
            self.hit_streak += 1
            self.max_streak = max(self.max_streak, self.hit_streak)
            if self.hit_streak >= 5:
                self.silenced = True

        def record_miss(self):
            self.misses += 1
            self.hit_streak = 0

        def record_decoy_click(self):
            self.hits = max(0, self.hits - 1)
            self.hit_streak = 0

    _ezreal_state = None


## ── Target screen ─────────────────────────────────────────────────────────────

screen ezreal_target_range(state, target_x, target_y, target_visible, is_decoy):
    # HUD
    frame:
        xalign 0.02
        yalign 0.02
        padding (10, 8)
        vbox:
            text "Target: [state.current]/[state.total]" style "ez_label"
            text "Hits: [state.hits]" style "ez_label"
            text "Accuracy: [state.accuracy()]%" style "ez_label"

    # Target
    if target_visible:
        frame:
            xpos target_x
            ypos target_y
            xanchor 0.5
            yanchor 0.5
            padding 0
            if is_decoy:
                # Decoy: rotated 45° to distinguish visually
                imagebutton:
                    idle  At("bt target.png", Transform(rotate=45))
                    hover At("bt target.png", Transform(rotate=45))
                    action Function(ezreal_click_decoy)
                    xsize 100
                    ysize 100
            else:
                imagebutton:
                    idle  "bt target.png"
                    hover "bt target.png"
                    action Function(ezreal_click_hit)
                    xsize 100
                    ysize 100

style ez_label:
    color "#7acce8"
    size 20
    bold True


## ── Labels ────────────────────────────────────────────────────────────────────

label ezreal_job:
    $ energy -= 1
    $ persistent.ezreal_visits += 1

    scene bg training grounds
    show ch ezreal profile default

    if persistent.ezreal_visits == 1:
        ez "Oh good, an audience. Just so we're clear, you're here to learn from a professional."
        ez "Ten targets. Shrinking. Click before they disappear."
        ez "No luck. All skill. Watch and then try to keep up."
    else:
        ez "Back for more? The bar was low last time. Let's see if you've raised it."

    $ _ezreal_state = _EzrealState(hard_mode=False)

    call ezreal_target_loop

    jump ezreal_resolve

label ezreal_job_hard:
    $ energy -= 1
    $ persistent.ezreal_visits += 1

    scene bg training grounds
    show ch ezreal profile default

    ez "Hard mode. Fifteen targets. One second each."
    ez "Three of them are decoys. Click a decoy and you lose a point."
    ez "The decoys are rotated. If you can't tell the difference, that's on you."
    ez "Try not to embarrass either of us."

    $ _ezreal_state = _EzrealState(hard_mode=True)
    python:
        import random
        _ezreal_state.decoy_ids = set(random.sample(range(_ezreal_state.total), 3))

    call ezreal_target_loop

    jump ezreal_resolve_hard

label ezreal_target_loop:
    $ import random as _rand
    while _ezreal_state.current < _ezreal_state.total:
        $ _target_x = _rand.uniform(0.1, 0.85)
        $ _target_y = _rand.uniform(0.15, 0.75)
        $ _is_decoy = _ezreal_state.current in _ezreal_state.decoy_ids
        $ _target_clicked = False

        show screen ezreal_target_range(
            _ezreal_state, _target_x, _target_y, True, _is_decoy)

        $ renpy.pause(_ezreal_state.shrink_time, hard=True)

        hide screen ezreal_target_range

        if not _target_clicked:
            $ _ezreal_state.record_miss()

        # Ezreal commentary
        if not _ezreal_state.silenced:
            if _ezreal_state.current == 0 and not _target_clicked:
                show ch ezreal profile default
                ez "First one. And you missed."
            elif _ezreal_state.current == 0 and _target_clicked:
                show ch ezreal profile default
                ez "One hit. Don't celebrate yet."
            elif _ezreal_state.hit_streak == 3:
                show ch ezreal profile sitting
                ez "Okay, three in a row. Fluke."
            elif _ezreal_state.hit_streak == 5:
                show ch ezreal profile default
                n "Ezreal stops talking."
                n "He watches the next target appear without saying a word."

        $ _ezreal_state.current += 1

    hide screen ezreal_target_range
    return


label ezreal_resolve:
    $ _acc = _ezreal_state.accuracy()
    show ch ezreal profile default

    if _acc >= 80:
        ez "Eighty percent. That's... not nothing."
        ez "Seriously, no luck? All skill?"
        $ strength += 5
        $ persistent.ezreal_hard_unlocked = True
        if _acc > persistent.ezreal_best:
            $ persistent.ezreal_best = _acc
        show screen system_overlay
        s "Strength +5. Accuracy: [_acc]%."
        hide screen system_overlay
    elif _acc >= 50:
        ez "Not bad. Not good. Mediocre, which in target practice is still mediocre."
        $ strength += 3
        show screen system_overlay
        s "Strength +3. Accuracy: [_acc]%."
        hide screen system_overlay
    else:
        ez "Under fifty percent. That's concerning."
        ez "Come back when you've practiced basic hand-eye coordination."
        $ strength += 1
        show screen system_overlay
        s "Strength +1. Accuracy: [_acc]%."
        hide screen system_overlay
    return

label ezreal_resolve_hard:
    $ _acc = _ezreal_state.accuracy()

    if _acc >= 80:
        show ch ezreal profile default
        n "He hasn't said anything for the last four targets."
        n "He's still not saying anything."
        n "He picks up his gauntlet from the bench and adjusts the calibration settings."
        ez "..."
        ez "Showers are that way. I need to cool down the gauntlet."
        n "It is not about the gauntlet."
        $ strength += 7
        $ persistent.ezreal_shower_unlocked = True
        if _acc > persistent.ezreal_best:
            $ persistent.ezreal_best = _acc
        show screen system_overlay
        s "Strength +7. Accuracy: [_acc]%. Ezreal seems... different."
        hide screen system_overlay

        if strength >= 30 and not ezreal_shower_scene_done:
            jump ezreal_shower_scene
        else:
            return

    elif _acc >= 50:
        show ch ezreal profile default
        ez "Fifty to eighty. In hard mode. I'll give you that."
        $ strength += 3
        show screen system_overlay
        s "Strength +3. Accuracy: [_acc]%."
        hide screen system_overlay
    else:
        show ch ezreal profile default
        ez "You hit three decoys. Three."
        ez "Go home."
        $ strength += 1
        show screen system_overlay
        s "Strength +1."
        hide screen system_overlay
    return


## ── Shower scene (Tier 2 lead-up + user Tier 3 block) ────────────────────────

label ezreal_shower_scene:
    # placeholder bg — needs bg ezreal range art
    scene bg city outside daytime
    show ch ezreal profile default

    n "He's already heading toward the door at the back of the range."
    n "He doesn't invite you again. He also doesn't say not to follow."

    # placeholder bg — needs bg ezreal showers art
    scene bg hot springs
    show ch ezreal profile default

    n "The showers are empty. He turns one on without looking at you."
    n "The performance infrastructure is completely down. He's just come off a hard session."
    n "No one to perform for. Except somehow you're here."

    ez "This isn't— I mean. You're not supposed to—"
    n "He tries a joke. It doesn't land."
    ez "Look, I have a girlfriend. You know I have a girlfriend. I've mentioned Lux at least—"
    n "He stops. He looks at you properly for the first time."
    ez "You have to swear this stays between us."
    ez "I'm serious. She would actually kill me."

    menu:
        "Swear it.":
            ez "Okay."
            n "That's all he says. Something in him has made a decision he hasn't fully caught up to yet."
        "Tell him you don't need to swear anything.":
            ez "..."
            n "He looks at you for a long moment."
            ez "That's— okay. That's actually worse. You understand that's worse."
            n "He is still here."

    # [EXPLICIT START]
    # User authors this section — Ezreal's shower encounter.
    # He keeps asking for discretion. He means it every time. It doesn't stop him.
    # [EXPLICIT END]

    n "Afterward he gets dressed fast."
    n "He doesn't make eye contact for a moment. Then the charm returns, slightly effortful."
    ez "That never happened."
    n "A beat."
    ez "I mean— you were great, obviously."
    n "Another beat."
    ez "But that never happened."

    $ ezreal_shower_scene_done = True
    $ affection_ezreal += 2
    return


## ── Helper functions ─────────────────────────────────────────────────────────

init python:
    _target_clicked = False

    def ezreal_click_hit():
        global _target_clicked, _ezreal_state
        if not _target_clicked:
            _target_clicked = True
            _ezreal_state.record_hit()
        renpy.return_statement()

    def ezreal_click_decoy():
        global _target_clicked, _ezreal_state
        if not _target_clicked:
            _target_clicked = True
            _ezreal_state.record_decoy_click()
        renpy.return_statement()
