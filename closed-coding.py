'''
This file uses GPT-4 to code each rule in the rule dataset.
'''

import json
import pandas as pd
from openai import OpenAI


def check_codes():
    df_codebook = pd.read_csv('data/codebook.csv')
    df_coded = pd.read_csv('data/coded-sample.csv')

    codes = list(df_codebook['code'])
    for i in range(len(codes)):
        codes[i] = codes[i].lower()

    coded = list(df_coded['Code(s)'])
    print('--- Invalid codes ---')
    for x in coded:
        x = x.strip().split('; ')
        for c in x:
            if c not in codes:
                print(c)


with open('config.json', 'r') as f:
    config = json.load(f)

# Initialize OpenAI client
client = OpenAI(api_key=config['openAIkey'])

# Read assistant and user prompts
with open('prompting/assistant-prompt.txt', 'r') as f1, open('prompting/user-prompt.txt', 'r') as f2:
    prompt_a = f1.read()
    prompt_u = f2.read()

