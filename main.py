# main.py
import praw
import os
import time
from datetime import datetime

reddit = praw.Reddit(
    client_id="Flairbottish",
    client_secret="uMbYRd9oWomON7gn5IoQWA",
    username="gamerharun109",
    password="gamerharun1",
    user_agent="Flair bot by /u/gamerharunyt"
)

subreddit = reddit.subreddit(os.getenv("FoundBob"))
target_user = os.getenv("gamerharunyt")  # your Reddit username

def get_flair_status():
    hour = datetime.now().hour
    if 6 <= hour < 22:
        return "☀️Awake"
    else:
        return "💤Sleeping"

while True:
    flair_text = get_flair_status()
    print(f"Setting your flair to '{flair_text}'")

    subreddit.flair.set(gamerharunyt, text=flair_text)
    time.sleep(3600)
