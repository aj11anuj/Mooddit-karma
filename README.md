# 🌈 Mooddit Karma

Mooddit Karma is a terminal-based sentiment analysis tool that allows users to fetch posts from any subreddit, store them in MongoDB, and analyze their sentiments using natural language processing. The goal is to understand the general mood of a subreddit community quickly.

## Features

- Fetch posts from any subreddit using Reddit's API
- Perform sentiment analysis (Positive, Negative, Neutral)
- Store and manage data using MongoDB
- Visualize sentiment distribution in the terminal using progress bars

## Requirements

- Python 3.8+
- [MongoDB](https://www.mongodb.com/)
- Reddit API credentials via [Reddit App](https://www.reddit.com/prefs/apps)
- PRAW (`pip install praw`)
- rich (`pip install rich`)

## Project Structure

```bash
Mooddit_Karma/
├── senti_count.py       # Sentiment analysis logic + visualization
├── fetch_data.py        # Script to fetch Reddit posts & store in MongoDB
├── clear_db.py          # Clears the MongoDB database (for fresh runs)
└── README.md            # You’re reading this!
```
<!--
## How to Use

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/Mooddit_Karma.git
cd Mooddit_Karma
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Reddit API
Edit the `fetch_data.py` file and insert your credentials:

```python
reddit = praw.Reddit(
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_SECRET',
    user_agent='YOUR_USER_AGENT'
)
```

### 4. Run the script
```bash
python fetch_data.py
```
- You’ll be prompted to enter the subreddit and number of posts.
- Data is saved in MongoDB.

### 5. Analyze Sentiment
```bash
python senti_count.py
```
- The script will analyze the freshly fetched posts and print visual sentiment stats in your terminal.
-->
## Sample Output

```bash
-> Fetched and stored 30 posts from r/technology

Sentiment Distribution:
Positive ━━━━━━━━━━━━━━ 40%
Negative ━━━━━━━━━━━━ 35%
Neutral ━━━━━━━ 25%
```
