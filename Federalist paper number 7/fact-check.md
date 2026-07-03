# Federalist No. 7 — Fact-Check Log (Gate 4)

Episode 7 · "What Would They Actually Fight About?" · checked 2026-07-03

## Part A — Source & continuity check

### Mechanical quote verification
Every quoted/lifted span and distinctive inline fragment was checked by normalized substring containment (lowercase, collapsed whitespace, normalized quotes/dashes) against the full canonical text of Federalist No. 7 (constitution.org / Avalon / Founders Online). The compiled reference at `_production/source-texts/federalist-no-7.txt` is only a partial compilation, so verification was run against the complete essay.

| # | Quote (first words) | Result |
|---|---------------------|--------|
| 1 | "...deluded in blood all the nations in the world" | ⚠️ ONE-WORD MISMATCH — canonical is **"deluged in blood"** (see below) |
| 2 | "Territorial disputes have at all times been found one of the most fertile sources of hostility among nations" | ✅ EXACT |
| 3 | "prevailing upon the States to make cessions to the United States for the benefit of the whole" | ✅ EXACT |
| 4 | "gave strong indications of dissatisfaction" | ✅ EXACT |
| 5 | "The competitions of commerce would be another fruitful source of contention" | ✅ EXACT |
| 6 | "New York, from the necessities of revenue, must lay duties on her importations" | ✅ EXACT |
| 7 | "A great part of these duties must be paid by the inhabitants of the two other States in the capacity of consumers" | ✅ EXACT |
| 8 | "Would Connecticut and New Jersey long submit to be taxed by New York for her exclusive benefit?" | ✅ EXACT |
| 9 | "we should be ready to denominate injuries those things which were in reality the justifiable acts of independent sovereignties consulting a distinct interest" | ✅ EXACT |
| 10 | "The apportionment, in the first instance, and the progressive extinguishment, afterwards, would be alike productive of ill-humor and animosity" | ⚠️ minor variant — canonical reads "extinguishment **afterward**" (no comma, no "s"); matches the source-text file |
| 11 | "there is nothing men differ so readily about ... as the payment of money" | ✅ EXACT |
| 12 | "we have observed the disposition to retaliation excited in Connecticut, in consequence of the enormities perpetrated by the legislature of Rhode Island" | ✅ EXACT (script adds one comma; wording verbatim) |
| 13 | "a war, not of parchment, but of the sword, would chastise such atrocious breaches of moral obligation" | ✅ EXACT |
| 14 | "entangled in all the pernicious labyrinths of European politics and wars" | ✅ EXACT |
| 15 | "divide et impera must be the motto of every nation that either hates or fears us" | ✅ EXACT (canonical sets *Divide et impera* in quotation marks) |

**Quote flag (⚠️):** The script's near-verbatim line "the same inducements which have, at different times, **deluded** in blood all the nations in the world" reproduces a one-word error. Hamilton's canonical wording is "**deluged** in blood" (i.e., *drenched/flooded* in blood — the correct sense). "Deluded in blood" does not parse. The error is inherited verbatim from the compiled reference `_production/source-texts/federalist-no-7.txt` (line 11). The line is narrated, not set apart in quotation marks, so it is not audio-critical, but the wording is factually wrong. Confirmed against Founders Online, Avalon, and constitution.org.

### Authorship
Federalist No. 7 — **Hamilton** ✅. Matches `SERIES-STATUS.md` ("7. Hamilton") and the source header, Founders Online, and Avalon.

### Continuity references checked against actual prior scripts
| Reference | Checked against | Result |
|-----------|-----------------|--------|
| Ep 6 recap: philosophical case, examples from ancient Athens, Tudor England, courts of Louis XIV and XV, Shays' Rebellion; "neighboring states are natural enemies unless bound in a confederate republic" | Episode 6 script | ✅ All present (Pericles/Athens, Wolsey/Henry VIII, Mme de Maintenon/Louis XIV, Mme de Pompadour/Louis XV, Shays; natural-enemies quote) |
| Ep 6 callback: republics/commercial republics still fight — "Greece, Rome, Carthage, Venice, Holland, and Britain" | Episode 6 script | ✅ All six covered in Ep 6 |
| Fed 8 teaser: Hamilton next turns to standing armies and the cost of disunion to liberty | Federalist No. 8 (Hamilton, standing armies) | ✅ Accurate preview |

### Source note
`_production/source-texts/federalist-no-7.txt` carries two inaccuracies that flow into the script: (1) "deluded in blood" for canonical "deluged in blood" (see quote flag); (2) the header "From the New-York Packet, November 15, 1787" (see Part B #1). Neither file was edited — audio is already produced; documented here for the human's decision.

## Part B — Web cross-check

| # | Claim in script | Verdict | Source(s) |
|---|-----------------|---------|-----------|
| 1 | Federalist No. 7 published in the New-York Packet on November 15, 1787 | ⚠️ inaccurate | First documented publication was the **Independent Journal, Nov 17, 1787**; reprinted Daily Advertiser Nov 19 and **New-York Packet Nov 20**. Nov 15 was a Tuesday and matches no authoritative record (only an outlier Ballotpedia note). "New-York Packet, Nov 15" reflects a traditional but bibliographically incorrect masthead. [Founders Online](https://founders.archives.gov/documents/Hamilton/01-04-02-0159); [Wikipedia](https://en.wikipedia.org/wiki/Federalist_No._7) |
| 2 | Territorial disputes are one of the most fertile sources of war; several states hold overlapping colonial "crown land" charters running west to the Mississippi and in a few cases (on paper) to the Pacific | ✅ verified | Connecticut's 1662 charter ran "to the South Sea" (Pacific); Virginia/Massachusetts held sea-to-sea claims. [Encyclopedia.com – Wyoming Valley](https://www.encyclopedia.com/defense/energy-government-and-defense-magazines/wyoming-valley-conflict); Federalist No. 7 text |
| 3 | Congress "wisely quieted" the western-lands question by getting states to cede claims to the U.S.; Virginia's cession (now Ohio/upper Midwest) was most important; this became the Northwest Territory | ✅ verified | Virginia authorized cession Dec 20, 1783; Congress accepted Mar 1, 1784; created the Northwest Territory, organized by the Northwest Ordinance (1787). [House History](https://history.house.gov/HouseRecord/Detail/25769819762); [Northwest Territory (Wikipedia)](https://en.wikipedia.org/wiki/Northwest_Territory) |
| 4 | Wyoming Valley: fertile land on the Susquehanna in NE Pennsylvania, claimed by both Connecticut and Pennsylvania under colonial charters; settlers fought with loss of life; a federal court at Trenton ruled for Pennsylvania in 1782; Connecticut was dissatisfied and only accepted after settlers were compensated | ✅ verified | Decree of Trenton, Dec 30, 1782 (first interstate adjudication under Art. IX) awarded the valley to Pennsylvania; Pennamite–Yankee Wars (1769–99); Connecticut held back the Western Reserve as an equivalent and PA's 1787 Confirming Act addressed settlers. [Articles of Confederation – Decree of Trenton](https://www.articlesofconfederation.com/p/1782-ct-vs-pa.html); [Pennamite–Yankee Wars](https://grokipedia.com/page/Pennamite%E2%80%93Yankee_War) |
| 5 | Vermont in 1787 was not a state but a disputed region; New York claimed it, its settlers considered themselves independent; New Hampshire, Massachusetts, and Connecticut encouraged its separation out of jealousy of New York's power | ✅ verified | Vermont Republic 1777–1791 (de facto independent, Green Mountain Boys resisted NY); admitted as a state Mar 4, 1791; neighboring claimant states were "more solicitous to dismember" NY (Hamilton's own account). [Vermont Republic (Wikipedia)](https://en.wikipedia.org/wiki/Vermont_Republic); [Partition and secession in New York](https://en.wikipedia.org/wiki/Partition_and_secession_in_New_York) |
| 6 | Commercial rivalry: New York taxes imports through its port, and consumers in New Jersey and Connecticut ultimately pay the duty; neighbors would not long submit | ✅ verified | Faithful rendering of Hamilton's New York / New Jersey / Connecticut duties argument. Federalist No. 7 text (Founders Online) |
| 7 | The Revolutionary War left an enormous shared debt, much owed to foreign lenders (especially the Dutch and the French) plus domestic creditors; apportioning and paying it would breed animosity | ✅ verified | France, Spain, and the Dutch lent the U.S. >$10M; U.S. stopped interest to France in 1785 and defaulted on installments due 1787; domestic "loan office certificates" owed to citizens. [U.S. State Dept – Debt and Foreign Loans 1775–1795](https://history.state.gov/milestones/1784-1800/loans) |
| 8 | Rhode Island (mid-1780s) issued large amounts of depreciated paper money and passed laws forcing creditors to accept it at face value; courts treated debts as paid and punished refusing creditors; Connecticut showed a disposition to retaliate | ✅ verified | May 1786 £100,000 emission; June 1786 force act (£100 fine, escalating) and Aug 1786 summary trial without jury; *Trevett v. Weeden* (Newport, Sept 1786). [Trevett v. Weeden (Wikipedia)](https://en.wikipedia.org/wiki/Trevett_v._Weeden); [Small State Big History](https://smallstatebighistory.com/the-story-behind-rhode-islands-most-important-legal-case-trevett-v-weeden-in-1786/) |
| 9 | Foreign entanglement: separate confederacies would seek European allies and be drawn "into the pernicious labyrinths of European politics and wars" | ✅ verified | Faithful to Hamilton's argument and text. Federalist No. 7 (Founders Online) |
| 10 | "Divide et impera" is an old Roman/European political maxim (divide and rule/conquer) | ✅ verified | Standard attribution; Hamilton quotes it verbatim to close the essay. |
| 11 | Modern parallel — when the Soviet Union dissolved, successor states fought almost immediately over border territory and over Soviet-era debt | ✅ verified | Post-1991 armed conflicts over territory (Nagorno-Karabakh, Transnistria, Georgia); Soviet debt/asset apportionment was a serious dispute settled by the 1993 "zero option" (Russia took all debt + assets), which Ukraine still has not ratified. *Note:* the debt dimension was a negotiated dispute rather than armed conflict — "fought" here reads as "quarreled," consistent with Hamilton's point about apportionment disputes. [Succession of the Soviet Union](https://en.wikipedia.org/wiki/Succession_of_the_Soviet_Union) |
| 12 | Modern parallel — Yugoslavia's dissolution reproduced Hamilton's fault lines: ethnic regions claimed by multiple successor states, commercial access to ports, inherited debts, and outside powers picking sides | ✅ verified | Well-documented (Krajina/Bosnia territorial claims; Adriatic port/Prevlaka disputes; SFRY debt-succession negotiations; early German recognition of Croatia/Slovenia, Russian sympathy for Serbia). [Breakup of Yugoslavia (Wikipedia)](https://en.wikipedia.org/wiki/Breakup_of_Yugoslavia) |
| 13 | Modern parallel — when Sudan split in 2011, the two new countries almost immediately fought over oil-revenue apportionment | ✅ verified | South Sudan independent July 9, 2011; oil transit-fee dispute led Juba to shut down production in Jan 2012; the Heglig Crisis (armed clashes) followed in 2012, resolved by a Sept 26, 2012 agreement. [Heglig Crisis (Wikipedia)](https://en.wikipedia.org/wiki/Heglig_Crisis) |

## Result

- ✅ verified: 12 of 13 web-checked claims; authorship correct; Ep 6 continuity fully consistent; 13 of 15 quoted spans verbatim (two others verbatim apart from punctuation).
- ⚠️ flagged: **2**
  - **Quote wording** — script says "**deluded** in blood all the nations in the world"; Hamilton wrote "**deluged** in blood." One-word error inherited from the source-text file; narrated (not a set-apart quotation), so not audio-critical, but factually incorrect.
  - **Publication line** — script says "published in the New-York Packet on November 15, 1787." First documented publication was the **Independent Journal, Nov 17, 1787**; the New-York Packet carried it as a reprint on **Nov 20**. Traditional-masthead artifact; does not distort the argument.
- ❌ errors: **0**

Every substantive historical claim, named event/place, and modern parallel checks out and none distort Hamilton's argument. The two ⚠️ items are wording/attribution inaccuracies, both inherited from `_production/source-texts/federalist-no-7.txt`, neither affecting the essay's meaning.

**Gate 4: PASS (with two minor ⚠️ flags noted above; audio already produced, fixes at the human's discretion).**
