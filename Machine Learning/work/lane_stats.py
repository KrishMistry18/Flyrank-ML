import csv
from collections import defaultdict

def safe_float(val):
    try:
        return float(val)
    except:
        return None

file_path = 'data/raw/content_refresh_anonymized.csv'

with open(file_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

cols = reader.fieldnames

print("## Dataset Overview")
print(f"**Shape**: {len(rows)} rows, {len(cols)} columns")
print(f"**Columns**: {', '.join(cols)}\n")

def print_stats(title, columns):
    print(f"## {title}")
    
    # Header
    print("| Metric | Count | Min | Max | Mean |")
    print("|---|---|---|---|---|")
    
    for c in columns:
        vals = [safe_float(r[c]) for r in rows if r.get(c) not in (None, '', 'unknown')]
        vals = [v for v in vals if v is not None]
        if not vals:
            print(f"| {c} | 0 | - | - | - |")
        else:
            count = len(vals)
            min_val = min(vals)
            max_val = max(vals)
            mean_val = sum(vals) / count
            print(f"| {c} | {count} | {min_val:g} | {max_val:g} | {mean_val:.2f} |")
    print("\n")

print_stats("Lane 1: Ranking Signal Analysis (Visibility & Search)", 
            ['impressions_90d', 'clicks_90d', 'avg_position', 'search_volume'])

print_stats("Lane 2: Refresh / Content Opportunity Scoring (Decline & Age)",
            ['content_age_days', 'days_since_last_update', 'impressions_last_30d', 'impressions_prev_30d'])

# Trend direction counts
trend_counts = defaultdict(int)
for r in rows:
    trend_counts[r.get('trend_direction', '')] += 1
print("**Trend Direction Counts:**")
for k, v in trend_counts.items():
    print(f"- {k}: {v}")
print("\n")

print_stats("Lane 3: Structured Content Archetype Clustering (Content Shape)",
            ['word_count', 'char_count'])

ctype_counts = defaultdict(int)
intent_counts = defaultdict(int)
for r in rows:
    ctype_counts[r.get('content_type', '')] += 1
    intent_counts[r.get('main_intent', '')] += 1

print("**Content Type Counts:**")
for k, v in ctype_counts.items():
    print(f"- {k}: {v}")
print("\n**Main Intent Counts:**")
for k, v in intent_counts.items():
    print(f"- {k}: {v}")
print("\n")

print_stats("Lane 4: CTR / Engagement Opportunity Scoring",
            ['ctr', 'engagement_rate', 'scroll_rate', 'pageviews_90d', 'sessions_90d'])

print_stats("Freestyle: AI Referral Opportunity",
            ['ai_sessions_90d', 'ai_traffic_pct'])
