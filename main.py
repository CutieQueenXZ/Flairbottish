import praw
import os
import time
from datetime import datetime

# Get Reddit credentials from environment variables
reddit = praw.Reddit(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    username=os.getenv("REDDIT_USERNAME"),
    password=os.getenv("REDDIT_PASSWORD"),
    user_agent=os.getenv("USER_AGENT")
)

# Subreddit and target user from environment variables
subreddit_name = os.getenv("YOUR_SUBREDDIT")
target_user = os.getenv("TARGET_USER")  # your Reddit username

# Check if variables are set
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
