import os
from dotenv import load_dotenv
from googleapiclient.discovery import build
import streamlit as st

load_dotenv()
API_KEY = os.getenv("api_key")

youtube = build('youtube', 'v3', developerKey=API_KEY)

def get_videos_from_channel(yt_handle):
    try:
        response = youtube.channels().list(part='snippet,contentDetails', forHandle=yt_handle).execute()
        data = response['items'][0]
        uploads = data['contentDetails']['relatedPlaylists']['uploads']
        channel_title = data['snippet']['title']
        channel_thumbnail = data['snippet']['thumbnails']['default']['url']

        videos, next_page_token = [], None

        while True:
            res = youtube.playlistItems().list(
                playlistId=uploads, part='snippet', maxResults=100, pageToken=next_page_token
            ).execute()

            for item in res['items']:
                snippet = item['snippet']
                videos.append({
                    'title': snippet['title'],
                    'videoId': snippet['resourceId']['videoId'],
                    'publishedAt': snippet['publishedAt'],
                    'channelTitle': channel_title,
                    'channelThumbnail': channel_thumbnail,
                    'thumbnail': snippet['thumbnails']['medium']['url']
                })

            next_page_token = res.get('nextPageToken')
            if not next_page_token:
                break

        return videos
    except Exception as e:
        st.warning(f"Error fetching channel {yt_handle}: {str(e)}")
        return []
