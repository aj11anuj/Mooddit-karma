from pymongo import MongoClient
from rich.console import Console
from rich.table import Table
from rich.bar import Bar
from rich.progress import Progress

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["MoodditKarma"]
collection = db["posts"]

# Initialize sentiment counts
sentiment_counts = {"positive": 0, "negative": 0, "neutral": 0}

# Fetch sentiment data
for post in collection.find({}, {"sentiment": 1}):
    if "sentiment" in post:
        sentiment_counts[post["sentiment"]] += 1

console = Console()

# Example sentiment count data
total_count = sum(sentiment_counts.values())

for sentiment, count in sentiment_counts.items():
    color = "green" if sentiment == "positive" else "red" if sentiment == "negative" else "blue"
    with Progress(console=console) as progress:
        progress.add_task(f"[{color}]{sentiment.capitalize()}[/]", total=total_count, completed=count)

