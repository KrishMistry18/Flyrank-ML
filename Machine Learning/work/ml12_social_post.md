Content decay silently erodes search traffic, but large sites can't manually review every page. During my ML Internship at FlyRank, I tackled this by building a machine learning workflow to flag at-risk content *before* it loses significant visibility.

I trained a RandomForest model on an anonymized sample of 30,000 pages from FlyRank's production dataset to predict future 30-day traffic decline. A critical lesson: our initial model showed an impressive 64% Precision@100, but a validation audit revealed target leakage (it relied on recent traffic signals like `impressions_prev_30d` that essentially measured the decline itself).

After stripping leaked features and applying a strict client-grouped validation split, the safe, defensible result was 51% Precision@100. Rather than using this for automated, unsupervised edits, we turned it into a Content Action Playbook—a ranked review queue that guides human editors to the highest-ROI updates.

Check out the full methodology and findings in my deployed research paper: https://krishmistry18.github.io/Flyrank-ML/
