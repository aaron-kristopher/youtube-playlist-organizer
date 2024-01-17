from googleapiclient.discovery import build
from src import utils, api_client
import google_auth_oauthlib.flow

def add_videos_to_playlist(video_ids, playlist_id):
    CLIENT_SECRET_FILE = "client_secrets.json"
    API_NAME = "youtube"
    API_VERSION = "v3"
    SCOPES = ["https://www.googleapis.com/auth/youtube"]

    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            CLIENT_SECRET_FILE, SCOPES)

    credentials = flow.run_local_server(port=0)
    youtube = build(API_NAME, API_VERSION, credentials=credentials)

    video_ids = utils.get_video_id_from_csv("./videos.csv")

    for video_id in video_ids:
        print(video_id)
        print()
        request_body = {
                "snippet" : {
                    "playlistId" : playlist_id,
                    "resourceId" : {
                        "kind" : "youtube#video",
                        "videoId" : video_id,
                }
            }
        }

        youtube.playlistItems().insert(
                part="snippet",
                body=request_body
        ).execute()

if __name__ == "__main__":

    # Gets all videos
    playlist_id_source = "PLwPOcpjobYWWnlK82-RgfCDIv1vcL4KPc" # Be Careful Playlist
    playlist_id_target = "PLDInhITVKdPrRFUnygaeONDJvq_clRSip" # Custom Playlist
    youtube = api_client.get_youtube_service()
    videos = api_client.get_videos_from_playlist(youtube, playlist_id_source)

    # Sorts videos
    sorted_videos = utils.get_sorted_videos(videos)
    utils.save_to_csv(sorted_videos)
    video_ids = utils.get_video_id_from_csv("./videos.csv")

    # Adds to playlist
    add_videos_to_playlist(video_ids, playlist_id_target)
    
