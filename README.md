# A Large-scale Analysis of Rules around AI-generated Content on Reddit

## Authors

- Alex Atcheson
- Andrea Cui

## Repo Structure

- `scrape-top-subreddits.py`: Uses Selenium and Chrome web driver to scrape Reddit's website for the top 100,000 subreddits. Populates `data/pages/`.
- `collect-subreddit-metadata.py`: Uses Reddit's API to collect rule data for each subreddit collected by `scrape-top-subreddits.py`. Populates `data/rules/`.
