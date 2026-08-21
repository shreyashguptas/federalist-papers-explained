# Fact-Check — Federalist No. 26

Gate 4 log. Part A checks the script against the source paper and against itself; Part B cross-checks every non-quote claim against the open web.

## Part A — Source and continuity check

**Quotes (verified word-for-word against `_production/source-texts/federalist-no-26.txt` by normalized substring match):**

All 16 quoted phrases matched the source exactly:

- "a zeal for liberty more ardent than enlightened" ✓
- "the necessity of doing it is implied in the very act of delegating power" ✓
- "the raising or keeping a standing army within the kingdom in time of peace, unless with the consent of Parliament, was against law" ✓
- "too temperate, too well-informed" ✓
- "an injudicious excess" ✓
- "superfluous, if not absurd" ✓
- "the result of a conflict between jealousy and conviction" ✓
- "by aiming at too much, is calculated to effect nothing" ✓
- "to deliberate upon the propriety of keeping a military force on foot" ✓
- "to come to a new resolution on the point" ✓
- "to declare their sense of the matter, by a formal vote in the face of their constituents" ✓
- "a favorable topic for declamation" ✓
- "not only vigilant but suspicious and jealous guardians" ✓
- "not only to be the voice, but, if necessary, the arm of their discontent" ✓
- "progressive augmentations" ✓
- "a continued conspiracy for a series of time" ✓

**Source OCR corrections (Avalon transcription artifacts, corrected in the source file to the true Federalist text):**
- "too wellinformed" → "too well-informed" (run-together OCR artifact; the correct text is "well-informed"). Swept the source file: 1 instance found and fixed, 0 remaining.

**Script correction driven by the source check:**
- The voice/arm line was reworded from "the states stand ready to be not only the voice…" to "the states stand ready not only to be the voice…" so the quoted span matches the source exactly ("not only to be the VOICE, but, if necessary, the ARM of their discontent"). 1 instance; 0 others.

**Internal consistency (script against itself):** all counts and figures agree with themselves.
- Charles the Second: five thousand troops. James the Second: about thirty thousand. (Appears consistently; no contradictory figure elsewhere.)
- Only two states restricted peacetime armies (Pennsylvania and North Carolina) — stated once, consistent.
- Dates: Norman Conquest "ten sixty-six"; revolution "sixteen eighty-eight" (2 instances, both agree); "seventeen eighty-seven" (2 instances, both agree).
- Two-year appropriations rule referred to consistently throughout.
- Senate turns over "one-third" every two years — consistent with the House "every two years."
- "About seven hundred years" back from 1787 to the Norman Conquest (721 years) — accurate as a round figure.

**Authorship:** Hamilton (as Publius) — matches the authorship reference and the continuation of the No. 23–25 sequence.

**Continuity callbacks (checked against the actual Ep 24 and Ep 25 scripts):**
- Recap of Ep 25's close (paper ban forbids nothing / leaves you helpless / gets trampled by necessity) — accurate to the Ep 25 script.
- Pennsylvania callback (its bill of rights declared armies dangerous, yet it raised troops in peacetime) — accurate to the Ep 25 set-piece; used here as a brief callback, not a re-tell.
- "the word energetic back in Number Twenty-Three" lineage and the two-year money-leash theme from Ep 24/25 — consistent.

## Part B — Web cross-check (every non-quote factual claim)

| # | Claim | Verdict | Source(s) | Note |
|---|-------|---------|-----------|------|
| 1 | Norman Conquest 1066; monarchy's power reduced over centuries, first by barons then the people | ✅ Verified | avalon.law.yale.edu/18th_century/fed26.asp; britannica.com/event/Norman-Conquest | "Barons then the people" is Hamilton's framing, a fair summary of the Magna Carta → Parliament arc |
| 2 | Glorious Revolution of 1688 put William, Prince of Orange, on the throne; seen as the triumph of English liberty | ✅ Verified | britannica.com/event/Glorious-Revolution; avalon fed26 | Matches Hamilton exactly |
| 3 | Charles II kept ~5,000 peacetime troops on his own authority; James II raised it to ~30,000 on his civil list | ✅ Verified (figures = Hamilton's; 30,000 approximate) | nam.ac.uk/explore/restoration-and-birth-british-army; en.wikipedia.org/wiki/Standing_army_(Great_Britain) | Charles II ~5,000 is the well-attested originally-established force; James II's army is documented ~20,000 (end 1685) rising to ~34,000 (1688). 30,000 is a defensible round figure. Script attributes the numbers to Hamilton and now says "about thirty thousand." |
| 4 | English Bill of Rights (1689) barred a peacetime standing army *without Parliament's consent* — not an outright ban | ✅ Verified | en.wikipedia.org/wiki/Bill_of_Rights_1689; britannica.com/topic/Bill-of-Rights-British-history | The consent-not-ban distinction (the hinge of the episode) is correct |
| 5 | Only Pennsylvania and North Carolina restricted peacetime armies, using "ought not" not "shall not"; New York silent and admired | ✅ Verified (Hamilton's characterization) | avalon fed26; founders.archives.gov/documents/Hamilton/01-04-02-0183 | Script explicitly frames the NY praise as Hamilton's "quiet pride," not neutral fact |
| 6 | The Constitution (Art. I, §8) caps army appropriations at a two-year term | ✅ Verified | constitution.congress.gov (Art. I, §8, cl. 12); law.cornell.edu | "no Appropriation of Money to that Use shall be for a longer Term than two Years" |
| 7 | House elected every 2 years; Senate turns over one-third every 2 years (staggered six-year terms) | ✅ Verified | constitution.congress.gov (Art. I, §3, cl. 2); senate.gov/about/origins-foundations/senate-and-constitution/senate-classes.htm | Three Senate classes; ~1/3 up each even-year election. The rotation detail is exactly right |
| 8 | Federalist No. 26 by Hamilton, as Publius, in the Independent Journal, December 1787 | ✅ Verified | founders.archives.gov/documents/Hamilton/01-04-02-0183; ballotpedia.org/Federalist_No._26 | Standard scholarly date: 22 December 1787 |
| 9 | (Teaser) Federalist No. 27, also Hamilton, argues a well-administered national government acting on individuals earns obedience and needs force far less | ✅ Verified | en.wikipedia.org/wiki/Federalist_No._27; avalon.law.yale.edu/18th_century/fed27.asp | Fair for a one-line teaser |
| 10 | Modern parallel: US military policy is contested through a recurring, on-the-record annual budget fight (tighter than the two-year ceiling) | ✅ Verified, not distorting | congress.gov/crs-product/IF10515; en.wikipedia.org/wiki/National_Defense_Authorization_Act | Defense is funded via two annual bills (NDAA + appropriations); FY2025 was the 64th consecutive NDAA. The two-year clause sets a maximum, not a required wait — framing is fair |

**Result:** No claim came back ❌ wrong or ⚠️ contested. All ten are ✅ verified with at least two independent high-quality sources. The only light-care items (the ~30,000 figure and the New York praise) are both already attributed to Hamilton in the script; the 30,000 was additionally softened to "about thirty thousand."
