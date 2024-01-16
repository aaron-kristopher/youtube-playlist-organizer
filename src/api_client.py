import os
from src import utils
from googleapiclient.discovery import build

def get_youtube_service():
    SECRET_API_KEY = os.environ.get("SECRET_API_KEY")
    youtube = build("youtube", "v3", developerKey=SECRET_API_KEY)
    return youtube


def search_videos_from_playlist(playlist_id):
    youtube = get_youtube_service()
    videos = []

    nextPageToken = None

    while True:
        playlist_request = youtube.playlistItems().list(
            part="contentDetails",
            playlistId=playlist_id,
            maxResults=50,
            pageToken=nextPageToken
        )

        playlist_response = playlist_request.execute()

        video_ids = []
        for item in playlist_response["items"]:
            video_ids.append(item["contentDetails"]["videoId"])

        video_request = youtube.videos().list(
            part = "statistics,snippet",
            id = ",".join(video_ids)
        )

        video_response = video_request.execute()


        for item in video_response["items"]:
            video_title = item["snippet"]["title"]

            video_id = item["id"]
            episode_number = utils.get_episode_number(video_title)
            youtube_link = f"https://youtu.be/{video_id}"

            videos.append(
                    {
                        "title" : video_title,
                        "episode_number" : episode_number,
                        "video_id" : video_id,
                        "url" : youtube_link
                    }
            )

        nextPageToken = playlist_response.get("nextPageToken")

        if not nextPageToken:
            return videos


def get_sorted_videos(playlist_id):
        videos = search_videos_from_playlist(playlist_id)

        sort_videos(videos)

        for video in videos:
            print(f"Title: {video['title']}\nEpisode Number: {video['episode_number']}\nLink: {video['url']}")
            print()

        print(videos)
        print(f"Videos Retrieved: {len(videos)}")

        return videos




def sort_videos(videos):

    print(videos)
    videos.sort(key=lambda vid:vid["episode_number"])



if __name__ == "__main__":
    playlist_id = "PL5UEpsh7xfCIMBsh7viJcd3HBjEqJt-Do"
    print(get_sorted_videos(playlist_id))
