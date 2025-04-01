from pymongo import MongoClient
import praw
from datetime import datetime, timezone
import json

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client["MoodditKarma"]
collection = db["posts"]

# Reddit API setup
reddit = praw.Reddit(client_id='_xMS4Og8V_7Qet6BSeY3Iw',
                      client_secret='mnx557x775kZcQwfMi6WAq1yR89Y_A',
                      user_agent='MoodditKarmaBot/0.1 by EcstaticChance3728')

# Get user input for subreddit and number of posts
subreddit_name = input("-> Enter the subreddit name: ").strip()
while True:
    try:
        post_limit = int(input("-> Enter the number of posts you want to fetch: "))
        if post_limit > 0:
            break
        else:
            print("Please enter a positive number.")
    except ValueError:
        print("Invalid input, Please enter a valid value.")

# Fetches data from reddit
def fetch_reddit_data(subreddit_name, limit):
    subreddit = reddit.subreddit(subreddit_name)
    posts = []
    
    for post in subreddit.hot(limit=limit):
        post_data = {
            "title": post.title,
            "selftext": post.selftext,
            "created_utc": datetime.fromtimestamp(post.created_utc, timezone.utc).isoformat(),
            "sentiment": None
        }
        collection.insert_one(post_data)
        posts.append(post_data)
    
    print(f"-> Fetched and stored {len(posts)} posts from r/{subreddit_name}")

if __name__ == "__main__":
    fetch_reddit_data(subreddit_name, post_limit)
