import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import json
import os

out_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'docs', 'img')
os.makedirs(out_dir, exist_ok=True)

# --- 1. Precision@100 comparison bar chart (validated) ---
labels = ['Random\nBaseline', 'Week-4\nHeuristic\n(Grouped)', 'Week-5 RF\n(Leaked, 64%)', 'Week-6 RF\n(Safe, Grouped)']
values = [0, 0, 64, 51]
colors = ['#555555', '#888888', '#ff6b6b', '#4f8ef7']
hatches = ['', '', '///', '']

fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(labels, values, color=colors, edgecolor='#222', linewidth=1.2, width=0.55)
for bar, h in zip(bars, hatches):
    bar.set_hatch(h)
for bar, val in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1.5,
            f'{val}%', ha='center', va='bottom', fontweight='bold', fontsize=12)

ax.set_ylabel('Precision @ 100 (%)', fontsize=12)
ax.set_title('Model Comparison: Precision@100 Under Different Validation Setups', fontsize=13, fontweight='bold')
ax.set_ylim(0, 80)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.axhline(y=51, color='#4f8ef7', linestyle='--', alpha=0.4, linewidth=1)
plt.tight_layout()
plt.savefig(os.path.join(out_dir, 'precision_bar.png'), dpi=200)
plt.close()
print("Saved precision_bar.png")

# --- 2. Feature importance (safe features only from ML-09) ---
safe_features = {
    'days_since_last_update': 0.054,
    'word_count': 0.106,
    'search_volume': 0.028,
    'competition': 0.018,
    'cpc': 0.015,
    'content_type (encoded)': 0.09,
    'main_intent (encoded)': 0.07,
}

sorted_feats = sorted(safe_features.items(), key=lambda x: x[1])
feat_names = [f[0] for f in sorted_feats]
feat_vals = [f[1] for f in sorted_feats]

fig, ax = plt.subplots(figsize=(8, 4.5))
bars = ax.barh(feat_names, feat_vals, color='#4f8ef7', edgecolor='#222', height=0.55)
ax.set_xlabel('Feature Importance (Gini)', fontsize=11)
ax.set_title('Safe Feature Importance — RandomForest (No Leaked Features)', fontsize=12, fontweight='bold')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig(os.path.join(out_dir, 'feature_importance.png'), dpi=200)
plt.close()
print("Saved feature_importance.png")

# --- 3. Priority distribution (reuse the w07 figure data) ---
priorities = {'P1': 0, 'P2': 12, 'P3': 188}  # approximate from queue data
fig, ax = plt.subplots(figsize=(6, 4))
bars = ax.bar(priorities.keys(), priorities.values(), color=['#ff6b6b', '#f7b731', '#4f8ef7'],
              edgecolor='#222', width=0.5)
for bar, val in zip(bars, priorities.values()):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2,
            str(val), ha='center', va='bottom', fontweight='bold', fontsize=12)
ax.set_ylabel('Number of Pages', fontsize=11)
ax.set_title('Action Queue Priority Distribution (Top 200)', fontsize=12, fontweight='bold')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig(os.path.join(out_dir, 'priority_distribution.png'), dpi=200)
plt.close()
print("Saved priority_distribution.png")

print("All figures generated.")
