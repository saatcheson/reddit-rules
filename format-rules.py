import json

rules = []
for i in range(1, 401):
    with open(f'data/rules/{i}.json', 'r') as f, open(f'data/rule.ignore', 'r') as g:
        ignore = [int(line.strip()) for line in g.readlines()]
        data = json.load(f)
        for d in data:
            for rule in d['rules']:
                cond1 = rule['id'] not in ignore
                cond2 = rule['ai_rule-short_name'] or rule['ai_rule-description']
                if cond1 and cond2:
                    rules.append({'subreddit': d['subreddit'],
                                 'short_name': rule['short_name'],
                                 'description': rule['description'],
                                  'id': rule['id']})

for r in rules:
