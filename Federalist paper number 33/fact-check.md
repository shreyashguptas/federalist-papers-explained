# Fact-check log — Episode 33 (Federalist No. 33)

Gate 4 of the episode production workflow. Part A verifies quotes and continuity against the
source text and the earlier scripts. Part B cross-checks every non-quote factual claim against
the open web.

**Result: 8 set-apart quotes, all verified. 34 external claims checked: 33 ✅ verified,
1 ⚠️ fairly hedged, 0 ❌ wrong.**

---

## Part A — Source and continuity check

### Quotes from the paper (mechanically verified)

Verified by normalised substring match against `_production/source-texts/federalist-no-33.txt`
(case, punctuation and whitespace normalised; the source's ALL-CAPS emphasis is rendered in
ordinary case in the script, as in every earlier episode). **13 of 13 pass, 0 fail.**

| # | Quote | Verdict |
|---|---|---|
| Q1 | Supremacy clause, *as Hamilton quotes it* ("That the Constitution and the laws of the United States made in pursuance thereof…") | ✅ exact |
| Q2 | The staircase of questions ("What is a power, but the ability or faculty of doing a thing?…") | ✅ exact |
| Q3 | "…would be precisely the same, if these clauses were entirely obliterated, as if they were repeated in every article" | ✅ exact |
| Q4 | "though it may be chargeable with tautology or redundancy, is at least perfectly harmless" | ✅ exact |
| Q5 | "the danger which most threatens our political welfare is that the State governments will finally sap the foundations of the Union" | ✅ exact |
| Q6 | "A law, by the very meaning of the term, includes supremacy. It is a rule which those to whom it is prescribed are bound to observe." | ✅ exact |
| Q7 | "it would otherwise be a mere treaty, dependent on the good faith of the parties" | ✅ exact |
| Q8 | "These will be merely acts of usurpation, and will deserve to be treated as such." | ✅ exact |

Reported speech also checked against the source and confirmed faithful: the "greater caution"
passage; "must judge, in the first instance, of the proper exercise of its powers, and its
constituents in the last"; "an independent and uncontrollable authority to raise revenue…except
duties on imports and exports"; "the only admissible substitute for an entire subordination";
and the "exaggerated colors of misrepresentation / hideous monster" passage.

### Three quote-accuracy problems found in the draft and fixed

1. **Spliced quote (fixed).** The draft ran "A law, by the very meaning of the term, includes
   supremacy…" straight into "It would otherwise be a mere treaty…" as one continuous block.
   In the paper those sentences sit **four sentences apart**. The script now separates them with
   narration and introduces the second as a later line ("And a few lines later he names what you
   would have instead").
2. **Hamilton's rendering presented as the clause (fixed).** The draft introduced Hamilton's
   quotation of the Supremacy Clause as though it were the text of Article VI. It is not: the
   ratified clause reads "This Constitution, and the Laws of the United States which shall be made
   in Pursuance thereof; and all Treaties made, or which shall be made, under the Authority of the
   United States, shall be the supreme Law of the Land; and the Judges in every State shall be
   bound thereby…". The script now says "here is the way Hamilton quotes it in the essay."
3. **Necessary and Proper Clause — deliberately quoted from the Constitution, not the essay.**
   Hamilton's own rendering in the paper is looser than the ratified text ("THE POWERS by that
   Constitution vested" for "the foregoing Powers, and all other Powers vested by this
   Constitution"). The script quotes the **ratified text** from the National Archives transcript
   and frames it as the Constitution, which is correct as written. ✅

### Source-text provenance

`_production/source-texts/federalist-no-33.txt` was created for this episode from the Yale Avalon
Project transcription, verbatim except that Avalon's closing `''` is normalised to `"`, matching
every earlier source file in the series. Avalon's transcription carries three OCR typos
("propermeans", "culumniated", "legitimatb"); none appears inside a quoted passage, and the script
uses the correct spelling "legitimate" in reported speech.

### Internal consistency (script against itself)

Every count, date and interval asserted in the script was extracted and compared. All agree:

- 428 words (Article I, §8) — asserted twice, plus "the four hundred before them"; **counted
  mechanically** from the National Archives transcript
- 39 words (Necessary and Proper Clause) — asserted three times as a deliberate refrain;
  **counted mechanically**
- 1788 → Marbury 1803 = "fifteen years in the future" ✅
- 1791 bank opinion → McCulloch 1819 = "twenty eight years later" ✅
- Jan 1788 → Feb 1791 = "three years forward" / "three years apart" ✅
- **Corrected:** the clause's Convention approval (Aug 1787) to the cabinet split (Feb 1791) was
  written as "three years later"; it is three and a half. Changed to "three and a half years
  later." Swept the whole script for other statements of that interval: 0 further instances.
- "the third time in two essays" — checked against Episode 32: the Tenth Amendment point and the
  necessary-and-proper point are both there, so this is the third. ✅

### Continuity against earlier scripts (checked against the files, not memory)

| Callback | Verdict |
|---|---|
| Brutus, anonymous Antifederalist in a rival New York newspaper, and his three-clause argument (taxing power + supremacy + necessary and proper) | ✅ Ep 31, lines 17–19 |
| "the people hold the scales" at the close of Number 31 | ✅ Ep 31, lines 149–151 |
| Ep 32 proved only that the *taxing clause* is not exclusive, leaving Brutus's real argument unanswered | ✅ Ep 32, line 199 |
| Nos. 32 and 33 ran in the same issue, "the next column on the page" | ✅ Ep 32, line 201 |
| Tenth Amendment as the written-down version of what Hamilton called already true | ✅ Ep 32, lines 59–61 |
| McCulloch v. Maryland covered last episode (the state-taxation half) | ✅ Ep 32, lines 179–195 |
| Jay wrote Federalist Nos. 2 through 5 on a divided America as prey to the outside world | ✅ Eps 2–5 |
| "The states did not sap the foundations of the union… both governments grew enormous together" | ✅ Ep 31, lines 135–139 |

---

## Part B — Web cross-check of non-quote claims

### Publication and the paper itself

| # | Claim | Verdict | Source |
|---|---|---|---|
| 1 | No. 33 first published 2 January 1788 in the *Independent Journal* | ✅ | [Wikipedia: Federalist No. 33](https://en.wikipedia.org/wiki/Federalist_No._33); [Founders Online](https://founders.archives.gov/documents/Hamilton/01-04-02-0190) |
| 2 | Nos. 32 and 33 appeared in the same issue, under the same title, as one continuous essay; the split into two numbered essays came with the later book edition | ✅ | [Founders Online, No. 32](https://founders.archives.gov/documents/Hamilton/01-04-02-0189); [Tara Ross, "The Federalist Papers: Nos. 32 & 33"](https://www.taraross.com/post/the-federalist-papers-no-32-33) |
| 3 | Hamilton locates the clause as "the last clause of the eighth section of the first article" | ✅ | It is clause 18 of 18 in Art. I §8 — [National Archives transcript](https://www.archives.gov/founding-docs/constitution-transcript) |

### The cold open

| # | Claim | Verdict | Source |
|---|---|---|---|
| 4 | Article I, Section 8 is 428 words long | ✅ | Counted mechanically from the [National Archives transcript](https://www.archives.gov/founding-docs/constitution-transcript) |
| 5 | The Necessary and Proper Clause is 39 words | ✅ | Same; counted mechanically |
| 6 | 428 words read aloud takes about three minutes | ✅ | At the series' own measured narration rate of ~156 words/minute, 428 words = 2 min 45 s |
| 7 | The U.S. Code has 54 titles | ✅ | [Office of the Law Revision Counsel](https://uscode.house.gov/about_code.xhtml) — "54 titles and five appendices" |
| 8 | Congress runs an air force, though Art. I §8 mentions only armies and a navy | ✅ | Direct reading of the [transcript](https://www.archives.gov/founding-docs/constitution-transcript): clauses 12–14 cover armies, navy, and land and naval forces; no air force |
| 9 | Opponents nicknamed it "the sweeping clause" | ✅ | [Constitution Annotated, Historical Background on the Necessary and Proper Clause](https://www.law.cornell.edu/constitution-conan/article-1/section-8/clause-18/historical-background-of-the-necessary-and-proper-clause) |
| 10 | Patrick Henry attacked it at the Virginia ratifying convention | ✅ | His own words, June 1788: "cannot they make it by this sweeping clause?" — [Virginia Ratifying Convention, 16 June 1788](https://constitution.org/1-Constitution/rc/rat_va_13.htm); [ConSource](https://www.consource.org/document/journal-notes-of-the-virginia-ratification-convention-proceedings-1788-6-16/) |

### The Convention set-piece

| # | Claim | Verdict | Source |
|---|---|---|---|
| 11 | Convention referred its resolutions to the Committee of Detail on 26 July 1787 | ✅ | [Constitution Annotated, Necessary and Proper Clause historical background](https://www.law.cornell.edu/constitution-conan/article-1/section-8/clause-18/historical-background-of-the-necessary-and-proper-clause) |
| 12 | The Committee replaced a single general grant of legislative power with an enumerated list, followed by the Necessary and Proper Clause | ✅ | Same |
| 13 | The Committee reported its draft on 6 August 1787 | ✅ | Same |
| 14 | The Convention approved the Necessary and Proper Clause unanimously on 20 August 1787, with no substantial debate | ✅ | Same; and [NPS, Constitutional Convention August 20](https://home.nps.gov/articles/000/constitutionalconvention-august20.htm) |
| 15 | William Paterson introduced the New Jersey Plan on 15 June 1787 | ✅ | [Britannica](https://www.britannica.com/topic/New-Jersey-Plan); [NPS, The New Jersey Plan](https://www.nps.gov/inde/learn/historyculture/the-new-jersey-plan.htm) |
| 16 | It was the small states' counterproposal and kept the basic shape of the Articles rather than replacing it | ✅ | [Britannica](https://www.britannica.com/topic/New-Jersey-Plan) — preserved state equality, retained the Articles' form while adding revenue and commerce powers. **Draft said "kept the national government deliberately weak"; corrected**, because the plan did add powers to Congress |
| 17 | The New Jersey Plan contained an early supremacy provision | ✅ | [Constitution Annotated, Supremacy Clause and the Convention](https://www.law.cornell.edu/constitution-conan/article-6/clause-2/the-supremacy-clause-and-the-constitutional-convention) — quotes the plan's text |
| 18 | The Convention rejected the New Jersey Plan | ✅ | [Britannica](https://www.britannica.com/topic/New-Jersey-Plan) — Virginia Plan chosen 19 June 1787 |
| 19 | Luther Martin moved the supremacy provision on 17 July 1787 and it was adopted unanimously | ✅ | [Constitution Annotated](https://www.law.cornell.edu/constitution-conan/article-6/supremacy-clause-and-the-constitutional-convention); [NPS, July 17](https://www.nps.gov/articles/000/constitutionalconvention-july17.htm); Madison's Notes for that day |
| 20 | Martin walked out, refused to sign, wrote *The Genuine Information*, and became a leading Antifederalist | ✅ | [Encyclopedia.com: Martin, Luther](https://www.encyclopedia.com/politics/encyclopedias-almanacs-transcripts-and-maps/martin-luther-1748-1826); [Luther Martin, Letter on the Federal Convention](https://constitution.org/1-Constitution/je/lumarltr.htm) |
| 21 | Martin came to regard the amended supremacy clause as "worse than useless" | ✅ | Martin's own characterisation, reported in [Constitutional Compromise and the Supremacy Clause, *Notre Dame L. Rev.*](https://scholarship.law.nd.edu/cgi/viewcontent.cgi?article=1262&context=ndlr) |

### The Jay / Treaty of Paris set-piece

| # | Claim | Verdict | Source |
|---|---|---|---|
| 22 | Treaty of Paris signed 1783; Article 4 barred lawful impediments to creditors recovering debts | ✅ | Verbatim: "It is agreed that Creditors on either Side shall meet with no lawful Impediment to the Recovery of the full Value in Sterling Money of all bona fide Debts heretofore contracted." — [Avalon Project](https://avalon.law.yale.edu/18th_century/paris.asp); [National Archives](https://www.archives.gov/milestone-documents/treaty-of-paris) |
| 23 | State legislatures and courts blocked British creditors and states confiscated Loyalist property in violation of the treaty | ✅ | [Encyclopedia.com: British Debts](https://www.encyclopedia.com/history/dictionaries-thesauruses-pictures-and-press-releases/british-debts) |
| 24 | Britain retained the northwestern frontier forts, citing American violations, and kept its hold on the fur trade | ✅ | [Office of the Historian, Jay Treaty](https://history.state.gov/milestones/1784-1800/jay-treaty) |
| 25 | Jay was Secretary for Foreign Affairs and laid his report before Congress on 13 October 1786 | ✅ | [Founders Online, John Jay Papers](https://founders.archives.gov/documents/Jay/01-04-02-0157) |
| 26 | Jay's line to John Adams: "there has not been a single day since it took effect, on which it has not been violated in America, by one or other of the States" | ✅ | Jay to Adams, 1 November 1786 — [Founders Online](https://founders.archives.gov/documents/Jay/01-04-02-0157); [Columbia, The Papers of John Jay](https://dlc.library.columbia.edu/jay/jay_constitution) |
| 27 | Congress resolved on 21 March 1787 that a ratified treaty is part of the law of the land, binding on the states, and that no state legislature may pass acts construing or impeding it | ✅ | [The Founders' Constitution, Art. 6 cl. 2](https://press-pubs.uchicago.edu/founders/tocs/a6_2.html); [Constitution Annotated, Treaties as Law of the Land](https://law.justia.com/constitution/us/article-2/16-treaties-as-law-of-the-land.html) |
| 28 | A circular letter to the states, drafted by Jay, was agreed on 13 April 1787 asking them to repeal repugnant laws | ✅ | Same sources |
| 29 | That episode fed directly into Article VI, clause 2 | ✅ | [Constitution Annotated, Treaties as Law of the Land](https://law.justia.com/constitution/us/article-2/16-treaties-as-law-of-the-land.html) — the draftsmen carried the March 1787 resolution's subject matter into the supremacy clause |

### The bank set-piece

| # | Claim | Verdict | Source |
|---|---|---|---|
| 30 | The bank bill passed Congress in February 1791; the constitutional objection was that no clause authorises Congress to create a corporation | ✅ | [Wikipedia: Bank Bill of 1791](https://en.wikipedia.org/wiki/Bank_Bill_of_1791) |
| 31 | Jefferson delivered his opinion 15 February 1791, reading "necessary" as those means without which the grant would be "nugatory," not those "merely convenient" | ✅ | Verbatim from the opinion — [Avalon Project](https://avalon.law.yale.edu/18th_century/bank-tj.asp); [Founders Online](https://founders.archives.gov/documents/Jefferson/01-19-02-0051) |
| 32 | Attorney General Edmund Randolph also found the bill unconstitutional | ⚠️ **hedged in the script** | [Constituting America](https://constitutingamerica.org/role-congress-creation-constitutionality-national-bank-part-2-guest-essayist-tony-williams/) reports Randolph declared it unconstitutional; the same source notes he wrote *two* essays, one against the Bank and one that did not take a clear position. The script says only "Edmund Randolph, the Attorney General, agreed with him," which is the mainstream account and does not overstate the firmness of his position |
| 33 | Hamilton delivered his opinion 23 February 1791; "necessary often means no more than needful, requisite, incidental, useful, or conducive to" | ✅ | Verbatim — [Avalon Project, Hamilton's Opinion](https://avalon.law.yale.edu/18th_century/bank-ah.asp) |
| 34 | Hamilton's three-part test (end within a specified power; measure has an obvious relation to that end; not forbidden) | ✅ | Verbatim in the same opinion; paraphrased in the script rather than quoted, to hold the set-apart quote count at 8 |
| 35 | Washington signed the bank bill on 25 February 1791 | ✅ | [Constituting America](https://constitutingamerica.org/role-congress-creation-constitutionality-national-bank-part-2-guest-essayist-tony-williams/); [Wikipedia: Bank Bill of 1791](https://en.wikipedia.org/wiki/Bank_Bill_of_1791) |

### McCulloch, judicial review, and the modern boundary

| # | Claim | Verdict | Source |
|---|---|---|---|
| 36 | McCulloch v. Maryland decided 1819 | ✅ | [Justia, 17 U.S. 316](https://supreme.justia.com/cases/federal/us/17/316/) |
| 37 | Marshall noted the clause sits among Congress's powers (§8), not among the limitations (§9) | ✅ | [Constitution Annotated, Early Doctrine and McCulloch](https://www.law.cornell.edu/constitution-conan/article-1/section-8/clause-18/the-necessary-and-proper-clause-doctrine-early-doctrine-and-mcculloch-v-maryland); [Wikipedia: Necessary and Proper Clause](https://en.wikipedia.org/wiki/Necessary_and_Proper_Clause) |
| 38 | The Articles of Confederation reserved to the states powers not "expressly delegated"; the Tenth Amendment drops "expressly," and Marshall said the omission was deliberate | ✅ | Marshall: "The men who drew and adopted this amendment had experienced the embarrassments resulting from the insertion of this word in the articles of confederation, and probably omitted it to avoid those embarrassments." — [Constitution Annotated, Early Tenth Amendment Jurisprudence](https://www.law.cornell.edu/constitution-conan/amendment-10/tenth-amendment-early-doctrine) |
| 39 | Marshall's "Let the end be legitimate…" passage, quoted verbatim | ✅ | [Constitution Annotated](https://www.law.cornell.edu/constitution-conan/article-1/section-8/clause-18/the-necessary-and-proper-clause-doctrine-early-doctrine-and-mcculloch-v-maryland) |
| 40 | Marbury v. Madison (1803) is fifteen years after January 1788; Hamilton takes up judicial review later, in Federalist No. 78 | ✅ | [Wikipedia: Federalist No. 78](https://en.wikipedia.org/wiki/Federalist_No._78) — published 28 May 1788, argues courts must "declare all acts contrary to the manifest tenor of the Constitution void" |
| 41 | In 2012 the Supreme Court held the Necessary and Proper Clause did not authorise the individual mandate: the clause supplies means for exercising a power already held, not the power itself | ✅ | [NFIB v. Sebelius, 567 U.S. 519](https://supreme.justia.com/cases/federal/us/567/519/); [CRS R42698](https://www.congress.gov/crs_external_products/R/PDF/R42698/R42698.3.pdf) |

### Next-episode preview

| # | Claim | Verdict | Source |
|---|---|---|---|
| 42 | Federalist No. 34 uses the Roman republic's two independent legislative bodies as proof two concurrent authorities can coexist | ✅ | The paper names the COMITIA CENTURIATA and COMITIA TRIBUTA as "two different political bodies not as branches of the same legislature, but as distinct and independent authorities" — [Avalon Project, Federalist 34](https://avalon.law.yale.edu/18th_century/fed34.asp) |
| 43 | No. 34 argues future needs, not present ones, are the right measure, and that war costs dwarf peacetime civil costs | ✅ | Same: constitutions are framed on "the probable exigencies of ages," and the expenses of the civil establishment are "circumscribed within very moderate bounds" |
| 44 | Federalist No. 34 published 5 January 1788 | ✅ | [Wikipedia: Federalist No. 34](https://en.wikipedia.org/wiki/Federalist_No._34) |

---

## Claims deliberately cut during fact-checking

- **"The bank became the Federal Reserve."** Cut. The lineage runs First Bank → Second Bank →
  charter lapses 1836 → national banking acts → Federal Reserve 1913; calling it one institution
  becoming another overstates a real but indirect descent. The script now says only that the
  clause is what lets the modern federal government do what it does.
- **The Sixteenth Amendment / 1913 income tax as "the largest single step."** Cut from this
  episode. It is stated in Episode 31 and repeating it here added length without adding anything.

## Corrections made, and the sweep for repeats

| Correction | Repeats found elsewhere in the script |
|---|---|
| "three years later" → "three and a half years later" (Convention → cabinet split) | 0 |
| New Jersey Plan "kept the national government deliberately weak" → "kept the basic shape of the Articles of Confederation rather than replacing it" | 0 |
| Spliced supremacy quote separated into two, four sentences apart as in the paper | 0 other spliced quotes; all 8 re-verified as contiguous substrings |
| Hamilton's rendering of the Supremacy Clause labelled as his rendering | 0 |
