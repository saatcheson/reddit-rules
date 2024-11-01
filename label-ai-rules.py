import re
import json


# configure the regex expression file to use for pattern matching
with open('patterns/p1.txt', 'r') as f:
    patterns = f.readlines()


def is_AI_rule(r):
    global patterns
    if r is not None:
        for p in patterns:
            if re.search(p, r):
                return True
    return False


def main():
    for i in range(1, 401):
        with open(f'data/rules/{i}.json', 'r') as f, open(f'data/rules-ai/{i}.json', 'w') as o:
            data = []
            for d in json.load(f):
                for r in d['rules']:
                    if is_AI_rule(r['short_name']) or is_AI_rule(r['description']):
                        r['ai_rule'] = 1    # yes
                    else:
                        r['ai_rule'] = 0    # no
                data.append(d)
            json.dump(data, o)
        print(f'{i} complete', flush=True)


if __name__ == '__main__':
    main()