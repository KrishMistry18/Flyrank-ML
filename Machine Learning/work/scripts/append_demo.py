import json
import os

path = os.path.join("Machine Learning", "work", "notebooks", "w07_action_playbook.ipynb")
with open(path, "r", encoding="utf-8") as f:
    nb = json.load(f)

cell_content = [
    "# 5-Minute Demo Outline\n",
    "\n",
    "## 0:00–0:45 — Question\n",
    "**What content problem are we trying to solve?**\n",
    "Search engines reward freshness, and content decay silently erodes traffic. However, large content portfolios can contain tens of thousands of pages. Human editors cannot review everything manually. The practical problem is prioritizing which pages deserve human review first, rather than blindly guessing or waiting for traffic to hit zero.\n",
    "\n",
    "## 0:45–1:30 — Data\n",
    "**What data was used?**\n",
    "We used an anonymized sample of 30,000 pages from FlyRank's production search dataset. The target was predicting whether a page's traffic would trend down in the subsequent 30 days (`trend_direction == \"down\"`). For safety and privacy, all client names, live URLs, and raw private queries were excluded. We also strictly removed any variables that directly calculated the target, like `trend_pct`.\n",
    "\n",
    "## 1:30–2:30 — Method\n",
    "**Methodology and Leakage Correction**\n",
    "We built a RandomForest classifier. Crucially, we validated it using `GroupShuffleSplit` on `client_id` so the model couldn't memorize client-specific patterns. During our validation audit (ML-09), we discovered that our initial model was \"cheating\" (target leakage) by using recent traffic metrics like `impressions_prev_30d` which essentially measured the decline itself. We removed those leaked features and re-validated.\n",
    "\n",
    "## 2:30–3:30 — One Chart\n",
    "**Priority Distribution (Action Queue)**\n",
    "Look at the Priority Distribution chart in the paper. It shows the top 200 recommended pages broken down by Priority (P1, P2, P3) based on search volume and staleness. This matters because it proves the model doesn't just flag pages—it segments them so an editor knows exactly where the highest-ROI work is. Instead of 30,000 pages, the editor sees 12 high-priority tasks.\n",
    "\n",
    "## 3:30–4:15 — Honest Result\n",
    "**Validated Results**\n",
    "The initial leaked model showed an inflated 64% Precision@100. Once we corrected the validation and removed leaked features, the defensible, safe result was **51.00% Precision@100**. This means out of the top 100 pages the model flags, about 51 are genuinely decaying. Compared to a heuristic baseline that scored 0% on unseen clients, this is a highly useful signal for a human review queue.\n",
    "\n",
    "## 4:15–5:00 — Recommendation\n",
    "**The Content Action Playbook**\n",
    "We don't use this model to automatically change production content. Instead, the model scores feed into a Ranked Review Queue. The workflow is: **MODEL → RANKED REVIEW QUEUE → HUMAN REVIEW → CONTENT DECISION**. Editors review the top-ranked pages using provided reason codes (like `CONTENT_STALE`), ensuring safe, human-in-the-loop decisions."
]

new_cell = {
    "cell_type": "markdown",
    "metadata": {},
    "source": cell_content
}

nb["cells"].append(new_cell)

with open(path, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("Added demo outline cell successfully")
