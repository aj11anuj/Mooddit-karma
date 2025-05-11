from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def perform_sentiment_analysis(posts):
    analyzed = []
    for post in posts:
        text = post.get("title", "") + " " + post.get("selftext", "")
        score = analyzer.polarity_scores(text)["compound"]
        sentiment = (
            "positive" if score >= 0.05 else
            "negative" if score <= -0.05 else
            "neutral"
        )
        analyzed.append({
            **post,
            "sentiment": sentiment
        })
    return analyzed
