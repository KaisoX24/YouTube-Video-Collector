# 📺 YouTube Playlist Collector

A powerful Streamlit app that collects videos from multiple YouTube channels (using @handles), sorts them, and organizes them into virtual playlists of up to 5000 videos each.

---

## 🚀 Features

- 🔍 **Search YouTube videos** by handle (@channelname)
- 📦 **Fetch all uploaded videos** from each channel
- 🧮 **Sort videos** by Newest or Oldest first
- 🔠 **Search by keyword** in video titles
- 🗓️ **Filter by upload date range**
- 🎞️ **View channel info and video thumbnails**
- 🧾 **Auto-generate virtual playlists** (max 5000 videos each)
- 📎 **Click to watch videos directly on YouTube**

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/) – UI & frontend
- [YouTube Data API v3](https://developers.google.com/youtube/v3) – for fetching video/channel data
- [Python](https://www.python.org/) – backend logic
- [dotenv](https://pypi.org/project/python-dotenv/) – environment variable management

---

## ⚙️ Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/channel-sort.git
   cd channel-sort
