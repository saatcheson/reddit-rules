import time
# import praw
import json
import pandas as pd
import requests
from requests.auth import HTTPBasicAuth

# Set up Reddit API credentials
# reddit = praw.Reddit(
#     client_id='OQYyBIkxSjo20DSCwqlHJw',        # Replace with your client ID
#     client_secret='L9o86SHohCMAzVy6hLs86HoV4L7Fgw',  # Replace with your client secret
#     user_agent='user: Proud_Tune6552; purpose: Checking rules of top subreddits'        # Replace with your user agent
# )

class RedditAPI:
    def __init__(self, c):
        self.client_id = c['client_id']
        self.client_secret = c['client_secret']
        self.username = c['username']
        self.password = c['password']
        self.access_token = None
        self.expiration_time = 0

    def get_access_token(self):
        client_auth = HTTPBasicAuth(self.client_id, self.client_secret)
        header = {'User-Agent': f'Linux:rules:v1 (by /u/{self.username})'}
        post_data = {'grant_type': 'password',
                'username': self.username,
                'password': self.password}
        token_info = requests.post("https://oauth.reddit.com/api/v1/access_token",
                                 auth=client_auth,
                                 data=post_data,
                                 headers=header).json()
        self.access_token = token_info['access_token']
        self.expiration_time = time.time() + token_info['expires_in']  # Current time + expiration duration

    def ensure_access_token(self):
        if self.access_token is None or time.time() >= self.expiration_time:
            self.get_access_token()

    def make_request(self, url):
        self.ensure_access_token()
        header = {'Authorization': f'bearer {self.access_token}',
                   'User-Agent': f'Linux:rules:v1 (by /u/{self.username})'}
        return requests.get(url, headers=header)


try:
    with open('config.json', 'r') as f:
        credentials = json.load(f)
    reddit = RedditAPI(credentials)
    print('verified', flush=True)
except Exception as e:
    print(e)
    exit(1)

# Fetch subreddit information
for i in range(1, 401):
    with open(f'data/top-subreddits/{i}.csv', 'r') as f, open(f'data/rules/{i}.json', 'w') as o:
        data = []
        subreddits = [s[2:] for s in pd.read_csv(f)['subreddit'].to_list()]
        # subreddits = reddit.info([s[2:] for s in pd.read_csv(f)['subreddit'].to_list()])
        for subreddit in subreddits:
            try:
                response = reddit.make_request(f'https://oauth.reddit.com/r/{subreddit}/about/rules.json')
                if response.status_code == 200:
                    data.append({'subreddit': subreddit,
                                 'rules': response.json()['rules'],
                                 'scraped_utc': time.time()})
                else:
                    print(f'{i},{subreddit},{response.status_code}\n', flush=True)
            except Exception as e:
                print(f'{i},{subreddit},{str(e)}\n', flush=True)
            time.sleep(0.65)
        json.dump(data, o)
        print(f'{i} complete', flush=True)

        # subreddits = reddit.info(['t5_2qh33'])
        # for subreddit in subreddits:
        #     for rule in subreddit.rules:
        #         print(rule)
        #     data.append({'subreddit': subreddit.display_name,
        #                  'description': subreddit.description,
        #                 'rules': list(subreddit.rules),
        #                 'created_utc': subreddit.created_utc})
        # json.dump(data, o)

        # print(f'{i} complete')
        # l.write(f'{i}, complete\n')
        # l.flush()