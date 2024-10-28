# A Large-scale Analysis of Rules around AI-generated Content on Reddit

## Authors

- Alex Atcheson
- Andrea Cui

## Contents

- `data`: Main data directory.
	- `top-subreddits.zip`: Subreddit directory. Each file in the directory is a CSV file with 250 subreddits, where the file name corresponds to the *Best of Reddit* page from which the results were scraped. Smaller numbered files indicate larger subreddits.
	- `rules.zip`: Rules directory: Each file contains rules corresponding to the subreddits from the associated `top-subreddits` file.
- `scrape-top-subreddits.py`: Uses Selenium to scrape Reddit's *Best of Reddit* webpages (e.g., https://www.reddit.com/best/communities/1/) for name, topic, and subscriber count data on the top 100,000 subreddits.
- `collect-subreddit-metadata.py`: Uses Reddit's API to collect rule data for each subreddit in the `top-subreddits` directory.
