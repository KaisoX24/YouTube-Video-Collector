import streamlit as st
from datetime import datetime

def render_playlists(all_videos, handles):
    chunks = [all_videos[i:i+5000] for i in range(0, len(all_videos), 5000)]

    st.success(f"Found {len(all_videos)} videos across {len(handles)} channels. Showing {len(chunks)} virtual playlists.")

    for idx, playlist in enumerate(chunks):
        with st.expander(f"🎞️ Virtual Playlist {idx+1} — {len(playlist)} videos", expanded=False):
            for vid in playlist:
                title = vid['title']
                video_id = vid['videoId']
                date_str = datetime.strptime(vid['publishedAt'], "%Y-%m-%dT%H:%M:%SZ").strftime("%b %d, %Y")
                thumbnail = vid['thumbnail']
                channel_name = vid['channelTitle']

                st.markdown(f"""
                    <div style='margin-bottom: 1.5rem;'>
                        <div style='margin-bottom: 6px; font-weight: bold; font-size: 1rem;'>
                            {channel_name}
                        </div>
                        <a href='https://www.youtube.com/watch?v={video_id}' target='_blank' style='text-decoration: none; color: inherit;'>
                            <img src='{thumbnail}' width='320' style='border-radius: 8px;'><br>
                            <span style='font-size: 1.1rem; font-weight: bold;'>{title}</span><br>
                            <span style='color: gray;'>({date_str})</span>
                        </a>
                        <hr style='margin-top: 1rem;'>
                    </div>
                """, unsafe_allow_html=True)
