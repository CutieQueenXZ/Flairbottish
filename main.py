import praw
import os
import time
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create Reddit instance using credentials from .env
reddit = praw.Reddit(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    username=os.getenv("REDDIT_USERNAME"),
    password=os.getenv("REDDIT_PASSWORD"),
    user_agent=os.getenv("USER_AGENT")
)

# Get subreddit and user from .env
subreddit_name = os.getenv("YOUR_SUBREDDIT")
target_user = os.getenv("TARGET_USER")

if not subreddit_name or not target_user:
    raise ValueError("Missing YOUR_SUBREDDIT or TARGET_USER in .env")

subreddit = reddit.subreddit(subreddit_name)

# Function to determine flair based on time
def get_flair_status():
    hour = datetime.now().hour
    if 6 <= hour < 22:
        return "☀️ Awake"
    else:
        return "💤 Sleeping"

# Main loop: update flair every hour
while True:
    flair_text = get_flair_status()
    print(f"Setting flair for u/{target_user} to '{flair_text}'")
    subreddit.flair.set(target_user, text=flair_text)
    time.sleep(3600)  # wait for 1 hour
