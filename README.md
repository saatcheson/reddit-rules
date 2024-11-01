# A Large-scale Analysis of Rules around AI-generated Content on Reddit

## Authors

- Alex Atcheson
- Andrea Cui

## Contents

- `data`: Main data directory.
	- `top-subreddits.zip`: Subreddit directory. Each file in the directory is a CSV file with 250 subreddits, where the file name corresponds to the *Best of Reddit* page from which the results were scraped. Smaller numbered files indicate larger subreddits.
	- `rules.zip`: Rules data. Each file contains rules corresponding to the subreddits from `top-subreddits`.
 	- `rules-ai.zip`: Identical to data in `rules-ai.zip`, except that each rule is labeled to indicate whether it is AI-related.
- `patterns`: Stores pattern files, where each pattern file consists of regex expressions for identifying AI-related rules.
- `scrape-top-subreddits.py`: Uses Selenium to scrape Reddit's *Best of Reddit* webpages (e.g., https://www.reddit.com/best/communities/1/) for name, topic, and subscriber count data on the top 100,000 subreddits.
- `collect-subreddit-rules.py`: Uses Reddit's API to collect rule data for each subreddit in `top-subreddits`.
- `label-ai-rules.py`: Using a pattern file from `patterns`, the description and short name of every rule in `rules` is matched against the regex expressions contained in the selected pattern file. Outputs labeled rules into `rules-ai`.
