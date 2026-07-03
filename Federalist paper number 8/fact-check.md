# Federalist No. 8 — Fact-Check Log (Gate 4)

Episode 8 · "How Disunion Would Cost Us Our Freedom" · checked 2026-07-03

## Part A — Source & continuity check

### Mechanical quote verification
Every quoted / set-apart span and distinctive inline fragment was extracted and checked against `_production/source-texts/federalist-no-8.txt` with a normalized substring test (lowercased, whitespace collapsed, punctuation and curly/straight-quote & em-dash differences stripped). Script: `/tmp/qcheck_fed8.py`. **All 27 fragments returned EXACT.**

| # | Fragment (as delivered) | Result |
|---|-------------------------|--------|
| 1 | "to be more safe … become willing to run the risk of being less free" | ✅ EXACT (both clauses) |
| 2 | "necessitated to strengthen the executive arm of government" | ✅ EXACT |
| 3 | "acquire a progressive direction toward monarchy" | ✅ EXACT |
| 4 | "It is of the nature of war to increase the executive at the expense of the legislative authority." | ✅ EXACT |
| 5 | "a nation of soldiers" | ✅ EXACT |
| 6 | "absorbed in the pursuits of gain" | ✅ EXACT |
| 7 | "the same engines of despotism which have been the scourge of the Old World" | ✅ EXACT |
| 8 | "not only as their protectors, but as their superiors" | ✅ EXACT |
| 9 | "considering them masters … neither remote nor difficult" | ✅ EXACT |
| 10 | "an advantage similar to that of an insulated situation" | ✅ EXACT |
| 11 | "our liberties would be a prey to the means of defending ourselves against the ambition and jealousy of each other" | ✅ EXACT |
| 12 | "Safety from external danger is the most powerful director of national conduct" | ✅ EXACT |
| 13 | "even the ardent love of liberty will, after a time, give way to its dictates" | ✅ EXACT |
| 14 | "at this day … a victim to the absolute power of a single man" | ✅ EXACT |
| 15 | "desultory and predatory" | ✅ EXACT |
| 16 | "towns taken and retaken / battles that decide nothing / retreats more beneficial than victories / much effort and little acquisition" | ✅ EXACT (all four) |
| 17 | "the calamities of individuals" | ✅ EXACT |
| 18 | "PLUNDER and devastation" | ✅ EXACT |
| 19 | "airy phantoms that flit before … the imaginations of … its adversaries" | ✅ EXACT |
| 20 | "firm and solemn pause" | ✅ EXACT |
| 21 | "solid and weighty" | ✅ EXACT |
| 22 | "serious and mature consideration of every … honest man of whatever party" | ✅ EXACT |
| 23 | "not superficial or futile" | ✅ EXACT |

**One delivery note (not an error):** the headline sentence is spoken twice with light spoken-word glosses — once as "to be more safe, **nations** at length become willing…" (pronoun swapped from the source's "they") and once as "to be more safe, they become willing…" (drops "at length"). Both distinctive clauses are verbatim in the source; the meaning is faithful ("they" = nations). Flagged only so a human knows neither spoken rendering is a continuous word-for-word quotation.

**Source file:** clean; no transcription typos found in `federalist-no-8.txt` (matches Founders Online / Avalon).

### Authorship
Federalist No. 8 — **Alexander Hamilton** ✅. Matches `SERIES-STATUS.md` ("| 8 | … | Hamilton |") and the source header; confirmed by Founders Online (The Federalist No. 8, [20 November 1787]).

### Continuity references (checked against the actual earlier scripts)
| Reference in Ep 8 | Checked against | Result |
|-------------------|-----------------|--------|
| Opening recap of Fed 7's flashpoints — territory / Wyoming Valley, NY harbor tax on neighbors, public debt, Rhode Island paper money, foreign "labyrinth" | Episode 7 script | ✅ all present |
| "A war, not of parchment, but of the sword" attributed to the close of Fed 7 | Episode 7 script (L93) — verbatim there | ✅ (it is a Fed 7 line quoted as recap, not a Fed 8 quote) |
| "nothing men differ so readily about as the payment of money" (recap) | Episode 7 script (L73) | ✅ |
| Closing arc: Fed 6 = divided America would fight itself (philosophical case); Fed 7 = named the specifics | Episodes 6 & 7 scripts | ✅ |
| Fed 9 teaser: still Hamilton; answers the "republics are fragile / faction & instability" objection using ancient Greece & Italy; "science of politics" has advanced; union as the cure that lets a republic survive | Federalist No. 9 (Wikipedia; American Presidency Project) | ✅ accurate |

## Part B — Web cross-check

| # | Claim in script | Verdict | Source(s) |
|---|-----------------|---------|-----------|
| 1 | Fed 8 published in the New-York Packet, November 20, 1787, by Hamilton | ✅ verified | [Founders Online](https://founders.archives.gov/documents/Hamilton/01-04-02-0160); [Wikipedia](https://en.wikipedia.org/wiki/Federalist_No._8) |
| 2 | England's monarchy restored in the 1660s after a civil war and a republic; Charles II kept a small permanent paid force around the crown in peacetime; England's tradition was a militia | ✅ verified | [National Army Museum — Restoration & birth of the British Army](https://www.nam.ac.uk/explore/restoration-and-birth-british-army) (Charles raised ~5,000 "King's Guards and Garrisons," 1660–61; militia re-established as counterweight); [Militia (England), Wikipedia](https://en.wikipedia.org/wiki/Militia_(England)) |
| 3 | James II was openly Catholic in a Protestant country; expanded the peacetime army to ~20,000; camped a good part of it just outside London at Hounslow Heath, understood as intimidation, not defense | ✅ verified | [Historic UK — Camp on Hounslow Heath](https://www.historic-uk.com/HistoryMagazine/DestinationsUK/Hounslow-Heath/); [National Army Museum — Glorious Revolution](https://www.nam.ac.uk/explore/army-and-glorious-revolution). *Note:* army-size estimates vary by year (≈8,500 at accession → ~20,000 mid-reign → ~34,000 by 1688; Hounslow reviews cited at 13,000–25,000). Script's hedged "something like twenty thousand … a good part of it" at Hounslow is a fair representative figure. |
| 4 | Glorious Revolution, 1688: James's officers/subjects abandoned him, he fled to France, Parliament handed the crown to William and Mary on new terms | ✅ verified | [The National Archives — Glorious Revolution](https://www.nationalarchives.gov.uk/education/resources/glorious-revolution/); [Britannica](https://www.britannica.com/event/Glorious-Revolution) (Churchill & other generals defected; James fled 23 Dec 1688; William & Mary accepted the throne with the Declaration of Rights) |
| 5 | The English Bill of Rights (1689) explicitly barred the king from keeping a standing army in peacetime without Parliament's consent | ✅ verified | [Bill of Rights 1689, Wikipedia](https://en.wikipedia.org/wiki/Bill_of_Rights_1689); [Avalon Project — English Bill of Rights](https://avalon.law.yale.edu/17th_century/england.asp) ("raising or keeping a standing army within the kingdom in time of peace, unless it be with consent of Parliament, is against law") |
| 6 | That memory was "less than a hundred years old" to Americans in 1787 | ✅ verified | 1689 → 1787 ≈ 98 years (arithmetic on #5) |
| 7 | "closer to them than the Second World War is to us" | ⚠️ imprecise | The Glorious Revolution (1688–89) sits ~98–99 yrs before 1787; WWII (ended 1945) sits ~81 yrs before a 2026 listener. So the memory was actually a bit **further** from Hamilton's readers than WWII is from us — the "closer" comparison is directionally reversed. Rhetorical proximity aid, not load-bearing to the argument. |
| 8 | Anti-Federalists were already objecting that the Constitution did not clearly forbid a standing army | ✅ verified | The paper itself ("Standing armies, it is said, are not provided against in the new Constitution"); a standard Anti-Federalist objection — [Federalist No. 8, Ballotpedia](https://ballotpedia.org/Federalist_No._8_by_Alexander_Hamilton_(1787)) |
| 9 | Eisenhower's farewell address, January 1961; he had been supreme allied commander in Europe in WWII and a five-star general; warned against the "military-industrial complex," its "unwarranted influence," and that "the potential for the disastrous rise of misplaced power exists and will persist"; a permanent armaments industry of vast proportions and a defense establishment of millions | ✅ verified | [National Archives — Eisenhower Farewell Address (1961)](https://www.archives.gov/milestone-documents/president-dwight-d-eisenhowers-farewell-address); [Avalon Project — Military-Industrial Complex Speech](https://avalon.law.yale.edu/20th_century/eisenhower001.asp) (delivered Jan 17, 1961; quoted phrases verbatim; "three and a half million men and women … directly engaged in the defense establishment") |
| 10 | Britain stayed comparatively free because its island situation + powerful navy meant it never needed a large peacetime home army | ✅ verified (Hamilton's own argument, historically grounded) | Hamilton's thesis in Fed 8; consistent with the standing-army history above — [English resistance to a standing army, Wikipedia](https://en.wikipedia.org/wiki/Standing_army_(Great_Britain)); [Avalon Project — English Bill of Rights](https://avalon.law.yale.edu/17th_century/england.asp) |
| 11 | Fed 9 teaser (next paper, still Hamilton): counters the "ancient republics were fragile / faction & instability" objection; argues the science of politics has advanced and a well-built union lets a republic survive its internal storms | ✅ verified | [Federalist No. 9, Wikipedia](https://en.wikipedia.org/wiki/Federalist_No._9); [American Presidency Project — Federalist No. 9](https://www.presidency.ucsb.edu/documents/federalist-no-9-the-utility-the-union-safeguard-against-domestic-faction-and-insurrection) |

## Result

- ✅ verified: **10** web claims (plus all 27 source quotes EXACT, authorship, and all continuity references)
- ⚠️ contested/imprecise: **1** (the "closer than WWII" proximity aside — direction reversed; non-load-bearing)
- ❌ wrong: **0**

**Gate 4: PASS.** No factual errors. The one ⚠️ is a minor rhetorical comparison a human may wish to soften; it does not affect Hamilton's argument. Audio is already produced — any fix is the human's call.
