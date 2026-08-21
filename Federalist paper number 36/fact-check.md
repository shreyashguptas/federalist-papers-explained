# Fact-check — Episode 36 (Federalist No. 36)

Script: `federalist-no-36-script.txt`
Source of record: `_production/source-texts/federalist-no-36.txt` (Yale Avalon transcription)

---

## Part A1 — Internal consistency (script against itself, run BEFORE any external checking)

Every count, date, interval and distinctive figure the script asserts was extracted and compared
against every other occurrence. **Four contradictions were found and fixed.**

| # | Error found | Why it was wrong | Fix | Swept? |
|---|---|---|---|---|
| 1 | "Eleven years later, in the summer of seventeen ninety eight" | January 1788 to July 1798 is ten years and six months, not eleven | → "Ten years later" | yes — 0 remaining occurrences of "eleven years" |
| 2 | "walking around in daylight eleven years later" | same interval, restated later in the episode | → "ten years later" | yes — caught by the same sweep as #1 |
| 3 | "two years before Hamilton wrote this essay, those farmers rose" | Shays' Rebellion began August 1786; this essay ran January 1788, i.e. ~17 months. The script *also* said "roughly eighteen months after" three paragraphs later, so it contradicted itself | → "about a year and a half before" | yes — 0 remaining occurrences of "two years before"; the surviving "roughly eighteen months" now agrees |
| 4 | "the longest continuous run on a single subject in the entire Federalist series" | False. Hamilton's run on the executive (Nos. 67–77) is eleven consecutive papers, and Nos. 15–22 on the defects of the Articles is eight | superlative removed → "the last of seven straight essays on the same question" | yes — 0 remaining occurrences of "longest continuous" |

Two further precision errors were caught in the same pass and corrected:

- "a run that started fourteen essays ago" was ambiguous arithmetic (Nos. 23–36 is fourteen essays,
  but "fourteen essays ago" from No. 36 would point at No. 22). Rewritten as "a run of fourteen
  essays that began back at Federalist Number Twenty Three."
- "unlike anything Hamilton has done in thirty six essays" implied Hamilton wrote all thirty six.
  He did not — Jay wrote Nos. 2–5 and Madison Nos. 10 and 14. Rewritten as "unlike anything we have
  seen in this series so far."
- The opening recap said the legislature would be "landowners, merchants, and lawyers" while the body
  correctly said "landholders, merchants, and members of the learned professions." Harmonised.

Confirmed consistent, no change needed: seven taxation essays (Nos. 30–36) stated twice and agreeing;
"five states" ratified as of 9 January 1788 agrees with Episode 35's "four states … Connecticut would
come four days later"; the three "ghosts" named once and taken up three times in the same order they
were named.

---

## Part A2 — Quote verification (mechanical, not by eye)

All quotations normalised (Unicode NFKD, smart quotes folded, hyphens and dashes → space,
non-alphanumerics stripped, lowercased, whitespace collapsed) and checked as substrings of the
normalised source text. Script: `verify36.py`.

**Result: 17/17 pass, 0 fail.**

| # | Quote (opening words) | Type | Verdict |
|---|---|---|---|
| 1 | "There are strong minds in every walk of life…" through "The door ought to be equally open to all" | set-apart | ✅ exact |
| 2 | "Many spectres have been raised out of this power of internal taxation…" | set-apart | ✅ exact |
| 3 | "The national legislature can make use of the system of each State within that State." | set-apart | ✅ exact |
| 4 | "the existence of such a power in the Constitution will have a strong influence…" | set-apart | ✅ exact |
| 5 | "As to poll taxes, I, without scruple, confess my disapprobation of them" | set-apart | ✅ exact |
| 6 | "I should lament to see them introduced into practice under the national government." | set-apart (same para as 5) | ✅ exact |
| 7 | "I acknowledge my aversion to every project that is calculated to disarm the government…" | set-apart | ✅ exact |
| 8 | "a minute topographical acquaintance with all the mountains, rivers, streams, highways, and bypaths in each State" | inline | ✅ exact |
| 9 | "worn too loose a garb to admit even of an accurate inspection of its real shape or tendency" | inline | ✅ exact |
| 10 | "all duties, imposts, and excises shall be uniform throughout the United States" | inline | ✅ exact |
| 11 | "effectually shuts the door to partiality or oppression" | inline | ✅ exact |
| 12 | "The quantity of taxes to be paid by the community must be the same in either case" | inline | ✅ exact |
| 13 | "making the luxury of the rich tributary to the public treasury" | inline | ✅ exact |
| 14 | "There may exist certain critical and tempestuous conjunctures of the State…" | inline | ✅ exact |
| 15 | "what greater affinity or relation of interest can be conceived between the carpenter and blacksmith…" | inline | ✅ exact |
| 16 | "does it follow because there is a power to lay them that they will actually be laid" | inline | ✅ exact |
| 17 | Cross-ref: Federalist 36 restates Federalist 35's "proprietors of land, of merchants, and of members of the learned professions" | continuity | ✅ present in No. 36 ¶1 |

**Two deliberate, disclosed modifications**, both required by the series' TTS rules and both
neutralised by the normalisation above:

- `poll-taxes` → `poll taxes` (the hyphen is read aloud literally by the voice).
- The source has capitalised emphasis (`SYSTEM OF EACH STATE WITHIN THAT STATE`) which is rendered
  in ordinary case. No words changed.

**One quote deliberately shortened** to avoid an artifact: the source reads "those States1 which have
uniformly been the most tenacious of their rights", carrying Hamilton's footnote marker. Rather than
silently drop the `1` from inside a quotation, the quote was cut at "disapprobation of them" and the
second half quoted separately. The footnote's content ("The New England States") is stated in the
host's own voice instead.

Also noted: the Avalon transcription contains an OCR defect, "Land taxes are co monly laid".
Nothing in the script quotes that sentence.

---

## Part B — External claims

**53 claims checked: 48 ✅ verified, 5 ⚠️ fairly hedged in the script, 0 ❌ wrong.**

No external claim required a correction, so no fix-and-sweep was needed in this section. As with
Episodes 34 and 35, the load-bearing history was researched *before* drafting rather than checked
afterwards, which is why this table has no ❌ rows.

### Publication, ratification, series structure

| Claim | Verdict | Source |
|---|---|---|
| Federalist No. 36 ran in the New York Packet, Tuesday 8 January 1788 | ✅ | source-text header (Avalon), https://avalon.law.yale.edu/18th_century/fed36.asp |
| Author is Alexander Hamilton | ✅ | Avalon; `SERIES-STATUS.md` authorship reference |
| Connecticut ratified 9 January 1788, 128 to 40, as the fifth state | ✅ | https://connecticuthistory.org/connecticut-ratifies-us-constitution-today-in-history/ ; https://www.usconstitution.net/rat_ct-html/ |
| A Massachusetts convention was gathering at this moment (ratified 6 Feb 1788, 187–168) | ✅ | https://www.usconstitution.net/rat_ct-html/ |
| Nos. 30–36 are seven straight essays on taxation | ✅ | the texts themselves; each is titled "Concerning the General Power of Taxation" |
| Nos. 23–36 form a fourteen-essay run on the powers of an energetic government | ✅ | the texts; No. 36's own closing paragraph ("such of the powers … as having an immediate relation to the energy of the government") |
| Federalist No. 37 is Madison, Daily Advertiser, 11 January 1788, "Concerning the Difficulties of the Convention in Devising a Proper Form of Government" | ✅ | https://en.wikipedia.org/wiki/Federalist_No._37 ; https://www.consource.org/document/the-federalist-no-37-1788-1-11/ |
| No. 36 / No. 37 is the conventional seam between the case for union and the examination of the structure | ⚠️ hedged | Script says the papers are "usually divided into parts" rather than asserting one canonical scheme. Scholars group them slightly differently. |

### The Direct Tax of 1798 and Fries's Rebellion

| Claim | Verdict | Source |
|---|---|---|
| July 1798: Congress laid $2 million in direct taxes, apportioned among the states as the Constitution requires | ✅ | https://en.wikipedia.org/wiki/Fries%27s_Rebellion ; https://www.forbes.com/sites/taxnotes/2024/12/09/how-the-first-federal-property-tax-sparked-an-armed-rebellion/ |
| Pennsylvania's share was $237,000 | ✅ | https://en.wikipedia.org/wiki/Fries%27s_Rebellion |
| It fell on land, dwelling houses, and enslaved people | ✅ | Forbes/Tax Notes (above); dwellings over $100 taxed 0.2%–1%, 50 cents per enslaved person aged 12–50 |
| The motive was the drift toward the Quasi-War with France | ✅ | Forbes/Tax Notes (above) |
| Houses were valued by the number and size of their windows | ✅ | https://en.wikipedia.org/wiki/Fries%27s_Rebellion ; https://goschenhoppen.org/window-pane-tax/ |
| Resistance centred on Bucks, Northampton and Montgomery counties, among German farmers | ✅ | https://philadelphiaencyclopedia.org/essays/fries-rebellion/ |
| Assessors were largely Quakers and Moravians, communities that had not fought in the Revolution, assessing men who had | ✅ | https://en.wikipedia.org/wiki/Fries%27s_Rebellion |
| Women poured hot water from upstairs windows on assessors; the episode is known as the "hot water war" | ✅ | https://en.wikipedia.org/wiki/Fries%27s_Rebellion (Pennsylvania German: *Heesses-Wasser Uffschtand*) |
| John Fries was an itinerant auctioneer and a Revolutionary War veteran who began organising meetings in February 1799 | ✅ | https://en.wikipedia.org/wiki/Fries%27s_Rebellion ; https://www.discoverlehighvalley.com/discover-the-fries-rebellion-a-historic-uprising-in-western-lehigh-valley/ |
| A federal marshal named Nichols arrested about a dozen resisters and held them at the Sun Inn, Bethlehem | ✅ | https://philadelphiaencyclopedia.org/essays/fries-rebellion/ (twelve men taken into custody; Sun Inn used as headquarters and temporary jail from 6 March) |
| The marshal's **first name** | ⚠️ hedged | Sources disagree: one gives "William Nichols", another "Col. Samuel Nichols". **The script names only the surname**, so it asserts nothing contested. |
| The confrontation was on 7 March 1799 and the marshal gave up the prisoners | ✅ | https://www.discoverlehighvalley.com/discover-the-fries-rebellion-a-historic-uprising-in-western-lehigh-valley/ ; https://philadelphiaencyclopedia.org/essays/fries-rebellion/ |
| The size of Fries's crowd | ⚠️ hedged | Sources give both ~140 and ~400. **The script states the range explicitly** ("from around a hundred and forty men up to four hundred") rather than picking one. |
| Fries was tried for treason, convicted, retried, convicted again, sentenced to hang | ✅ | https://en.wikipedia.org/wiki/Fries%27s_Rebellion |
| John Adams issued a general amnesty on 21 May 1800 | ✅ | https://en.wikipedia.org/wiki/Fries%27s_Rebellion |
| **The 1798 tax was administered by federal officers, not state ones**: presidentially appointed boards of commissioners in each state, well over 1,500 frontline federal assessors, and several hundred more senior federal assessors hearing appeals | ✅ | Parrillo, *A Critical Assessment of the Originalist Case Against Administrative Regulatory Power*, Yale Law Journal — https://yalelawjournal.org/article/a-critical-assessment ; https://www.archives.gov/publications/prologue/2007/spring/tax-lists.html |
| Hamilton had left the Treasury three years earlier (resigned January 1795) and this was Adams's administration | ✅ | standard biography; the 1798 act is signed under Adams |

This last row is the episode's most important external finding and it is load-bearing, so it was
required to meet the two-source rule: the Yale Law Journal study of the 1798 tax and the National
Archives description of the tax lists both describe a federally staffed valuation apparatus. The
script uses it to show that Hamilton's two most confident practical predictions in this paper —
that the union would "make use of the system of each State within that State", and that there could
be "no room for double sets of officers" — were both contradicted the first time the power was used.

### Constitutional provisions

| Claim | Verdict | Source |
|---|---|---|
| Direct taxes are apportioned among the states by population under Article I, section 2 | ✅ | US Constitution, Art. I §2; and No. 36 itself cites "the second section of the first article" |
| That same clause counted an enslaved person as three fifths of a person for apportionment | ✅ | US Constitution, Art. I §2 ("three fifths of all other Persons") |
| Duties, imposts and excises must be uniform throughout the United States (Art. I §8) | ✅ | US Constitution, Art. I §8; quoted by Hamilton in No. 36 |

### Hylton v. United States and the fate of apportionment

| Claim | Verdict | Source |
|---|---|---|
| Congress taxed privately owned carriages by an Act of 5 June 1794 | ✅ | https://supreme.justia.com/cases/federal/us/3/171/ |
| Daniel Hylton was a wealthy Virginian; the parties waived a jury and agreed the facts | ✅ | https://supreme.justia.com/cases/federal/us/3/171/ ; https://allthingsliberty.com/2020/06/hylton-v-u-s-and-alexander-hamiltons-defense-of-congressional-taxing-authority/ |
| He stipulated 125 chariots kept for his own private use, a figure chosen to clear the jurisdictional threshold; the case was an arranged test | ✅ | https://supreme.justia.com/cases/federal/us/3/171/ ; https://www.courtlistener.com/opinion/84686/hylton-v-united-states/ |
| Argued February 1796 (23 February), decided 8 March 1796 | ✅ | https://en.wikipedia.org/wiki/Hylton_v._United_States |
| Hamilton argued for the government; his only Supreme Court appearance | ✅ | https://allthingsliberty.com/2020/06/hylton-v-u-s-and-alexander-hamiltons-defense-of-congressional-taxing-authority/ ; Justia report names "Hamilton, the late Secretary of the Treasury" as counsel in support of the tax |
| The Court held the carriage tax was not a direct tax and needed no apportionment | ✅ | https://en.wikipedia.org/wiki/Hylton_v._United_States ; https://supreme.justia.com/cases/federal/us/3/171/ |
| Direct taxes were read narrowly, essentially as taxes on land and head taxes | ✅ | seriatim opinions of Chase, Paterson and Iredell, per the report |
| Madison and Jefferson thought the decision wrong | ✅ | https://allthingsliberty.com/2020/06/hylton-v-u-s-and-alexander-hamiltons-defense-of-congressional-taxing-authority/ |
| In 1895 *Pollock v. Farmers' Loan & Trust* struck down a federal income tax as an unapportioned direct tax | ✅ | https://en.wikipedia.org/wiki/Pollock_v._Farmers%27_Loan_%26_Trust_Co. ; https://supreme.justia.com/cases/federal/us/157/429/ |
| The Sixteenth Amendment (1913) lets Congress tax income from any source without apportionment | ✅ | https://en.wikipedia.org/wiki/Sixteenth_Amendment_to_the_United_States_Constitution |

The script does **not** claim Hamilton's Hylton argument caused the Sixteenth Amendment. It says the
narrow reading of "direct tax" left his apportionment safeguard covering very little, and that the
remainder was amended away in the open. That is the defensible version and it is what was written.

### Poll taxes, then and after

| Claim | Verdict | Source |
|---|---|---|
| Hamilton's own footnote identifies the states he means as the New England states | ✅ | source text footnote 1 |
| Massachusetts leaned heavily on a head tax in the 1780s | ✅ | https://www.digitalhistory.uh.edu/teachers/lesson_plans/pdfs/unit2_5.pdf ; https://www.newworldencyclopedia.org/entry/Shays'_Rebellion |
| The share of Massachusetts revenue the poll tax represented | ⚠️ hedged | Sources disagree: one gives "a full 40 percent of the tax burden", another "1/3 of the State's revenue". **The script says "somewhere around a third … with some accounts putting it higher"** rather than picking a number. |
| Western Massachusetts farmers lived largely by barter and rarely saw hard money | ✅ | https://www.newworldencyclopedia.org/entry/Shays'_Rebellion |
| Shays' Rebellion began 29 August 1786 and the head tax was among its grievances | ✅ | https://www.zinnedproject.org/news/tdih/shays-rebellion/ ; https://en.wikipedia.org/wiki/Shays%27s_Rebellion |
| Roughly eighteen months separate the rebellion's outbreak from this essay | ✅ | arithmetic: Aug 1786 → Jan 1788 = 17 months |
| From the 1890s southern states tied poll-tax payment to voting, often cumulatively | ✅ | https://constitutioncenter.org/the-constitution/interpretations/the-twenty-fourth-amendment-by-deborah-archer-and-derek-muller |
| *Breedlove v. Suttles* (1937) unanimously upheld Georgia's poll tax | ✅ | https://en.wikipedia.org/wiki/Breedlove_v._Suttles ; https://supreme.justia.com/cases/federal/us/302/277/ |
| The Twenty-fourth Amendment was ratified in January 1964 and reaches federal elections | ✅ | https://constitutioncenter.org/the-constitution/interpretations/the-twenty-fourth-amendment-by-deborah-archer-and-derek-muller |
| Five states still had poll taxes then: Alabama, Arkansas, Mississippi, Texas, Virginia | ✅ | https://constitutioncenter.org/the-constitution/interpretations/the-twenty-fourth-amendment-by-deborah-archer-and-derek-muller ; https://constitution.heritage.org/essays/amdt-24/ |
| *Harper v. Virginia Board of Elections* (1966), 6–3, ended them in state elections | ✅ | https://supreme.justia.com/cases/federal/us/383/663/ ; https://www.zinnedproject.org/news/tdih/harper-v-virginia-elections/ |
| The disenfranchising poll taxes were **state** taxes levied under a power the states already held, doing a job unrelated to revenue | ✅ | Breedlove and Harper both concern state statutes; Hamilton's own text confirms "Every State in the Union has power to impose taxes of this kind" |

**On fairness here.** This is the one place in the episode where a modern parallel could easily
become an unfair charge, so the script states the limit explicitly before drawing the lesson: the
poll taxes that disenfranchised millions were state taxes under a pre-existing state power, and no
reading of Federalist 36 produces them. What the script does claim is narrower and is supported by
Hamilton's own words: his argument rests on the premise that possessing a power tells you little
about how it will be used, and he offers the states as his proof ("Are the State governments to be
stigmatized as tyrannies, because they possess this power?"). History answered that specific
rhetorical question badly. The script says so and stops there.

### Modern parallels

| Claim | Verdict | Source |
|---|---|---|
| Property tax for schools is assessed by county/local offices, not federally | ✅ | general US practice; uncontested |
| Medicaid is jointly funded and state-administered, which is why it differs by state | ✅ | https://pmc.ncbi.nlm.nih.gov/articles/PMC8242625/ |
| Unemployment insurance is a federal framework with state administration and state collection | ✅ | https://www.congress.gov/crs-product/IF10838 ; https://www.dol.gov/resource-library/unemployment-insurance-ui-administrative-funding-and-costs-literature-review |
| Federal highway money is largely spent through state transportation departments | ✅ | standard structure of the Federal-Aid Highway Program |
| "Cooperative federalism" is the standard term for this arrangement | ✅ | standard political-science usage |

### Continuity references (checked against the actual earlier scripts, not memory)

| Claim | Verdict | Check |
|---|---|---|
| Episode 35 argued that a tariff's name is not its payer and a representative's biography is not his bond | ✅ | read `Federalist paper number 35/federalist-no-35-script.txt` |
| Episode 35's sign-off promised exactly this episode's three spectres and Hamilton's poll-tax reversal | ✅ | read the last paragraph of the Episode 35 script; this episode delivers all three in that order |
| Requisitions failing was covered in Episodes 15 and 16 | ✅ | `grep -c requisition` → Ep 15: 5 hits, Ep 16: 7 hits |
| Shays' Rebellion was covered in Episode 6 | ✅ | `grep -il shays` → Episode 6 among others |
| Federalist 35 describes the legislature as "proprietors of land, of merchants, and of members of the learned professions" | ✅ | that phrase appears in No. 36 ¶1 restating No. 35 |

---

## Gate summary

- Gate 3 (storytelling): passes. Set-apart quotes: **6** (target 4–6, ceiling 8), none adjacent.
  Story set-pieces: **3** (Fries's Rebellion; Hylton and the fate of apportionment; the poll tax's
  second life). Listener-question moments: **5**, spread across the body. Modern parallels appear in
  four separate places in the body, not bunched at the end.
- Gate 3 (exegesis test): passes. The episode's order is not the paper's order. Hamilton's ¶12 (the
  "spectres" passage) is pulled to the front to serve as the episode's frame; his ¶10 (the
  requisition backstop) is moved late to be the intellectual peak; his ¶11 and ¶14 are compressed to
  brisk paraphrase. Paragraph-opening sentences read as a host deciding what to teach next, not as a
  tour of the paper.
- Gate 5 (runtime): 5,269 words / 29,664 characters ≈ 32:43 estimated. Lower-middle of the 25–40 band.
- Gate 6 (TTS): zero em-dashes, zero digits, zero hyphens, zero ellipses, no "No.", no Roman numerals.
  Four intentional short paragraphs used as beats, well separated, no stacks.
