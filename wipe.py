from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/") 
db = client["MoodditKarma"]
collection = db["posts"] 

# Clear the collection
result = collection.delete_many({})

print(f"-> Cleared {result.deleted_count} documents from the database")
print("-> It Will now perform analysis on fresh real-time data only")
