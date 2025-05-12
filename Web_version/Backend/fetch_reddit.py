import asyncpraw
import os
from datetime import datetime, timezone
from dotenv import load_dotenv

load_dotenv()

reddit = asyncpraw.Reddit(
    client_id=os.environ.get('REDDIT_CLIENT_ID'),
    client_secret=os.environ.get('REDDIT_CLIENT_SECRET'),
    user_agent=os.environ.get('REDDIT_USER_AGENT')
)

async def fetch_reddit_data(subreddit_name, limit):
    posts = []
    subreddit = await reddit.subreddit(subreddit_name)
    async for post in subreddit.hot(limit=limit):
        posts.append({
            "title": post.title,
            "selftext": post.selftext,
            "created_utc": datetime.fromtimestamp(post.created_utc, timezone.utc).isoformat()
        })
    return posts
