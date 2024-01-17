import re
from src.api_client.py import search_videos_from_playlist


regex = r"(?i)(?:episode|ep)\s*(?P<episode_number>\d{1,4})(?:\s+of\s+\d+\s*)?.*"


def get_episode_number(title):
    match = re.search(regex, title)
    if match:
        return int(match.group("episode_number"))
    else:
        return None  # Or handle cases where no episode number is found


def remove_non_episode_video(videos):

    for index, video in enumerate(videos):
        if video["episode_number"] is None:
            videos.pop(index)

    return videos



def get_sorted_videos(playlist_id):
        videos = search_videos_from_playlist(playlist_id)

        sort_videos(videos)

        for video in videos:
            print(f"Title: {video['title']}\nEpisode Number: {video['episode_number']}\nLink: {video['url']}")
            print()

        print(f"Videos Retrieved: {len(videos)}")

        return videos


def sort_videos(videos):
    videos.sort(key=lambda vid:vid["episode_number"])
