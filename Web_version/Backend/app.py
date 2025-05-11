from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from analyze import perform_sentiment_analysis
from senti_count import get_sentiment_counts
from fetch_reddit import fetch_reddit_data 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze(request: Request):
    try:
        body = await request.json()
        subreddit = body.get("subreddit")
        count = body.get("count", 100)

        if not subreddit:
            raise HTTPException(status_code=400, detail="Subreddit is required.")
        posts = await fetch_reddit_data(subreddit, count)
        if not posts:
            raise HTTPException(status_code=404, detail="No posts found for this subreddit.")
        analyzed = perform_sentiment_analysis(posts)
        counts = get_sentiment_counts(analyzed)

        return {
            "cleaned_docs": f"{len(posts)} docs cleaned.",
            "fetched_posts": len(posts),
            "positive": counts.get("positive", 0),
            "neutral": counts.get("neutral", 0),
            "negative": counts.get("negative", 0)
        }

    except Exception as e:
        print("Error during /analyze:", e)
        raise HTTPException(status_code=500, detail=str(e))
