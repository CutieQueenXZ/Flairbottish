# main.py
import praw
import time

reddit = praw.Reddit(
    client_id="Flairbottish",
    client_secret="uMbYRd9oWomON7gn5IoQWA",
    username="gamerharun109",
    password="gamerharun1",
    user_agent="Flair bot by /u/gamerharunyt"
)

subreddit = reddit.subreddit("foundbob")

# Get current hour (24hr)
def get_flair_status():
    hour = datetime.now().hour
    if 7 <= hour < 23:
        return "Awake"
    else:
        return "Sleeping"

while True:
    flair_text = get_flair_status()
    print(f"Setting flair to '{flair_text}' for contributors...")

    for user in subreddit.contributor():
        subreddit.flair.set(user, text=flair_text)
        print(f"Set {user} flair to '{flair_text}'")

    time.sleep(3600)  # Wait an hour before checking again
