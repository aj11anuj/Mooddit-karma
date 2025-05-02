# 🌈 Mooddit Karma

Mooddit Karma is a terminal-based sentiment analysis tool that allows users to fetch posts from any subreddit, store them in MongoDB, and analyze their sentiments using natural language processing. The goal is to understand the general mood of a subreddit community quickly.

## Features

- Fetch live posts from any subreddit using Reddit's API
- Perform sentiment analysis using Vader
- Store and manage data using MongoDB
- Terminal-based KPI and progress bar visualization

## File Overview

  | File              | Description                                      |
  |-------------------|--------------------------------------------------|
  | `main.py`         | Master script to run all modules sequentially    |
  | `fetch_reddit.py` | Fetches posts from a subreddit and saves to DB   |
  | `analyze.py`      | Performs sentiment analysis on the posts         |
  | `senti_count.py`  | Shows the count of each sentiment type           |
  | `visuals.py`      | Displays colored terminal bars for sentiment     |
  | `wipe.py`         | Clears previous post data from MongoDB           |

## Requirements

- Python 3.8+
- [MongoDB](https://www.mongodb.com/)
- Reddit API credentials via [Reddit App](https://www.reddit.com/prefs/apps)
- PRAW (`pip install praw`) - Reddit's API
- rich (`pip install rich`) - Some UI based functionalities

## How to Use

- ### Clone the repository
    ```bash
    git clone https://github.com/aj11anuj/Mooddit-Karma.git
    cd Mooddit_Karma
    ```

- ### Install dependencies
    ```bash
    pip install pymongo praw vaderSentiment rich
    ```

- ### Setup MongoDB
  - Ensure MongoDB is installed and running on your system at the default port `27017`.

- ### Reddit's API Setup
  - Go to [Reddit App Preferences](https://www.reddit.com/prefs/apps).
  - Click **“Create App”** > **“script”**
  - Set `client_id`, `client_secret`, and `user_agent` in `fetch_reddit.py`:
    ```python
    reddit = praw.Reddit(
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_SECRET',
    user_agent='MoodditKarmaBot/0.1 by YOUR_USERNAME'
    )
    ```

- ### Usage
  - Once setup is done, just run:
    ```bash
    python main.py
    ```

## Sample Output

```bash
Cleaning the database...
-> Cleared 30 documents from the database
-> It will now perform analysis on fresh real-time data only
    
Fetching Reddit posts...
-> Enter the subreddit name: technology
-> Enter the number of posts you want to fetch: 50
-> Fetched and stored 50 posts from r/technology
    
Performing Sentiment Analysis...
-> Sentiment analysis completed and updated in MongoDB!
    
KPI for the data...
-> Sentiment Frequency:
  -> Positive: 22
  -> Neutral: 17
  -> Negative: 11
    
Visualization...
  Positive ━━━━━━━━━━━━━━ 40%
  Negative ━━━━━━━━━━━━ 35%
  Neutral ━━━━━━━ 25%
    
All tasks completed!
```
