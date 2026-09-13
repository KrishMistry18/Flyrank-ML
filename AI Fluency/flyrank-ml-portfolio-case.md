# Portfolio Case — FlyRank ML Internship

## Voice card
**direct, curious, plain, no fluff, shows the work**

*(Standing instruction for the Claude Project: "Write in my voice — direct, curious, plain, no fluff, shows the work. No 'results-driven,' no 'passionate about,' no LinkedIn-speak. Short sentences. Say what I actually decided and why, including the parts that didn't work. If you don't have the real number or the real reason, ask me instead of inventing one.")*

---

## The interview

*Below is a one-question-at-a-time interview about the FlyRank ML internship project (a content-refresh prioritization pipeline built on anonymized Google Search Console data — prepare → baseline → train → evaluate → report). Answer each honestly and messily in your own words — replace the bracketed drafts with what actually happened. Once your answers are in, the case study beats below rewrite themselves from this.*

**Q1. In one sentence, what were you actually asked to build, and for whom?**
> [Draft: "A model that tells FlyRank's SEO team which pages on a client site are worth refreshing first, using traffic and ranking history instead of a person manually scanning every URL."] — *your real answer:*

**Q2. Before you touched any code, what was actually broken or slow about how this got done manually?**
> [Draft: "Someone had to eyeball a spreadsheet of hundreds of pages and guess which ones had decaying traffic. It was slow and inconsistent — two people would flag different pages."] — *your real answer:*

**Q3. Walk me through the data — what did you actually have, and what was wrong with it at first?**
> [Draft: "90 days of query-level GSC data, anonymized and salted, with a long tail of low-impression queries and some Google-anonymized rows. I had to decide how to handle the rare-query noise before building anything."] — *your real answer:*

**Q4. What was the first version you tried, and why did you pick that instead of something fancier?**
> [Draft: "Started with a baseline — a simple rule/threshold model on traffic decline — before touching anything ML-y, so I'd have something to actually beat."] — *your real answer:*

**Q5. What went wrong or surprised you once you actually trained something?**
> [Draft: "The leak-guard in the pipeline caught me using future data to predict the past — I had to rebuild my train/test split around the 90-day window."] — *your real answer:*

**Q6. What decision are you most sure was right, and what's your evidence?**
> [Draft: "Keeping the rare-query tail as an aggregate feature instead of dropping it — it improved recall on pages that would've been missed otherwise."] — *your real answer:*

**Q7. What's the actual outcome — in numbers if you have them, in plain language if you don't?**
> [Draft: "The model's top-priority list matched what a human reviewer would flag [X]% of the time, and cut the review list from hundreds of pages to a ranked shortlist."] — *your real answer:*

**Q8. If someone else picked this up tomorrow, what would you tell them to fix first?**
> [Draft: "The model doesn't account for pages that recently got refreshed already — that's the next thing I'd add."] — *your real answer:*

---

## Case study draft

### FlyRank Content-Refresh Prioritization Model

**The problem**
FlyRank's SEO team needed a way to know which pages on a client's site were worth refreshing first — without a person manually scanning search performance data page by page. [Fill in the real scale/pain: how many pages, how long it took manually, who was doing it.]

**What I did**
I built a pipeline on 90 days of anonymized Google Search Console data — prepare, baseline, train, evaluate — rather than jumping straight to a model. [Replace with your real decisions: how you handled the low-impression query tail, what baseline you compared against, what broke in your first train/test split, and why you chose the approach you landed on over the alternatives.]

**What came of it**
[Replace with your real result: an accuracy/recall number, a time saved, a shortlist size, or an honest "it's not deployed yet but here's what it does today."]

---

## Bio

Krish Mistry — building ML pipelines that turn raw search data into decisions someone can actually act on. Currently in FlyRank's ML internship, working end-to-end from anonymized Google Search Console data to a ranked, explainable output.

## Contact / CTA
Want to see the notebook or talk through the approach? [Connect on LinkedIn](https://www.linkedin.com/in/krishmistry18/) — happy to walk through the decisions, not just the results.

---

## Before / after

**Before (generic AI line):**
"Leveraged machine learning to deliver data-driven insights that optimized content strategy and drove measurable results for the client."

**After (edited, in voice):**
"I built a model that ranks pages by how much their traffic is decaying, so the SEO team stops guessing which ones to refresh first."

---

### Note on this draft
I couldn't pull your actual notebooks or results from the repo (GitHub blocks automated crawling of file contents), so every bracket above is a placeholder built from the internship's known structure, not your real work. Fill in the Q&A honestly, then the case study beats above will already be close to final — just delete anything you wouldn't say out loud.
