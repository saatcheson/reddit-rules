import pandas as pd
import glob
import matplotlib.pyplot as plt
import json
import numpy as np

# Load all CSV files from the directory with a similar structure as "1.csv"
csv_files = glob.glob("data/top-subreddits-v2/*.csv")  # Adjust path if needed

# Combine all the CSVs into a single DataFrame
subreddits_data = pd.concat([pd.read_csv(file) for file in csv_files], ignore_index=True)

# Load the text file with subreddits to ignore
ignore_file_path = 'data/subreddits.ignore'
with open(ignore_file_path, 'r') as f:
    subreddits_to_ignore = f.read().splitlines()

# Filter out the subreddits to ignore from the combined dataset
filtered_subreddits_data = subreddits_data[~subreddits_data['subreddit'].isin(subreddits_to_ignore)]

# Inspect the combined data
subreddits_data.head(), subreddits_data.shape
#print(subreddits_data.head())
#print(subreddits_data.shape)#(99798, 6)

# Inspect the filtered dataset
filtered_subreddits_data.head(), filtered_subreddits_data.shape
#print(filtered_subreddits_data.head())
#print(filtered_subreddits_data.shape)#(99798, 6)??? same

# Perform the analysis on the provided file to answer question 1.

# 1. Distribution of subreddit sizes (subscribers) and topics:

subreddit_size_distribution = filtered_subreddits_data['subscribers'].describe()
subreddit_topics_distribution = filtered_subreddits_data['topic'].value_counts()

print(subreddit_size_distribution)
print(subreddit_topics_distribution)

# Print the top 10 subreddits based on the number of subscribers
top_10_subreddits = filtered_subreddits_data.nlargest(10, 'subscribers')[['subreddit', 'subscribers', 'topic']]
print("\nTop 10 Subreddits by Number of Subscribers:")
print(top_10_subreddits)

top_15_subreddits = filtered_subreddits_data.nlargest(15, 'subscribers')[['subreddit', 'subscribers', 'topic']]
print("\nTop 15 Subreddits by Number of Subscribers:")
print(top_15_subreddits)

# 1. Subreddit Sizes
size_summary = filtered_subreddits_data['subscribers'].describe()
print("Summary Statistics for Subreddit Sizes:")
print(size_summary)

# Plotting the distribution of subreddit sizes
plt.figure(figsize=(10, 6))
plt.hist(filtered_subreddits_data['subscribers'] / 1e6, bins=30, color='lightblue', log=True)
plt.title("Distribution of Subreddit Sizes")
plt.xlabel("Number of Subscribers (in millions)")
plt.ylabel("Frequency (log scale)")
plt.show()


import matplotlib.pyplot as plt

# Data for the top subreddits
subreddit_topics = [
    "Funny/Humor", "Learning and Education", "Gaming", "World News",
    "Learning and Education", "Animals and Pets", "Music",
    "Internet Culture and Memes", "Movies", "Science"
]
subreddit_sizes = [
    64727346, 48984649, 44093395, 42114027, 38421465,
    37052889, 35148058, 34670399, 33859245, 33044799
]

# Plot the data
plt.figure(figsize=(12, 6))
plt.bar(subreddit_topics, subreddit_sizes, color='skyblue')

# Add labels and title
plt.xlabel("Topic", fontsize=12)
plt.ylabel("Number of Subscribers", fontsize=12)
plt.title("Top Subreddits by Topic and Number of Subscribers", fontsize=14)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.tight_layout()

# Display the plot
plt.show()


#plotting of the topics:
# Data for the top 15 subreddits
top_15_subreddits = [
    ("r/funny", 64727346, "Funny/Humor"),
    ("r/AskReddit", 48984649, "Learning and Education"),
    ("r/gaming", 44093395, "Gaming"),
    ("r/worldnews", 42114027, "World News"),
    ("r/todayilearned", 38421465, "Learning and Education"),
    ("r/aww", 37052889, "Animals and Pets"),
    ("r/Music", 35148058, "Music"),
    ("r/memes", 34670399, "Internet Culture and Memes"),
    ("r/movies", 33859245, "Movies"),
    ("r/science", 33044799, "Science"),
    ("r/Showerthoughts", 33026108, "Funny/Humor"),
    ("r/pics", 31192981, "Art"),
    ("r/Jokes", 30056025, "Funny/Humor"),
    ("r/news", 28876381, "World News"),
    ("r/space", 26847738, "Science")
]

# Convert the data to a DataFrame for easier plotting
top_15_df = pd.DataFrame(top_15_subreddits, columns=["subreddit", "subscribers", "topic"])

# Plotting the top 15 subreddits by subscribers
plt.figure(figsize=(12, 6))
plt.barh(top_15_df["subreddit"], top_15_df["subscribers"], color="lightblue", edgecolor="black")
plt.title("Top 15 Subreddits by Number of Subscribers", fontsize=14)
plt.xlabel("Number of Subscribers", fontsize=12)
plt.ylabel("Subreddit", fontsize=12)
plt.gca().invert_yaxis()  # Invert y-axis for better readability
plt.tight_layout()

# Show the plot
plt.show()


# # 2. Subreddit Topics
# topic_counts = filtered_subreddits_data['topic'].value_counts()
# print("\nNumber of Subreddits per Topic:")
# print(topic_counts)

# # Plotting the distribution of subreddit topics
# plt.figure(figsize=(12, 6))
# topic_counts.plot(kind='bar')
# plt.title("Distribution of Subreddit Topics")
# plt.xlabel("Topic")
# plt.ylabel("Number of Subreddits")
# plt.xticks(rotation=45, ha='right')
# plt.show()



# 2. What % of subreddits in our sample have AI rules? How many rules do they have, on average?

# Get all JSON files in the 'rules' directory
json_files = glob.glob("data/rules/*.json")

# Initialize counters for AI rules and total rules
subreddits_with_ai_rules = 0
total_ai_rules = 0
total_subreddits = 0
rules_total = 0

# Loop through each JSON file
for file in json_files:
    with open(file, 'r') as f:
        subreddit_data = json.load(f)
        if subreddit_data:  # Check if the file is not empty
            for subreddit in subreddit_data:
                total_subreddits += 1
                has_AI_rules = 0
               
                for rule in subreddit["rules"]:
                    rules_total += 1
                    print(rule.get('ai_rule-short_name'), rule.get('ai_rule-description'))
                    if rule['ai_rule-short_name'] != 0 or rule['ai_rule-description'] != 0:
                        has_AI_rules = 1
                        # Assuming 'rules' contains the list of rules
                        total_ai_rules += 1
                subreddits_with_ai_rules += has_AI_rules
                
# Calculate the percentage of subreddits with AI rules
percent_with_ai_rules = (subreddits_with_ai_rules / total_subreddits) * 100 

# Calculate the average number of rules for all subreddits:
average_rules = rules_total / total_subreddits if total_subreddits > 0 else 0

# Calculate the average number of rules for subreddits with AI rules
average_ai_rules = total_ai_rules / subreddits_with_ai_rules if subreddits_with_ai_rules > 0 else 0
print('22222')
print(percent_with_ai_rules, average_ai_rules)
print(average_rules)
print('End 22222')
#This ensures you’re correctly iterating through the JSON data.
#print(subreddit_data[:2] if isinstance(subreddit_data, list) else subreddit_data)


# 3. What is the distribution of subreddit sizes among those subreddits that have AI rules?

# Load the CSV files containing subreddit subscriber information
csv_files = glob.glob("data/top-subreddits-v2/*.csv")
subreddit_data_csv = pd.concat([pd.read_csv(file) for file in csv_files], ignore_index=True)

# Create a dictionary to map subreddit names to their subscriber counts
subreddit_to_subscribers = dict(zip(subreddit_data_csv['subreddit'], subreddit_data_csv['subscribers']))

# Initialize a list to store subreddit sizes for subreddits with AI rules
subreddit_sizes_with_ai_rules = []

# Get all JSON files in the 'rules' directory
json_files = glob.glob("data/rules/*.json")

# Loop through each JSON file to extract subreddit sizes for those with AI rules
for file in json_files:
    with open(file, 'r') as f:
        subreddit_data = json.load(f)
        if subreddit_data:  # Check if the file is not empty
            for subreddit in subreddit_data:
                has_AI_rules = 0

                # Check if any rule qualifies as an AI rule
                for rule in subreddit["rules"]:
                    if rule['ai_rule-short_name'] != 0 or rule['ai_rule-description'] != 0:
                        has_AI_rules = 1
                        break  # Stop checking once an AI rule is found
                
                # If the subreddit has AI rules, record its size using the CSV mapping
                if has_AI_rules:
                    subreddit_name = "r/" + subreddit.get('subreddit')
                    #print(subreddit_name)
                    if subreddit_name in subreddit_to_subscribers:
                        
                        subreddit_sizes_with_ai_rules.append(subreddit_to_subscribers[subreddit_name])

# Calculate the distribution of subreddit sizes with AI rules
subreddit_sizes_distribution = {
    "mean": np.mean(subreddit_sizes_with_ai_rules),
    "median": np.median(subreddit_sizes_with_ai_rules),
    "min": np.min(subreddit_sizes_with_ai_rules),
    "max": np.max(subreddit_sizes_with_ai_rules),
    "std_dev": np.std(subreddit_sizes_with_ai_rules),
}

# Output the distribution of subreddit sizes
print(subreddit_sizes_distribution)

import matplotlib.pyplot as plt

# Data from the distribution
data = {
    'mean': 348669.5065934066,
    'median': 14745.5,
    'min': 401,
    'max': 64727346,
    'std_dev': 2406665.904601825
}

# Prepare data for a more visually appealing scatter plot
sorted_sizes = sorted(subreddit_sizes_with_ai_rules, reverse=True)
subreddit_sizes_log = np.log10(sorted_sizes)

# Create an improved scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(range(len(sorted_sizes)), subreddit_sizes_log, color='steelblue', edgecolor='black', alpha=0.8, s=50)
plt.title("Distribution of Subreddit Sizes with AI Rules (Log Scale)", fontsize=16)
plt.xlabel("Subreddit Rank (Sorted by Size)", fontsize=12)
plt.ylabel("Log10(Number of Subscribers)", fontsize=12)
plt.grid(alpha=0.1)
plt.tight_layout()
plt.show()


# 4. Within each topic, what % of subreddits have AI rules?
# Load the CSV files containing subreddit topic information
csv_files = glob.glob("data/top-subreddits-v2/*.csv")
subreddit_data_csv = pd.concat([pd.read_csv(file) for file in csv_files], ignore_index=True)

# Create a dictionary to map subreddit names to their topics
subreddit_to_topic = dict(zip(subreddit_data_csv['subreddit'], subreddit_data_csv['topic']))

# Initialize counters for topic-level AI rule percentages
topic_ai_rule_counts = {}
topic_total_counts = {}

# Get all JSON files in the 'rules' directory
json_files = glob.glob("data/rules/*.json")

# Loop through each JSON file to determine AI rules by topic
for file in json_files:
    with open(file, 'r') as f:
        subreddit_data = json.load(f)
        if subreddit_data:  # Check if the file is not empty
            for subreddit in subreddit_data:
                has_AI_rules = 0

                # Check if any rule qualifies as an AI rule
                for rule in subreddit["rules"]:
                    if rule['ai_rule-short_name'] != 0 or rule['ai_rule-description'] != 0:
                        has_AI_rules = 1
                        break  # Stop checking once an AI rule is found
                
                # Get subreddit name and check if it belongs to a topic
                subreddit_name = "r/" + subreddit.get('subreddit')
                if subreddit_name in subreddit_to_topic:
                    topic = subreddit_to_topic[subreddit_name]
                    
                    # Initialize topic counters if not already present
                    if topic not in topic_ai_rule_counts:
                        topic_ai_rule_counts[topic] = 0
                        topic_total_counts[topic] = 0

                    # Increment total subreddits for the topic
                    topic_total_counts[topic] += 1

                    # Increment AI rule count if the subreddit has AI rules
                    if has_AI_rules:
                        topic_ai_rule_counts[topic] += 1

# Calculate the percentage of subreddits with AI rules by topic
topic_ai_rule_percentages = {
    topic: (topic_ai_rule_counts[topic] / topic_total_counts[topic]) * 100
    for topic in topic_total_counts
}

# Output the results as a DataFrame for better readability
df_topic_ai_rule_percentages = pd.DataFrame(
    topic_ai_rule_percentages.items(), columns=["Topic", "% with AI Rules"]
)

# Display the DataFrame
print(df_topic_ai_rule_percentages)

# Optionally save to a CSV file
df_topic_ai_rule_percentages.to_csv("topic_ai_rule_percentages.csv", index=False)



from wordcloud import WordCloud
import random

# Load the CSV file provided by the user
file_path = "topic_ai_rule_percentages.csv"
data = pd.read_csv(file_path)

# Filter topics with non-zero percentages
filtered_data = data[data["% with AI Rules"] > 0]

# Randomly sample 50 topics
sampled_data = filtered_data.sample(n=min(50, len(filtered_data)), random_state=42)

# Create a dictionary for the word cloud (Topic: Percentage)
wordcloud_data = dict(zip(sampled_data["Topic"], sampled_data["% with AI Rules"]))

# Generate the word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='viridis').generate_from_frequencies(wordcloud_data)

# Display the word cloud
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Word Cloud of Topics with AI Rules", fontsize=16)
plt.show()
