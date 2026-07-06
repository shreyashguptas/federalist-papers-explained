# Federalist No. 25 — Fact-Check Log

Gate 4 pass for Episode 25. Part A checks the script against the source paper and against itself; Part B cross-checks every non-quote factual claim against the open web (two independent sources required for load-bearing claims).

## Part A — Source & internal-consistency check

- **Quotes verified word-for-word.** Every set-apart quote was checked mechanically (normalized substring match) against `_production/source-texts/federalist-no-25.txt`. All 15 checked passages match exactly:
  - "encircle the Union from Maine to Georgia"
  - "the security of all would thus be subjected to the parsimony, improvidence, or inability of a part"
  - "engines for the abridgment or demolition of the national authority"
  - "the people are always most in danger when the means of injuring their rights are in the possession of those of whom they entertain the least suspicion"
  - "the most extraordinary spectacle which the world has yet seen"
  - "a nation incapacitated by its Constitution to prepare for defense, before it was actually invaded"
  - "We must receive the blow, before we could even prepare to return it"
  - "created by our choice, dependent on our will"
  - "had like to have lost us our independence"
  - "erected eternal monuments to their fame"
  - "War... is a science to be acquired and perfected by diligence, by perseverance, by time, and by practice"
  - "how unequal parchment provisions are to a struggle with public necessity"
  - "flimsy subterfuge"; "nourished by mutual jealousy"; "the whole military force of the Union in the hands of two or three"
- **Source-file OCR corrections (swept).** The Avalon transcription carried two obvious optical-scan corruptions that are not the true Federalist text: "national authcrity" → **"national authority"**, and "by perserverance" → **"by perseverance"**. Both were corrected in the source file so the quote authority is accurate; the true Federalist text unambiguously reads these words. A stray double period ("public necessity..") was also normalized. Swept the whole source for further instances: 0 remaining.
- **Authorship:** Hamilton — consistent with the authorship reference in `SERIES-STATUS.md`.
- **Internal consistency:** All counts/dates asserted in the script agree with themselves. Episode numbering ("Twenty-Three," "Twenty-Four," "Twenty-Five," "Twenty-Six"), publication year ("seventeen eighty-seven"), Pearl Harbor year ("nineteen forty-one"), and "two hundred and forty years" are used consistently and match the rest of the series. No contradictions found.
- **Continuity callbacks checked against the actual earlier scripts:** the two-year appropriations leash and "power of the purse" (Ep 24), "energetic" government / means-match-ends (Ep 23), state-rivalry-breeds-war (Eps 6–7), Shays' Rebellion (Eps 6–7), Hamilton at Valley Forge as Washington's aide (Ep 23). All grounded.

## Part B — Web cross-check (all non-quote claims)

| # | Claim | Verdict | Sources |
|---|-------|---------|---------|
| 1 | Fed. No. 25 by Hamilton, New York Packet, Friday Dec 21, 1787 | ✅ Verified | Founders Online (founders.archives.gov Hamilton/01-04-02-0182); Wikipedia "Federalist No. 25". Dec 21, 1787 was a Friday. |
| 2 | 1787: Britain still garrisoned frontier forts on U.S. soil (Northwest); Spain held Florida, Louisiana, New Orleans, controlling the mouth of the Mississippi | ✅ Verified | history.state.gov (Pinckney's Treaty); U. Chicago / State Dept. Britain held the Northwest posts until the Jay Treaty; Spain kept the Mississippi closed until Pinckney's Treaty (1795). |
| 3 | Articles of Confederation (Art. VI) barred states from keeping warships/troops in peacetime without Congress's consent | ✅ Verified | National Archives (Articles of Confederation); press-pubs.uchicago.edu Founders. |
| 4 | Shays' Rebellion (1786–87): Massachusetts raised troops to suppress it without waiting for Congress's sanction, and kept a corps in pay afterward | ✅ Verified | Wikipedia "Shays's Rebellion"; Mount Vernon Digital Encyclopedia. State acted via militia + privately-funded force; the "corps kept in pay" detail is Hamilton's own account in the paper and is consistent with the record. Script attributes it to Hamilton. |
| 5 | Pennsylvania's 1776 Declaration of Rights declared standing armies in peacetime dangerous to liberty and that they ought not be kept up | ✅ Verified | press-pubs.uchicago.edu Founders (Bill of Rights §5); Avalon Project (pa08.asp). Verbatim in Art. XIII. |
| 6 | Sparta barred holding the admiralty twice; after a naval defeat the allies demanded Lysander, and Sparta gave him the real power under a nominal vice-admiral title | ✅ Verified | Britannica "Lysander"; Wikipedia "Lysander". Rule, allied demand, and the epistoleus/vice-admiral workaround (under nominal admiral Aracus) all confirmed. Script keeps the naval defeat unnamed (the prompting defeat was Arginusae, 406 BC; Aegospotami, 405 BC, was Lysander's later victory) — so no dating error is asserted. |
| 7 | By the 18th century the formal ceremony of declaring war before attacking had fallen into disuse | ✅ Verified | Oxford Public International Law; ICRC Casebook. Matches Hamilton's own line. |
| 8 | Pearl Harbor: surprise Japanese attack Dec 7, 1941; strong prior U.S. isolationist sentiment | ✅ Verified | National WWII Museum; Wikipedia "Attack on Pearl Harbor". 1930s Neutrality Acts + isolationist movement preceded U.S. entry. (Used as an illustrative parallel to Hamilton's "receive the blow" point, honestly framed.) |
| 9 | The modern U.S. National Guard is regarded as the organized descendant of the founding-era militia | ✅ Verified | nationalguard.mil "How We Began"; Wikipedia "National Guard (United States)". Lineage to colonial militias (Mass., 1636). |
| 10 | Federalist No. 26 is also Hamilton, on restraining the legislature regarding the common defense | ✅ Verified | Avalon Project (fed26.asp); Wikipedia "Federalist No. 26". Dec 22, 1787. (Used only in the closing teaser.) |
| 11 | Hamilton served as Washington's aide-de-camp for much of the Revolution, incl. Valley Forge | ✅ Verified | NPS; Museum of the American Revolution. Aide-de-camp 1777–1781. |

**Result:** All claims ✅ verified. None wrong, none genuinely contested. Script cleared Gate 4.
