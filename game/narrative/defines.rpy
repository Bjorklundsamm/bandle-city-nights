# narrative/defines.rpy
# All character defines and game-wide defaults.
# Add new characters and variables here — nowhere else.


## ── Solid-color images ───────────────────────────────────────────────────────

image bg black = "#000000"


## ── Character defines ────────────────────────────────────────────────────────

define n    = Character("Narrator")
define mc   = Character("[player_name]")
define s    = Character("System")
define b    = Character("Barkeep")
define unkwn = Character("???")

define t    = Character("Tristana")
define p    = Character("Poppy")
define l    = Character("Lulu")
define f    = Character("Fizz")
define vx   = Character("Vex")
define k    = Character("Katarina")
define a    = Character("Ahri")
define ez   = Character("Ezreal")
define neo  = Character("Neeko")
define ni   = Character("Nidalee")
define j    = Character("Jinx")
define mf   = Character("Miss Fortune")
define mo   = Character("Morgana")
define co   = Character("Corki")
define ru   = Character("Rumble")
define te   = Character("Teemo")


## ── Stats ────────────────────────────────────────────────────────────────────
# Max values: constitution 50 (10 hearts × 5), strength/charisma/intellect 50 each.
# Stats are displayed per-heart only for constitution; STR/CHA/INT are raw numbers.
# These are per-playthrough — use default, not persistent.

default constitution = 1
default strength     = 1
default charisma     = 1
default intellect    = 1

## Energy & Gold
default energy       = 3   # resets to 3 each morning
default gold         = 0


## ── Pipe puzzle (Corki's Auto-Repair) ───────────────────────────────────────

default pipe_grid      = []
default pipe_rows      = 4
default pipe_cols      = 5
default pipe_start_row = 1   # row index on the left edge
default pipe_end_row   = 2   # row index on the right edge


## ── Minigame tracking ────────────────────────────────────────────────────────
# visit_counts — scale difficulty on repeat visits
default persistent.corki_visits    = 0
default persistent.rumble_visits   = 0
default persistent.morgana_visits  = 0
default persistent.teemo_visits    = 0
default persistent.ezreal_visits   = 0

# hard mode unlocked flags — set True on first normal-mode pass
default persistent.corki_hard_unlocked    = False
default persistent.rumble_hard_unlocked   = False
default persistent.morgana_hard_unlocked  = False
default persistent.teemo_hard_unlocked    = False
default persistent.ezreal_hard_unlocked   = False

# best scores (used for Rumble streak tracking etc.)
default persistent.rumble_best    = 0
default persistent.ezreal_best    = 0   # best accuracy % (0–100)

# Morgana special unlock (hard mode reward)
default persistent.morgana_reward_seen = False

# Ezreal shower scene unlock (hard mode reward)
default persistent.ezreal_shower_unlocked = False


## ── Player ───────────────────────────────────────────────────────────────────

default player_name             = "Stranger"
default constitution_hud_visible = False
default energy_hud_visible      = False
default day2_outside_announced  = False
default current_day             = 1


## ── Emotion icon ─────────────────────────────────────────────────────────────
# Set to an image tag string (e.g. "ch tristana icon horny") to show the icon
# in the bottom-left of the textbox. Set to None to hide.
# If the image doesn't exist yet, the tag name is displayed as placeholder text.

default emotion_icon = None


## ── Met flags ────────────────────────────────────────────────────────────────
# met_tristana is an integer: 1 = rescued you (gameStart), 2+ = tavern scene done.

default met_tristana      = 1
default met_poppy         = True
default met_barkeep       = True
default met_lulu          = True
default met_vex           = False
default met_katarina      = False
default met_ahri          = False
default met_ezreal        = False
default met_nidalee_neeko = False
default met_jinx          = False
default met_fizz          = False
default met_miss_fortune  = False
default met_kindred       = False
default met_lilia         = False
default met_morgana       = False


## ── Affection ────────────────────────────────────────────────────────────────

default affection_barkeep     = 0
default affection_tristana    = 0
default affection_poppy       = 0
default affection_lulu        = 0
default affection_vex         = 0
default affection_katarina    = 0
default affection_ahri        = 0
default affection_ezreal      = 0
default affection_nidalee     = 0
default affection_neeko       = 0
default affection_jinx        = 0
default affection_fizz        = 0
default affection_miss_fortune = 0
default affection_kindred     = 0
default affection_lilia       = 0
default affection_morgana     = 0


## ── Tavern presence flags ────────────────────────────────────────────────────
# Set to True/False before entering each night's tavern loop.
# Barkeep and Poppy are always present — no flags needed for them.

default tristana_in_tavern      = True
default vex_in_tavern           = True
default katarina_in_tavern      = True
default ahri_in_tavern          = True
default ezreal_in_tavern        = True
default nidalee_neeko_in_tavern = True
default jinx_in_tavern          = True

# poppy_off_duty — True on days Poppy is away; unlocks Lulu arc scenes.
default poppy_off_duty          = False


## ── Scene unlock flags ───────────────────────────────────────────────────────
# Track which escalation scenes have been seen; prevents repeat triggers.

default tristana_scene_1_done   = False   # flirtation
default tristana_scene_2_done   = False   # drunk confession
default tristana_scene_3_done   = False   # debt reveal
default tristana_explicit_done  = False

default poppy_armwrestle_done   = False
default poppy_gym_arc_started   = False
default poppy_orlon_told        = False
default poppy_hammer_told       = False
default poppy_explicit_done     = False

default lulu_in_tavern          = True    # set False when she leaves after day2 conversation
default lulu_pix_talk_done      = False
default lulu_scene_1_done       = False
default lulu_explicit_done      = False
default lulu_arc_active         = False   # set True once Lulu scene 1 fires; blocks Ahri

default katarina_scene_1_done   = False
default katarina_explicit_done  = False

default vex_scene_1_done           = False
default vex_explicit_done          = False
default vex_journal_pages_collected = 0   # max 5; unlocks Vex ultimate fantasy route

default ahri_available          = False   # set True once Yordle-essence gate passes
default ahri_scene_1_done       = False
default ahri_explicit_done      = False

default neeko_shoma_done        = False
default neeko_trust_done        = False
default neeko_explicit_done     = False

default nidalee_confronted      = False
default nidalee_scene_1_done    = False
default nidalee_explicit_done   = False

default ezreal_trained_once     = False
default ezreal_shower_scene_done = False
default ezreal_explicit_done    = False

default morgana_reward_scene_done = False
default morgana_explicit_done   = False

default fizz_explicit_done      = False

default jinx_gate_done          = False   # requires tristana affection max
default jinx_explicit_done      = False

default mf_scene_1_done         = False   # first meeting / loan offer accepted
default mf_scene_2_done         = False   # pistol return arc — player makes choice
default mf_scene_3_done         = False   # titjob scene (tier 2)
default mf_scene_4_done         = False   # room scene (tier 3)
default mf_paid_in_full         = False   # waited and received full 200g repayment
default mf_times_visited        = 0       # visit counter for MF arriving in town


## ── Inventory / item flags ───────────────────────────────────────────────────

default inventory_unlocked  = False
default journal_unlocked    = False
default has_loaded_dice     = False
default has_mf_pistol       = False
default mf_loan_active      = False
