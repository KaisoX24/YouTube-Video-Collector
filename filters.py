from datetime import datetime

def apply_filters(videos, sort_order, search_keyword, date_range):
    # Sort
    videos.sort(key=lambda x: x['publishedAt'], reverse=(sort_order == "Newest First"))

    # Keyword filter
    if search_keyword:
        videos = [v for v in videos if search_keyword.lower() in v['title'].lower()]

    # Date filter
    if len(date_range) == 2:
        start = datetime.combine(date_range[0], datetime.min.time())
        end = datetime.combine(date_range[1], datetime.max.time())
        videos = [v for v in videos if start <= datetime.strptime(v['publishedAt'], "%Y-%m-%dT%H:%M:%SZ") <= end]

    return videos
