# minigames/minigame_corki.rpy
# Corki's Auto-Repair — Pipe Puzzle
#
# Normal mode: 5×5 grid, straight + corner pipes.
# Hard mode:   7×7 grid, straight + corner + T-junction; two simultaneous paths.
#
# Rewards
#   Normal success: +2 STR, +1 CHA, +50g
#   Normal fail:    +1 STR
#   Hard success:   normal + +1 STR, +1 CHA, +25g
#   Hard fail:      +1 STR
#
# Hard mode unlocked: persistent.corki_hard_unlocked after first normal pass.

## ── Python helpers ────────────────────────────────────────────────────────────

init python:

    # --- Pipe type definitions ---
    # Each type maps rotation (0/1/2/3 = 0°/90°/180°/270°) to open directions.
    # Directions: 0=up, 1=right, 2=down, 3=left
    PIPE_TYPES = {
        "straight": {
            0: {0, 2},   # up/down
            1: {1, 3},   # right/left
            2: {0, 2},
            3: {1, 3},
        },
        "corner": {
            0: {1, 2},   # right/down
            1: {2, 3},   # down/left
            2: {0, 3},   # up/left
            3: {0, 1},   # up/right
        },
        "tjunction": {
            0: {1, 2, 3}, # right/down/left
            1: {0, 2, 3}, # up/down/left
            2: {0, 1, 3}, # up/right/left
            3: {0, 1, 2}, # up/right/down
        },
    }

    def corki_open_dirs(ptype, rot):
        return PIPE_TYPES[ptype][rot % 4]

    def corki_opposite(d):
        return (d + 2) % 4

    def corki_neighbor(r, c, d, rows, cols):
        """Return (nr, nc) in direction d from (r,c), or None if out of bounds."""
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < rows and 0 <= nc < cols:
            return (nr, nc)
        return None

    def corki_check_path(grid, rows, cols, starts, ends):
        """
        BFS from each start cell. Returns True if all ends are reachable.
        grid[r][c] = (ptype, rotation)
        starts = list of (r, c) edge cells with their inbound direction already handled
        ends   = list of (r, c) target cells
        """
        from collections import deque
        reached = set()
        for (sr, sc) in starts:
            visited = set()
            queue = deque([(sr, sc)])
            visited.add((sr, sc))
            while queue:
                r, c = queue.popleft()
                reached.add((r, c))
                ptype, rot = grid[r][c]
                for d in corki_open_dirs(ptype, rot):
                    nb = corki_neighbor(r, c, d, rows, cols)
                    if nb is None:
                        continue
                    nr, nc = nb
                    if (nr, nc) in visited:
                        continue
                    nb_ptype, nb_rot = grid[nr][nc]
                    if corki_opposite(d) in corki_open_dirs(nb_ptype, nb_rot):
                        visited.add((nr, nc))
                        queue.append((nr, nc))
        return all(e in reached for e in ends)

    def corki_make_grid(rows, cols, hard_mode=False):
        """Generate a random pipe grid. Returns list of lists of [ptype, rot]."""
        import random
        types = ["straight", "corner"]
        if hard_mode:
            types.append("tjunction")
        grid = []
        for r in range(rows):
            row = []
            for c in range(cols):
                ptype = random.choice(types)
                rot = random.randint(0, 3)
                row.append([ptype, rot])
            grid.append(row)
        return grid


## ── Screens ───────────────────────────────────────────────────────────────────

screen corki_pipe_grid(grid, rows, cols, tile_size=80):
    style_prefix "corki"
    frame:
        xalign 0.5
        yalign 0.5
        padding (20, 20)
        vbox:
            spacing 0
            for r in range(rows):
                hbox:
                    spacing 0
                    for c in range(cols):
                        python:
                            ptype, rot = grid[r][c]
                            img_name = "bt pipe {}.png".format(ptype)
                        imagebutton:
                            idle    At(img_name, Transform(rotate=rot*90, zoom=tile_size/100.0))
                            hover   At(img_name, Transform(rotate=rot*90, zoom=tile_size/100.0, alpha=0.8))
                            action  Function(corki_rotate_tile, r, c)
                            xsize   tile_size
                            ysize   tile_size

screen corki_hud(hard_mode):
    frame:
        xalign 0.5
        yalign 0.02
        padding (16, 10)
        hbox:
            spacing 20
            text ( "HARD MODE" if hard_mode else "NORMAL MODE" ) style "corki_label"
            text "Connect START → END" style "corki_label"

style corki_label:
    color "#e8c87a"
    size 22
    bold True


## ── Labels ────────────────────────────────────────────────────────────────────

label corki_job:
    $ energy -= 1
    $ persistent.corki_visits += 1

    scene bg corki shop
    show screen corki_hud(False)

    # --- Intro dialogue (first visit only) ---
    if persistent.corki_visits == 1:
        show ch corki neutral
        co "Eh? You want work? Fine. See these pipes? They need connecting."
        co "Left side to right side. Click a tile to rotate it."
        co "Simple enough even for a human. Get going."
    else:
        show ch corki neutral
        co "Back again? The left wall's leaking. Same deal."

    hide screen corki_hud

    # --- Build grid ---
    $ _corki_rows, _corki_cols = 5, 5
    $ _corki_grid = corki_make_grid(_corki_rows, _corki_cols, hard_mode=False)
    # Start = left edge col 0, row 2. End = right edge col 4, row 2.
    $ _corki_starts = [(2, 0)]
    $ _corki_ends   = [(2, 4)]

    call screen corki_pipe_grid(_corki_grid, _corki_rows, _corki_cols)
    # (the screen loops until corki_solve_check sets _solved)

    if _corki_solved:
        jump corki_success
    else:
        jump corki_fail

label corki_job_hard:
    $ energy -= 1
    $ persistent.corki_visits += 1

    scene bg corki shop
    show screen corki_hud(True)

    show ch corki neutral
    co "Hard mode? Two circuits. Both have to connect."
    co "Don't blow up the compressor this time."
    show ch rumble back
    ru "I told you that coolant loop needed a T-fitting."
    co "Nobody asked you, Rumble."

    hide screen corki_hud

    $ _corki_rows, _corki_cols = 7, 7
    $ _corki_grid = corki_make_grid(_corki_rows, _corki_cols, hard_mode=True)
    $ _corki_starts = [(1, 0), (5, 0)]
    $ _corki_ends   = [(1, 6), (5, 6)]

    call screen corki_pipe_grid(_corki_grid, _corki_rows, _corki_cols, tile_size=70)

    if _corki_solved:
        jump corki_hard_success
    else:
        jump corki_hard_fail

label corki_success:
    show ch corki pleased
    co "Hm. Not terrible."
    co "Here's your cut."
    $ strength += 2
    $ charisma += 1
    $ gold += 50
    $ persistent.corki_hard_unlocked = True
    show screen system_overlay
    s "Strength +2. Charisma +1. [50]g earned."
    hide screen system_overlay
    return

label corki_fail:
    show ch corki neutral
    co "Forget it. Watch a professional next time."
    $ strength += 1
    show screen system_overlay
    s "Strength +1."
    hide screen system_overlay
    return

label corki_hard_success:
    show ch corki pleased
    co "Both circuits. Clean run."
    co "You're almost useful."
    show ch rumble back
    ru "..."
    # Rumble says nothing. That means something.
    $ strength += 3
    $ charisma += 2
    $ gold += 75
    show screen system_overlay
    s "Strength +3. Charisma +2. [75]g earned."
    hide screen system_overlay
    return

label corki_hard_fail:
    show ch corki neutral
    co "Two circuits. You couldn't even do one."
    $ strength += 1
    show screen system_overlay
    s "Strength +1."
    hide screen system_overlay
    return


## ── Helper called by screen button ───────────────────────────────────────────

init python:
    _corki_solved = False

    def corki_rotate_tile(r, c):
        global _corki_grid, _corki_rows, _corki_cols
        global _corki_starts, _corki_ends, _corki_solved
        _corki_grid[r][c][1] = (_corki_grid[r][c][1] + 1) % 4
        if corki_check_path(_corki_grid, _corki_rows, _corki_cols,
                            _corki_starts, _corki_ends):
            _corki_solved = True
            renpy.return_statement()
        renpy.restart_interaction()
