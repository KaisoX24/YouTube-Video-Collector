import streamlit as st
from youtube_utils import get_videos_from_channel
from filters import apply_filters
from display_playlists import render_playlists

# Streamlit UI
st.set_page_config(page_title="YouTube Channels Playlist Creator ", layout="wide")
st.title("📺 YouTube Channel Video Collector")

handles_input = st.text_area("Enter YouTube Handles (one per line):")
sort_order = st.radio("Sort videos by:", ["Newest First", "Oldest First"])
search_keyword = st.text_input("Search video titles (optional):")
date_range = st.date_input("Filter by upload date range:", [])
fetch_btn = st.button("Fetch & Generate Virtual Playlists")

if fetch_btn and handles_input:
    handles = [h.strip() for h in handles_input.split("\n") if h.strip()]
    all_videos = []

    with st.spinner("Fetching videos from all channels..."):
        for handle in handles:
            videos = get_videos_from_channel(handle)
            all_videos.extend(videos)

    filtered_videos = apply_filters(all_videos, sort_order, search_keyword, date_range)
    render_playlists(filtered_videos, handles)
