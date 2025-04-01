from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/") 
db = client["MoodditKarma"]
collection = db["posts"]  

# Count the number of posts for each sentiment category
positive_count = collection.count_documents({"sentiment": "positive"})
neutral_count = collection.count_documents({"sentiment": "neutral"})
negative_count = collection.count_documents({"sentiment": "negative"})

# Print the results
print("-> Sentiment Frequency:")
print(f"   -> Positive: {positive_count}")
print(f"   -> Neutral: {neutral_count}")
print(f"   -> Negative: {negative_count}")