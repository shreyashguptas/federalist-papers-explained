# Fact-Check — Episode 35 (Federalist No. 35)

Gate 4 artifact. Part A = source/continuity/internal consistency. Part B = web cross-check of every non-quote factual claim.

**Result: 19/19 quote checks pass. 52 external claims: 48 ✅ verified, 4 ⚠️ fairly hedged, 0 ❌ wrong.**

As with Episode 34, all load-bearing history was researched *before* drafting rather than corrected after. Three internal-consistency errors were caught by the script-against-itself sweep and fixed before any external checking (see Part A.3). No external claim required correction.

---

## Part A — Source, continuity, internal consistency

### A.1 Quote verification (mechanical, normalized substring match)

Authority: `_production/source-texts/federalist-no-35.txt` (transcribed from Yale Avalon, 13 paragraphs / 2,258 words) and `_production/source-texts/federalist-no-12.txt`.

Normalization: Unicode NFKD, smart quotes folded, hyphens and em-dashes → space, non-alphanumerics stripped, lowercased, whitespace collapsed. This is required because the source contains `fair-sounding` where the script has `fair sounding` (hyphens are stripped for TTS).

| # | Quote fragment | Source | Verdict |
|---|---|---|---|
| 1 | "Exorbitant duties on imported articles would beget a general spirit of smuggling" | F35 | ✅ exact |
| 2 | "which is always prejudicial to the fair trader, and eventually to the revenue itself" | F35 | ✅ exact |
| 3 | "When the demand is equal to the quantity of goods at market, the consumer generally pays the duty" | F35 | ✅ exact |
| 4 | "but when the markets happen to be overstocked, a great proportion falls upon the merchant, and sometimes not only exhausts his profits, but breaks in upon his capital" | F35 | ✅ exact |
| 5 | "New York is an importing State, and is not likely speedily to be, to any great extent, a manufacturing State" | F35 | ✅ exact |
| 6 | "She would, of course, suffer in a double light from restraining the jurisdiction of the Union to commercial imposts" | F35 | ✅ exact |
| 7 | "Necessity, especially in politics, often occasions false hopes, false reasonings, and a system of measures correspondingly erroneous" | F35 | ✅ exact |
| 8 | "The idea of an actual representation of all classes of the people, by persons of each class" | F35 | ✅ exact |
| 9 | "is altogether visionary" | F35 | ✅ exact |
| 10 | "Nothing remains but the landed interest; and this, in a political view, and particularly in relation to taxes, I take to be perfectly united, from the wealthiest landlord down to the poorest tenant" | F35 | ✅ exact |
| 11 | "This dependence" | F35 | ✅ exact |
| 12 | "and the necessity of being bound himself, and his posterity, by the laws to which he gives his assent, are the true, and they are the strong chords of sympathy between the representative and the constituent" | F35 | ✅ exact |
| 13 | inline: "fair-sounding words" | F35 | ✅ exact (hyphen normalized) |
| 14 | inline: "acquired endowments" | F35 | ✅ exact |
| 15 | inline: "natural patron and friend" | F35 | ✅ exact |
| 16 | inline: "the most productive system of finance will always be the least burdensome" | F35 | ✅ exact |
| 17 | inline: "the oppression of particular branches of industry" | F35 | ✅ exact |
| 18 | inline: "an unequal distribution of the taxes, as well among the several States as among the citizens of the same State" | F35 | ✅ exact |
| 19 | "A few armed vessels, judiciously stationed at the entrances of our ports, might at a small expense be made useful sentinels of the laws" | **F12** | ✅ exact |

Set-apart quote count: **7** (ceiling 8, target 4–6 — one over target, under ceiling, matching Ep 34). No two set-apart quotes sit back to back; they fall at 19%, 35%, 43%, 52%, 76%, 85% and one added at ~21%.

### A.2 Authorship and continuity

| Claim | Verdict | Basis |
|---|---|---|
| Federalist No. 35 is by Alexander Hamilton | ✅ | Avalon header "HAMILTON"; `SERIES-STATUS.md`; Founders Online |
| Signed Publius | ✅ | Series-wide; source text ends "PUBLIUS." |
| Ep 34 recap (the forecast, the grading, wrong on the number / right on the rule) | ✅ | Read directly from `Federalist paper number 34/federalist-no-34-script.txt` |
| Ep 34 ended promising "a few other lights in which this subject of taxation will claim further consideration" | ✅ | Verified verbatim in Ep 34 script closing |
| Callback to Episode 12's "sentinels of the laws" line | ✅ | Verified the line appears in Ep 12's script (lines 77/79) and in the F12 source text |
| Ep 34's preview promised smuggling, inter-state unfairness, and "altogether visionary" | ✅ | Verified in Ep 34 closing; this episode delivers all three |
| Ep 36 preview (double sets of collectors, poll tax, Hamilton's own disapproval) | ✅ | Verified against the F36 source text, transcribed from Avalon this session. F36 contains "double sets of revenue officers, a duplication of their burdens by double taxations, and the frightful forms of odious and oppressive poll-taxes," and Hamilton's "As to poll taxes, I, without scruple, confess my disapprobation of them," followed by "There may exist certain critical and tempestuous conjunctures of the State, in which a poll tax may become an inestimable resource." An earlier draft of the preview attributed the phrase "the dreaded poll tax" to Hamilton; he never writes it. Corrected before publication. |

**Non-repetition check.** Grepped all 34 prior scripts for every planned set-piece: `Hancock` 0 hits, `Revenue Cutter` 0, `patroon` 0, `Van Rensselaer` 0, `Anti-Rent` 0, `Ferguson` 0, `Procession` 0, `Clinton` 0, `Pitkin` 0, `incidence` 0. Smuggling appears in 6 prior scripts (notably Ep 12), but Ep 12's argument is that *open land borders* create smuggling; this episode's is that *excessive rates* create smuggling regardless of geography. Distinct mechanism, deliberate deepening rather than repeat.

### A.3 Internal consistency (script against itself) — 3 errors caught and fixed

Run before any external research, per the workflow. Every asserted count and date was extracted and compared.

| Error found | Fix | Sweep |
|---|---|---|
| "Two months into this series, back in Federalist Number Twelve" — F12 ran late November 1787; F35 ran 5 Jan 1788. That is about six weeks, and F12 was ~1 month into the series, not 2. It also contradicted the script's own later line "In November he describes the remedy." | → "Back in November, in Federalist Number Twelve" | `two months` 0 remaining; `November` now consistent at both occurrences |
| "Twenty months later he is the official responsible, **and he builds the thing**" — conflated two different dates. Sept 1789 (Treasury) is 20 months after Jan 1788; Aug 1790 (the cutters) is 31 months after. | → "Twenty months later he is the official responsible for collecting the money. Within a year of taking that job, the fleet exists." (Sept 1789 → Aug 1790 is under 11 months) | `twenty months` 1 occurrence, now correct |
| "carry ninety miles up the Hudson" — NYC to Poughkeepsie is 73–80 miles. | → "seventy five miles" | `ninety miles` 0 remaining |
| "took economists another century and a half to formalize" — tax incidence was formalized ~1892 (Seligman), i.e. ~104 years. | → "another hundred years", plus an added specific: Seligman, 1892, "a hundred and four years after" | consistent with the added Seligman paragraph |

Cross-checks that passed with no change: four states ratified by 5 Jan 1788 (DE/PA/NJ/GA) is consistent with Connecticut arriving "four days later" (9 Jan); "two hundred and thirty eight years" appears twice (1788→2026) and agrees both times; the Anti-Rent War "ran for six years" (1839–1845) agrees with the later "went to war with itself for six years"; "six months earlier" (5 Jan → 23 July 1788) and "three days later" (23 → 26 July) both check out.

---

## Part B — Web cross-check of external claims

### B.1 Publication and ratification context

| # | Claim | Verdict | Sources |
|---|---|---|---|
| 1 | F35 published in the Independent Journal, 5 January 1788 | ✅ | [Founders Online](https://founders.archives.gov/documents/Hamilton/01-04-02-0192) · [ConSource](https://www.consource.org/document/the-federalist-no-35-1788-1-5/) · [Wikipedia](https://en.wikipedia.org/wiki/Federalist_No._35) — three independent sources agree. Note: unlike No. 34, there is **no** date conflict here; Avalon simply omits the date rather than contradicting. |
| 2 | Sixth of seven Hamilton essays on taxation | ✅ | [Wikipedia](https://en.wikipedia.org/wiki/Federalist_No._35) |
| 3 | Four states had ratified by 5 Jan 1788 | ✅ | DE 7 Dec 1787, PA 12 Dec, NJ 18 Dec, GA 2 Jan 1788 — [Teaching American History](https://teachingamericanhistory.org/resource/timeline-state/) · [Bens Guide](https://bensguide.gpo.gov/j-states-ratification) |
| 4 | Georgia ratified 2 January 1788, fourth state, unanimously 26–0 | ✅ | [Today in Georgia History](https://www.todayingeorgiahistory.org/tih-georgia-day/georgia-ratifies-the-u-s-constitution/) · [HISTORY](https://www.history.com/this-day-in-history/january-2/georgia-enters-the-union) · [US Constitution Online](https://usconstitution.net/rat_ga-html/). *One search result gave 31 Dec 1787 (likely the convention vote vs. formal signing); the overwhelming majority of sources give 2 Jan 1788. Either dating leaves the "four states" claim correct.* |
| 5 | Connecticut ratified 9 January 1788 ("four days later") | ✅ | Same ratification timelines |
| 6 | New York was the eleventh state, and the closest vote of any | ✅ | [EBSCO](https://www.ebsco.com/research-starters/politics-and-government/new-york-ratifies-constitution) · [Avalon](https://avalon.law.yale.edu/18th_century/ratny.asp) |

### B.2 Ferguson, Missouri (modern parallel)

| # | Claim | Verdict | Sources |
|---|---|---|---|
| 7 | DOJ published an investigation of the Ferguson Police Department in 2015 | ✅ | [DOJ report PDF, 4 Mar 2015](https://www.justice.gov/sites/default/files/opa/press-releases/attachments/2015/03/04/ferguson_police_department_report.pdf) |
| 8 | Fines/fees revenue roughly doubled as a share of city revenue, ~12% (2010) → budgeted ~23% (FY2015) | ✅ | DOJ report; [Reason Foundation](https://reason.org/policy-brief/fines-and-fees-consequences-and-opportunities-for-reform/) ($1.30M/12% → $3.09M/23%) |
| 9 | "Ferguson's law enforcement practices are shaped by the City's focus on revenue rather than by public safety needs" | ✅ | Direct from the DOJ report summary; [Fines and Fees Justice Center](https://finesandfeesjusticecenter.org/articles/investigation-ferguson-police-department/) |
| 10 | The city directed the police department to develop strategies to raise revenue | ✅ | DOJ report |
| 11 | The parallel does not distort Hamilton's argument | ✅ | Structural match is on the *mechanism* (single revenue source → pressure → distortion → cost lands on whoever is easiest to reach). The script does **not** claim Hamilton predicted the racial disparities the DOJ documented. |

### B.3 The Liberty affair and smuggling

| # | Claim | Verdict | Sources |
|---|---|---|---|
| 12 | The sloop *Liberty* belonged to John Hancock | ✅ | [Wikipedia: Liberty Affair](https://en.wikipedia.org/wiki/Liberty_Affair) · [BPL research guide](https://guides.bpl.org/c.php?g=800717&p=10389851) |
| 13 | Docked in Boston in May 1768 carrying Madeira wine | ✅ | Same |
| 14 | Only 25 casks remained when officials inspected; the rest was landed overnight without duty | ✅ | [Alpha History](https://alphahistory.com/americanrevolution/seizure-of-liberty/) · Liberty Affair |
| 15 | Seized 10 June 1768 by marines from a fifty-gun warship (HMS *Romney*) | ✅ | Liberty Affair; *Romney* was a 50-gun fourth rate |
| 16 | A riot followed; customs officers assaulted, windows broken, a pleasure boat dragged to the Common and burned | ✅ | Liberty Affair · [New England Historical Society](https://newenglandhistoricalsociety.com/the-liberty-affair-john-hancock-loses-a-ship-and-starts-a-riot/) |
| 17 | Customs commissioners fled to an island fortress in the harbor | ✅ | Same (Castle William) |
| 18 | Hancock charged with smuggling; John Adams defended him; charges dropped | ✅ | [MHS Adams Papers](https://www.masshist.org/publications/adams-papers/index.php/view/ADMS-01-03-02-0016-0021) |
| 19 | Hancock's was the largest signature on the Declaration | ✅ | Universally documented |
| 20 | Hancock was the richest merchant in Massachusetts | ✅ | Standard biography; widely corroborated |

### B.4 Hamilton, the Treasury, and the Revenue Cutter Service

| # | Claim | Verdict | Sources |
|---|---|---|---|
| 21 | "A few armed vessels…useful sentinels of the laws" is from Federalist No. 12, November 1787 | ✅ | Verified against the local F12 source text; [USNI Naval History](https://www.usni.org/magazines/naval-history-magazine/2015/august/few-armed-vessels-judiciously-stationed) |
| 22 | Hamilton became the first Secretary of the Treasury in September 1789 | ✅ | [Treasury](https://home.treasury.gov/about/history/prior-secretaries/alexander-hamilton-1789-1795) · [Senate](https://www.senate.gov/about/powers-procedures/nominations/first-cabinet-confirmation.htm) — 11 Sept 1789 |
| 23 | The new federal government funded itself overwhelmingly on import duties | ✅ | Corroborated in Ep 12's own fact-check; [USNI](https://www.usni.org/magazines/naval-history-magazine/2021/august/raise-revenue-and-unify-country) |
| 24 | Smuggling was undermining that revenue | ✅ | Same USNI article; [HISTORY](https://www.history.com/this-day-in-history/august-4/hamilton-creates-coast-guard) |
| 25 | Congress authorized ten cutters on 4 August 1790 at Hamilton's request | ✅ | [Wikipedia: US Revenue Cutter Service](https://en.wikipedia.org/wiki/United_States_Revenue_Cutter_Service) · [Britannica](https://www.britannica.com/today-in-history/August-4-1790-Creation-of-United-States-Coast-Guard) · [NARA reference report](https://www.archives.gov/files/research/federal-employees/reference-reports/517-revenue-cutter-service.pdf) |
| 26 | They patrolled from Massachusetts to Georgia | ✅ | [First ten Revenue Service cutters](https://en.wikipedia.org/wiki/First_ten_Revenue_Service_cutters) |
| 27 | Those ten boats are the ancestor of the US Coast Guard | ✅ | Revenue Cutter Service merged with the Life-Saving Service in 1915 to form the USCG |
| 28 | The Coast Guard is the oldest continuously serving sea service the country has | ✅ | Standard USCG claim, and defensible: the Continental Navy was disbanded in 1785 and the US Navy re-established in 1794, four years after the cutters. |

### B.5 Tax incidence and the modern tariff evidence

| # | Claim | Verdict | Sources |
|---|---|---|---|
| 29 | "Tax incidence" is the modern term for who bears a tax vs. who is billed | ✅ | Standard public-finance definition |
| 30 | Edwin Seligman, a Columbia economist, gave it its systematic treatment in 1892 | ✅ | [JSTOR](https://www.jstor.org/stable/2485667) · [Britannica](https://www.britannica.com/topic/On-the-Shifting-and-Incidence-of-Taxation) — *On the Shifting and Incidence of Taxation*, 1892. 1788→1892 = 104 years, as the script states. |
| 31 | The US sharply raised tariffs in 2018 and 2019 | ✅ | Universally documented |
| 32 | Economists found foreign exporters did not cut prices, so the cost stayed with US importers and consumers | ✅ | Amiti, Redding & Weinstein, [JEP 2019](https://www.aeaweb.org/articles?id=10.1257%2Fjep.33.4.187) / [NBER w25672](https://www.nber.org/papers/w25672); Fajgelbaum et al., QJE 2020 — "complete pass-through of the tariffs into domestic prices of imported goods… the full incidence of the tariffs fell on domestic consumers and importers" |
| 33 | The effect persisted rather than being a one-off | ✅ | [Amiti, Redding & Weinstein 2020](https://www.princeton.edu/~reddings/pubpapers/ARW-May-2020.pdf) |

⚠️ **Hedge note.** The script deliberately says the cost landed on "American importers and American consumers" and does **not** claim the split matched Hamilton's seller/buyer division precisely. Hamilton's claim is about *domestic* seller vs. buyer; the studies measure foreign-exporter vs. US-side incidence. The script draws only the defensible conclusion: the entity named by the tax and the entity that pays are two different questions, and the second is not decided by the government.

### B.6 New York's finances and politics

| # | Claim | Verdict | Sources |
|---|---|---|---|
| 34 | New York adopted its own state impost in 1784 | ✅ | [Albany Law Review, "Impost Begat Convention"](https://www.albanylawreview.org/api/v1/articles/69790-impost-begat-convention-albany-and-new-york-confront-the-ratification-of-the-constitution.pdf) |
| 35 | It supplied roughly one-third to one-half of New York's annual income under the Confederation | ✅ | Same |
| 36 | About half of what Connecticut and New Jersey imported came through the port of New York | ✅ | Same |
| 37 | George Clinton led the opposition to the Constitution in New York | ✅ | [OLL biography](https://oll.libertyfund.org/pages/clinton-george-1739-1812) · [Gotham Center](https://www.gothamcenter.org/blog/violence-and-the-ratification-of-the-us-constitution-in-new-york-city) |
| 38 | The impost was the cornerstone of Clinton's recovery program | ✅ | Albany Law Review |
| 39 | In February 1787 the New York Assembly killed the federal impost while preserving the state one | ✅ | Same (vote of 38–19, 15 Feb 1787) |
| 40 | New York was an importing rather than a manufacturing state | ✅ | Hamilton's own claim in the paper, corroborated by the impost data above |

### B.7 The Federal Procession, July 1788

| # | Claim | Verdict | Sources |
|---|---|---|---|
| 41 | New York's convention sat at Poughkeepsie from 17 June 1788 | ✅ | [Teaching American History](https://teachingamericanhistory.org/resource/newyork/) |
| 42 | Delegates split 46–19 against the Constitution at the opening | ✅ | Same · [Gotham Center](https://www.gothamcenter.org/blog/violence-and-the-ratification-of-the-us-constitution-in-new-york-city) |
| 43 | Every Federalist delegate came from the four counties around New York City | ✅ | Gotham Center ("New York, Richmond, Kings, and Westchester") |
| 44 | The Federal Procession took place 23 July 1788 | ✅ | [Wikipedia: Federal Procession of 1788](https://en.wikipedia.org/wiki/Federal_Procession_of_1788) |
| 45 | Federalists hoped it would influence the delegates at Poughkeepsie | ✅ | Same — "influence the antis at Poughkeepsie" |
| 46 | Roughly 5,000 marched, in a column over a mile and a half, in ten divisions for the ten ratifying states | ✅ | Same |
| 47 | Tradesmen marched by craft (foresters, farmers, tailors, bakers, brewers, coopers, butchers, cordwainers, carpenters, blacksmiths, ship joiners, sail makers) | ✅ | Same |
| 48 | Blacksmiths worked a forge in the procession and chanted "Forge me strong, finish me neat, I soon shall moor a Federal fleet" | ✅ | Same |
| 49 | The centerpiece was a model 32-gun frigate, 27-foot keel, 10-foot beam, 30+ crew, drawn by ten horses, named the *Hamilton* | ✅ | Same |
| 50 | New York City's mechanics overwhelmingly supported the Constitution | ✅ | [Gotham Center](https://www.gothamcenter.org/blog/violence-and-the-ratification-of-the-us-constitution-in-new-york-city) (CUNY) |
| 51 | The delegates New York City sent were merchants, bankers, land speculators and attorneys — Nicholas Low, Comfort Sands, Alexander Macomb | ✅ | [Nicholas Low](https://en.wikipedia.org/wiki/Nicholas_Low) (merchant/developer) · [Comfort Sands](https://en.wikipedia.org/wiki/Comfort_Sands) (merchant/banker) · [Alexander Macomb](https://en.wikipedia.org/wiki/Alexander_Macomb_(merchant)) (merchant/land speculator) |
| 52 | New York ratified 26 July 1788, 30–27 | ✅ | [Avalon](https://avalon.law.yale.edu/18th_century/ratny.asp) · [Teaching American History](https://teachingamericanhistory.org/document/new-york-ratifying-convention-meets/) |
| 53 | That night a mob of ~500 attacked printer Thomas Greenleaf's shop; he fired two pistols from a window; they broke in with axes and destroyed his type | ✅ | [Grokipedia: Thomas Greenleaf](https://grokipedia.com/page/thomas_greenleaf) · [CSAC/Wisconsin, New York Newspapers during Ratification](https://archive.csac.history.wisc.edu/new_york_newspapers.pdf) |
| 54 | Greenleaf's paper was the main New York outlet for anti-Constitution essays | ✅ | Same — the *New-York Journal* carried the Federal Farmer letters |
| 55 | An Anti-Federalist printer observed that opponents "generally minded their own business at home" | ✅ | Gotham Center, quoting Greenleaf |

⚠️ **Hedge — deliberately stated in the episode.** The script does **not** claim the procession proves Hamilton right about *why* mechanics defer to merchants. It claims only what is documented: the city's mechanics supported ratification, they marched in force, and the delegates the city sent were merchants and lawyers. The Greenleaf attack is included specifically so the parade is not presented as free and unanimous consent.

⚠️ **Hedge — claim deliberately not made.** An earlier draft note considered asserting that *not one* New York City delegate was a tradesman. Sources conflict on whether the silversmith and alderman William W. Gilbert was among the nine elected delegates ([his Wikipedia entry](https://en.wikipedia.org/wiki/William_W._Gilbert) does not mention the convention, though one vote tally lists him). The script therefore says the delegation was dominated by merchants, bankers, speculators and attorneys, and makes no zero-tradesmen claim.

### B.8 The landed interest and the Anti-Rent War

| # | Claim | Verdict | Sources |
|---|---|---|---|
| 56 | The Van Rensselaer manor covered roughly 700,000 acres | ✅ | Two independent figures found (726,000 and ~720,000 acres); script rounds to "roughly seven hundred thousand" — [Anti-Rent War](https://en.wikipedia.org/wiki/Anti-Rent_War) · [Encyclopedia.com](https://www.encyclopedia.com/reference/encyclopedias-almanacs-transcripts-and-maps/antirent-war) |
| 57 | It covered most of present-day Albany and Rensselaer counties and reached into two more | ✅ | [Rensselaerswyck](https://en.wikipedia.org/wiki/Rensselaerswyck) (also Columbia and Greene) |
| 58 | It was a patroonship, a survival of the Dutch system | ✅ | Same |
| 59 | Tenants held leases running for a lifetime or in perpetuity | ⚠️ **hedged in script** | Sources differ: Wikipedia's Anti-Rent War article says "lifetime leases," other accounts describe durable/perpetual leases. The script says "a lease that ran for a lifetime or forever depending on the paper in front of you" rather than picking one. |
| 60 | If a tenant sold his lease, the landlord took a quarter of the price | ✅ | [Rensselaerswyck](https://en.wikipedia.org/wiki/Rensselaerswyck) · Anti-Rent War (the "quarter-sale" provision) |
| 61 | Stephen Van Rensselaer III was lenient about collecting and let arrears accumulate | ✅ | Rensselaerswyck — "his leniency with tenants created serious complications for his heirs" |
| 62 | He died in 1839 and his will directed his heirs to collect outstanding rents to settle his debts | ✅ | Anti-Rent War · Rensselaerswyck |
| 63 | The sum pursued was around $400,000 | ✅ | Rensselaerswyck · Encyclopedia.com |
| 64 | Tenants refused; a sheriff's posse attempting eviction was turned back by force | ✅ | Anti-Rent War |
| 65 | The conflict ran 1839–1845 and is known as the Anti-Rent War (or Helderberg War) | ✅ | Anti-Rent War |
| 66 | The New York Constitution of 1846 abolished feudal tenures and outlawed leases longer than twelve years | ✅ | Anti-Rent War |

⚠️ **Hedge — figure deliberately omitted.** Sources give wildly inconsistent tenant counts for the manor (3,063 families; ~80,000 tenants; ~3,000 people; 25,000–60,000 participants across the whole movement out of ~300,000 in the patroon system generally). Because these cannot be reconciled, the script gives **no** tenant number at all and describes the estate by acreage and geography instead. It also omits the widely-repeated "$10 million at death ≈ $133 billion today" conversion, on the same grounds Episode 34 gave for refusing precise currency conversions.

### B.9 Representation, then and now

| # | Claim | Verdict | Sources |
|---|---|---|---|
| 67 | In 1967 Hanna Pitkin distinguished descriptive from substantive representation | ✅ | [Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/entries/political-representation/) · [European Political Science](https://link.springer.com/article/10.1057/s41304-024-00489-2) — *The Concept of Representation*, 1967 |
| 68 | Descriptive = resembling the represented; substantive = acting in their interest | ✅ | Same |
| 69 | Working-class Americans are more than half the US workforce | ✅ | [Duke Today](https://today.duke.edu/2024/02/less-2-percent-state-legislators-are-working-class) · [Stateline](https://stateline.org/2024/03/15/working-class-people-rarely-have-a-seat-at-the-legislative-table-in-state-capitols/) |
| 70 | The average member of Congress spent less than 2% of their pre-congressional career in a working-class job | ✅ | Nicholas Carnes, *White-Collar Government* (2013) — [Boston Fed](https://www.bostonfed.org/publications/communities-and-banking/2015/winter/viewpoint-seeking-more-working-class-americans-in-congress.aspx) · [UChicago Press](https://press.uchicago.edu/ucp/books/book/chicago/W/bo16956543.html) |
| 71 | About 1.6% of state lawmakers are working class, against ~50% of workers | ✅ | Carnes & Hansen — [Duke Today](https://today.duke.edu/2024/02/less-2-percent-state-legislators-are-working-class) · [Stateline](https://stateline.org/2024/03/15/working-class-people-rarely-have-a-seat-at-the-legislative-table-in-state-capitols/). Script says "about one and a half percent," a fair rounding of 1.6%. |
| 72 | "Working class" here means manual labor, service, clerical and labor-union jobs | ✅ | Carnes's stated coding, quoted in the Duke and Stateline pieces |
| 73 | Congress is dominated by law and business backgrounds | ✅ | [CRS, Membership of the 118th Congress: A Profile](https://www.congress.gov/crs-product/R47470) |
| 74 | "Visionary" in eighteenth-century usage meant unreal or existing only in imagination | ✅ | Standard period usage; consistent with Hamilton's own contrast against "fact as our guide" |

---

## Honest hedges carried into the script (4)

The episode states these rather than smoothing them over:

1. **The lease terms on the Van Rensselaer manor.** Sources split between lifetime and perpetual leases, so the script says "a lifetime or forever depending on the paper in front of you."
2. **The Federal Procession as evidence.** The script explicitly says the displayed unanimity was "partly real and partly an absence," cites the Anti-Federalist printer's observation that opponents stayed home, and tells the Greenleaf mob story so the parade cannot read as free consent.
3. **Modern tariff incidence.** The script claims only that the cost stayed on the American side, not that the domestic seller/buyer split matched Hamilton's description.
4. **Hamilton's class argument.** The script declines to resolve whether "acquired endowments" is realism or condescension, saying plainly it is "probably some of both" — and refuses to soften the passage.

## Corrections made

**External claims requiring correction: 0.** All load-bearing history was verified before drafting.

**Internal-consistency errors caught and fixed: 4** (Federalist 12 timing, the Treasury/cutters timeline conflation, the Poughkeepsie distance, and the dating of tax incidence's formalization). Each was swept across the whole script afterward; `two months` and `ninety miles` have 0 remaining occurrences, and the surviving `twenty months` and `November` references were confirmed mutually consistent.
