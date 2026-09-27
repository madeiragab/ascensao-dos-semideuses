# Comeback/escalation, refusing defeat, locational armor damage, and perverse-incentive safeguards (reference notes for a Saint Seiya RPG)

> **Method and source-quality note (read first).** In this session the egress proxy blocked direct fetches of almost every RPG site (fate-srd.com, bladesinthedark.com, 13thagesrd.com, dungeonworldsrd.com, Reddit, Stack Exchange, Wikipedia, Sirlin.net, gamedeveloper.com, and others), and the shared web-search budget ran out partway through. So there are two tiers of evidence:
> - **Tier A (primary text, quoted verbatim):** Blades in the Dark SRD, Fate Core SRD, Fate Condensed SRD, Dungeon World (official CC text), Lancer (pre-release Community Edition text plus final-edition table text taken from the official-licensed Foundry VTT system), GURPS hit-location data (Foundry system), WFRP4e hit-location code (Foundry system), and an Exalted 3e attack-resolution gist. All were read from GitHub clones.
> - **Tier B (search-engine summaries):** 13th Age, Masks, Apocalypse World, Savage Worlds, Exalted Crash, Feng Shui 2, Burning Wheel, Tenra Bansho Zero, Marvel Heroic, Dogs in the Vineyard, Mouse Guard/Torchbearer, D&D 4e, and the fighting games. These come from search-result snippets and summaries. I could not open the full pages, so treat any wording attributed to them as paraphrase unless marked otherwise.
> - Systems I could not verify at all are listed under **Gaps**. Anything I recall but could not source is flagged there as *unverified*.

---

## 1. How the listed systems implement comeback/escalation and "refusing defeat"

### Takeaway
Almost no well-regarded tabletop system hands out power **directly in proportion to damage taken**. The ones that come close (the SFIV Revenge gauge, the SFV V-Gauge, Tekken Rage, D&D 4e "when first bloodied" monster triggers) are fighting games, where both sides have the same tools, or GM-controlled monsters. Tabletop systems instead pay for defeat and suffering with **currency that arrives later or is spent under a cost** (Fate concession and compels, Blades stress/XP, Burning Wheel Artha, Tenra Aiki/Kiai), or they let the fight's momentum grow on a **clock that is independent of damage** (13th Age escalation die, Exalted initiative). "Getting back up" is almost always a one-shot or heavily escalating option that leaves a **permanent mark**: Dungeon World's Last Breath, Fate's extreme consequence, Blades trauma, Apocalypse World's "life untenable", Lancer cloning.

### Cited Findings

**Blades in the Dark (Tier A, SRD)**
- Stress is a reserve you spend to refuse consequences: "When they suffer a consequence that they don't want to accept, they can take stress instead." — [Blades SRD](https://github.com/amazingrando/blades-in-the-dark-srd-content/blob/main/Blades-in-the-Dark-SRD.md)
- Resistance always works. Only the cost is random: "Resistance is always automatically effective—the GM will tell you if the consequence is reduced in severity or if you avoid it entirely." "Your character suffers **6 stress** when they resist, **minus the highest die result**… If you get a **critical** result, you also **clear 1 stress**." — [Blades SRD](https://github.com/amazingrando/blades-in-the-dark-srd-content/blob/main/Blades-in-the-Dark-SRD.md)
- Built-in guards against abuse: "**You may only roll against a given consequence once.**" and "You can't roll first and see how much stress you'll take, then decide whether or not to resist." — [Blades SRD](https://github.com/amazingrando/blades-in-the-dark-srd-content/blob/main/Blades-in-the-Dark-SRD.md)
- Pushing yourself costs 2 stress per bonus, and each bonus can be taken once per action: "+1d", "+1 level to your effect", or "**Take action when you're incapacitated.**" This is Blades' "get up and keep fighting" button, paid in stress. — [Blades SRD](https://github.com/amazingrando/blades-in-the-dark-srd-content/blob/main/Blades-in-the-Dark-SRD.md)
- Harm: level 3 harm leaves you incapacitated "unless you have help from someone else or **push yourself**". Harm that finds its row full rolls up to the next row. Past the top row comes "a **catastrophic, permanent consequence** (loss of a limb, sudden death…)". Level 4 is "Fatal". — [Blades SRD](https://github.com/amazingrando/blades-in-the-dark-srd-content/blob/main/Blades-in-the-Dark-SRD.md)
- Trauma is the escalating cost of running out: "When a PC marks their last stress box, they suffer a level of **trauma**… you're taken out of action… When you return, **you have zero stress**." "**Trauma conditions are permanent**… can earn xp by using it to cause trouble. **When you mark your fourth trauma condition**, your character cannot continue." — [Blades SRD](https://github.com/amazingrando/blades-in-the-dark-srd-content/blob/main/Blades-in-the-Dark-SRD.md)
- Trauma raises ongoing upkeep: "If you do not or cannot indulge your vice during downtime, you take stress equal to your **trauma**." — [Blades SRD](https://github.com/amazingrando/blades-in-the-dark-srd-content/blob/main/Blades-in-the-Dark-SRD.md)
- XP for danger, not for damage: "mark xp: When you make a **desperate action roll**. Mark 1 xp in the attribute for the action you rolled." — [Blades SRD](https://github.com/amazingrando/blades-in-the-dark-srd-content/blob/main/Blades-in-the-Dark-SRD.md)
- The GM usually decides who is in a desperate position: "Once the player chooses their action, the GM sets the **position**… **By default, an action roll is risky.**" — [Blades SRD](https://github.com/amazingrando/blades-in-the-dark-srd-content/blob/main/Blades-in-the-Dark-SRD.md)
- A player can still volunteer for danger, but only by giving up safety in exchange for effect: "a player might want to trade position for effect… push their luck and make a desperate roll but with great effect." The desperate position also raises the stakes: "Since the position was desperate, the GM inflicts severe harm" (level 3 in the example). — [Blades SRD](https://github.com/amazingrando/blades-in-the-dark-srd-content/blob/main/Blades-in-the-Dark-SRD.md)
- The designers say outright that desperate-for-XP is intended, and they bound it: "No matter how low-Tier or outmatched you are, a desperate position is the worst thing that can result… you might even want those desperate rolls to generate more xp for the PCs, which helps to bootstrap starting characters into advancement." — [Blades SRD](https://github.com/amazingrando/blades-in-the-dark-srd-content/blob/main/Blades-in-the-Dark-SRD.md)
- XP from suffering has anti-farming language and caps: "You struggled with issues from your vice or traumas… Simply indulging your vice doesn't count as struggling with it (unless you **overindulge**)." Per-category XP is capped ("2 xp is the maximum for that category"). — [Blades SRD](https://github.com/amazingrando/blades-in-the-dark-srd-content/blob/main/Blades-in-the-Dark-SRD.md)
- Armor is an ablative, refreshable resource, not a damage reduction value: "mark an armor box to reduce or avoid a consequence… When an armor box is marked, it can't be used again until it's restored. All of your armor is restored when you choose your **load** for the next score." Heavy armor gives a second box. — [Blades SRD](https://github.com/amazingrando/blades-in-the-dark-srd-content/blob/main/Blades-in-the-Dark-SRD.md)
- Death is partly the player's choice: "If they suffer level 4 fatal harm and they don't resist it, they die. *Sometimes this is a choice a player wants to make…*" — [Blades SRD](https://github.com/amazingrando/blades-in-the-dark-srd-content/blob/main/Blades-in-the-Dark-SRD.md)
- The crew upgrade "Hardened" gives each PC "+1 trauma box" and costs three upgrades. It "may bring a PC with 4 trauma back into play." — [Blades SRD](https://github.com/amazingrando/blades-in-the-dark-srd-content/blob/main/Blades-in-the-Dark-SRD.md)

**Fate Core / Fate Condensed (Tier A, SRD)**
- Stress boxes are momentum ("you only have so many last-second saves in you"). Consequences are "mild, moderate, and severe… two, four, and six" shifts. — [Fate Core SRD](https://github.com/amazingrando/fate-srd/blob/main/docs/markdown/fate-core.md)
- Your wound is the enemy's resource: "The opponent who forced you to take a consequence gets a free invocation… because the slant on it is so negative, it's far more likely to be used to your character's detriment." — [Fate Core SRD](https://github.com/amazingrando/fate-srd/blob/main/docs/markdown/fate-core.md)
- The extreme consequence is the "refuse to fall" option, and it has a cap and a permanent cost: "every PC also gets one last-ditch option to stay in a fight—the extreme consequence. Between major milestones, you can only use this option once… absorb up to 8-shifts… you must replace one of your aspects (except the high concept)… taking it literally changes who you are… you can't make a recovery action." — [Fate Core SRD](https://github.com/amazingrando/fate-srd/blob/main/docs/markdown/fate-core.md)
- Concession is the one place where Fate pays you **per wound taken**, and only if you give up the stakes: "you can interrupt any action at any time before the roll is made to declare that you concede… Concession gives the other person what they wanted from you… you get a fate point for choosing to concede… an additional fate point for each consequence… These fate points may be used once this conflict is over." — [Fate Core SRD](https://github.com/amazingrando/fate-srd/blob/main/docs/markdown/fate-core.md)
- Fate Condensed adds explicit anti-gaming language: "You must concede before your opponent rolls the dice. You can't wait to see the outcome of the dice and concede when it's obvious you can't win—that's poor form." It also allows a heroic sacrifice: "The more significant the cost you pay, the greater the benefit your side should receive… one member choosing to concede as a heroic (and fatal) last stand could mean everyone else is spared!" — [Fate Condensed SRD](https://github.com/amazingrando/fate-srd/blob/main/docs/markdown/Fate-Condensed-SRD-CC-BY.md)
- Fate points for suffering, via the aspect economy. Accepting a compel earns a FP; refusing one costs a FP. "If someone pays a fate point to invoke an aspect attached to your character, you gain their fate point at the end of the scene. This includes… consequences." — [Fate Core SRD](https://github.com/amazingrando/fate-srd/blob/main/docs/markdown/fate-core.md)
- The GM should telegraph lethal intent so players can concede: "make sure that you telegraph the opponent's lethal intent… so the players will know which NPCs really mean business, and can concede." NPCs who concede carry their FPs into the GM's next-scene pool. — [Fate Core SRD](https://github.com/amazingrando/fate-srd/blob/main/docs/markdown/fate-core.md)
- A "fight on now, pay later" stunt (Hard Boiled): "ignore a mild or moderate consequence for the duration of the scene… At the end of the scene it comes back worse… mild… becomes moderate… moderate, it becomes severe." — [Fate Core SRD](https://github.com/amazingrando/fate-srd/blob/main/docs/markdown/fate-core.md)
- Fate Condensed offers "Conditions" as a replacement for consequences: pre-defined harm boxes, each consequence level split into "two conditions of half the value". — [Fate Condensed SRD](https://github.com/amazingrando/fate-srd/blob/main/docs/markdown/Fate-Condensed-SRD-CC-BY.md)

**Dungeon World (Tier A, official text)**
- Last Breath: "When you're dying you catch a glimpse of what lies beyond the Black Gates… roll (just roll, +nothing—yeah, Death doesn't care how tough or cool you are). On a 10+ you've cheated death—you're in a bad spot but you're still alive. On a 7–9 Death will offer you a bargain. Take it and stabilize or refuse and pass beyond… On a miss, your fate is sealed… you'll cross the threshold soon." — [Dungeon World Moves.xml](https://github.com/Sagelt/Dungeon-World/blob/master/text/Moves.xml)
- GM guidance: "Death knows and sees all and tailors his bargains accordingly. This is a trade… Offer something that will be a challenge to play out… a brush with death, succeed or fail, is a significant moment that should always lead to change." It also notes that "he remembers this slight" on a 10+. — [Dungeon World Moves_Discussion.xml](https://github.com/Sagelt/Dungeon-World/blob/master/text/Moves_Discussion.xml)
- XP for failure: "A 6 or lower is trouble, but you also get to mark XP." — [Dungeon World Playing_the_Game.xml](https://github.com/Sagelt/Dungeon-World/blob/master/text/Playing_the_Game.xml)

**Lancer (Tier A; pre-release CE text plus final-edition table strings)**
- HP resets in layers: "When a mech… is reduced to 0 HP, it takes 1 structure damage, makes a structure check, then resets its HP to full. It then takes any damage that 'spills over'… Player mechs have 4 structure." — [Lancer Community Edition, damage.tex](https://github.com/AshleyMoni/Lancer-Community-Edition/blob/master/source/theMech/damage.tex)
- The check gets worse the more you are hurt, because the dice pool grows with damage and you keep the **lowest** die: "roll 1d6 per point of structure damage you have marked… choose the lowest result." — [Lancer CE damage.tex](https://github.com/AshleyMoni/Lancer-Community-Edition/blob/master/source/theMech/damage.tex)
- Structure results (final wording): Glancing Blow "impaired until the end of your next turn". System Trauma "Roll 1d6. On a 1–3, all weapons on one mount of your choice are destroyed; on a 4–6, a system of your choice is destroyed." Direct Hit at 3+ structure "stunned"; at 2 "Roll a HULL check… On a failure, your mech is destroyed". Crushing Hit (multiple 1s) "destroyed". — [Lancer Foundry system, en.json](https://github.com/Eranziel/foundryvtt-lancer/blob/master/public/lang/en.json)
- A self-inflicted danger zone that grants power: "When a mech has 1/2 of its total heat capacity filled, it's in the danger zone. Certain mech weapons and talents only activate in this area." Heat mostly comes from the player's own choices (overcharging and so on), with a parallel reactor-stress track and meltdown risk. — [Lancer CE damage.tex](https://github.com/AshleyMoni/Lancer-Community-Edition/blob/master/source/theMech/damage.tex)
- The death-refusal cap: cloning or revival "always comes back with a Quirk… If a cloned or revived character would be cloned or revived a second time, they can no longer be played… you're one and done." — [Lancer CE damage.tex](https://github.com/AshleyMoni/Lancer-Community-Edition/blob/master/source/theMech/damage.tex)

**Exalted 3e (Tier A gist, plus Tier B summary)**
- Initiative works as offensive health. Withering attacks: "The target loses Xi… You gain (X + 1)i." Decisive attacks: "The damage roll is (your current Initiative)… your Initiative resets to 3." "The target gets a −1 onslaught penalty to Defense until their next turn." "If the target is Crashed by the attack, apply Break or Shift." — [Exalted 3e attack resolution gist](https://gist.github.com/drumanagh/01ebace965e8b66066d358874a8b3042)
- A crashed character can't make decisive attacks. Initiative Shift: if the crashed character crashes their attacker back, "they instantly return to base initiative… roll Join Battle again… and then get to make an immediate additional attack". A crashed character resets to base initiative after three rounds. — [Exalted3e wikidot Combat 301 (search summary)](http://exalted3e.wikidot.com/ess:combat-301); [bragrman cheat sheet (search summary)](https://bragrman.com/wp-content/uploads/2017/01/exalted-3e-combat-cheat-sheet-2.pdf)

**13th Age (Tier B)**
- The escalation die starts at 0, adds +1 each round from round 2, and caps at +6. PCs and a few select monsters add it to attack rolls. Monsters normally don't; dragons are an exception. If the GM judges the PCs are avoiding the fight, the die doesn't advance, and it resets to 0 if combat "virtually ceases". Its stated purpose is "increasing momentum and building teamwork… shortening most battles". — [Roll20 13th Age Combat](https://roll20.net/compendium/13thage/Combat); [13th Age SRD Combat Rules](https://www.13thagesrd.com/combat-rules/)
- On giving it to monsters: adding it to all monster attacks "would eliminate 13th Age's dramatic curve, in which battles start out stacked against the heroes but tip in their favor as they dig in and fight." — [Pelgrane, "13th Sage: Escalation for Everyone?"](https://pelgranepress.com/2014/08/07/13th-sage-escalation-for-everyone/) (summary; full text not read)

**Masks: A New Generation (Tier B)**
- There are five emotional conditions (Afraid, Angry, Guilty, Hopeless, Insecure), each −2 to specific moves: Angry −2 to comfort/support and pierce the mask; Afraid −2 to directly engage; Guilty −2 to provoke and assess; Hopeless −2 to unleash your powers; Insecure −2 to defend and reject influence. "Take a powerful blow" is the basic move that is "never taken voluntarily". Too many conditions takes a character out. — [Strange Assembly review](https://www.strangeassembly.com/2018/masks-review); [Obsidian Portal, Effect of Conditions](https://masksanewgeneration-1.obsidianportal.com/wikis/effect-of-conditions)

**Apocalypse World (Tier B)**
- The harm clock: harm before 6:00 heals on its own, and harm after 9:00 worsens unless stabilized. Marking 11:00–12:00 makes life "untenable", and the options are: "a penalty to hard, a bonus to weird, change to a new playbook, or die". Past 9:00 a character can take a permanent **debility** instead. — [Troy Press, Harm Systems in PbtA](https://troypress.com/harm-systems-in-pbta-games/); [AW rules/playbooks PDF](http://bignose.whitetree.org/tmp/apocalypse-world/rules-playbooks.pdf)

**Savage Worlds Adventure Edition (Tier B)**
- Soak: a Wild Card spends a Benny for a Vigor roll, and "a success and each raise reduce the number of Wounds… by one". Wild Cards are Incapacitated beyond 3 Wounds and then roll Vigor. Failure means an Injury Table result that is permanent. Success means the injury heals when all Wounds heal. A raise means it goes away in 24 hours. — [Kanka SW Basics](https://app.kanka.io/w/what-lies-beneath/entities/1444790/html-export); [System sans Setting SW summary](https://samhaine.wordpress.com/2020/04/06/savage-worlds-rules-summary/)

**Feng Shui 2 (Tier B)**
- 25+ Wound Points gives 1 Impairment and 30+ gives 2, applied to attacks, skills, and Defense. Past 35, PCs make "Up Checks" to stay standing and can collect Marks of Death. After the fight, anyone with a Mark makes a Death Check ("after a suitable melodramatic speech"). Featured Foes auto-drop at 35. — [Alexandrian FS2 cheat sheet](https://thealexandrian.net/wordpress/43049/roleplaying-games/feng-shui-2-system-cheat-sheet); [Mors Rattus FS writeup](https://writeups.letsyouandhimfight.com/mors-rattus/feng-shui/) (summarized together in search results; I couldn't tell which page says what)

**Burning Wheel (Tier B)**
- Artha comes in three kinds. Fate is earned by playing your Beliefs and Instincts "even when it would cause them trouble". Persona comes from accomplishing personal goals. Deeds come from "hard work and sacrifice" and "greatly modify a die roll". — [hectorgrey BW writeup](https://writeups.letsyouandhimfight.com/hectorgrey/burning-wheel/); [Wikipedia: The Burning Wheel](https://en.wikipedia.org/wiki/The_Burning_Wheel)

**Tenra Bansho Zero (Tier B)**
- Other players give you Aiki chits for playing to your Fates or doing something cool. Aiki converts to Kiai, which is spent on bonus dice, raised skills, or automatic successes. Spending Kiai builds Karma, and Karma over 108 turns the character into an evil NPC. Weakening or erasing Fates during intermissions lowers Karma. — [Mythcreants](https://mythcreants.com/blog/tenra-bansho-zero-is-fun-insanity/); [High Level Games](https://www.highlevelgames.ca/blog/4-cool-mechanics-from-tenra-bansho-zero)

**Marvel Heroic Roleplaying / Cortex Plus (Tier B)**
- The Watcher (GM) has a Doom Pool. Any 1 a player rolls is an Opportunity, and the Watcher can add a d6 to the Doom Pool or step up a die. Plot Points can "change a form of incoming stress from one type to another". — [RPGnet review](https://www.rpg.net/reviews/archive/15/15570.phtml); [Marvel Plot Points, Doom Pool economics](https://marvelplotpoints.com/2012/04/04/the-doom-pool-economics-how-the-marvel-rpg-balances-itself-according-to-party-size/)

**Dogs in the Vineyard (Tier B)**
- Players escalate from talking to physical, then fighting, then guns to bring in new dice, and can de-escalate on a later raise. "Only gunfights are going to result in death." The fallout/experience system turns what happened in a conflict into new or changed traits. — [Wikipedia: DitV](https://en.wikipedia.org/wiki/Dogs_in_the_Vineyard); [jhkim strategy notes](https://www.darkshire.net/~jhkim/rpg/dogsinthevineyard/strategy.html)

**Mouse Guard / Torchbearer (Tier B)**
- The conditions are Hungry/Thirsty, Angry, Afraid, Tired/Exhausted, Injured, and Sick, and each has a specific penalty (for example, Injured is −1D to skills, Nature, Will, and Health). Recovery must follow an order (you can't clear Afraid before Hungry/Angry). — [Firebroadside primer](https://firebroadside.blogspot.com/2018/07/a-mouse-guard-and-torchbearer-primer.html); [Mythcreants on MG failure](https://mythcreants.com/blog/why-mouse-guard-handles-failure-better-than-any-other-rpg/)

**D&D 4e (Tier B)**
- Bloodied means at or below half HP. Several monsters have "when first bloodied" reaction attacks (owlbear, veteran), and some powers work better against bloodied targets. — [Crit Academy, Bloodied and Bruised](https://www.critacademy.com/post/bloodied-and-bruised-dynamic-combat-monster-manual-options)

**Fighting games (Tier B)**
- Street Fighter IV's Revenge Gauge "fills when one takes damage", including chip damage and armor-absorbed hits. Ultra needs at least 50%, and a full gauge does about 1.5× the damage of a half gauge (Akuma: ~340 vs ~510). — [Street Fighter Wiki: Revenge Gauge](https://streetfighter.fandom.com/wiki/Revenge_Gauge); [Ultra Combo](https://streetfighter.fandom.com/wiki/Ultra_Combo)
- Street Fighter V's V-Gauge fills from V-Skills, **taking damage**, blocking, and Crush Counters. The fill from damage is **percentage-based**, so a low-health character like Ibuki "will build the same amount of V-Gauge as… Abigail after taking 20% damage." — [Street Fighter Wiki: V-Gauge](https://streetfighter.fandom.com/wiki/V-Gauge); [SuperCombo V-System](https://wiki.supercombo.gg/w/Street_Fighter_V/V-System)
- Tekken Rage turns on below a health threshold. In Tekken 8, Rage Art damage scales up as the user's health falls. Player complaints include that "a yolo raw rage art… gives an opportunity for a free mix up that can usually result in a win, even if the player was losing the entire match", and that the leading player is pushed into cautious play. — [Hotspawn T8 Rage guide](https://www.hotspawn.com/tekken/guide/tekken-8-understanding-the-rage-system); [Steam, "The reason rage is a bad mechanic"](https://steamcommunity.com/app/389730/discussions/0/3002178258651838760/); [Steam, "Rage arts are way too safe"](https://steamcommunity.com/app/1778820/discussions/0/4691153809035662563/?ctp=3)
- Sirlin frames it as "slippery slope" (falling behind makes you fall further) versus "perpetual comeback" (being behind gives an advantage). — [Sirlin, Slippery Slope and Perpetual Comeback](https://www.sirlin.net/articles/slippery-slope-and-perpetual-comeback)
- Law of Game Design on rubber bands: "Done right, they keep matches entertaining… Done wrong, rubber bands make good play meaningless." It calls SF4's Ultra (usable "only after taking a beating") a classic and "in at least some cases, very good" rubber band. MvC3's X-Factor is once per game and powers you up more the fewer characters you have left, and it inspired Sirlin's Puzzle Strike comeback mechanic. — [Law of Game Design, Theory: Rubber Bands](https://lawofgamedesign.com/2014/08/25/theory-rubber-bands/)

### Inferences
- The design family closest to the Saint Seiya pitch (power grows as you get hurt) is the fighting-game one (SFIV/SFV/Tekken). Those games are symmetric: both players have the same meter, and matches are short and zero-sum. A co-op RPG with GM-run enemies has neither property, so the "just don't get hit" counter-pressure disappears.
- Tabletop systems that want suffering to pay usually **route the payout through a currency** (fate points, XP, Kiai, Artha) instead of raising power immediately in the same fight. Fate is the clearest case: a FP per consequence, but only on concession and only after the conflict ends.
- Every "get back up" mechanic found has at least one of these: (a) a hard use cap (Fate extreme consequence once per milestone, Lancer clone once, MvC3 X-Factor once per game); (b) an escalating or permanent cost (Blades trauma to retirement, Fate rewriting an aspect, AW debility or playbook change, Tenra Karma 108); (c) a result that doesn't care about power (DW Last Breath "roll +nothing").

### Gaps
- No direct designer quote was found on **why** 13th Age's escalation die is time-based rather than damage-based. The only related Tier B rationale is the "dramatic curve" comment. The "Secret Origins of the Escalation Die" post exists ([Pelgrane](https://pelgranepress.com/2015/11/13/13th-sage-secret-origins-of-the-escalation-die/)) but I couldn't read it.
- Not verified (search budget ran out): Final Fantasy limit breaks (FFVII fill-on-damage, FFVIII critical-HP Limits, FFX Overdrive modes such as "Stoic" and "Comrade"); the Smash Bros rage mechanic; Street Fighter RPG (White Wolf) Chi/Willpower/Health; Savage Worlds "Adrenaline Surge"; Tenra's **Kegare**; Marvel Heroic "Limits" (earning PP by shutting down a power); D&D 4e PC "bloodied" features (e.g., Dragonborn Fury); Cortex Prime stress/trauma step-ups; Dogs in the Vineyard "giving" and fallout details; Honor/Grit mechanics.
- *Unverified recollection, check before citing:* in Masks each condition is cleared by acting it out (for example, Angry by hurting someone or breaking something important, Afraid by running from something difficult), and players mark Potential (XP) on a miss.

---

## 2. Choice + cost vs. raw damage, narrative triggers, caps — and how systems stop "get hit on purpose"

### Takeaway
Games avoid the "take hits on purpose" trap in recurring ways:
1. The trigger is something other than damage: time or rounds (13th Age), your own offense (Exalted), GM-set danger (Blades), or other players' approval (Tenra).
2. Players commit before they know the result (Blades resistance, Fate concession).
3. The payoff comes after the fight or only if you lose the stakes (Fate concession).
4. The wound also feeds the opponent (Fate free invoke, Marvel Doom Pool).
5. The payoff is proportional rather than absolute (SFV percent-based meter).
6. Uses are capped with permanent scars (Fate extreme consequence, Blades trauma, Lancer clone).

### Cited Findings
**Comeback tied to player choice plus a cost (rather than raw damage)**
- Blades: push yourself (2 stress, each bonus once per action, including acting while incapacitated). The Devil's Bargain "is always a free choice… The Devil's Bargain occurs regardless of the outcome of the roll… the GM has final say over which Devil's Bargains are valid." — [Blades SRD](https://github.com/amazingrando/blades-in-the-dark-srd-content/blob/main/Blades-in-the-Dark-SRD.md)
- Fate: extreme consequence (once per major milestone, rewrites an aspect) and concession (lose the stakes, collect FPs later). — [Fate Core SRD](https://github.com/amazingrando/fate-srd/blob/main/docs/markdown/fate-core.md)
- Lancer: power in the danger zone comes from heat you usually generate yourself, and you pay with overheat and meltdown risk. — [Lancer CE damage.tex](https://github.com/AshleyMoni/Lancer-Community-Edition/blob/master/source/theMech/damage.tex)
- Tenra: spending Kiai builds Karma, capped at 108 before the PC becomes an NPC. — [Mythcreants](https://mythcreants.com/blog/tenra-bansho-zero-is-fun-insanity/)

**Comeback tied to narrative triggers (conviction, bonds, allies)**
- Fate compels on your own aspects pay FPs. Any player can propose a compel on their own character for free, and the GM is final arbiter of validity. — [Fate Core SRD](https://github.com/amazingrando/fate-srd/blob/main/docs/markdown/fate-core.md)
- Burning Wheel pays Fate for playing Beliefs and Instincts even when it causes trouble, and Deeds for sacrifice. — [BW writeup](https://writeups.letsyouandhimfight.com/hectorgrey/burning-wheel/)
- Tenra Bansho Zero: Aiki is granted by other players for playing to your Fates, a **socially gated** trigger. — [High Level Games](https://www.highlevelgames.ca/blog/4-cool-mechanics-from-tenra-bansho-zero)
- Blades XP for "express[ing] your beliefs, drives, heritage" and for struggling with vice or trauma, with explicit anti-farming wording. — [Blades SRD](https://github.com/amazingrando/blades-in-the-dark-srd-content/blob/main/Blades-in-the-Dark-SRD.md)
- Fate Condensed: a costlier concession buys a bigger benefit for the side, up to a heroic last stand that spares everyone. — [Fate Condensed SRD](https://github.com/amazingrando/fate-srd/blob/main/docs/markdown/Fate-Condensed-SRD-CC-BY.md)
- Dungeon World: Death's bargain is tailored to "the behaviors of the character and the things you've learned about him in play". — [DW Moves_Discussion.xml](https://github.com/Sagelt/Dungeon-World/blob/master/text/Moves_Discussion.xml)

**Comeback tied to raw damage (the risky group)**
- The SFIV Revenge gauge and SFV V-Gauge fill when you are hit, and Tekken Rage turns on at low health. — [SF Wiki Revenge Gauge](https://streetfighter.fandom.com/wiki/Revenge_Gauge); [SF Wiki V-Gauge](https://streetfighter.fandom.com/wiki/V-Gauge); [Hotspawn](https://www.hotspawn.com/tekken/guide/tekken-8-understanding-the-rage-system)
- D&D 4e "when first bloodied" monster reactions are GM-side, so players can't farm them. — [Crit Academy](https://www.critacademy.com/post/bloodied-and-bruised-dynamic-combat-monster-manual-options)

**Caps found**
- 13th Age: +6 maximum, no advancement if PCs stall, reset if fighting stops. — [Roll20 13th Age Combat](https://roll20.net/compendium/13thage/Combat)
- SFIV: Ultra needs ≥50% gauge, and damage scales only to about 1.5× at full. — [SF Wiki Ultra Combo](https://streetfighter.fandom.com/wiki/Ultra_Combo)
- Fate: extreme consequence once per major milestone. Blades: 4 trauma then retirement, one resistance roll per consequence, each push bonus once per action. Lancer: revival once. — [Fate Core SRD](https://github.com/amazingrando/fate-srd/blob/main/docs/markdown/fate-core.md); [Blades SRD](https://github.com/amazingrando/blades-in-the-dark-srd-content/blob/main/Blades-in-the-Dark-SRD.md); [Lancer CE](https://github.com/AshleyMoni/Lancer-Community-Edition/blob/master/source/theMech/damage.tex)

**Specific anti-exploit devices, quoted**
- Commit blind: "You can't roll first and see how much stress you'll take, then decide whether or not to resist." (Blades). "You must concede before your opponent rolls the dice… that's poor form." (Fate Condensed) — [Blades SRD](https://github.com/amazingrando/blades-in-the-dark-srd-content/blob/main/Blades-in-the-Dark-SRD.md); [Fate Condensed SRD](https://github.com/amazingrando/fate-srd/blob/main/docs/markdown/Fate-Condensed-SRD-CC-BY.md)
- Deferred payout: concession FPs "may be used once this conflict is over". — [Fate Core SRD](https://github.com/amazingrando/fate-srd/blob/main/docs/markdown/fate-core.md)
- The wound empowers the enemy: the attacker gets a free invoke on your consequence (Fate), and player 1s feed the Doom Pool (Marvel). — [Fate Core SRD](https://github.com/amazingrando/fate-srd/blob/main/docs/markdown/fate-core.md); [RPGnet MHR review](https://www.rpg.net/reviews/archive/15/15570.phtml)
- Proportional meter: SFV fills V-Gauge by **percent** of health lost, so low-health characters don't benefit more. — [SF Wiki V-Gauge](https://streetfighter.fandom.com/wiki/V-Gauge)
- Anti-stall: 13th Age's die doesn't advance if PCs avoid the fight. — [Roll20 13th Age Combat](https://roll20.net/compendium/13thage/Combat)
- Worse outcomes come bundled with the reward: in Blades a desperate position gives XP but also harsher harm (the level 3 example). — [Blades SRD](https://github.com/amazingrando/blades-in-the-dark-srd-content/blob/main/Blades-in-the-Dark-SRD.md)
- A known failure case: Tekken rage lets a losing player win with a single guess and changes how the leader plays. — [Steam thread](https://steamcommunity.com/app/389730/discussions/0/3002178258651838760/)

### Inferences (applied to the Saint Seiya design; these are my synthesis, not sourced claims)
- **Raise the Cosmo *ceiling*, not current Cosmo, when a character is hurt.** Current Cosmo then has to be *spent into* by invoking a conviction (a narrative trigger, like a Fate compel or BW Belief). Getting hit makes a burst *possible* but never free. This mirrors the Fate split between consequence (harm) and FP (fuel), and the Lancer split between danger zone (unlock) and heat (cost).
- **Make the Cosmo gain proportional to severity, and one-shot per wound tier.** For example, gain Cosmo only the *first* time each harm tier or sense is lost, as in 4e's "when *first* bloodied" and Fate's one consequence slot per severity. Chip damage then gives nothing and deliberate "farming" hits yield diminishing returns. The SFV lesson is to scale by percent or tier, not absolute HP.
- **Have the enemy profit from the same event.** For example, when a Saint takes a wound that raises Cosmo, the GM gains a "Destiny/Doom" die, or the attacker gets a free invoke on the wound (Fate). Taking a hit on purpose then becomes a trade, not a gift.
- **Rising again from 0 HP:** borrow Blades trauma and the Lancer/Fate caps. Each rise permanently marks a "Scar" condition that adds a cost (e.g., +1 Cosmo to rise next time, or −1 to recovery), and the Nth rise kills or retires the character, like Blades' 4th trauma. Make the player **declare the conviction before any roll** (commit blind). The DW Last Breath "Death's bargain" works as the 7–9 band.
- **Also add a time or team escalator that doesn't depend on damage** (13th Age), so the "Cosmo climax" arrives even in fights where nobody is badly hurt. That removes the incentive to get hurt just to reach the finale. Stall prevention: no advancement when players only defend.
- **Arc pacing:** consider a Fate-style "extreme consequence" equivalent (a Seventh Sense awakening) usable once per arc/milestone that rewrites an aspect. Canonically it is rare and transformative.

### Gaps
- No tabletop source was found that openly discusses players "getting hit on purpose" in their system. Reddit and Stack Exchange threads were unreachable, and the search budget was exhausted.
- I could not verify how Masks' Potential (XP on a miss) and label shifts interact with conditions, or how Marvel Heroic stress feeds the Doom Pool beyond 1s.

---

## 3. Localized damage and armor by body part (speed, ablation vs. sundering, repair)

### Takeaway
Three models exist:
- **True hit locations with per-location tracking** (GURPS, WFRP, BattleTech-style). Granular, but each hit needs an extra roll and table lookup.
- **Abstract HP with a "part breaks" table on threshold events** (Lancer). Fast: you roll for a broken part only when a structure box is lost, and the *player* picks which mount or system breaks.
- **Ablative armor boxes refreshed between missions** (Blades). Fastest, but not locational.

For five cloth parts with separate repair, the Lancer model (break a part only on big thresholds, player chooses which, repair from a limited pool) is the most play-tested fast option I found.

### Cited Findings
- **Lancer.** A part breaks only when structure is lost: "System Trauma… Roll 1d6. On a 1–3, all weapons on one mount of your choice are destroyed; on a 4–6, a system of your choice is destroyed… If there are no valid systems or weapons remaining, this result becomes a DIRECT HIT instead." — [Lancer Foundry en.json](https://github.com/Eranziel/foundryvtt-lancer/blob/master/public/lang/en.json)
- **Lancer repair economy.** "1 repair can: Refill HP to maximum; Repair a destroyed weapon or system." "Repair Capacity is equal to 4+HULL… If a pilot has no repairs left, they cannot repair their mech!" "Any weapons or systems that are destroyed remain so unless that mech spends its own repairs to fix them." A full repair needs "at least 10 hours of downtime in a secure location". — [Lancer CE damage.tex](https://github.com/AshleyMoni/Lancer-Community-Edition/blob/master/source/theMech/damage.tex)
- **Lancer escalating fragility.** Rolling 1d6 per marked structure and keeping the lowest means each additional break makes the next one likelier to be catastrophic. In the pre-release CRITICAL state, "When you take damage, you make a structure check." — [Lancer CE damage.tex](https://github.com/AshleyMoni/Lancer-Community-Edition/blob/master/source/theMech/damage.tex) (the CRITICAL state is pre-release wording; the final rules may differ)
- **Lancer Monstrosity table.** It gives body-part flavor without extra bookkeeping: "The attack blows a limb or chunk off the Monstrosity; it takes 1d6 KINETIC damage and becomes slow for the rest of the scene." — [Lancer Foundry en.json](https://github.com/Eranziel/foundryvtt-lancer/blob/master/public/lang/en.json)
- **GURPS.** A 3d6 location table with aiming penalties: Skull roll 3–4, −7; Face 5, −5; Right Leg 6–7, −2; Right Arm 8, −2; Torso 9–10, 0; Groin 11, −3; Left Arm 12, −2; Left Leg 13–14, −2; Hand 15, −4; Eyes −9; Vitals −3; "Arm, holding shield" −4. Crippling injury is a separate rule (Basic Set p. B420). — [GURPS Foundry hitlocation.js](https://github.com/crnormand/gurps/blob/main/module/hitlocation/hitlocation.js); [GURPS Foundry en.json](https://github.com/crnormand/gurps/blob/main/lang/en.json)
- **WFRP 4e.** Hit location costs no extra roll because the attack roll is reversed. The code swaps the d100's digits (e.g., 37 becomes 73) to find the location. — [WFRP4e Foundry test-wfrp4e.js](https://github.com/moo-man/WFRP4e-FoundryVTT/blob/master/src/system/rolls/test-wfrp4e.js)
- **WFRP house-rule example of armor ablation** (from the "Moo" house-rules module, **not core**): "Upon suffering a Critical Hit, for each AP in the location, the Critical Wound roll is reduced by 10… After the Critical Wound is resolved, the outermost layer of armor is damaged, its AP reduced by 1." — [WFRP4e Foundry en.json](https://github.com/moo-man/WFRP4e-FoundryVTT/blob/master/static/lang/en.json)
- **Blades armor ablation.** Mark a box to reduce harm by a level. Boxes are restored when choosing load for the next score. — [Blades SRD](https://github.com/amazingrando/blades-in-the-dark-srd-content/blob/main/Blades-in-the-Dark-SRD.md)
- **Fate "Armor".** Not locational. Toolkit adversaries get an "Armor rating or extra stress boxes" via stunts, and weaknesses or resistances are aspects. — [Fate Adversary Toolkit SRD](https://github.com/amazingrando/fate-srd/blob/main/docs/markdown/fate-adversary-toolkit.md)
- **Structure and stress as tracks.** Community discussion treats Lancer's structure/stress checks as a well-known pain point that people house-rule (e.g., alternative structure/stress and "brace" rules). — [Train Lightning house rules](https://trainlightning.com/house-rules-structure-overheating/); [Lancer CE issue #240](https://github.com/AshleyMoni/Lancer-Community-Edition/issues/240) (titles only; content not read)

### Inferences
- **Speed ranking (inference):** Blades armor boxes are fastest. Lancer is next: one table roll per structure loss, and the player chooses the part. WFRP reversal needs no extra roll but has per-location AP and crit tables. GURPS has an extra 3d6 and aiming penalties. Full per-location HP (BattleTech-style) is slowest.
- **For the cloth:** treat each part (helmet, chest, arms, legs, shield) as an ablative box that can absorb **one** hit tier, like Blades armor and Fate consequence slots. When absorbing, the *player* marks "Cracked", and a second hit marks "Shattered". A shattered part gives up its bonus until repaired from a limited pool: Lancer's Repair Cap maps nicely onto Mu of Jamir and blood. Let the player choose which part takes it, as Lancer's System Trauma does, and reserve a random or GM-chosen part only for special attacks.
- **Sundering vs. ablation:** the shield could use a "sacrifice to negate one hit" rule (sundering: break it to cancel a hit), while body parts use ablation (lose the bonus progressively). The Lancer rule "if nothing valid remains, escalate to DIRECT HIT" is a good model: when all cloth parts are broken, further breaks go to the body.
- **Anti-exploit for armor:** don't give Cosmo for cloth breaking. Otherwise players will prefer to let the cloth absorb hits for fuel. Or tie any Cosmo gain to the cloth failing *on a hit tier you chose to resist*.

### Gaps
- Could not verify (search budget exhausted, sites blocked): BattleTech / MechWarrior Destiny location tables; Mekton Zeta servo "kills" by location (*unverified recollection:* servos are head, torso, arms, legs, and so on, with weapons mounted in them lost when the servo is destroyed); Rolemaster, HârnMaster, and The Riddle of Steel location and crit mechanics; core WFRP4e armour-damage rules; The One Ring "smash shield"; the ShadowDark "shields shall be splintered" house rule; Shadow of the Demon Lord; Dragonbane weapon/shield durability on parry (*unverified recollection:* a parry that takes more damage than the item's durability breaks it until repaired).
- No playtime data was found comparing locational systems. The speed ranking above is inference.

---

## 4. Sense or condition tracks that grant compensatory benefits (precedent for the five senses)

### Takeaway
I found no system with a "lose a sense, sharpen the others" track. The closest verified precedents are:
- Harm that opens a supernatural channel (Apocalypse World's "life untenable → +1 weird").
- Negative conditions that pay a meta-currency when they cause trouble: a Fate "Blinded" aspect can be compelled for fate points, and Blades trauma gives XP when it causes trouble.
- A permanent identity-changing mark in exchange for staying in the fight (Fate extreme consequence).
- A power unlock that only works while in danger (the Lancer danger zone).

### Cited Findings
- **Apocalypse World.** When life becomes untenable, the options include "a bonus to weird" (weird is the psychic or supernatural stat), alongside −hard, a playbook change, or death. — [Troy Press](https://troypress.com/harm-systems-in-pbta-games/); [AW rules PDF](http://bignose.whitetree.org/tmp/apocalypse-world/rules-playbooks.pdf)
- **Fate: sense loss as a consequence that pays the victim.** "Temporary Blinding… places a Blinded aspect on a target, which could require them to get rid of the aspect with an overcome action before doing anything dependent on sight. Blinded might also present opportunities for a compel, so keep in mind that your opponent can take advantage of this to replenish fate points." "Temporarily Blinded" is listed as a mild consequence example. — [Fate Core SRD](https://github.com/amazingrando/fate-srd/blob/main/docs/markdown/fate-core.md)
- **Fate.** A consequence "is treated like any other aspect". Invokes against you by others pay you a FP at the end of the scene. — [Fate Core SRD](https://github.com/amazingrando/fate-srd/blob/main/docs/markdown/fate-core.md)
- **Blades.** Trauma conditions are permanent, and you "can earn xp by using it to cause trouble". — [Blades SRD](https://github.com/amazingrando/blades-in-the-dark-srd-content/blob/main/Blades-in-the-Dark-SRD.md)
- **Blades Cutter-style ability.** "Penalties from harm are one level less severe (though level 4 harm is still fatal)… Record the harm at its original level." This separates harm *recorded* from harm *penalty*, which is useful for a "senses lost but Cosmo compensates" rule. — [Blades SRD](https://github.com/amazingrando/blades-in-the-dark-srd-content/blob/main/Blades-in-the-Dark-SRD.md)
- **Masks.** Each condition penalizes a *specific* set of moves (−2), not everything. This is the structural model for "each sense lost hurts specific actions". — [Obsidian Portal, Effect of Conditions](https://masksanewgeneration-1.obsidianportal.com/wikis/effect-of-conditions)
- **Mouse Guard/Torchbearer.** Conditions recover in a fixed order, which could map to senses being lost and regained in canonical order. — [Firebroadside primer](https://firebroadside.blogspot.com/2018/07/a-mouse-guard-and-torchbearer-primer.html)
- **Lancer danger zone.** Talents that only work while at half heat or more, a rule of "power while imperiled". — [Lancer CE damage.tex](https://github.com/AshleyMoni/Lancer-Community-Edition/blob/master/source/theMech/damage.tex)
- **Tenra Bansho Zero.** The power currency (Kiai) accrues Karma toward a 108 threshold. This is a precedent for a "closer to transcendence / closer to the edge" track. — [Mythcreants](https://mythcreants.com/blog/tenra-bansho-zero-is-fun-insanity/)

### Inferences
- A **Five Senses track** could be built as Masks-style conditions (each sense lost gives −X to specific actions: sight to ranged/defense, hearing to reactions, and so on) plus a Fate-style compensation. Each lost sense (a) raises the Cosmo ceiling by one step and (b) is an aspect the GM can compel for Cosmo, as with Blinded.
- The **Seventh Sense** trigger could be a threshold on the senses track (e.g., 5 senses lost, or 3+ lost combined with invoking a conviction) that works like Fate's extreme consequence: once per arc, rewrites an aspect, and can't be recovered during the arc. That gives canon-appropriate rarity.
- Keep the "senses lost" track separate from HP. Senses are lost when the player **chooses** to resist lethal harm, not from arbitrary hits. This mirrors Blades, where you convert a consequence into a different cost by choice, and it closes the perverse-incentive loophole: the benefit only exists when the alternative was being taken out.

### Gaps
- No verified precedent was found for a literal "lose one sense, sharpen another" mechanic. Candidates not verified because of the exhausted search budget:
  - Call of Cthulhu, where maximum Sanity falls as Cthulhu Mythos (forbidden knowledge and power) rises (*unverified recollection:* max SAN = 99 − Mythos).
  - Delta Green "adapted to violence/helplessness" (*unverified:* immunity to one type of SAN loss at a stat or bond cost).
  - D&D blindsight and Blind-Fight feats.
  - Unknown Armies "hardened" madness notches.
- These are worth checking next.
