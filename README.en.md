> 🇬🇧 **English** · 🇧🇷 [Português](README.md)

# Ascensão dos Semideuses — a tabletop RPG

An independent, unofficial tabletop RPG project. Its rules, text, and creation
engines are original; its setting presents Greek demigods in the modern world
on a d20 foundation.

**Live:** https://madeiragab.github.io/ascensao-dos-semideuses/

> **Independence notice:** this is an unofficial, non-profit project.
> *Percy Jackson* and elements specific to that franchise belong to their
> respective authors and rights holders, including Rick Riordan and licensed
> companies. This project is not affiliated with, endorsed by, or sponsored by them.

> The books themselves are written in **Brazilian Portuguese**. This page explains
> the design and the tooling in English.

What separates this project from a pile of house rules is the combination of
**simulation and table playtesting**: numbers are measured, improvised rulings are
recorded, and rules only close after surviving both. The four times the numbers
contradicted intuition are documented below.

**Current version:** 0.14.0 · [Changelog](CHANGELOG.md)

---

## The five books

| | Book | Contents |
|---|---|---|
| **I** | [Player's Book](https://madeiragab.github.io/ascensao-dos-semideuses/livro-do-jogador.html) | How to play, character creation, combat, optional Demigod Fury, item catalogue, divine materials, and the ability engine |
| **II** | [Bestiary](https://madeiragab.github.io/ascensao-dos-semideuses/bestiario.html) | The Kleos Scale, the monster-building engine, and 38 creatures |
| **III** | [Grimoire](https://madeiragab.github.io/ascensao-dos-semideuses/grimorio.html) | Mist Magic: learned spellcasting, with a Disbelief rule |
| **IV** | [Game Master's Guide](https://madeiragab.github.io/ascensao-dos-semideuses/guia.html) | Running one-shots to long campaigns, NPCs, investigation, breaking objects, environmental hazards |
| **V** | [Character Sheet](https://madeiragab.github.io/ascensao-dos-semideuses/ficha.html) | Fillable, calculates lineage, advancement, and Grade, takes a portrait, and downloads or imports an editable A4 PDF |

All five books now have clickable contents and cross-references. A small floating
trident opens the other volumes without taking over the reading layout.

PDFs downloaded from version 0.13.1 onward carry their editable sheet data inside
the file and can be imported later. Everything is read locally in the browser;
older PDFs were image-only and cannot be reconstructed. From version 0.13.2 onward,
the original portrait is also preserved without cropping, resizing, or recompression
throughout that cycle.

---

## How the system works

**The core roll** is unchanged, but each opposition now has a ready target.
Skill checks roll `1d20 + modifier + proficiency` against a difficulty; attacks
roll against Defense; effects roll against passive Fortitude, Reflexes or Will.
Each passive defense is `14 + ability + proficiency` when trained, and the effect
source rolls. Base 14 is exactly probability-equivalent to the former model,
including inverted Advantage and Disadvantage.

**Three resources**, each on its own recovery clock. Hit Points come back slowly —
a long rest returns only half. Stamina returns in full after an hour. Mana only
returns after sleeping. This is what makes attrition across an adventuring day
actually accumulate.

**Hubris** is the character's fatal flaw, and it has teeth. The GM offers a
*Provocation*; if the player accepts and plays the flaw, they earn *Impetus*, which
buys Advantage among other things. Once per story arc the GM may declare a
*Rupture*, and then the flaw decides for you. Impetus can be earned at most once
per scene and spent at most once per turn.

As an optional module, **Demigod Fury** turns Rupture into three stages of
divine overflow shaped by Bonds, lineage, Hubris and emotion. Each character
receives a personal manifestation, while control, consent, anchors and lasting
consequences keep that power from becoming an every-fight transformation.

**Abilities don't come as a spell list.** Players build each one by buying effects
with points, and only then convert points into a resource:

```
POINTS = duration + extra effects + range + modifiers
COST   = points × the Grade of the point
```

Duration already includes the first point of effect: instantaneous 1, sustained 2,
scene 4. Sustaining costs half the final cost per round.

**Progression is the Grade**, and the Grade is simply the level band — 1 at levels
1–4 up to 5 at 17–20. Every effect table has one row per Grade: a point of
single-target damage buys `1d8` to `5d8`, an area point `1d6` to `5d6`, a movement
point +3 m to +15 m. A point of Grade G costs G, so **damage per MP stays flat**:
the Grade changes how much fits into one action, not how far the resource goes.
Conditions and Advantage don't grow with Grade — they reach more creatures.
Defence never grows: +2 remains the cap, because measured at level 20 each point
of DEF is worth almost seven points of win rate.

An ability written at level 1 never has to be rebuilt: it stays on the sheet and
is simply paid for at the new Grade, delivering more.

**Universal table rules** now cover the former edge cases: passive defenses, combined effects,
activation, Minor Affinity Manifestations, friendly fire, carrying allies, hands
and objects, skill criticals, stabilization, and Impetus timing. The Portuguese
quick reference is [`regras/regras-universais.md`](regras/regras-universais.md).

**Items are level-gated.** Six grades run from Mortal equipment to Divine
relics, while Attunement limits active permanent powers. Beyond weapons and
armor, the Player's Book now includes 21 utility items, 12 curatives and 24
magic items, all priced in drachmas.

**Fourteen skills**, not sixteen: *Arcana* was absorbed into Mythology — in a world
where all magic is Greek there aren't two bodies of knowledge — and *Animal Handling*
folded into Survival.

**Monsters are measured in Kleos** — the glory it costs to bring one down. Eleven
named rungs: Rumour, Hearsay, Tale, Exploit, Deed, Song, Legend, Myth, Epic,
Theomachy, Cataclysm. A creature of Kleos N is a fair and dangerous fight for N
demigods.

**Every creature has a discoverable Mythic Weakness.** The Hydra is unwinnable
without fire. The Nemean Lion is immune to weapons. Cerberus wants to play fetch.
Finding that out *is* the game.

---

## The simulator

Python 3, no external dependencies. Run from inside `sim/`.

```bash
cd sim
python experimentos.py      # diagnosis of the original system
python comparar.py          # original vs. the corrected proposal
python dia_de_aventura.py   # attrition curve across several fights
python kleos.py             # validates the Bestiary's danger scale
python habilidades.py       # validates the ability-building engine
python condicoes.py         # prices control against damage
python calibrar_kleos.py    # tests the Kleos scale at every level
python equilibrio.py        # audit: Kleos by level, classes, weapons, armour
python tecnicas.py          # measures all 36 class techniques, one by one
python defesas_passivas.py  # proves exact base-14 probability equivalence
```

It measures two ways, and both matter. The **analytic** side computes exact d20
probability with no luck involved — good for closed claims like "this technique is
always better than that one". The **simulation** side runs thousands of complete
fights with real dice, reaching what isolated math cannot: initiative order, target
focus, resource spending, who drops first.

### The four times the tests proved me wrong

1. **Heavy Attack had no numerical fix.** I was going to swap −2/+5 for another
   pair. I swept seven variants: none works while Fierce Attack grants free
   Advantage on the same attack, because Advantage pays off any to-hit penalty. The
   fix had to be structural — forbid the combination.
2. **Packs of weak enemies are worth less, not more.** I had written that many
   enemies add up above their total Kleos. The opposite is true: three Kleos 1
   creatures give a 96% win rate against 82% for a single Kleos 3, because the
   party focuses fire and every kill stops dealing damage forever. The rule became
   `sum × 3/4`, with a maximum error of 0.3 on a scale of eleven.
3. **Spending mana doesn't buy damage.** I had concluded the caster wins the day on
   accumulated damage. It doesn't: 80 against the melee class's 97, and that class
   spends nothing. What mana buys is range, area, conditions and choice.
4. **The Kleos Scale was wrong above level 1.** The rule said a hero was worth 1, 2,
   3 or 4 Kleos by level band. Measured, it's 1 · 1¾ · 2¼ · 2¾ · 3 — a level-20
   character is worth less than *three* times a level-1 one, not four. A level-15
   party following the old rule would be sent against something three rungs above
   what it can survive.

---

## Repository layout

```
livro-do-jogador.html   bestiario.html   grimorio.html
guia.html               ficha.html
                                                        ← generated, don't edit
index.html              the shelf page

template/               book shells and the single stylesheet
  livro.css             CSS shared by all five books
  livro-do-jogador.html hand-written
  bestiario.html        shell; content comes from the markdown
  grimorio.html         shell, with its own green-and-gold palette
  guia.html             the GM's Guide, purple-and-gold palette
  ficha.html            the fillable sheet, black-and-gold palette

regras/                 chapters in markdown, plus the system map
  regras-universais.md  quick reference born from the first full playtest
bestiario/              Book II in markdown
imagens/                original covers and generated thumbnails
sim/                    the simulator
fonte/                  the original document, the system's initial state
vendor/                 bundled MIT libraries for direct A4 PDF generation
CHANGELOG.md            version history and rule decisions
```

Start with **[`regras/SUMARIO.md`](regras/SUMARIO.md)** (in Portuguese): the map of
every chapter, what's finished, what has holes, and what doesn't exist yet.

### Building the books

The published HTML is self-contained — no external files are loaded, and the covers
are embedded as data URIs. Hence a build step:

```bash
powershell -ExecutionPolicy Bypass -File build.ps1
```

The script resizes the covers, generates the shelf thumbnails, and calls
`build_livros.py`, which converts the markdown and assembles the five books.

To repeat the complete numerical regression:

```bash
powershell -ExecutionPolicy Bypass -File test.ps1
```

> **Always edit `template/` and the markdown.** The `.html` files at the root are
> generated and will be overwritten on the next build.

---

## Known debts

The Player's Book is complete enough to play from level 1 to 20. What's left is
refinement:

1. **Ten techniques the simulator cannot represent.** 26 of the 36 were measured;
   the rest depend on positioning, forced movement, fear or rerolls, which the
   engine does not model. They need a table, not a simulator.
2. **Long-form drachma economy.** Initial prices and rewards work, but inflation,
   upkeep and rewards across long campaign arcs still need measurement.

### Known limits of the simulator

- **Legendary-style actions and Refusals** aren't modelled, which widens the error
  margin on Kleos rungs 6 to 11 — the Bestiary's full creatures are more dangerous
  than the tested version.
- Conditions **are** modelled since the Conditions chapter was calibrated, but only
  three families: losing your turn, attacking at Disadvantage, and bleeding.
- No positioning or distance: everyone reaches everyone.
- Opportunity attacks exist in the rules but not in the simulator.

---

## Licence

A personal work in progress. The creatures and deities come from Greco-Roman
mythology, which is public domain; the rules system, the prose and the Kleos Scale
are original work.
