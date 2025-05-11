def get_sentiment_counts(posts):
    counts = {"positive": 0, "neutral": 0, "negative": 0}

    for post in posts:
        sentiment = post.get("sentiment", "neutral")
        if sentiment in counts:
            counts[sentiment] += 1

    return counts
