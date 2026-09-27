# Dice engines for "die size = power tier (Sense) / number of dice = growing resource (Cosmo)"

Research notes for evaluating the fan-made Saint Seiya proposal: Sense sets the die size (Sixth d8, Seventh d10, Eighth d12), Cosmo sets how many dice are rolled, burning Cosmo adds dice; alternative: keep the current d20 + modifier core (the project's `regras/` currently use "d20 + attribute modifier + proficiency bonus").

Source-quality notes that apply to the whole file:
- The session's network egress blocked direct page fetches for almost every RPG site (reddit, rpg.stackexchange, rpg.net, anydice, SRD hosts, blogs). Cited findings below therefore come from web-search result excerpts of the linked pages, not from full reads. Where an excerpt looked garbled or suspicious it is flagged.
- Numbers marked **[calc]** were computed by the researcher by exact enumeration (Python, full outcome enumeration; ORE multi-set figures by 200k-trial Monte Carlo, flagged as "~"). They are reproducible on anydice.com with snippets such as `output [highest 1 of 5d8]`, `output [highest 2 of 5d8]`, `output 5d8`, `output [count {6..12} in 5d12]`, `output [explode d8]`.

---

## 1. Cortex Prime / Cortex Plus (Marvel Heroic Roleplaying, Smallville, Firefly): mixed-size pools, keep two + effect die, stepping, Plot Points, Doom Pool, 1s

### Takeaway
Cortex is the closest existing model for "die size = power tier": MHR literally labels d8/d10/d12 as Enhanced/Superhuman/Godlike, and the roll is "build a pool of mixed dice, keep two for the total, keep a third die's *size* as the effect". Its costs are well known: pool-building is fiddly, bigger pools produce more 1s (hitches), and stepping rules need special cases above d12.

### Cited Findings
- Cortex Plus is a roll-and-keep system: you roll one die from each trait category and by default keep the two highest dice and add them for the total. — [Cortex wiki: Roll and Keep](https://cortex.fandom.com/wiki/Roll_and_Keep); [Wikipedia: Cortex Plus](https://en.wikipedia.org/wiki/Cortex_Plus)
- Die sizes are d4, d6, d8, d10, d12; "step up" = next larger die, "step down" = next smaller. — [Mephit James: Cortex Prime review](https://mephitjamesblog.wordpress.com/2022/05/31/cortex-prime-game-system-review/); [Gnome Stew review](https://gnomestew.com/cortex-prime-review/)
- Effect die: a die not used in the total; only its *size* matters and sets the magnitude of the effect (a d4 effect die is weak, a d12 very strong). The effect die is chosen from the largest remaining die after the two total dice are chosen. — [KillerShrike: Complications (Cortex Prime)](https://www.killershrike.com/Cortex/Heroic/Fantasy/Complications.aspx); [Cannibal Halfling: Cortex Prime review](https://cannibalhalflinggaming.com/2020/10/21/cortex-prime-review/)
- Heroic success: beating the difficulty by a large margin steps the effect die up (review example: 17 vs 10 is a heroic success, effect die d4 -> d6). The commonly cited threshold is 5+ over the difficulty; the excerpt did not state the number explicitly, so treat "5" as unverified here. — [Cannibal Halfling review](https://cannibalhalflinggaming.com/2020/10/21/cortex-prime-review/); [Gnome Stew review](https://gnomestew.com/cortex-prime-review/)
- Hitches and botches: any die showing 1 is a hitch (a setback the GM can buy, typically giving the player a Plot Point); all 1s is a botch. 1s are not usable in the total. — [Cannibal Halfling review](https://cannibalhalflinggaming.com/2020/10/21/cortex-prime-review/); [Gnome Stew review](https://gnomestew.com/cortex-prime-review/)
- Complications are usually created by spending an effect die from a successful action; the complication gets the size of that die. An effect die larger than an existing complication removes it; an equal one steps it down. A complication stepped past d12 takes the target out (in that hack: "Stressed Out"). — [KillerShrike: Complications](https://www.killershrike.com/Cortex/Heroic/Fantasy/Complications.aspx)
- Stepping past d12 inside a pool (KillerShrike's Cortex Prime hack, not necessarily the core book): "If a d12 in a dice pool would be stepped up, instead step up the next lower die in the dice pool. If all dice that remain in your dice pool are d12's, add a d6." — [KillerShrike: Dice Pools](https://www.killershrike.com/Cortex/Heroic/HereThereBeMonsters/DicePools.aspx)
- Plot Points let players add more traits to the pool or keep more dice in the total; some games add Hero Dice that are added after the roll. — search excerpt of [KillerShrike: Dice Pools](https://www.killershrike.com/Cortex/Heroic/HereThereBeMonsters/DicePools.aspx)
- Doom Pool (MHR / Cortex Prime GM option): the GM's own dice pool; the GM rolls some or all doom dice to oppose players; the GM can spend a doom die to create a scene complication/asset of that size; in MHR, two d12s in the Doom Pool let the GM end the scene immediately. — [Wikipedia: Marvel Heroic Roleplaying](https://en.wikipedia.org/wiki/Marvel_Heroic_Roleplaying); [Faith, Fiction & Fatherhood: Doom Pools for heists](https://faithfictionfatherhood.com/2023/01/11/running-heists-in-cortex-prime-using-doom-pools/)
- MHR power tiers by die size: d6 for low/first rung, Enhanced (peak human or just above) d8, Superhuman d10, Godlike d12. Example Ares: Enhanced Speed d8, Godlike Strength d12, Superhuman Durability d10, Godlike Stamina d12, Leaping d6. Godlike Intellect d12 is described as "nearly unparalleled mental capacities of cosmic beings". — [MHR wiki: Ares](https://marvelheroicrp.fandom.com/wiki/Ares); [MHR wiki: Intellect](https://marvelheroicrp.fandom.com/wiki/Intellect)
- Single-die contests: each step up yields roughly 5-10 percentage points more chance of meeting or beating an opposing die. — [Scott's Game Room: Mixed Dice Probabilities](https://scottsgameroom.com/2012/03/13/core-mechanics-mixed-dice/). Checked [calc]: P(d8 >= d8) 56.2%, P(d10 >= d8) 65.0%, P(d12 >= d8) 70.8%; P(d12 >= d12) 54.2%, P(d8 >= d12) 37.5%, P(d6 >= d12) 29.2%.
- A dedicated Cortex Prime probability calculator exists (Icepool). — [Icepool Cortex Prime calculator](https://highdiceroller.github.io/icepool/apps/cortex_prime.html)
- Keep-2 with 1s excluded (Cortex-like), same-size pools [calc]:

| Pool | Mean total | P(total >= 11) | P(total >= 15) | P(at least one 1 = hitch) | P(botch, all 1s) |
|---|---|---|---|---|---|
| 3d8 | 10.9 | 59% | 12% | 33% | 0.20% |
| 5d8 | 13.0 | 85% | 29% | 49% | ~0% |
| 3d10 | 13.5 | 78% | 43% | 27% | 0.10% |
| 5d10 | 16.0 | 95% | 72% | 41% | ~0% |
| 2d12 | 12.8 | 67% | 38% | 16% | 0.69% |
| 3d12 | 16.0 | 87% | 65% | 23% | 0.06% |
| 5d12 | 19.0 | 98% | 89% | 35% | ~0% |

### Inferences
- If the Saint Seiya pool is all one size (all dice = Sense die), Cortex's effect die collapses to "effect = your Sense die" automatically, which is thematically neat (a Seventh-Sense blow always carries a d10 effect) but loses Cortex's main tactical choice (which die to sacrifice as effect). Mixed pools (e.g., Sense die + Constellation/technique die + Cloth die) restore that choice at the cost of more dice types.
- Cortex's "1s = hitch, GM pays you a Plot Point" is a ready-made cost for burning Cosmo: each extra die raises hitch odds (5d8: 49% at least one 1), and higher Sense lowers them (5d12: 35%), i.e., higher Sense = more control. That matches Saint Seiya fiction reasonably well.
- The MHR tier ladder (d8 Enhanced / d10 Superhuman / d12 Godlike) is a direct precedent for Sixth d8 / Seventh d10 / Eighth d12 — but note MHR only has 3 useful superhuman steps before d12; Saint Seiya canon has Sixth, Seventh, Eighth (Arayashiki) and Ninth/God level, so the ladder runs out at d12 unless you adopt a "past d12" rule (extra die, flat bonus, or d20).

### Gaps
- Could not read the Cortex Prime SRD/Handbook directly (egress blocked); exact current wording of heroic success threshold, Plot Point costs, and official step-up-past-d12 rule is unverified here.
- No community quantitative study found on Cortex table speed (time per roll).

---

## 2. Savage Worlds (SWADE): trait die steps d4–d12+, Wild Die, Acing, raises every 4, Bennies

### Takeaway
SWADE shows how a single step die per trait feels: simple and fast, but exploding dice make the ladder non-monotonic at specific target numbers (a smaller die can beat a bigger one), and above d12 the ladder degrades into flat +1 bonuses — the "d12+1" plateau is exactly the problem a Sense ladder would hit past Eighth Sense.

### Cited Findings
- Roll trait die (d4–d12) plus a Wild Die (d6) for Wild Cards; each die explodes ("aces") on its max and is re-rolled and added; take the higher of the two. — [NateFinch: Savage Math](https://natefinch.com/post/savage-math/); [Hours without sleep: Savage World Probabilities](https://hourswithoutsleep.wordpress.com/2017/05/20/savage-world-probabilities/)
- Target Number 4; each full 4 points over the TN is a "raise"; this "every 4" rule stays the same above d12. — [SWADE Rules Reference, Gamers Plane](https://gamersplane.com/forums/thread/28387/); [PEG forum: traits above d12](https://www.pegforum.com/forum/savage-worlds/official-answers-on-core-rules/46147-derived-stats-from-traits-above-d12)
- Above d12, each further step adds +1 (d12+1, d12+2...). Derived stats get half the modifier rounded down: Fighting d12+1 -> Parry 8, d12+2 -> Parry 9. — [PEG forum: derived stats above d12](https://www.pegforum.com/forum/savage-worlds/official-answers-on-core-rules/46147-derived-stats-from-traits-above-d12); [SWEX to SWADE conversion notes (PEG)](https://s3-us-west-2.amazonaws.com/peg-swade/SWEX_to_SWADE.pdf)
- Critical Failure: a Wild Card rolls 1 on both trait die and Wild Die; it cannot be rerolled with Bennies. Extras (no Wild Die) who roll a 1 roll a d6 when it matters; on a 1 it is a Critical Failure. Bennies reroll any Trait roll (including the Wild Die) or damage roll; multiple Bennies can be spent, keep the best. — [System sans Setting: SW rules summary](https://samhaine.wordpress.com/2020/04/06/savage-worlds-rules-summary/); [Savage Tales of Eberron: Critical Failure](https://savageeberrontales.com/2021/11/22/i-love-it-when-a-plan-falls-apart-critical-failure-in-savage-worlds/)
- Known anomaly: when the TN equals a die's size, the die one step smaller can have better odds because it explodes (you cannot roll exactly "4 then stop" on a d4, etc.). — [RPGnet: SW dice probabilities fixed](https://forum.rpg.net/threads/savage-worlds-dice-probabilities-fixed.483367/); [RPGnet: SW exploding dice house rule](https://forum.rpg.net/index.php?threads/probability-savage-worlds-house-rule-for-exploding-dice.741457/). Note: the search excerpt computed d4 vs TN 6 as "1/4 x 3/4 = 3/8", which is an arithmetic error; the correct value is 3/16 = 18.75% [calc], still higher than d6's 16.7%. The excerpt also said designers "accepted this quirk" — unverified.
- The official SW Facebook group circulated an anydice program for Wild-Die odds (anydice.com/program/1897); an online SW success-rate calculator also exists. — search excerpts citing [NateFinch](https://natefinch.com/post/savage-math/) and [SW Success Rate Calculator](https://nicolas-van.github.io/sw_stats/)
- SWADE odds [calc] (exploding, Wild Die d6, take higher):

| Trait | Alone P>=4 | +WD P>=4 (success) | +WD P>=8 (1 raise) | +WD P>=12 (2 raises) | Crit fail (both 1s) |
|---|---|---|---|---|---|
| d4 | 25.0% | 62.5% | 19.3% | 4.3% | 4.2% |
| d6 | 50.0% | 75.0% | 25.8% | 5.5% | 2.8% |
| d8 | 62.5% | 81.2% | **24.7%** | 10.4% | 2.1% |
| d10 | 70.0% | 85.0% | 39.7% | **11.5%** | 1.7% |
| d12 | 75.0% | 87.5% | 49.8% | **10.9%** | 1.4% |
| d12+1 | — | 91.7% | 56.9% | 19.0% | — |
| d12+2 | — | 95.8% | 64.1% | 27.1% | — |

  Bold cells show the non-monotonic ladder: d8 gets a raise less often than d6; d12 gets two raises less often than d10. Alone, P(>=TN) at TN = die size: d6 16.7% vs d4 18.8%; d8 12.5% vs d6 13.9%; d10 10.0% vs d8 10.9%; d12 8.3% vs d10 9.0% [calc].
- Success chance vs TN 4 with Wild Die rises only 62.5% -> 87.5% across the whole d4->d12 ladder [calc]: the Wild Die compresses the ladder at the low end; step differences show up mostly in raises.

### Inferences
- Exploding step dice are a poor fit if die size must be a *strict* power ordering (Seventh must always be better than Sixth): acing creates inversions at specific TNs. If explosions are wanted for "Cosmo burst" drama, restrict them (e.g., explode only when burning Cosmo) or accept the quirk.
- The d12+N plateau shows the ladder "going flat": above d12 steps are worth roughly +4 to +7 points of raise chance per step, which feels weaker than the d10->d12 jump. For Eighth Sense and beyond, a Sense ladder would need a different mechanism (extra kept die, auto-success, or bigger dice like d20).
- The Wild Die is a precedent for a "hero die" separate from the trait die — an analogue for a dedicated "Cosmo die" or "Sense die" added to a pool of generic dice.

### Gaps
- Could not read the SWADE core/test drive text directly; Bennies economy numbers (starting 3 per session, etc.) not verified here.
- No quantitative data found on SWADE table speed.

---

## 3. One-Roll Engine (ORE): Wild Talents / Reign / Godlike — width & height, hard and wiggle dice, speed from width

### Takeaway
ORE is the strongest existing model for "speed = number of blows": one roll of Nd10 gives initiative (width), quality/location (height), damage (width), and multiple actions (multiple sets). But ORE is d10-only, so tier cannot be die size; ORE expresses super-tiers through special dice (hard = auto-10, wiggle = set after roll) that cost 2x and 4x a normal die.

### Cited Findings
- Roll a pool of d10s and look for matching sets. Width = number of matching dice (speed and, in combat, damage); Height = face value (quality and hit location). Written WxH, e.g., a pair of 5s = 2x5, three 9s = 3x9. — [Wikipedia: One-Roll Engine](https://en.wikipedia.org/wiki/One-Roll_Engine); [Arc Dream: How to Play Wild Talents](https://arcdream.com/home/2011/04/how-to-play-wild-talents/)
- Hard Dice are always set to 10 (not rolled); two hard dice = automatic success at maximum, with no fine control. Wiggle Dice are set to any value after the other dice are rolled, so one wiggle die guarantees a match. — [Milton Keynes RPG Club: Wild Talents](https://www.mk-rpg.org.uk/Wild_Talents); [Wikipedia: ORE](https://en.wikipedia.org/wiki/One-Roll_Engine)
- Costs: hard dice cost 2x and wiggle dice 4x a normal die; Hyperstats cost 4/8/16 points per normal/hard/wiggle die, Hyperskills 1/2/4; hard dice count toward the 10-die maximum. — [RPGnet review of Wild Talents 2e](https://www.rpg.net/reviews/archive/14/14795.phtml); [Arc Dream: Wild Talents Reference PDF](https://arcdream.com/pdf/WT2%20Reference.pdf)
- Width of an attack determines both damage and initiative. — [Arc Dream: WT Reference](https://arcdream.com/pdf/WT2%20Reference.pdf); [Arc Dream: One for Width](https://arcdream.com/home/2011/05/one-for-width/)
- Reign multiple actions: use the lower of the two pools, remove one die, and you need two different sets; each extra action removes another die and requires another set. — [RPG Writeups: Reign](https://writeups.letsyouandhimfight.com/wapole-languray/reign-a-game-of-lords-and-leaders/); [RPG Systems wiki: ORE](http://rpgsystems.wikidot.com/one-roll-engine)
- Gobble dice (defense): each gobble die removes one die of equal or lower height from the attacker's set; a set reduced to one die is gone; gobbling requires acting first (higher width). — [RPG Writeups: Reign](https://writeups.letsyouandhimfight.com/wapole-languray/reign-a-game-of-lords-and-leaders/)
- ORE pool odds [calc] (exact for "any set"; "~" = Monte Carlo 200k trials):

| Pool | P(any set) | P(width >= 3) | P(two or more sets) |
|---|---|---|---|
| 2d10 | 10.0% | 0% | 0% |
| 3d10 | 28.0% | ~1.0% | 0% |
| 4d10 | 49.6% | ~3.7% | ~2.7% |
| 5d10 | 69.8% | ~8.5% | ~11.6% |
| 6d10 | 84.9% | ~15.7% | ~28.1% |
| 7d10 | 94.0% | ~25.3% | ~49.7% |
| 8d10 | 98.2% | ~36.2% | ~70.1% |
| 10d10 | 99.96% | ~60.5% | ~94.4% |

### Inferences
- "Cosmo = pool size" maps naturally onto ORE: more Cosmo -> more sets -> more blows per turn and faster (wider) blows, which fits "Pegasus Ryu Sei Ken = hundreds of punches"/"light-speed" fiction. Small pools are brutal, though: below 5d10 most rolls produce nothing (2d10: 90% no set), which is ORE's best-known pain point for low-level characters.
- Sense as a tier could be modeled ORE-style as dice *quality* rather than size: Sixth = normal dice, Seventh = hard die (guaranteed high, "no fine control"), Eighth = wiggle die (total control). The 1:2:4 cost ratio is a published precedent for pricing tiers.
- Width-as-speed makes "light speed vs Mach 1" comparisons explicit, but it ties damage and speed together; Saint Seiya fights often have fast-but-weak vs slow-but-crushing blows, which ORE cannot separate without house rules.

### Gaps
- Could not read the ORE SRD; exact Wild Talents rules for combining hard/wiggle dice with width-based initiative ties and the 10-die cap for superhuman stats were only seen in excerpts.
- No sourced community data on ORE table speed; anecdotally praised as "one roll does everything" in reviews (excerpt), not quantified.

---

## 4. Year Zero Engine (Free League): pushing, stress dice as both boost and risk; step-dice variant

### Takeaway
YZE is the best precedent for "burning Cosmo": pushing a roll and stress dice add success chances *and* a risk that grows with every added die. Its step-dice variant (Twilight: 2000 4e, Blade Runner) is also a published "die size = rating" system with a fixed success threshold (6+) and bonus successes on 10+.

### Cited Findings
- Core: success requires rolling 6+ on at least one base die; in the step-dice variant a single die showing 10+ (only possible on d10/d12) counts as two successes. — [Free League: YZE Standard Reference Document v1.0](https://freeleaguepublishing.com/wp-content/uploads/2023/11/YZE-Standard-Reference-Document.pdf)
- Pushing: after a roll you may push to re-roll dice; 1s on Base and Gear dice (banes) have no effect on the first roll but count against you (damage, exhaustion, fear, gear damage) if you push. — [YZE SRD](https://freeleaguepublishing.com/wp-content/uploads/2023/11/YZE-Standard-Reference-Document.pdf); [DriveThruRPG: How to play YZE](https://pages.drivethrurpg.com/how-to-play-the-year-zero-rpg-system/). The DriveThruRPG excerpt described pushing as re-rolling dice "that didn't show a 1"; the usual rule is re-rolling dice that did not show a 6 (and, in some games, not 1s either) — exact per-game wording unverified.
- Alien RPG: pushing raises Stress Level by 1 before re-rolling, adding a Stress Die; Stress Dice are added to every roll (making you better), but any 1 on a Stress Die triggers a Panic Roll (d6 + Stress Level; 1–6 hold together, 7+ some debilitating effect); you cannot push after rolling a 1 on a Stress Die. — [RPG Game Gems: Alien RPG guide](https://rpggg.com/posts/master-the-terror-complete-guide-to-the-alien-rpg-system/); [DriveThruRPG: How to play YZE](https://pages.drivethrurpg.com/how-to-play-the-year-zero-rpg-system/)
- Twilight: 2000 4e step dice: ratings A=d12, B=d10, C=d8, D=d6; roll one attribute die + one skill die; 6+ = success; 10+ on one die = two successes; the boxed-set dice mark faces 6+ with a success symbol and 10–12 with two. — [Dice and Ink: TW2K dice mechanics](https://diceandink.com/a-twilight-2000-4th-edition-story/tw2k-dice-mechanics/)
- Community comparison: step dice give a gentler difficulty curve, fewer dice, faster checks, less chance of rolling the wrong number of dice; d6 pools give more suspense/"adrenaline" from rolling a handful. — [Collettivo Antracite: YZE dice pool vs step dice](https://www.collettivoantracite.it/en/year-zero-engine-dice-pool-vs-step-dice-which-system-should-you-choose-opinions-and-comparison/)
- YZE odds [calc] (P at least one 6 on Nd6; "with push" assumes all non-6 dice are re-rolled once, an upper bound):

| Nd6 | 1 | 2 | 3 | 4 | 5 | 6 | 8 |
|---|---|---|---|---|---|---|---|
| First roll | 17% | 31% | 42% | 52% | 60% | 67% | 77% |
| With push | 31% | 52% | 67% | 77% | 84% | 89% | 95% |
| Panic trigger: P(>=1 one) on k stress dice | 17% | 31% | 42% | 52% | 60% | 67% | — |

- Step-die value per die at TN 6 [calc]: d6 0.167, d8 0.375, d10 0.500 (0.600 expected successes with 10+ = 2), d12 0.583 (0.833 with 10+ = 2). So under T2K rules a d12 is worth ~2.2 d8s and ~5 d6s in expected successes.

### Inferences
- Burning Cosmo as "Alien stress dice" is a strong fit: each burned die adds success chance but also a risk die whose 1s trigger a consequence (Cosmo exhaustion, Cloth damage, "burning out"). The risk scales naturally with how much you burn (1 burned die: 17% risk; 4 dice: 52%).
- A T2K-style "Sense die + skill/technique die, 6+ = success, 10+ = two successes" reads fast and gives tier breakpoints for free: a d8 (Sixth) can never score a double success, a d10/d12 can — a clean mechanical expression of "only the Seventh Sense reaches this level".
- Diminishing returns: with "at least one success" reads, extra dice give +23pp, +9pp, +3pp... on d8 [calc], so large Cosmo pools become nearly meaningless unless extra successes are spent on something (damage, extra blows, effects).

### Gaps
- Could not verify the exact per-game push rules (which dice are re-rolled, which 1s count) from primary text.

---

## 5. Genesys / FFG narrative dice: upgrades, advantage/threat

### Takeaway
Genesys separates "how many dice" from "how good the dice are": pool size = the higher of characteristic/skill, upgrades = the lower. That is a direct template for Cosmo (count) + Sense (upgrade quality). Its costs are proprietary symbol dice and a reading step that interprets two axes (success/failure and advantage/threat).

### Cited Findings
- Pool construction: the higher of characteristic and skill = number of green Ability dice; the lower = how many of those are upgraded to yellow Proficiency dice (e.g., Athletics 2, Brawn 3 -> 3 dice, 2 upgraded). — [Genesys Wiki: Dice & Dice Pools](https://www.genesys.wiki/index.php/Dice_&_Dice_Pools); [RPG Writeups: Genesys core mechanics](https://writeups.letsyouandhimfight.com/citizenkeen/genesys/)
- Upgrades: players spend Story Points to upgrade Ability -> Proficiency; the GM spends to upgrade Difficulty -> Challenge. — [Cannibal Halfling: Genesys review](https://cannibalhalflinggaming.com/2017/12/01/genesys-review-part-one/); [Matt Goes Rogue: narrative dice](https://www.mattgoesrogue.com/genesys-narrative-dice/)
- Triumph appears only on Proficiency dice (a success plus a major benefit); Despair only on Challenge dice (a failure plus a major bane); their success/failure parts cancel normally but the special effects remain. — [Matt Goes Rogue](https://www.mattgoesrogue.com/genesys-narrative-dice/); [Cannibal Halfling: Genesys in depth](https://cannibalhalflinggaming.com/2020/09/16/genesys-in-depth/)

### Inferences
- Genesys-style mapping: Cosmo = number of dice; Sense = how many are "upgraded" (or the upgrade tier). Burning Cosmo = add dice; awakening a higher Sense = upgrade dice. This keeps a single die type per tier while giving two distinct growth axes — arguably better than pure "bigger die" because the upgrade can add *special outcomes* (Triumph-like "Big Bang" results) that only high-Sense dice can produce.
- The custom-symbol requirement is a real barrier for a fan game; the same logic can be imitated with standard dice (e.g., upgraded = d12 where 12 = "miracle", or d6 pools where upgraded dice succeed on a lower threshold — see Burning Wheel shades below).

### Gaps
- No probability data collected for Genesys pools (custom dice); not computed.

---

## 6. Other pool systems: Shadowrun, Chronicles of Darkness, Blades in the Dark, Burning Wheel shades, Riddle of Steel, Storypath/Scion 2e (plus the DCC dice chain)

### Takeaway
Two families matter most for the proposal: (a) threshold-by-tier pools (Burning Wheel shades: same d6, but higher shade lowers the success number — a tier model that needs only d6s), and (b) budgeted pools (Riddle of Steel: a pool you split across attack/defense and that refreshes — a model for Cosmo as a spendable resource). Storypath's Scale shows how to handle huge tier gaps without inflating pools.

### Cited Findings
- **Shadowrun 5e**: count hits (5 or 6 on d6); if more than half the dice show 1, it's a glitch; a glitch with no hits is a critical glitch. — [Shadowrun 5th SRD wiki: Dice Mechanics](https://shadowrun-5th-srd.fandom.com/wiki/Dice_Mechanics)
- **Chronicles of Darkness**: d10 pool, 8+ = success, 10s re-rolled ("10-again"; 9-again/8-again widen this); with one die P(>=1 success) = 0.30 (0.51 for rote actions); P(at least S successes on one die) = 0.3·(1.1 − r/10)^(S−1). — [Techgnostic Psychonaut: CofD dice probability](https://m45t1g05.blogspot.com/2016/02/chronicles-of-darkness-dice-probability.html); [CofD rules: probabilities](https://cod.spiele-bund.net/base/probabilities/)
- **Blades in the Dark**: roll Nd6, read the highest: 1–3 failure, 4–5 partial success, 6 full success, two or more 6s critical; 0 dice = roll 2, take lowest. Cumulative table: 0d: 4+ 25.0%, 6 2.8%; 1d: 50.0% / 16.7%; 2d: 75.0% / 30.6% / crit 2.8%; 3d: 87.5% / 42.1% / 7.4%; 4d: 93.8% / 51.8% / 13.2%; 6d: 98.4% / 66.5% / 26.3%. — [Blades community: cumulative probabilities](https://community.bladesinthedark.com/t/cumulative-probabilities-for-action-rolls/1536); [AnyDice article: Blades in the Dark](https://anydice.com/articles/blades-in-the-dark/); [Columbia stat blog: Blades probabilities](https://statmodeling.stat.columbia.edu/2020/07/15/probabilities-for-action-and-resistance-in-blades-in-the-dark/)
- **Burning Wheel**: exponent = number of d6; Obstacle (Ob) = successes needed; shade sets the per-die threshold: Black 4+ (50%), Grey 3+, White 2+ (fails only on 1); grey/white represent heroic/supernatural ability. — [RPG Systems wiki: Burning Wheel](http://rpgsystems.wikidot.com/burning-wheel); [Keep on the Heathlands: BW](https://keepontheheathlands.com/2017/11/27/burning-wheel-the-intimidating-game-that-is-not-actually-intimidating/); [RPGnet: BW, what are the colors for?](https://forum.rpg.net/index.php?threads/burning-wheel-what-are-the-colors-for.240411/). A statistical critique of BW's difficulty table exists: [Quantifying Strategy](https://www.quantifyingstrategy.com/2020/05/is-burning-wheels-difficulty-table.html) (not read).
- Burning Wheel odds [calc] P(successes >= Ob):

| Shade / exponent | Ob1 | Ob2 | Ob3 | Ob4 | Ob5 |
|---|---|---|---|---|---|
| Black B4 | 94% | 69% | 31% | 6% | 0% |
| Black B6 | 98% | 89% | 66% | 34% | 11% |
| Grey B4 | 99% | 89% | 59% | 20% | 0% |
| Grey B5 | 100% | 95% | 79% | 46% | 13% |
| White B4 | 100% | 98% | 87% | 48% | 0% |
| White B5 | 100% | 100% | 96% | 80% | 40% |

  Expected successes per die: black 0.50, grey 0.67, white 0.83 [calc]. Ratios grey/black = 1.33 and white/black = 1.67 are close to plain step dice counted at 6+: d10/d8 = 0.500/0.375 = 1.33 and d12/d8 = 0.583/0.375 = 1.56 [calc] — shade (threshold) and die size are near-interchangeable ways to express tier.
- **The Riddle of Steel**: Combat Pool = Reflex + proficiency rank; each exchange attacker and defender secretly commit dice from the pool to maneuvers; spent dice are gone until the pool refreshes; the pool must be budgeted over two exchanges; Pain is subtracted on refresh. — [TROS wiki: Combat Pool](http://tros.thewestwinds.net/index.php?title=Combat_Pool); [TROS wiki: Refresh Combat Pool](http://tros.thewestwinds.net/index.php?title=Refresh_Combat_Pool); [Deeper in the Game: TROS](https://bankuei.wordpress.com/2010/04/18/the-riddle-of-steel/)
- **Storypath / Scion 2e**: Enhancements add extra successes only if the roll already has at least one success; Scale is shorthand for overwhelming size/speed etc. (a giant crushing a car gets Enhancement); excerpts state Scale = Legend/2 rounded up and that in a contest the higher-Scale side gains +2 Enhancement per point of Scale difference (both unverified against the book). — [Scion 2e wiki: Cheatsheet](https://scion-origin.fandom.com/wiki/Cheatsheet); [Onyx Path forum: Questions on Scale](https://forum.theonyxpath.com/forum/main-category/main-forum/scion/1437449-sc-2e-questions-on-scale)
- **DCC dice chain** (step-die precedent beyond d12): d3–d4–d5–d6–d7–d8–d10–d12–d14–d16–d20–d24–d30; "improved die" moves one step right, "reduced die" one step left; needs Zocchi dice. — [Roll20: DCC starter rules](https://roll20.net/compendium/dcc/DCC%20RPG%20Starter%20Rules); [Gnome Stew: Climbing the dice chain](https://gnomestew.com/climbing-the-dice-chain/)

### Inferences
- Burning Wheel shades are the cleanest "tier changes the success threshold" model and need only d6s: Sixth = succeed on 4+, Seventh = 3+, Eighth = 2+ (Ninth/God = auto-successes). Cosmo = number of d6; burning Cosmo = more d6. This keeps both axes, avoids buying d8/d10/d12 in bulk, and is as fast to read as Shadowrun hits. The tier gap is large but not absolute: Grey B4 at Ob3 (59%) is close to Black B6 (66%); in expectation one grey die = 1.33 black dice, one white die = 1.67.
- Riddle of Steel's refreshing pool is the best fit if Cosmo should be *spent in the fight* (split between attack, defense, and special techniques) rather than simply rolled. It creates tactical bluffing but slows combat (secret allocations every exchange).
- Storypath's Scale is a precedent for handling "god vs mortal" gaps without adding dozens of dice: a separate tier comparison grants flat bonus successes/automatic effects.
- DCC's chain offers a way past d12 (d14, d16, d20...) for Eighth Sense/God tiers, at the cost of unusual dice.

### Gaps
- Could not verify Storypath's exact Scale rules; treat excerpt numbers as unconfirmed.
- No source found giving CofD's per-die expected successes directly (0.333 under 10-again follows from the cited formula: 0.3/(1−0.1)).

---

## 7. Probability: "N dice of size S, sum" vs "N dice, take highest" vs "count successes"; step vs pool; huge tier gaps; d20 comparison

### Takeaway
The read-out method decides which axis dominates. With **sum**, pool size (Cosmo) swamps die size (Sense): 6d8 beats 2d12 97% of the time. With **keep highest**, die size dominates and caps the result (Sixth can never exceed 8), and extra dice have steep diminishing returns. **Keep two** (Cortex) and **count successes** sit in between. Choose the read-out according to how much a larger Cosmo should be able to beat a higher Sense.

### Cited Findings
All figures in this section are [calc] unless another source is given.
- **Sum (NdS)** mean ± SD: 3d8 13.5±4.0; 5d8 22.5±5.1; 3d10 16.5±5.0; 3d12 19.5±6.0; 5d12 32.5±7.7. Each die adds (S+1)/2 regardless of pool size (linear returns).
- **Keep highest** E[max]: d8 pools 1→6 dice: 4.50, 5.81, 6.47, 6.86, 7.11, 7.29; d12 pools: 6.50, 8.49, 9.48, 10.07, 10.47, 10.74. Marginal gain of +1 die on d12: +1.99, +0.99, +0.59, +0.39, +0.28, +0.21 (steep diminishing returns).
- **Keep highest** P(max >= T): d8 P(>=8) for 1–6 dice: 12%, 23%, 33%, 41%, 49%, 55%. d12 P(>=10): 25%, 44%, 58%, 68%, 76%, 82%.
- **Count successes at 6+** (YZE/T2K): per-die rates d6 0.167 / d8 0.375 / d10 0.500 / d12 0.583; with 10+ = 2 successes: d10 0.600, d12 0.833.
- **Equivalence** (dice needed to match 3d12's average): sum: 5d8 or 4d10 or 6d6; count 6+: 5d8, 4d10, 11d6; keep highest: 10d10, and no number of d8 (the average of highest-of-Nd8 never reaches 9.48 because the max is 8).
- **Opposed rolls, P(attacker wins) / P(tie)**:

| Attacker vs defender | Sum | Keep highest | Keep 2 | Successes 6+ | Successes 6+, 10+=2 |
|---|---|---|---|---|---|
| 3d8 vs 3d8 (mirror) | 47 / 7 | 39 / 22 | 45 / 9 | 34 / 33 | 34 / 33 |
| 3d10 vs 3d8 (+1 Sense) | 65 / 6 | 69 / 11 | 67 / 7 | 47 / 30 | 54 / 26 |
| 3d12 vs 3d8 (+2 Sense) | 77 / 4 | 82 / 7 | 80 / 5 | 55 / 27 | 70 / 18 |
| 3d12 vs 3d6 (+3 steps) | 89 / 3 | 92 / 4 | 91 / 3 | 77 / 18 | 83 / 12 |
| 5d8 vs 3d12 (big Cosmo, low Sense) | 62 / 5 | 14 / 8 | 24 / 6 | 38 / 28 | 27 / 21 |
| 6d8 vs 2d12 | 97 / 1 | 28 / 9 | 50 / 7 | 65 / 22 | 52 / 22 |
| 8d8 vs 3d12 | 97 / 1 | 17 / 9 | n/c | 67 / 19 | 50 / 19 |
| 4d10 vs 3d12 | 59 / 5 | 27 / 11 | 39 / 7 | 42 / 29 | 38 / 20 |

- **Tier-gap ceiling under keep highest**: however many d8 a Sixth-Sense character rolls, P(d8 side strictly beats M d12s) is at most (7/12)^M: 58% vs 1d12, 34% vs 2d12, 20% vs 3d12, 12% vs 4d12; the d12 side rolls above 8 (unreachable for d8) 33%/56%/70%/80% of the time with 1–4 dice.
- **Ties**: keep-highest mirror matches tie often (3d8 vs 3d8: 22%; 5d8 vs 5d8: 34%; 3d12 vs 3d12: 15%); count-successes mirror matches tie ~33% at 3d8. Both need an explicit tie rule; sum and keep-2 tie 5–9%.
- **1s frequency** (if 1s = complication): P(at least one 1): d8 pools 2–8 dice: 23%, 33%, 41%, 49%, 55%, 61%, 66%; d12 pools: 16%, 23%, 29%, 35%, 41%, 46%, 50%.
- **d20 alternative** (d20+A vs d20+B, defender wins ties): bonus difference 0: 47.5% (tie 5%); +2: 57.2%; +4: 66.0%; +5: 70.0%; +8: 80.5%; +10: 86.2%; +15: 96.2%. Against a fixed DC, each +1 = +5 percentage points (flat, linear). 2d10 for comparison: P(>=11) 55%, P(>=16) 15%.
- Dice pools trend toward the mean as more dice are rolled, which designers use for "probability control". — [Collettivo Antracite](https://www.collettivoantracite.it/en/year-zero-engine-dice-pool-vs-step-dice-which-system-should-you-choose-opinions-and-comparison/)

### Inferences
- **Sum** makes Cosmo the dominant stat and erases tier: a Sixth-Sense Saint with 6 Cosmo (6d8) beats an Eighth-Sense Saint with 2 Cosmo (2d12) 97% of the time. It also forces adding 5–8 dice per roll (slow). Only suitable if Sense is meant to be secondary.
- **Keep highest** makes Sense dominant with a hard ceiling: burning Cosmo past ~3–4 dice adds little (+0.4 average per die on d12 at 4→5), so "burn everything!" moments feel flat. It does model canon well ("no amount of Bronze-level cosmo reaches Gold level without awakening the Seventh Sense"), but it makes the game about awakening (stepping the die), not about burning.
- **Keep two (Cortex)** is the most balanced of the "read numbers" options: 6d8 vs 2d12 is a coin flip, 5d8 vs 3d12 ~24%, so big Cosmo can overcome one Sense step but rarely two.
- **Count successes vs fixed TN** gives linear returns per die (burning always matters) and lets die size set efficiency; adding "10+ = 2 successes" amplifies tier (d12 worth 2.2 d8). It reads fast (count symbols), and extra successes can buy damage/extra blows, which directly supports "speed = number of blows".
- **d20**: the tier gap has to be expressed as flat bonuses; a +5 gap (70% win) feels like one Sense step in the step-die engines (65–69% win for d10 vs d8), and +10 (86%) like two steps. d20 cannot express "more dice = more reliability" (variance never shrinks), so "burning Cosmo" becomes +X bonus or advantage-like rolls.

### Gaps
- Did not find a published anydice/StackExchange analysis specifically of "Nd(S) where S = tier" for the three read-outs; the comparisons here are the researcher's own calculations and should be spot-checked on anydice.
- Exploding variants of the pools (e.g., d12 explode on 12) were computed only for SWADE.

---

## 8. Known design problems: fiddly dice swapping, table speed, exploding-dice variance, tiny pools, many dice types — and community discussion

### Takeaway
Every engine above has a documented weak spot that maps onto the proposal: Cortex (fiddly pool-building, more 1s from bigger pools), SWADE (exploding-die inversions, flat top end), ORE (tiny pools rarely match), YZE (sharp diminishing returns on "at least one"), Genesys (custom dice). Step dice are praised for speed; pools for drama.

### Cited Findings
- Cortex Prime reviewers call pool manipulation fiddly; "dice pools lead to more 1s", "bigger dice don't always help statistically, as you can still roll a 1 on a d12"; the potential statistical spreads are "mind-boggling"; one reviewer reported repeatedly re-explaining mechanics at the table. — search excerpts of [Jeff's Game Box: Cortex Prime review](https://jeffsgamebox.blog/2022/08/05/cortex-prime-a-review/) and [Mephit James: Cortex Prime review](https://mephitjamesblog.wordpress.com/2022/05/31/cortex-prime-game-system-review/) (which quote belongs to which review could not be confirmed)
- A community hack exists explicitly aimed at fewer dice ("Minimum Dice, Maximum Fun"); a separate blog series discusses difficulty/grit adjustments to Cortex Prime. — [Tim Bannock: Another simple Cortex Prime hack](https://timbannock.com/another-simple-cortex-prime-hack-minimum-dice-maximum-fun/); [Faith, Fiction & Fatherhood: Grit in Cortex Prime](https://faithfictionfatherhood.com/2022/01/24/back-to-the-mud-putting-some-grit-in-cortex-prime-part-ii-general-difficulties/) (contents not read; title evidence only)
- Savage Worlds' exploding-dice anomaly (lower die better at TN = die size) is a long-running community complaint with multiple house-rule proposals. — [RPGnet: SW dice probabilities fixed](https://forum.rpg.net/threads/savage-worlds-dice-probabilities-fixed.483367/); [RPGnet: SW exploding dice house rule](https://forum.rpg.net/index.php?threads/probability-savage-worlds-house-rule-for-exploding-dice.741457/)
- Step dice: fewer dice, faster to resolve, less chance of rolling the wrong number of dice; pools: suspense of rolling a handful. — [Collettivo Antracite](https://www.collettivoantracite.it/en/year-zero-engine-dice-pool-vs-step-dice-which-system-should-you-choose-opinions-and-comparison/)
- Genesys and DCC require non-standard dice (proprietary symbol dice; Zocchi d3/d5/d7/d14/d16/d24/d30). — [Matt Goes Rogue: Genesys dice](https://www.mattgoesrogue.com/genesys-narrative-dice/); [Roll20: DCC starter rules](https://roll20.net/compendium/dcc/DCC%20RPG%20Starter%20Rules)
- Tiny ORE pools: 2d10 produce a set only 10% of the time, 3d10 28%, 4d10 49.6% [calc].

### Inferences
- **Dice-type burden of the proposal**: with Sense = die size and Cosmo up to ~6–10 dice, each player needs many dice of their own Sense size (e.g., 8d8 for a Bronze Saint, 8d12 for a Gold), and the GM needs many of every size. A shade/threshold version with only d6s (Burning Wheel) or a "one Sense die + Cosmo d6s" version (SWADE Wild Die / T2K style) avoids this.
- **Dice swapping**: Sense changes mid-fight (awakening the Seventh Sense during a battle is a genre staple) means swapping a whole pool from d8 to d10. Cortex's step-up/step-down proves this works for one or two dice but gets fiddly for whole pools; a threshold change (4+ -> 3+) requires no swap at all.
- **Table speed**: sum of 6–8 dice is the slowest read; keep-highest and count-successes are the fastest; keep-2 is moderate. Summing large d12 pools also inflates numbers (5d12 ≈ 32.5), forcing large damage/HP scales.
- **Variance**: exploding dice for Cosmo bursts create memorable spikes but break strict tier ordering (see SWADE table); if strict ordering matters, avoid explosions or restrict them.
- **Top of the ladder**: d12 is the last common die. Eighth Sense = d12 leaves no room for Ninth/God tier; options are d20 (DCC chain), extra kept dice, auto-successes (ORE hard dice), or threshold 2+/auto (BW white shade), or Storypath-style Scale.

### Gaps
- Could not access Reddit/RPG StackExchange/RPGnet threads directly, so community sentiment is based on titles and excerpts rather than full discussions. No timing studies (seconds per roll) were found for any engine.

---

## 9. Applying the findings to the Sense-die / Cosmo-pool proposal vs staying on d20

### Takeaway
The proposal is viable and has clear precedents (MHR tiers, T2K step dice, YZE pushing, Genesys upgrades), but its behavior depends almost entirely on the read-out. "Sum" lets Cosmo erase Sense; "keep highest" lets Sense erase Cosmo; "keep two" or "count successes" balance them. Staying on d20 is simpler but can only express tiers and Cosmo as flat bonuses.

### Cited Findings
- Die-size tiers are established in published design (MHR: d8 Enhanced / d10 Superhuman / d12 Godlike). — [MHR wiki: Intellect](https://marvelheroicrp.fandom.com/wiki/Intellect); [MHR wiki: Ares](https://marvelheroicrp.fandom.com/wiki/Ares)
- Step-die ratings with a fixed 6+ threshold and double success on 10+ are published (Twilight: 2000 4e A–D = d12–d6). — [Dice and Ink](https://diceandink.com/a-twilight-2000-4th-edition-story/tw2k-dice-mechanics/)
- Resource-driven extra dice with built-in risk are published (Alien stress dice; YZE push). — [RPG Game Gems: Alien](https://rpggg.com/posts/master-the-terror-complete-guide-to-the-alien-rpg-system/); [YZE SRD](https://freeleaguepublishing.com/wp-content/uploads/2023/11/YZE-Standard-Reference-Document.pdf)
- Quantity/quality separation is published (Genesys: higher value = dice, lower value = upgrades). — [Genesys Wiki](https://www.genesys.wiki/index.php/Dice_&_Dice_Pools)
- Key [calc] results for the proposal's exact dice (Sixth d8, Seventh d10, Eighth d12): same Cosmo 3 vs 3, one Sense step up wins 65–69% (sum/highest/keep-2) or 47–54% (successes); two steps up win 77–82% or 55–70%. A Sixth-Sense character with double the Cosmo (6d8 vs 2d12) wins 97% (sum), 50% (keep-2), 28% (highest), 52–65% (successes). On d20, the equivalent of one step is about +4/+5 (66–70%), two steps about +8/+10 (80–86%).

### Inferences
- **If the design goal is "Sense is a qualitative leap, Cosmo is effort within a tier"**: use keep-2 (Cortex) or count-successes with 10+ = 2 (T2K). Both keep a Bronze Saint burning everything competitive against one Sense step but not two, matching canon where Bronzes beat Golds only after awakening the Seventh Sense.
- **Model "awakening" as a die step (Cortex step-up) and "burning" as dice added (YZE push/stress)**: the two most iconic Saint Seiya moments then have distinct mechanics. Make burned dice carry risk (1s on burned dice = Cosmo exhaustion/damage, Alien-style), so burning is a gamble, not free power.
- **Consider the no-new-dice variant**: Cosmo = number of d6; Sense = success threshold (Sixth 4+, Seventh 3+, Eighth 2+) per Burning Wheel shades. Per-die value 0.50/0.67/0.83 successes, with tier ratios (1.33x, 1.67x) close to plain d8/d10/d12 counted at 6+ (1.33x, 1.56x); only d6s, no pool swapping on awakening.
- **Speed = number of blows**: count-successes or ORE-like sets both turn extra Cosmo into extra blows naturally; sum and keep-highest do not.
- **Staying on d20**: minimal disruption to the existing rules (the project's `regras/` and `sim/` are built on d20 + modifiers), well-understood math (each +1 = 5pp), fast reads. It loses the tactile "burn Cosmo, grab more dice" moment and the variance-shrinks-with-effort effect; Cosmo would become flat bonuses or advantage-style rerolls. A hybrid (d20 core, plus a small "Cosmo die" pool added to the d20, sized by Sense: +1d8/+1d10/+1d12 per burn) keeps d20 infrastructure while giving the step-die feel; its math would need a separate simulation.
- **Hard-ceiling danger**: under keep-highest, a d8 side can never exceed 8, so any DC above 8 is literally impossible for Sixth Sense. That can be a feature (canon-accurate "only a Seventh Sense can reach light speed") but must be deliberate; it removes Bronze-Saint underdog victories unless awakening/step-up is available in play.

### Gaps
- The hybrid "d20 + Sense-sized Cosmo dice" was not simulated.
- No playtest or published fan-game data on a Saint Seiya die-size engine was found (not searched in depth; out of this note's mechanics scope).
