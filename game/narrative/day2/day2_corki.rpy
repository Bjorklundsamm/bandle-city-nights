# narrative/day2/day2_corki.rpy
# Corki's Auto-Repair — pipe puzzle minigame.
# Player rotates tiles to form a connected pipe path from START to END.
# Rewards: +2 STR, +1 CHA, +50g on solve.


## ── Python logic ─────────────────────────────────────────────────────────────

init python:

    def pipe_opens(tile_type, rotation):
        """Return the set of open directions for a tile given its type and rotation.
        Straight: horizontal (E/W) or vertical (N/S).
        Corner: two perpendicular directions, rotated clockwise."""
        r = rotation % 4
        if tile_type == "straight":
            return {"W", "E"} if r in (0, 2) else {"N", "S"}
        # corner
        if r == 0: return {"E", "S"}
        if r == 1: return {"S", "W"}
        if r == 2: return {"W", "N"}
        return {"N", "E"}

    _PIPE_OPP = {"N": "S", "S": "N", "E": "W", "W": "E"}
    _PIPE_DD  = {"N": (-1, 0), "S": (1, 0), "E": (0, 1), "W": (0, -1)}

    def pipe_reachable(grid, rows, cols, start_row):
        """BFS from (start_row, 0). Returns set of (r, c) reachable via valid connections."""
        visited = set()
        queue = [(start_row, 0)]
        visited.add((start_row, 0))
        while queue:
            r, c = queue.pop(0)
            for d in pipe_opens(grid[r][c]["type"], grid[r][c]["rot"]):
                dr, dc = _PIPE_DD[d]
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    if _PIPE_OPP[d] in pipe_opens(grid[nr][nc]["type"], grid[nr][nc]["rot"]):
                        visited.add((nr, nc))
                        queue.append((nr, nc))
        return visited

    def make_pipe_grid(rows, cols):
        """Generate a fresh random grid. Each cell: dict with 'type' and 'rot'."""
        import random
        types = ["straight", "corner"]
        return [
            [{"type": random.choice(types), "rot": random.randint(0, 3)}
             for _ in range(cols)]
            for _ in range(rows)
        ]

    def pipe_tile_char(tile):
        """ASCII placeholder char for a tile.
        Straight: '-' (horizontal) or '|' (vertical).
        Corner rots 0-3: 'F' (E+S), '7' (S+W), 'J' (W+N), 'L' (N+E)."""
        r = tile["rot"] % 4
        if tile["type"] == "straight":
            return "-" if r in (0, 2) else "|"
        return ["F", "7", "J", "L"][r]


## ── Screen ───────────────────────────────────────────────────────────────────

screen pipe_puzzle(grid, rows, cols, start_row, end_row, reachable):
    modal True
    zorder 100

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 6

        text "[[CORKI'S AUTO-REPAIR — bg placeholder]" xalign 0.5 size 20 color "#888888"
        text "Rotate tiles to connect START to END" xalign 0.5 size 22
        null height 12

        for r in range(rows):
            hbox:
                xalign 0.5
                spacing 4

                # Start arrow (left edge)
                if r == start_row:
                    text ">" xsize 32 ysize 50 size 28 color "#00ff88" xalign 0.5 yalign 0.5
                else:
                    null width 32

                # Tile buttons — yellow when reachable from start, grey otherwise
                for c in range(cols):
                    textbutton pipe_tile_char(grid[r][c]):
                        xsize 50
                        ysize 50
                        text_xalign 0.5
                        text_yalign 0.5
                        text_size 32
                        text_color ("#ffcc00" if (r, c) in reachable else "#555555")
                        action Return(("rotate", r, c))

                # End arrow (right edge)
                if r == end_row:
                    text ">" xsize 32 ysize 50 size 28 color "#ff4444" xalign 0.5 yalign 0.5
                else:
                    null width 32


## ── Hub screen ────────────────────────────────────────────────────────────────

screen loc_auto_repair_hub():
    zorder 50

    imagebutton:
        idle  Transform("ch corki shop position", alpha=0.9)
        hover Fixed(Transform("ch corki shop position", zoom=1.005, anchor=(0.5, 1.0), align=(0.5, 1.0)), xysize=(1920, 1088))
        focus_mask True
        pos (0, 0)
        hover_sound "audio/sfx/hover_selectable.mp3"
        activate_sound "audio/sfx/click_selectable.mp3"
        action Return("interact")

    textbutton "← Leave":
        xalign 0.02
        yalign 0.96
        text_size 22
        text_color "#c8c8c8"
        text_hover_color "#ffffff"
        activate_sound "audio/sfx/click_selectable.mp3"
        action Return("leave")


## ── Label ────────────────────────────────────────────────────────────────────

label loc_auto_repair:

    scene bg corkis autoshop with dissolve

    call screen loc_auto_repair_hub()
    if _return == "leave":
        return

    show ch corki shop position
    n "Corki's Auto-Repair. The smell of engine oil and scorched copper hits you from half a block away."
    n "A small Yordle in a flight helmet is halfway inside an engine block, legs kicking in the air."

    co "HEY! You there — big legs. You any good with your hands?"
    n "He doesn't wait for an answer before rattling off the problem."
    co "Coolant line's a mess. The whole pipe routing's gone to hell. Fix it and I'll make it worth your while."

    menu:
        "Get to work.":
            $ energy -= 1
            $ renpy.block_rollback()

            python:
                pipe_grid = make_pipe_grid(pipe_rows, pipe_cols)

            python:
                _reach = pipe_reachable(pipe_grid, pipe_rows, pipe_cols, pipe_start_row)
                _solved = (pipe_end_row, pipe_cols - 1) in _reach

            while not _solved:
                call screen pipe_puzzle(pipe_grid, pipe_rows, pipe_cols, pipe_start_row, pipe_end_row, _reach)

                python:
                    _act = _return
                    if _act[0] == "rotate":
                        _r, _c = _act[1], _act[2]
                        pipe_grid[_r][_c]["rot"] = (pipe_grid[_r][_c]["rot"] + 1) % 4
                    _reach = pipe_reachable(pipe_grid, pipe_rows, pipe_cols, pipe_start_row)
                    _solved = (pipe_end_row, pipe_cols - 1) in _reach

            show screen system_overlay
            s "Pipes connected. Corki's repairs are back on schedule."
            s "Strength +2   Charisma +1   Gold +50"
            call screen system_got_it
            hide screen system_overlay

            $ strength += 2
            $ charisma += 1
            $ gold += 50
            $ persistent.corki_visits += 1

        "Head back.":
            pass

    return
