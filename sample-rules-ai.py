import json
import random


rules = []
for i in range(1, 401):
    with open(f'data/rules-ai/{i}.json', 'r') as f, open(f'data/rule-id-ignore.txt', 'r') as g:
        ignore = [int(line.strip()) for line in g.readlines()]
        data = json.load(f)
        for d in data:
            for rule in d['rules']:
                cond1 = rule['id'] not in ignore
                cond2 = rule['ai_rule-short_name'] or rule['ai_rule-description']
                if cond1 and cond2:
                    rules.append({'subreddit': d['subreddit'],
                                 'short_name': rule['short_name'],
                                 'description': rule['description']})

size = 50
sample = random.sample(rules, size)
with open('data/sample-ai-rules.json', 'w') as f:
    json.dump(sample, f)