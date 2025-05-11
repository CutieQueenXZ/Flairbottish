
# Flairbottish 🏷️

**Flairbottish** is a simple Reddit bot that automatically changes a user's flair based on the time of day! It was built for fun and runs using [PRAW](https://praw.readthedocs.io/) — the Python Reddit API Wrapper.

---

## ✨ Features

- Automatically sets flair based on time:
  - ☀️ **Awake** (between 6 AM and 10 PM)
  - 😴 **Sleeping** (between 10 PM and 6 AM)
- Customizable timezone using a `.env` file
- Great for "status-like" flair changes in a subreddit

---

## 🛠️ Setup

### 1. Clone the repo

```bash
git clone https://github.com/your-username/Flairbottish.git
cd Flairbottish
```

### 2. Install requirements

```bash
pip install -r requirements.txt
```

### 3. Create a Reddit App

- Go to [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps)
- Click **"create another app"**
- Choose **script**
- Set `http://localhost:8080` as redirect URI
- Copy the **Client ID** (under the app name) and **Secret**

---

## 🌍 Environment Variables

Create a `.env` file in the root directory like this:

```env
CLIENT_ID=your_client_id
CLIENT_SECRET=your_secret
REDDIT_USERNAME=your_reddit_username
REDDIT_PASSWORD=your_reddit_password
USER_AGENT=Flairbottish/0.1 by your_reddit_username
YOUR_SUBREDDIT=name_of_your_subreddit
TARGET_USER=username_whose_flair_to_change
TIMEZONE=Your/Timezone  # e.g., Europe/Warsaw
```

### Example

```env
TIMEZONE=Asia/Jakarta
```

((which is default the timezone, so ignore it))
To find your timezone name, check [here](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).

---

## 🚀 Run the bot

```bash
python main.py
```

It will update the user's flair every hour based on the current time in your selected timezone.

---

## 🤝 Contributing

Pull requests are welcome! If you're new to Reddit bots, feel free to fork and experiment. Suggestions and feedback are encouraged.

---

## 📄 License

MIT License — free to use, modify, and share!

---

## 💬 Credits

Created with ❤️ by me as a fun automation project!
