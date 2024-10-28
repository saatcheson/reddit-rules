from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

# Set up Chrome options (optional)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (optional)
chrome_options.add_argument("user-agent=email:saatcheson@gmail.com; purpose:searching for top subreddits")

# Set up the WebDriver
service = Service('scrape-venv/chromedriver-mac-x64/chromedriver')  # Update with the path to your ChromeDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    with open('scrape.log', 'w') as f:
        for i in range(1, 401): # 400 web top-subreddits, each page contains 250 subreddits
            data = {'subreddit': [], 'subscribers': [], 'topic': [], 'subreddit_id': [], 'time': []}
            try:
                # Open the webpage
                driver.get(f"https://www.reddit.com/best/communities/{i}/")  # Replace with your target URL

                # Wait for the page to load (you may want to use WebDriverWait for better control)
                wait = WebDriverWait(driver, 10)  # Maximum wait time of 10 seconds
                divs = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div.flex.flex-wrap.justify-center.py-\\[0\\.75rem\\]')))
                h6s = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'h6.flex-grow.h-md.text-12.truncate.py-\\[0\\.125rem\\].w-\\[11rem\\].m-0')))

                # Extract attribute values
                ds = []
                for div, h6 in zip(divs, h6s):
                    subreddit = div.get_attribute("data-prefixed-name")
                    subreddit_id = div.get_attribute('data-community-id')
                    subscribers = div.get_attribute('data-subscribers-count')
                    topic = h6.text
                    ds.append((subreddit, subreddit_id, subscribers, topic, time.time()))

                for d in ds:
                    data['subreddit'].append(d[0])
                    data['subreddit_id'].append(d[1])
                    data['subscribers'].append(d[2])
                    data['topic'].append(d[3])
                    data['time'].append(d[4])

                print(f'{i} complete', flush=True)
                f.write(f'{i} complete\n')
                f.flush()

                df = pd.DataFrame(data)
                df.to_csv(f'data/top-subreddits/{i}.csv')

            except Exception as e:
                f.write(f'{i}, {str(e)}\n')
                f.flush()

            time.sleep(0.5)

finally:
    # Close the WebDriver
    driver.quit()