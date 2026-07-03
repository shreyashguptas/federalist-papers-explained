# Fact-Check Log — Episode 17 (Federalist No. 17)

Gate 4 of the production workflow. Two parts: (A) source + continuity check against the authoritative source text; (B) web cross-check of every non-quote factual claim, two independent sources required for load-bearing claims.

**Outcome: 0 wrong, 0 contested. All quotes exact. All claims ✅ verified (with honest hedges built into the script where sources flagged a precision nuance). Gate 4: PASS.**

---

## Part A — Source & continuity check

**Authority:** `_production/source-texts/federalist-no-17.txt` (Hamilton, Federalist No. 17), fetched from Project Gutenberg ebook 1404, formatted to match the series' source files.

### Quote verification (mechanical, normalized-substring against the source)
Every phrase the script presents as Hamilton's own words was verified as an exact normalized substring of the source file (case/punctuation-insensitive). All 25 passed.

| # | Quote (as spoken) | Type | Verdict |
|---|---|---|---|
| 1 | "It will always be far more easy for the State governments to encroach upon the national authorities than for the national government to encroach upon the State authorities." | set-apart | ✅ exact |
| 2 | "It is a known fact in human nature, that its affections are commonly weak in proportion to the distance or diffusiveness of the object." | set-apart | ✅ exact |
| 3 | "unless the force of that principle should be destroyed by a much better administration of the latter" | set-apart | ✅ exact |
| 4 | "has given our jealousy a direction to the wrong side" | set-apart | ✅ exact |
| — | "the most powerful, most universal, and most attractive source of popular obedience and attachment" | inline | ✅ exact |
| — | "the immediate and visible guardian of life and property" | inline | ✅ exact |
| — | "its benefits and its terrors in constant activity before the public eye" | inline | ✅ exact |
| — | "great cement of society" | inline | ✅ exact |
| — | "a kind of sovereign" | inline | ✅ exact |
| — | "slender allurements to ambition" | inline | ✅ exact |
| — | "the times of feudal anarchy" | inline | ✅ exact |
| — | "mere domestic police of a State" | inline | ✅ exact |
| — | "as troublesome as it would be nugatory" | inline | ✅ exact |
| — | "Commerce, finance, negotiation, and war" | inline | ✅ exact |
| — | "uprightness and prudence" | inline | ✅ exact |
| — | "complete counterpoise" / "not unfrequently, dangerous rivals" / "so decided an empire" | inline | ✅ exact |
| — | "speculative men" | inline | ✅ exact |
| — | "clemency and justice" / "mutual danger and mutual interest" | inline | ✅ exact |
| — | "spirit of clanship" / "constant overmatch for the power of the [monarch]" | inline | ✅ exact |
| — | "confidence and good-will of the people" / "legitimate and necessary authority" | inline | ✅ exact |

Set-apart stop-and-explain quotes: **4** (ceiling is 8; target 4–6). ✅

### Paraphrase fidelity
- "police" in the paper = the whole internal regulation/housekeeping of a state, not police officers — the script explicitly glosses this. ✅
- The "flip" thesis (danger runs from states→union, not union→states), the affection-by-proximity ladder, the justice-as-cement argument, the "no temptation" argument, the feudal/Scotland analogy, and the "jealousy aimed at the wrong side" close are all faithful to the paper's spine. ✅

### Authorship & continuity
- Authorship: **Hamilton** — matches `SERIES-STATUS.md` authorship reference (No. 17 = Hamilton). Undisputed (not among the contested Madison/Hamilton essays). ✅
- Continuity callbacks checked against the actual earlier scripts:
  - Ep 16 (courts-not-armies, laws-on-individuals, "majesty of the national authority… courts of justice"): accurate; Ep 16's closing teaser explicitly set up this episode's "danger runs the opposite way" framing. ✅
  - "since Number Fifteen" (the diagnosis of the confederation's weakness): accurate. ✅
  - Teaser forward to Number Eighteen (Hamilton + Madison open the survey of historical confederacies, beginning with ancient Greece): accurate — see Part B claim 10. ✅

---

## Part B — Web cross-check (every non-quote factual claim)

### Cluster 1 — Publication & historical claims

| # | Claim | Verdict | Sources |
|---|---|---|---|
| 1 | No. 17 written by Alexander Hamilton (undisputed) | ✅ verified | founders.archives.gov/documents/Hamilton/01-04-02-0171 ; en.wikipedia.org/wiki/Federalist_No._17 |
| 2 | First published December 5, 1787 | ✅ verified | founders.archives.gov/documents/Hamilton/01-04-02-0171 ; en.wikipedia.org/wiki/Federalist_No._17 |
| 3 | First appeared in *The Independent Journal* (NY) | ✅ verified (first venue; reprinted in the *New-York Packet* & *Daily Advertiser* Dec 7) | en.wikipedia.org/wiki/Federalist_No._17 ; constitutingamerica.org (Federalist No. 17 entry) |
| 4 | Nos. 15 (Dec 1), 16 (Dec 4), 17 (Dec 5) in tight succession, all Hamilton | ✅ verified | founders.archives.gov/documents/Hamilton/01-04-02-0168 ; …/01-04-02-0170 |
| 5 | Signed "Publius," shared pen name of Hamilton/Madison/Jay | ✅ verified | avalon.law.yale.edu/18th_century/fed17.asp ; en.wikipedia.org/wiki/The_Federalist_Papers |
| 6 | Standard title "The Same Subject Continued: The Insufficiency of the Present Confederation to Preserve the Union" | ✅ verified | avalon.law.yale.edu/18th_century/fed17.asp ; ballotpedia.org (Federalist No. 17) |
| 7 | "Times of feudal anarchy" — weak central sovereign, semi-sovereign barons, frequent baronial wars — accurate picture of feudalism | ✅ verified | avalon.law.yale.edu/18th_century/fed17.asp ; britannica.com/topic/feudalism |
| 8 | Monarchs beat barons partly because barons oppressed their own dependents, so commoners sided with the crown | ✅ verified (recognized state-formation dynamic) | avalon.law.yale.edu/18th_century/fed17.asp ; britannica.com/topic/history-of-Europe/The-emergence-of-modern-Europe |
| 9 | Scotland: powerful clans/nobles overmatched the crown until the "incorporation with England" = **Acts of Union 1707** (Great Britain) | ✅ verified | britannica.com/place/Scotland/Scotland-in-the-15th-century ; en.wikipedia.org/wiki/Acts_of_Union_1707 ; britannica.com/event/Act-of-Union-Great-Britain-1707 |
| 10 | Closing sets up the confederacy survey of Nos. 18–20 (Greek leagues; Germanic/Holy Roman Empire + Switzerland; United Netherlands) | ✅ verified | avalon.law.yale.edu/18th_century/fed18.asp ; founders.archives.gov/documents/Madison/01-10-02-0201 |

### Cluster 2 — Modern-parallel claims (the "great reversal")

| # | Claim | Verdict | Sources |
|---|---|---|---|
| 1 | 16th Amendment (ratified 1913) let the federal government tax incomes directly | ✅ verified (Amendment removed the constitutional barrier; the 1913 Revenue Act imposed the tax — script says the amendment "let the federal government tax incomes," and hedges that the mass reach came "in time") | archives.gov/milestone-documents/16th-amendment ; constitution.congress.gov/constitution/amendment-16/ |
| 2 | Social Security created by the Social Security Act of 1935 (direct federal benefits to individuals) | ✅ verified (created 1935; monthly checks began 1940 — script says "created Social Security… the promise of a retirement check," avoiding the date trap) | ssa.gov/history/35act.html ; archives.gov/milestone-documents/social-security-act |
| 3 | 1930s New Deal expanded federal reach into daily economic life (relief, jobs, retirement, FDIC deposit insurance 1933/34) | ✅ verified | fdic.gov/history/1930-1939 ; archives.gov/milestone-documents/social-security-act ; federalreservehistory.org (Glass-Steagall) |
| 4 | Federal health coverage for the old and poor created 1965 (Medicare/Medicaid) | ✅ verified | archives.gov/milestone-documents/medicare-and-medicaid-act ; cms.gov/about-cms/who-we-are/history |
| 5 | **Load-bearing:** everyday criminal & civil justice is still overwhelmingly STATE/LOCAL today (most crimes, lawsuits, family/property matters in state courts; most police state/local) | ✅ verified — strongly true. State courts ≈70M incoming cases/yr; federal criminal filings ≈66k/yr. State/local sworn officers ≈708k vs ≈134k federal (mostly specialized). | uscourts.gov/.../comparing-federal-state-courts ; ncsc.org/resources-courts/data ; bjs.ojp.gov (sworn officers 2020 / federal officers 2023) |
| 6 | Federal government today has large *direct* ties to individuals (IRS collects income tax from individuals; SSA pays benefits to tens of millions ≈70M) | ✅ verified | ssa.gov/policy/docs/quickfacts/stat_snapshot/ ; irs.gov/statistics/returns-filed-taxes-collected-and-refunds-issued |
| 7 | In 1787/early republic, almost all law touching daily life was state/local; federal footprint on individuals was *small* (customs, post, small army/navy, limited-jurisdiction courts) — "small," not "nonexistent" | ✅ verified — script lists actual federal touchpoints, so it does not overstate | constitution.congress.gov/browse/essay/artI-S8-C1-1-2/ ; loc.gov (Creating the U.S. — taxation) |

### Hedges deliberately built into the script (per fact-checker precision notes)
- Income tax: phrased as the amendment that "let the federal government tax incomes," with mass reach "in time" — not claiming universal income tax in 1913.
- Social Security: phrased as "created Social Security, the promise of a retirement check" — not claiming checks flowed in the 1930s (they began 1940).
- Early federal footprint: described as a customs house / post road / distant army / narrow-jurisdiction courts — i.e., *small, not nonexistent.*
- Hamilton's prediction: explicitly framed as *overtaken in outcome but right in mechanism* — the honest, two-sided verdict, not a claim that he was simply right or simply wrong.

**All claims ✅ verified. Gate 4: PASS.**
