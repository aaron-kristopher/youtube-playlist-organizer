import unittest
from unittest.mock import patch
from src.api_client import get_sorted_videos


class TestGetSortedVideos(unittest.TestCase):

    @patch('src.api_client.search_videos_from_playlist')
    def test_sort_videos(self, mock_search_videos_from_playlist):
        playlist_id = 'PL5UEpsh7xfCIMBsh7viJcd3HBjEqJt-Do'

        # Mock API response with videos in unsorted order
        mock_videos = [
            {'title': 'Full Episode 3', 'episode_number': 3, 'video_id': 'VIDEO_ID_3', 'url': 'URL_3'},
            {'title': 'Full Episode 1', 'episode_number': 1, 'video_id': 'VIDEO_ID_1', 'url': 'URL_1'},
            {'title': 'Full Episode 2', 'episode_number': 2, 'video_id': 'VIDEO_ID_2', 'url': 'URL_2'},
        ]

        mock_search_videos_from_playlist.return_value = mock_videos

        sorted_videos = get_sorted_videos(playlist_id)

        # Assert that videos are sorted by episode number
        self.assertEqual(sorted_videos, [
            {'title': 'Full Episode 1', 'episode_number': 1, 'video_id': 'VIDEO_ID_1', 'url': 'URL_1'},
            {'title': 'Full Episode 2', 'episode_number': 2, 'video_id': 'VIDEO_ID_2', 'url': 'URL_2'},
            {'title': 'Full Episode 3', 'episode_number': 3, 'video_id': 'VIDEO_ID_3', 'url': 'URL_3'},
        ])






if __name__ == "__main__":
    unittest.main()
