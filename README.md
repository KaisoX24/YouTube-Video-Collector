# 📺 YouTube Video Collector

This is a Streamlit web app that lets you fetch all videos from multiple YouTube channels using their handles, organize them into virtual playlists, and filter them by date, title, or channel — all visually with thumbnails and clickable video links.

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
## 🧑‍💻 How It Works

- **You input YouTube handles (one per line).**

- **It uses the YouTube Data API to get the channel’s uploads playlist.**

- **All videos are retrieved and stored with metadata (title, ID, thumbnail, published date, etc).**

- **Videos are sorted, filtered, and shown with thumbnails and links.**
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

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   venv\Scripts\activate  # or source venv/bin/activate on MAC

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt

4. **Create a .env file with your YouTube API key:**

   ```env
   api_key=YOUR_YOUTUBE_DATA_API_KEY


   

