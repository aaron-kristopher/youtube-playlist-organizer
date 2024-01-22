import os
from src import utils
from googleapiclient.discovery import build
import google_auth_oauthlib.flow

def get_youtube_service():
    SECRET_API_KEY = os.environ.get("SECRET_API_KEY")
    youtube = build("youtube", "v3", developerKey=SECRET_API_KEY)
    return youtube

def get_youtube_oauth_service():
    CLIENT_SECRET_FILE = "client_secrets.json"
    API_NAME = "youtube"
    API_VERSION = "v3"
    SCOPES = ["https://www.googleapis.com/auth/youtube"]

    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            CLIENT_SECRET_FILE, SCOPES)
    credentials = flow.run_local_server(port=0)

    return build(API_NAME, API_VERSION, credentials=credentials)

def get_videos_from_playlist(youtube, playlist_id):
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
            part = "snippet",
            id = ",".join(video_ids)
        )

        video_response = video_request.execute()

        for item in video_response["items"]:
            video_title = item["snippet"]["title"]
            episode_number = utils.get_episode_number(video_title)
            video_id = item["id"]
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

def get_playlist_length(youtube, playlist_id):
    playlist_response = youtube.playlists().list(
            part="contentDetails",
            id=playlist_id
            ).execute()

    playlist_length = playlist_response["items"][0]["contentDetails"]["itemCount"]
    print(f"Number of videos in playlist {playlist_length}")

    return playlist_length


if __name__ == "__main__":
    playlist_id = "PL5UEpsh7xfCIMBsh7viJcd3HBjEqJt-Do"
    
    youtube = get_youtube_service()
    videos = get_videos_from_playlist(youtube, playlist_id)
    
    utils.save_to_csv(videos)

    
