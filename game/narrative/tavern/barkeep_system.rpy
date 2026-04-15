# narrative/tavern/barkeep_system.rpy
# The "ask about someone" system and all per-character barkeep overview labels.
# Called from any day's barkeep interaction label via `call barkeep_ask_about`.
# Add a new barkeep_overview_[character] label here when a character joins the roster.


## ── Ask about someone ────────────────────────────────────────────────────────

label barkeep_ask_about:

    python:
        _barkeep_roster = []
        if met_tristana:
            _barkeep_roster.append(("Tristana",   affection_tristana,   "barkeep_overview_tristana"))
        if met_poppy:
            _barkeep_roster.append(("Poppy",      affection_poppy,      "barkeep_overview_poppy"))
        if met_lulu:
            _barkeep_roster.append(("Lulu",       affection_lulu,       "barkeep_overview_lulu"))
        if met_vex:
            _barkeep_roster.append(("Vex",        affection_vex,        "barkeep_overview_vex"))
        if met_katarina:
            _barkeep_roster.append(("Katarina",   affection_katarina,   "barkeep_overview_katarina"))
        if met_ahri:
            _barkeep_roster.append(("Ahri",       affection_ahri,       "barkeep_overview_ahri"))
        if met_ezreal:
            _barkeep_roster.append(("Ezreal",     affection_ezreal,     "barkeep_overview_ezreal"))
        if met_nidalee_neeko:
            _barkeep_roster.append(("Nidalee",    affection_nidalee,    "barkeep_overview_nidalee"))
            _barkeep_roster.append(("Neeko",      affection_neeko,      "barkeep_overview_neeko"))
        if met_jinx:
            _barkeep_roster.append(("Jinx",       affection_jinx,       "barkeep_overview_jinx"))
        if met_fizz:
            _barkeep_roster.append(("Fizz",       affection_fizz,       "barkeep_overview_fizz"))
        if met_miss_fortune:
            _barkeep_roster.append(("Miss Fortune", affection_miss_fortune, "barkeep_overview_miss_fortune"))

    if not _barkeep_roster:
        b "You haven't spoken to anyone yet. Get out there first."
        return

    b "Who did you have in mind?"

    $ _barkeep_page = 0
    $ _barkeep_per_page = 4

    label barkeep_ask_about_page:

        python:
            _barkeep_total  = len(_barkeep_roster)
            _barkeep_pages  = (_barkeep_total + _barkeep_per_page - 1) // _barkeep_per_page
            _barkeep_start  = _barkeep_page * _barkeep_per_page
            _barkeep_slice  = _barkeep_roster[_barkeep_start:_barkeep_start + _barkeep_per_page]

        call screen barkeep_name_select(_barkeep_slice, _barkeep_page, _barkeep_pages)

        if _return == "prev":
            $ _barkeep_page -= 1
            jump barkeep_ask_about_page
        elif _return == "next":
            $ _barkeep_page += 1
            jump barkeep_ask_about_page
        elif _return == "back":
            return
        else:
            call expression _return
            b "Anyone else you wanted to ask about?"
            jump barkeep_ask_about_page


## ── Overview labels ──────────────────────────────────────────────────────────

label barkeep_overview_tristana:
    if affection_tristana >= 5:
        b "Tristana? She's taken a shine to you, that much is clear."
        b "Keep showing up. She respects people who don't fold."
    elif affection_tristana >= 3:
        b "She likes you well enough. The trick with Tristana is matching her energy."
        b "She doesn't have much patience for hesitation."
    elif affection_tristana >= 1:
        b "She's noticed you exist, which is a start."
        b "Join her at the table sometime. Win or lose, she'll remember you better for it."
    else:
        b "Tristana. Gunner. Here most nights, losing most nights, refusing to acknowledge either."
        b "She responds well to a dare. Badly to being ignored."
    return

label barkeep_overview_poppy:
    if affection_poppy >= 5:
        b "Poppy's got her eye on you — in the good way. That doesn't happen easily."
        b "Just keep doing what you're doing."
    elif affection_poppy >= 3:
        b "She's warming up to you. Slowly. That's fast by her standards."
        b "She responds well to people who take the work seriously. Whatever work that is."
    elif affection_poppy >= 1:
        b "You've made an impression. She mentioned you, which she doesn't do."
        b "Don't push. Let her come to you on her own terms."
    else:
        b "Poppy keeps this place from falling apart. She's been doing it longer than I've known her."
        b "She's not unfriendly — she's just not warm on first contact. Give it time."
    return

label barkeep_overview_lulu:
    if affection_lulu >= 5:
        b "Lulu has decided you're interesting. That means Pix has too."
        b "They'll find you. They always do when they've decided."
    elif affection_lulu >= 3:
        b "She's been watching you. Pix too. Take that as the compliment it is."
        b "She opens up in her own time, in her own order. Just follow where she leads."
    elif affection_lulu >= 1:
        b "She's curious about you. With Lulu that's most of the work already done."
        b "Find her during the day. She's more herself away from the evening crowd."
    else:
        b "Lulu. She's been around longer than she looks, and she looks at things the rest of us miss."
        b "Don't try to make sense of everything she says. Just listen to the parts that land."
    return

label barkeep_overview_vex:
    if affection_vex >= 5:
        b "I don't know what you did, but Vex is... different around you."
        b "Don't make a thing of it. She'll close back up if you do."
    elif affection_vex >= 3:
        b "She's stopped making it obvious she wants you to leave. Progress."
        b "Keep showing up. Consistency matters more to her than charm."
    elif affection_vex >= 1:
        b "She hasn't run you off yet. That's more than most people get."
        b "Shadow's the tell — watch it, not her face."
    else:
        b "Vex. Corner booth, far end. Drinks more than she should and talks less than she could."
        b "She's not as indifferent as she looks. Shadow gives her away."
    return

label barkeep_overview_katarina:
    if affection_katarina >= 5:
        b "Katarina's invested. I wouldn't know what to do with that information if I were you."
        b "Whatever you're doing — carefully keep doing it."
    elif affection_katarina >= 3:
        b "She's watching you differently than she watches everyone else."
        b "She doesn't do things without a reason. Figure out what she wants and decide if you want to give it."
    elif affection_katarina >= 1:
        b "You passed her first assessment. She has several more."
        b "Don't try to charm her. She's had better try and fail. Just be direct."
    else:
        b "Katarina. Noxian. Dangerous in ways I'm not going to enumerate."
        b "She comes here to relax, which apparently involves taking everyone's money. Don't play her at dice."
    return

label barkeep_overview_ahri:
    if affection_ahri >= 5:
        b "Ahri's decided something about you. I don't know what, but her tails don't lie."
        b "Whatever she offers, go in with your eyes open."
    elif affection_ahri >= 3:
        b "She's started staying longer when you're here. She thinks I haven't noticed."
        b "She'll come to you when she's ready. Don't rush it."
    elif affection_ahri >= 1:
        b "She's filed you somewhere interesting. That's a start."
        b "Spend time in the city. The more this place gets into you, the more she'll find worth looking at."
    else:
        b "Ahri passes through when she needs something from the wood's edge. She's not a regular."
        b "She reads people. Literally, near as I can tell. Don't try to perform anything — she'll see through it."
    return

label barkeep_overview_ezreal:
    if affection_ezreal >= 5:
        b "Ezreal's dropped the performance around you. That's rare."
        b "He'll never say it directly. Just notice when the stories get quieter."
    elif affection_ezreal >= 3:
        b "He's started telling you the real versions instead of the good ones."
        b "Ask him about Shurima sometime. The answer he gives you will tell you a lot."
    elif affection_ezreal >= 1:
        b "He likes you. He likes most people, but he likes you slightly differently."
        b "Find something to challenge him on. He doesn't respect people who don't push back."
    else:
        b "Ezreal. Explorer, treasure hunter, chronic storyteller."
        b "Half of what he says is true and the other half is what he wished happened. Usually in that order."
    return

label barkeep_overview_nidalee:
    if affection_nidalee >= 5:
        b "Nidalee trusts you. I'm not sure she knows that yet."
        b "Don't give her a reason to reconsider."
    elif affection_nidalee >= 3:
        b "She's stopped tracking you as a variable and started tracking you as a presence."
        b "That's significant, coming from her."
    elif affection_nidalee >= 1:
        b "She's classified you as something other than background noise. That's the first step."
        b "Don't be unpredictable around her. She doesn't like what she can't read."
    else:
        b "Nidalee. She came from the deep wood and never fully left it."
        b "She communicates in assessments, not pleasantries. Don't take it personally."
    return

label barkeep_overview_neeko:
    if affection_neeko >= 5:
        b "Neeko's added you to her internal tribe. In her terms, that's everything."
        b "She'll be you sometimes, when she's thinking about you. It's a compliment."
    elif affection_neeko >= 3:
        b "She's been watching your sho'ma — your essence, near as I can translate it."
        b "Let her be curious. She opens up fast once she decides she trusts someone."
    elif affection_neeko >= 1:
        b "She's interested. With Neeko, interested is most of the distance."
        b "Answer her questions directly, even the strange ones. Especially the strange ones."
    else:
        b "Neeko. She's the last of her kind, though she doesn't dwell on it the way you'd expect."
        b "She shapeshifts — not for disguise, just out of curiosity. Don't be startled."
    return

label barkeep_overview_jinx:
    if affection_jinx >= 5:
        b "Jinx has put you in the category of people she keeps track of. That's not nothing."
        b "She'll remember things you said months ago. She always does, with people who matter."
    elif affection_jinx >= 3:
        b "She's started including you in the Fishbones conversations. Take that seriously."
        b "She doesn't let many people into that."
    elif affection_jinx >= 1:
        b "She's decided you're interesting. You've got maybe a few minutes before she tests that conclusion."
        b "Don't be boring. She has a very low tolerance for boring."
    else:
        b "Jinx. Blue hair, large weapon, very specific relationship with said weapon."
        b "She's not dangerous. Mostly. Just... keep your distance from anything she's pointing Fishbones at."
    return

label barkeep_overview_fizz:
    if affection_fizz >= 5:
        b "Fizz is very enthusiastic about you. I'm going to leave it at that."
    elif affection_fizz >= 3:
        b "He asks about you when you're not around. Tries to be subtle. He's not."
    elif affection_fizz >= 1:
        b "He's noticed you. Trust me, you'll know when Fizz has noticed someone."
    else:
        b "Fizz. He works for Katarina. Bodyguard, more or less — she'd hate that word."
        b "He's harmless. Enthusiastic. Keep an eye on where his enthusiasm is pointed."
    return

label barkeep_overview_miss_fortune:
    if affection_miss_fortune >= 5:
        b "Miss Fortune is still talking about you. Favorably, which is unusual for her."
    elif affection_miss_fortune >= 3:
        b "She's asking around about you. In Bilgewater terms that means she's interested."
        b "In what, I couldn't say. Could be business. Could be something else."
    elif affection_miss_fortune >= 1:
        b "She's filed you as a useful contact. That's a start."
        b "Don't be late on debts with her. She has a long memory and short patience."
    else:
        b "Sarah Fortune. Merchant out of Bilgewater. Moves things that don't move through normal channels."
        b "She's here on a trade run. Not a regular — but she comes through every few months."
    return
