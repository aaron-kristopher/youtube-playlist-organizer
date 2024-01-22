from src import utils, api_client


def create_playlist():
    youtube = api_client.get_youtube_oauth_service()
    request = youtube.playlists().insert(
        part="string.title,status.privacyStatus",
        body={
          "snippet": {
            "title": "Be careful With My Heart Episodes",
            "description": "A playlist of all available episodes for the TV series 'Be Careful With My Heart' as the original playlist is not ordered correctly."
          },
          "status": {
            "privacyStatus": "public"
          }
        }
    )
    response = request.execute()

    print(response)


def add_videos_to_playlist(video_ids, playlist_id):
    youtube = api_client.get_youtube_oauth_service()
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
    """
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
    """  

    create_playlist()
