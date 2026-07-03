# Fact-Check Log — Episode 18 (Federalist No. 18)

Gate 4 of the production workflow. Two parts: (A) source + continuity check against the authoritative source text; (B) web cross-check of every non-quote factual claim, two independent sources required for load-bearing claims.

**Outcome: 0 wrong, 0 contested-left-unhedged. All quotes exact. All claims ✅ verified, with honest hedges built into the script wherever a source flagged a precision or interpretive nuance. Gate 4: PASS.**

---

## Part A — Source & continuity check

**Authority:** `_production/source-texts/federalist-no-18.txt` (Hamilton and Madison, Federalist No. 18). Built from the Yale Avalon transcription, with two obvious Avalon typos corrected against the standard text ("weakenened" → "weakened"; "vicissitudes convulsions" → "vicissitudes, convulsions").

### Quote verification (mechanical, normalized-substring against the source)
Every phrase the script presents as the paper's own words was verified as an exact normalized substring of the source file (case/punctuation-insensitive). All passed.

| # | Quote (as spoken) | Type | Verdict |
|---|---|---|---|
| 1 | "In theory, and upon paper, this apparatus of powers seems amply sufficient for all general purposes." | set-apart | ✅ exact |
| 2 | "Had Greece, says a judicious observer on her fate, been united by a stricter confederation, and persevered in her union, she would never have worn the chains of Macedon; and might have proved a barrier to the vast projects of Rome." | set-apart | ✅ exact |
| 3 | "The popular government, which was so tempestuous elsewhere, caused no disorders in the members of the Achaean republic, because it was there tempered by the general authority and laws of the confederacy." | set-apart | ✅ exact |
| 4 | "A victorious and powerful ally is but another name for a master." | set-apart | ✅ exact |
| 5 | "By these arts this union, the last hope of Greece, the last hope of ancient liberty, was torn into pieces." | set-apart | ✅ exact |
| 6 | "the tendency of federal bodies rather to anarchy among the members, than to tyranny in the head." | set-apart | ✅ exact |
| — | "Very different ... was the experiment from the theory" | inline | ✅ exact |
| — | "satellites of the orbs of primary magnitude" | inline | ✅ exact |
| — | "infinitely more mischief than they had suffered from Xerxes" | inline | ✅ exact |
| — | "made little figure" | inline | ✅ exact |
| — | "a fatal damp" | inline | ✅ exact |
| — | "mercenary instruments" | inline | ✅ exact |
| — | "proclaimed universal liberty throughout Greece" | inline | ✅ exact |
| — | "loaded with chains" / "under which it is groaning at this hour" | inline | ✅ exact |
| — | "the arbiter of Greece" | inline | ✅ exact |

Set-apart stop-and-explain quotes: **6** (ceiling is 8; target 4–6). ✅

### Paraphrase fidelity
- The episode's spine — (1) paper-power vs. real power; (2) a weak center lets the strong members bully the weak; (3) a divided league is an open door for a foreign predator (Philip, then Rome); (4) the tighter Achaean union produced *better* domestic government; (5) the closing verdict that confederacies tend to anarchy among the members, not tyranny in the head — is all faithful to the paper. ✅
- The structural diagnosis the host foregrounds (the league acted on member cities through deputies who answered to the cities, not on individuals) is faithful to the paper's own sentence ("administered by deputies appointed wholly by the cities in their political capacities; and exercised over them in the same capacities") and is the correct tie-back to Episodes 15–16. ✅

### Authorship & continuity
- Authorship: **Hamilton and Madison** (joint attribution under "Publius"). Modern scholarly consensus: Madison was the principal author of Nos. 18–20, with Hamilton's exact contribution debated. The script states "the modern view of historians is that Madison did most of the actual writing here, with Hamilton helping" — does **not** claim equal co-authorship and does **not** assert the traditional "merged notes" story as settled. ✅
- Continuity callbacks checked against the actual earlier scripts:
  - Ep 17: the closing promissory note ("a concise review of the events that have attended confederate governments… shall form the subject of some ensuing papers") and the "jealousy a direction to the wrong side" line — both accurate; Ep 17's teaser explicitly set up this episode (Greece, Hamilton + Madison together). ✅
  - Ep 15–16: the "law acts on states/cities, not individuals" disease — accurate and genuinely the paper's diagnosis. ✅
  - Ep 6: Hamilton blamed the Peloponnesian War partly on Pericles' private grudges — accurate to the Ep 6 script. ✅
  - Ep 5 (Jay: foreign fleets easier to receive than remove) and Ep 7 ("pernicious labyrinths"; "divide et impera") — accurate callbacks. ✅
  - Madison wrote No. 10 and No. 14 (he was not new to the project) — matches `SERIES-STATUS.md`. ✅
  - Forward teaser to No. 19 (Hamilton + Madison, the Holy Roman / Germanic confederacy and the Swiss cantons) — accurate; No. 19 covers the Germanic empire and Switzerland. ✅

---

## Part B — Web cross-check (every non-quote factual claim)

Three independent background researchers cross-checked the publication/authorship cluster, the Amphictyonic/classical-Greek cluster, and the Achaean-League/Rome cluster. Two independent high-quality sources required for every load-bearing claim. **No claim returned WRONG.** Every flagged nuance was reworded into the script (see "Hedges applied" below).

### Cluster 1 — Publication, authorship, Madison's research, modern parallel

| # | Claim | Verdict | Sources |
|---|---|---|---|
| 1 | First published early December 1787 (dated Dec 7; New-York Packet Dec 7, Independent Journal Dec 8) | ✅ verified | founders.archives.gov/documents/Hamilton/01-04-02-0175 ; archive.csac.history.wisc.edu/18.pdf |
| 2 | Nos. 18–20 jointly attributed to Hamilton and Madison; modern consensus = Madison principal author, Hamilton assisted (exact share debated) | ✅ verified (live scholarly nuance) | en.wikipedia.org/wiki/The_Federalist_Papers ; founders.archives.gov/documents/Madison/01-10-02-0177 |
| 3 | Madison wrote No. 10 (Nov 22, 1787) and No. 14 (Nov 30, 1787), before No. 18 | ✅ verified | en.wikipedia.org/wiki/Federalist_No._10 ; lva.virginia.gov (Federalist No. 10) |
| 4 | Madison's pre-Convention research "Notes on Ancient and Modern Confederacies" (1786); Jefferson, in Paris, shipped him European books | ✅ verified | founders.archives.gov/documents/Madison/01-09-02-0001 ; contextus.org (Notes on Ancient and Modern Confederacies) |
| 5 | League of Nations (founded 1920): collective security on paper, acted on member states, could not compel them, failed against 1930s aggression | ✅ verified | en.wikipedia.org/wiki/League_of_Nations ; e-ir.info (Manchurian & Abyssinian crises) |

### Cluster 2 — Amphictyonic Council & classical Greece

| # | Claim | Verdict | Sources |
|---|---|---|---|
| 1 | Amphictyonic Council = association of Greek peoples/states, guardian of the Delphi sanctuary of Apollo, votes in a common council, members retained independence | ✅ verified | britannica.com/topic/Amphictyonic-League ; worldhistory.org/Amphictyonic_League |
| 2 | Broad powers in principle (managed Delphi, oath-bound mutual obligations, could in theory coordinate/discipline) but in practice captured by the strongest members | ✅ verified | en.wikisource.org (EB 9th ed., "Amphictyony") ; worldhistory.org/Amphictyonic_League |
| 3 | Hegemony passed Athens → Sparta → Thebes | ✅ verified (sequence); ancient year-counts treated as the sources' figures | en.wikipedia.org/wiki/Spartan_hegemony ; Demosthenes, Third Philippic §23 |
| 4 | Battle of Leuctra (371 BC): Thebes under Epaminondas broke Spartan dominance | ✅ verified | en.wikipedia.org/wiki/Battle_of_Leuctra ; thecollector.com (Leuctra) |
| 5 | Greeks united vs. Xerxes (480 BC); Athens/Sparta rivalry → Peloponnesian War (431–404 BC) → defeat of Athens | ✅ verified (war-guilt hedged) | en.wikipedia.org/wiki/Peloponnesian_War ; en.wikipedia.org/wiki/Second_Persian_invasion_of_Greece |
| 6 | Third Sacred War: Phocians farmed sacred Delphic land, fined, refused; drew in Philip II, who gained the Phocian Council seats (346 BC) and mastered Greece (sealed at Chaeronea, 338 BC) | ✅ verified | en.wikipedia.org/wiki/Third_Sacred_War ; en.wikipedia.org/wiki/Battle_of_Chaeronea_(338_BC) |

### Cluster 3 — Achaean League & Rome

| # | Claim | Verdict | Sources |
|---|---|---|---|
| 1 | Achaean League = a true political/military federation (Peloponnese), more centralized than the Amphictyony; federal council + elected general ("strategos"; the paper's "praetor"); two magistrates, later one | ✅ verified | britannica.com/topic/Achaean-League ; en.wikipedia.org/wiki/Achaean_League |
| 2 | Members shared common laws/usages, weights, measures, coinage; degree of federal compulsion uncertain | ✅ verified (Madison's own caveat kept) | Polybius 2.37 (politeia.unimi.it) ; founders.archives.gov (Fed. 18) |
| 3 | Philopoemen brought Sparta in; abolition of the Lycurgan institutions (c. 188 BC) | ✅ verified | en.wikipedia.org/wiki/Philopoemen ; Oxford Classical Dictionary (Lycurgus) |
| 4 | Cleomenean War; league called in Macedon (Antigonus III Doson); Cleomenes defeated at Sellasia (222 BC); Macedonian influence grew (price = Acrocorinth) | ✅ verified | en.wikipedia.org/wiki/Cleomenean_War ; en.wikipedia.org/wiki/Battle_of_Sellasia |
| 5 | Rome defeated Philip V (Second Macedonian War, Cynoscephalae 197 BC); Achaeans allied with Rome (causation softened — Rome drawn in chiefly by Pergamon/Rhodes/Athens) | ✅ verified | en.wikipedia.org/wiki/Titus_Quinctius_Flamininus ; britannica.com/biography/Titus-Quinctius-Flamininus |
| 6 | Flamininus proclaimed the "freedom of the Greeks" at the Isthmian Games, 196 BC; functioned as freedom on Rome's terms (interpretation, not bare fact) | ✅ verified | britannica.com/biography/Titus-Quinctius-Flamininus ; Livy 33.33 (judaism-and-rome.org) |
| 7 | Callicrates = mid-2nd-c. BC Achaean leader who advanced Roman interests (reputation largely from his rival Polybius) | ✅ verified | Oxford Classical Dictionary (Callicrates) ; imperiumromanum.pl (Callicrates) |
| 8 | Rome crushed and dissolved the league in the Achaean War of 146 BC; Mummius sacked Corinth; Greece under Roman domination | ✅ verified | en.wikipedia.org/wiki/Achaean_War ; britannica.com/biography/Lucius-Mummius |
| 9 | In 1787 Greece was under Ottoman rule (since 1453); independence not until 1821–1832 — a 1780s writer could call Greece "in chains" | ✅ verified | britannica.com/event/War-of-Greek-Independence ; en.wikipedia.org/wiki/Greek_War_of_Independence |

### Hedges deliberately built into the script (per fact-checker precision notes)
- **Publication:** "the New York newspapers in the first week of December" — does not pin a single paper.
- **Authorship:** "Madison did most of the actual writing here, with Hamilton helping" — no equal-co-author claim, no "merged notes" assertion.
- **Madison's books:** "Jefferson… had been shipping him crate after crate of books" — a steady supply, not a single targeted order for this project.
- **League of Nations:** "had its small successes in the calm of the nineteen twenties," then "Helpless when it mattered most" — not "never worked."
- **Year-counts:** Athens's dominance given as "the count he borrows from… Demosthenes" and rounded to "some seventy years" (Madison's "73" differs from the surviving Demosthenes "75").
- **Peloponnesian War guilt:** "the city whose own ambition had done so much to bring it on" — not "the city that started it" (responsibility is genuinely contested).
- **Philip's method:** "by intrigue and bribery first, and by the sword when it came to that" — does not deny his battlefield victories (Chaeronea).
- **"Praetor":** flagged as Madison "reaching for a Roman word" (the Greek title was *strategos*).
- **Achaean common laws/money:** Madison's own caveat preserved ("we cannot be sure how much of that the league actually compelled").
- **Achaeans + Rome:** "As Madison tells the story, they threw in with Rome and helped draw Roman power deeper into Greece" — softened from a sole "they summoned Rome."
- **Rome's "universal liberty":** "freedom on Rome's terms — which is to say, it was also a weapon" — the "tool of control" reading presented as interpretation, not bare fact; the manipulation of cities framed as flattery, not a factual "lie."
- **Callicrates:** kept Madison's verified phrase "mercenary instruments," glossed as "bought men," dropping the loaded "traitor."

**All claims ✅ verified. Gate 4: PASS.**
