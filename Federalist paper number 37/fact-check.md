# Fact-check — Episode 37 (Federalist No. 37)

Script: `federalist-no-37-script.txt`
Source of record for quotes: `_production/source-texts/federalist-no-37.txt` (Yale Avalon transcription)

**Result: 17/17 quote verifications pass. 56 external claims checked: 51 ✅ verified, 5 ⚠️ fairly hedged, 0 ❌ wrong.**

As with Episodes 34, 35 and 36, the load-bearing history was researched *before* drafting. No external claim required a fix-and-sweep. Four precision errors and one overstatement were caught by the internal-consistency sweep and by re-reading the source texts; all are logged below with their sweeps.

---

## Part A — Source and continuity check

### A1. Quote verification (mechanical)

Method: Unicode NFKD normalisation, smart quotes folded, hyphens and dashes to space, non-alphanumerics stripped, lowercased, whitespace collapsed, then substring test against the source file. Not verified by eye, and not verified against the web (a web transcription can be worse than the source file).

**Six substantial set-apart quotes:**

| # | Quote (opening words) | Verdict |
|---|---|---|
| 1 | "can therefore furnish no other light than that of beacons, which give warning of the course to be shunned…" | ✅ exact |
| 2 | "Here, then, are three sources of vague and incorrect definitions… indistinctness of the object, imperfection of the organ of conception, inadequateness of the vehicle of ideas." | ✅ exact |
| 3 | "But no language is so copious as to supply words and phrases for every complex idea…" | ✅ exact |
| 4 | "When the Almighty himself condescends to address mankind in their own language…" | ✅ exact |
| 5 | "All new laws, though penned with the greatest technical skill… liquidated and ascertained by a series of particular discussions and adjudications." | ✅ exact |
| 6 | "The real wonder is that so many difficulties should have been surmounted, and surmounted with a unanimity…" | ✅ exact |

**Eleven inline fragments:** "a faultless plan was not to be expected"; "Not less arduous"; "such delicate shades and minute gradations that their boundaries have eluded the most subtle investigations"; "the medium through which the conceptions of men are conveyed to each other adds a fresh embarrassment"; "the vicissitudes and uncertainties which characterize the State administrations"; "the interfering pretensions of the larger and smaller States"; "Other combinations, resulting from a difference of local position and policy"; "sacrifice theoretical propriety to the force of extraneous considerations"; "a finger of that Almighty hand"; "Sense, perception, judgment, desire, volition, memory, imagination"; and the three-source list. **All ✅ exact against the source file.**

**Disclosed modifications (five, all non-substantive except where noted):**
1. Quote 2 is repunctuated for TTS — the source colon-and-comma list is rendered as four sentences. Wording unchanged.
2. Quote 6, the "medium" fragment, the "interfering pretensions" fragment and the "Other combinations" fragment each have an attribution phrase inserted mid-sentence ("he writes" / "he calls them"). Wording otherwise unchanged.
3. **Substantive, and deliberate:** Madison's list of mental faculties is rendered in the host's voice as "Sense, perception, judgment, desire, **will**, memory, imagination." The source reads "volition." This is spoken as the host's own plain-English list, not as a quotation, and "will" is the ordinary modern rendering of "volition." Flagged here because it is a word change, not punctuation.
4. The Chiafalo quotation renders the opinion's ampersands ("liquidate & settle", "terms & phrases") as "and" for TTS.
5. Madison's convention-notes line expands his manuscript abbreviation "adjourng." to "adjourning." No other change: "After several unsuccessful attempts for silently postponing the matter by adjourning, the adjournment was at length carried, without any vote on the motion."

**Not quoted:** Madison's preface sentence about never missing a day is delivered as reported speech in the third person ("He was not absent a single day, he tells us…"), not as a first-person quotation. The original reads "It happened, also, that I was not absent a single day, nor more than a casual fraction of an hour in any day, so that I could not have lost a single speech, unless a very short one."

**Source defect noted, not quoted:** the Avalon transcription of No. 37 contains an OCR error — "which marks the *ermination* of the former" (for "termination"). Nothing in the script quotes that sentence.

### A2. Authorship and continuity

| Claim | Verdict |
|---|---|
| No. 37 is Madison's, published in the Daily Advertiser, 11 January 1788 | ✅ source header; matches `SERIES-STATUS.md` |
| No. 38 is Madison's, New York Packet, 15 January 1788 | ✅ verified by transcribing the source (see below) |
| Ep 36 covered Hamilton's last paper and his incentives-not-intentions move | ✅ checked against `federalist-no-36-script.txt` |
| Hamilton's run was fourteen essays (Nos. 23–36), of which seven were on money (Nos. 30–36) | ✅ matches Ep 36's own closing statement |
| Episodes 18, 19 and 20 walked through the ancient and modern confederacies; Ep 20 was the Dutch republic | ✅ checked against those scripts and their metadata |
| Madison's paper points back to the United Netherlands as a former paper | ✅ source text, final paragraph |
| The Constitution's ratification needed nine states | ✅ Article VII |

**Next-episode preview verified against the source, not memory.** `_production/source-texts/federalist-no-38.txt` was transcribed from Yale Avalon this session for exactly this purpose. Doing so corrected three things in the draft preview:
- Draft said "every famous constitution in the ancient world was handed down by one man." The paper's actual claim is narrower: *in every case reported by ancient history in which government was established with deliberation and consent*, the framing was done by an individual rather than an assembly. **Corrected.**
- Draft said Madison "asks why anybody would prefer that to a convention." The paper's move is the reverse direction — he asks how a people as jealous of liberty as the Greeks came to hand their destiny to one citizen, and concludes America improved on the ancient mode. **Corrected.**
- Draft said the critics have offered "nothing." The paper's charge is that they cannot agree on a substitute. **Corrected**, and the paper's cleanest line was added: "It is not necessary that the former should be perfect; it is sufficient that the latter is more imperfect."

### A3. Internal consistency (the script against itself) — run BEFORE any external checking

Every count, date, interval and quantity in the script was extracted mechanically and compared. **Four precision errors found and fixed:**

1. **"four months after signing it."** The Constitution was signed 17 September 1787; this essay ran 11 January 1788. That is three months and twenty five days. → **Fixed to "not quite four months."**
2. **"four months watching fifty five difficult people."** The convention sat 25 May to 17 September 1787 — three months and twenty three days. → **Fixed to "nearly four months."** Both instances now agree.
3. **"a letter he wrote thirty years afterward."** This essay is January 1788; Madison's letter to Spencer Roane is 2 September 1819 — thirty one years. → **Fixed to "thirty one years afterward."** Sweep: 0 remaining instances of "thirty years."
4. **"Two hundred and forty years later"** (twice). 1788 to 2026 is 238 years. → **Fixed to "Nearly two hundred and forty years later"** in both places. Sweep confirms both instances now match.

**Ambiguity fixed:** the stability/energy/liberty paragraph named three things and then said "Those two things cannot both be maximized," which pointed at an unclear pair. → Rewritten as "You cannot have all of that at once."

**Overstatement softened:** "the worst month of Madison's life" → "the worst weeks of Madison's summer." Madison lived to eighty five and had demonstrably worse months, including the burning of Washington in 1814 while he was President.

**Arithmetic confirmed consistent, no change needed:** 1787→1840 = 53 years (notes); 1958−1788 = 170 years (Hart); 1791+25 = 1816 (bank); 1791–1811 = 20 years of the first bank's charter; 28 June → 30 June = two days (Franklin's motion to Madison's slavery speech); 9 January → 11 January = two days (Connecticut to publication); 2019 → 2020 ("the following year").

---

## Part B — Web cross-check

### B1. The publication moment

| # | Claim | Verdict | Source |
|---|---|---|---|
| 1 | Five states had ratified by 11 January 1788 | ✅ | usconstitution.net ratification table; Teaching American History timeline |
| 2 | Delaware 7 Dec 1787, Pennsylvania 12 Dec 1787, New Jersey 18 Dec 1787, Georgia 2 Jan 1788, Connecticut 9 Jan 1788 | ✅ | https://usconstitution.net/ratifications-html/ ; https://teachingamericanhistory.org/resource/timeline-state/ |
| 3 | Connecticut ratified two days before this essay | ✅ | 9 Jan → 11 Jan |
| 4 | Nine states were needed | ✅ | Article VII; LOC ratification timeline |
| 5 | The Massachusetts convention opened in Boston on 9 January 1788 and ran to February | ✅ | https://teachingamericanhistory.org/resource/massachusetts/ (9 Jan – 5 Feb sitting; ratified 6 Feb 1788, 187–168) |
| 6 | It was the largest ratifying convention any state held | ✅ | Teaching American History; EBSCO Research — ~370 delegates elected, 355 voting; larger than any other state's |
| 7 | Massachusetts had put down an armed rebellion barely a year earlier | ✅ | Shays' Rebellion; consistent with Episodes 6 and 36 |

### B2. Madison, and the room

| # | Claim | Verdict | Source |
|---|---|---|---|
| 8 | Madison was thirty six | ✅ | b. 16 March 1751; 36 through the convention and on 11 Jan 1788 |
| 9 | About five feet four, rarely much over a hundred pounds | ✅ | doctorzebra.com presidential health history; History.com |
| 10 | He described "a constitutional liability to sudden attacks, somewhat resembling epilepsy" | ✅ | his own phrase, widely reproduced; doctorzebra.com |
| 11 | His voice was so quiet people had trouble hearing him | ✅ | multiple biographical sources |
| 12 | He was not absent a single day, nor more than a casual fraction of an hour | ✅ | Madison's own Preface to the Debates — https://www.consource.org/document/james-madison-preface-to-the-debates-in-the-convention-of-1787/ ; reprinted in Farrand's *Records* |
| 13 | He chose a seat in front of the presiding member, delegates to his right and left, as a favourable position for hearing | ✅ | same Preface, verbatim |
| 14 | He noted in abbreviations and marks intelligible to himself, and wrote them out afterward | ✅ | same Preface |
| 15 | Convention sat 25 May – 17 September 1787 at the Pennsylvania State House | ✅ | National Archives; NPS |
| 16 | Secrecy rule adopted 29 May 1787; windows shut, sentries at the doors | ✅ | NPS / Teaching American History "The Rules of the Convention"; National Archives |
| 17 | The notes were withheld until after his death; he died 1836; published 1840 | ✅ | LOC James Madison Papers; Bill of Rights Institute |
| 18 | He was the last surviving delegate | ✅ | died 28 June 1836, last of the framers |
| 19 | Historians examining the manuscript find decades of later revision | ✅ | Mary Sarah Bilder, *Madison's Hand: Revising the Constitutional Convention* (Harvard UP, 2015) — "minor, but extensive, revisions of the text over the next fifty years"; added slips of paper, marginal and overwritten revisions |
| 20 | Madison rejected "Father of the Constitution," calling it not "the offspring of a single brain" but "the work of many heads and many hands" | ✅ | Madison to William Cogswell, 10 March 1834 — https://founders.archives.gov/documents/Madison/99-02-02-2952 |

### B3. Hamilton at the convention (the contrast the episode is built on)

| # | Claim | Verdict | Source |
|---|---|---|---|
| 21 | Hamilton was mostly absent that summer | ✅ | Teaching American History delegate attendance record: present from 28 May, left 29 June, in New York after 2 July, briefly present 13 July and 13 August, in New York 20 Aug – 2 Sept |
| 22 | He gave one enormous speech in June that was not taken up | ✅ | 18 June 1787; NPS "June 18, 1787: Hamilton Speaks" — the speech lasted the entire day and the convention did not act on his plan |
| 23 | He signed alone for New York because the other two delegates had walked out | ✅ | Robert Yates and John Lansing withdrew 10 July 1787; NPS "July 10, 1787: A New Division"; National Archives Founding Fathers: New York |

### B4. Language, boundaries, and the modern parallels

| # | Claim | Verdict | Source |
|---|---|---|---|
| 24 | Madison's three-sources passage compresses Book III of Locke's *Essay Concerning Human Understanding* on the imperfection of words | ⚠️ **fairly hedged** — the script does **not** claim Locke as a source; it presents the argument as Madison's. Scholars do read it as a distillation of Locke | Wake Forest Law Review (Schwartz), "Madison's Federalist 37 and the Structure of…" |
| 25 | Biologists still argue whether a virus is alive; there is no agreed definition of life | ✅ | Scientific American; Microbiology Society; Science News; JSTOR Daily — 120+ competing definitions of life; viruses in the "grey area" |
| 26 | A virus carries genetic material, evolves and replicates, but has no metabolism and cannot replicate without a host cell | ✅ | Microbiology Society; News-Medical |
| 27 | Herbert Hart, a British legal philosopher, offered the "no vehicles in the park" hypothetical in the Harvard Law Review in 1958 | ✅ | H. L. A. Hart, "Positivism and the Separation of Law and Morals," 71 Harv. L. Rev. 593 (1958); Schauer, "A Critical Guide to Vehicles in the Park," 83 N.Y.U. L. Rev. (2008) |
| 28 | It is the most famous hypothetical in the common law world | ⚠️ **fairly hedged** — script says "what has become the most quoted hypothetical in the English speaking legal world." Schauer calls it "the most famous hypothetical in the common law world," which is a scholar's judgement, not a measurement | Schauer, NYU Law Review |
| 29 | Hart's point was a core of settled meaning with a fuzzy penumbra requiring a decision | ✅ | Hart 1958; Schauer's guide |

### B5. Liquidation

| # | Claim | Verdict | Source |
|---|---|---|---|
| 30 | In eighteenth-century usage "liquidate" meant to settle, clarify, or resolve a dispute | ✅ | Baude, *Constitutional Liquidation*, 71 Stan. L. Rev. 1 (2019) |
| 31 | Madison's doctrine requires a genuine textual indeterminacy first; practice can expound but not alter a clear provision; and it requires a deliberate, repeated course of decisions | ✅ | Baude 2019, the article's three stated elements |
| 32 | William Baude published "Constitutional Liquidation" in the Stanford Law Review in 2019, and traces the idea's first appearance to Federalist 37 | ✅ | https://review.law.stanford.edu/wp-content/uploads/sites/3/2019/01/Baude-71-Stan.-L.-Rev.-1-2019.pdf |
| 33 | In 1791 Madison argued in Congress that a national bank was unconstitutional, and lost | ✅ | Madison, Speech on the Bank Bill, 2 February 1791 |
| 34 | In 1816, as President, he signed the charter of the Second Bank of the United States | ✅ | signed 10 April 1816; Federal Reserve History; EBSCO. **Note:** Madison's own 1831 letter misremembers this as 1817 (the bank *opened* in January 1817). The script uses 1816, the documented signing date |
| 35 | His stated reason was respect for deliberate and reiterated precedents, twenty years of annual legislative recognition, and national acquiescence | ✅ | Madison to Charles J. Ingersoll, 25 June 1831 — https://constitution.org/1-History/rf/jm_18310625.htm |
| 36 | In 2020 the Supreme Court decided a case on whether a state may punish presidential electors who break their pledge, and ruled unanimously that it may | ✅ | *Chiafalo v. Washington*, 591 U.S. ___ (6 July 2020); Kagan for eight justices, Thomas concurring in the judgment; Congressional Research Service LSB10515 describes the holding as unanimous |
| 37 | The Court quoted Madison — "a regular course of practice" can "liquidate & settle the meaning of" disputed or indeterminate "terms & phrases" | ✅ | *Chiafalo*, Part II.B, via Cornell LII |
| 38 | That quotation is from Madison's letter to Spencer Roane (2 Sept 1819), **not** from Federalist 37, and the Court cites Federalist 37 separately on the same page | ✅ | *Chiafalo* citation is "Letter to S. Roane (Sept. 2, 1819), in 8 Writings of James Madison 450 (G. Hunt ed. 1908)." **The script states this distinction explicitly rather than letting the listener assume the Court quoted this essay.** |

### B6. The convention's difficulties

| # | Claim | Verdict | Source |
|---|---|---|---|
| 39 | State legislatures were passing, repealing and re-passing laws so fast that planning was impossible, and this drove Madison toward a new government | ✅ | Madison, "Vices of the Political System of the United States" (April 1787), on the mutability of the laws; matches his own phrase in this paper |
| 40 | The Great Compromise passed on 16 July 1787 by five states to four, one delegation divided | ✅ | NPS "July 16, 1787: The Great Compromise Passes"; U.S. Senate historical minute; EBSCO |
| 41 | Madison came with a plan for proportional representation in both chambers and lost that fight | ✅ | Virginia Plan; NPS — "Madison, whose Virginia Plan had set the agenda, feared the convention was finished" |
| 42 | Population decides the House, equality decides the Senate | ✅ | Connecticut Compromise |
| 43 | Madison spent the winter after the convention writing essays urging ratification of the plan that beat him | ✅ | The Federalist, October 1787 – 1788 |
| 44 | Madison's "other combinations… difference of local position and policy" refers to the sectional division over slavery | ⚠️ **fairly hedged** — the script states this as the host's reading and then proves it from Madison's own convention speech rather than asserting it flatly. The paper itself does not say the word | Source text; Madison's 30 June 1787 speech (below) |
| 45 | On 30 June 1787 Madison told the convention the states were divided not by size but by circumstances resulting "partly from climate, but principally from the effects of their having or not having slaves," and that the division lay between North and South, not large and small | ✅ | Madison's Notes, 30 June 1787 — https://avalon.law.yale.edu/18th_century/debates_630.asp (verbatim) |
| 46 | The compromises covered by "theoretical propriety… extraneous considerations" include the three-fifths clause and the twenty-year protection of the slave trade | ✅ | Art. I §2 and Art. I §9. Madison himself frames the latter as "twenty years" in Federalist 38 |

### B7. Unanimity, and Franklin

| # | Claim | Verdict | Source |
|---|---|---|---|
| 47 | Fifty five men attended the convention at one point or another | ✅ | standard figure; National Archives |
| 48 | Thirty nine signatures went onto the document | ✅ | National Constitution Center; NPS "September 17, 1787" |
| 49 | Three men who stayed to the end refused to sign: Randolph, Mason, Gerry | ✅ | https://constitutioncenter.org/signers/the-dissenters-to-the-constitution ; NPS |
| 50 | Randolph, governor of Virginia, introduced the plan the convention started from | ✅ | the Virginia Plan, presented 29 May 1787 (drafted by Madison, presented by Randolph); National Archives |
| 51 | Mason wrote Virginia's declaration of rights | ✅ | Virginia Declaration of Rights, adopted 12 June 1776 |
| 52 | Mason and Gerry both wanted a bill of rights and became leading opponents of ratification | ✅ | Constitution Center, "The Dissenters." Randolph's grounds differed (he wanted a second convention) and the script does **not** attribute the bill-of-rights objection to him |
| 53 | The signature formula made the states, not the individuals, the parties consenting, which is what lets "unanimity" be defended | ✅ | "Done in Convention by the Unanimous Consent of the States present"; blog.consource.org on the drafting of that formula |
| 54 | On 28 June 1787 Franklin, then eighty one, moved for daily prayers; Sherman seconded; Hamilton and others objected that it would look like a confession of trouble; Williamson said the convention had no funds; Randolph proposed a Fourth of July sermon instead and Franklin seconded it; the convention adjourned without ever voting on the motion | ✅ | Madison's Notes, 28 June 1787 — https://avalon.law.yale.edu/18th_century/debates_628.asp (verbatim, including "the adjournment was at length carried, without any vote on the motion"); NPS "June 28, 1787: Franklin's Proposal for Prayer" |
| 55 | Franklin wrote on his own manuscript of the speech: "The Convention except three or four persons, thought Prayers unnecessary" | ✅ | Franklin's endorsement in his hand, reproduced as a footnote in Farrand's *Records* vol. 1 p. 452; corroborated by Sirico, "Benjamin Franklin, Prayer, and the Constitutional Convention," and by the WallBuilders reproduction of the manuscript |
| 56 | Franklin was eighty one on that date | ✅ | b. 17 January 1706 |

---

## The five hedges, stated in the episode rather than smoothed over

1. **Locke.** The script presents the three-sources argument as Madison's own and never claims he was copying Locke, though scholars read it as a compression of Locke's Book III. Attribution left unmade rather than overstated.
2. **"Most quoted hypothetical."** Hedged as "what has become the most quoted hypothetical in the English speaking legal world." It is a scholarly consensus judgement, not a countable fact.
3. **The slavery reading.** The script does not simply assert that "local position and policy" means slavery. It says so and then proves it from Madison's own convention speech two days after Franklin's prayer motion, and explicitly limits the charge: Madison is not lying, everything in his sentence is true, and the accusation is the narrow one that he wrote so a reader could finish the paragraph without learning anything.
4. **The unanimity claim.** Rather than calling Madison wrong, the script gives the reading on which he is defensible — the states, not the individuals, were the consenting parties — and then says that from the man who watched Mason and Gerry refuse in front of him, it is "a little generous."
5. **Madison's notes.** The script states plainly that historians examining the manuscript find decades of later revision, so the record is not a perfect camera. This was added deliberately: an episode about the unreliability of written records should not present the founding's most famous written record as flawless.

---

## Gate 5 — runtime note

Final script: **5,456 words / 30,693 characters / 100 paragraphs.** Estimated 34 to 35 minutes at the series' measured narration rate of 156 to 161 words per minute.

This sits above the gold-standard episodes' 24–34 minute range and below the workflow's 38-minute red-flag line. The red flag exists to catch exegesis, so the structural test was run rather than assumed: the paragraph-opening sweep shows host-led transitions ("Here is where things stand," "Now picture the room he never left," "Start with the simplest part of the problem," "Watch what he does to prove the first one," "We know he meant it, because he did it to himself"), not a chain of "Madison opens… then says… then turns to." The episode's running order is deliberately not the paper's: the paper's eleventh and twelfth paragraphs (the three sources of vagueness, and the liquidation sentence) are pulled to the middle to serve as the spine, and the paper's earlier material on the convention's difficulties is pushed behind them. Six set-apart quotes against a ceiling of eight. Three story set-pieces. Length is carried by those set-pieces, not by even coverage. Runtime accepted on that basis.

## Gate 6 — TTS scan

Zero digits, zero em-dashes, zero en-dashes, zero hyphens, zero ellipses, zero markdown separators, zero non-standard characters, no uppercase labels, no stage directions, no initials-with-periods. Script begins and ends on spoken content. Every list that names a count is followed by explicit ordinals ("three sources" → first, second, and third; "three parts" → first, second, third; "two separate complaints" → the first, the second).
