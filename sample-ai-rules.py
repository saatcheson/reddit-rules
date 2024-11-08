import json
import random


rules = []
for i in range(1, 401):
    with open(f'data/rules-ai/{i}.json', 'r') as f:
        data = json.load(f)
        for d in data:
            for rule in d['rules']:
                if rule['ai_rule-short_name'] or rule['ai_rule-description']:
                    rules.append({'subreddit': d['subreddit'],
                                 'short_name': rule['short_name'],
                                 'description': rule['description']})

size = 200
sample = random.sample(rules, size)
with open('data/sample-ai-rules.json', 'w') as f:
    json.dump(sample, f)