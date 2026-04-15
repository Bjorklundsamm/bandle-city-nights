# narrative/defines.rpy
# All character defines and game-wide defaults.
# Add new characters and variables here — nowhere else.


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


## ── Persistent stats ─────────────────────────────────────────────────────────

default persistent.constitution = 1
default persistent.strength     = 1
default persistent.charisma     = 1
default persistent.intellect    = 1
default persistent.fizz_met     = False


## ── Player ───────────────────────────────────────────────────────────────────

default player_name             = "Stranger"
default constitution_hud_visible = False
default current_day             = 1


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

default tristana_in_tavern     = True
default vex_in_tavern          = True
default katarina_in_tavern     = True
default ahri_in_tavern         = True
default ezreal_in_tavern       = True
default nidalee_neeko_in_tavern = True
default jinx_in_tavern         = True


## ── Inventory / item flags ───────────────────────────────────────────────────

default inventory_unlocked  = False
default journal_unlocked    = False
default has_loaded_dice     = False
default has_mf_pistol       = False
default mf_loan_active      = False
