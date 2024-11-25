import json
import pandas as pd


sample = {'ID': [], 'rule': []}
with open('data/sample-ai-rules.json', 'r') as f:
    data = json.load(f)
    for i, r in enumerate(data):
        r = f'[subreddit]: {r["subreddit"]}\n[short_name]: {r["short_name"]}\n[description]: {r["description"]}'
        sample['ID'].append(i)
        sample['rule'].append(r)

df = pd.DataFrame(sample)
df.to_csv('data/formatted-sample-2.csv', index=False)