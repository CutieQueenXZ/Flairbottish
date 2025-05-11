# main.py
import praw
import os
import time
from datetime import datetime

reddit = praw.Reddit(
    client_id="Flairbottish",
    client_secret="uMbYRd9oWomON7gn5IoQWA",
    username="flairbottish",
    password="flairbot111",
    user_agent="Flair bot by /u/gamerharunyt"
)

# Subreddit and target user should also be set through environment variables
subreddit_name = os.getenv("FoundBob")
target_user = os.getenv("gamerharunyt")  # your Reddit username

if not subreddit_name or not target_user:
    raise ValueError("Missing subreddit name or target user")

subreddit = reddit.subreddit(subreddit_name)

def get_flair_status():
    hour = datetime.now().hour
    if 6 <= hour < 22:
        return "☀️ Awake"
    else:
        return "💤 Sleeping"

while True:
    flair_text = get_flair_status()
    print(f"Setting your flair to '{flair_text}'")

    # Set flair for the target user
    subreddit.flair.set(target_user, text=flair_text)
    time.sleep(3600)  # Sleep for 1 hour before checking again
