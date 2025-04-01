from pymongo import MongoClient
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["MoodditKarma"]
collection = db["posts"]

analyzer = SentimentIntensityAnalyzer()
posts = collection.find({"sentiment": None})

for post in posts:
    text = post.get("title", "") + " " + post.get("selftext", "")
    sentiment_score = analyzer.polarity_scores(text)["compound"]
    
    if sentiment_score >= 0.05:
        sentiment = "positive"
    elif sentiment_score <= -0.05:
        sentiment = "negative"
    else:
        sentiment = "neutral"
    
    collection.update_one({"_id": post["_id"]}, {"$set": {"sentiment": sentiment}})

print("-> Sentiment analysis completed and updated in MongoDB!")
