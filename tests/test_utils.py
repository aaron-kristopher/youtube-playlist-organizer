import unittest
from src.utils import get_episode_number, remove_non_episode_video
from src.utils import get_sorted_videos, remove_duplicate_videos

class TestEpisodeNumberExtraction(unittest.TestCase):


    def test_standard_episode_titles(self):
        titles = [
            "Full Episode 52 | Be Careful With My Heart",
            "Full Episode 602 | Be Careful With My Heart",
        ]
        expected_numbers = [52, 602]
        for title, expected_number in zip(titles, expected_numbers):
            with self.subTest(title=title):
                self.assertEqual(get_episode_number(title), expected_number)

    def test_episodes_with_total_count(self):
        titles = [
            "Be Careful With My Heart Full Episode 14 of 20 | iWant BETS",
            "Be Careful With My Heart Full Episode 30 of 40 | iWantTFC Series",
        ]
        expected_numbers = [14, 30]
        for title, expected_number in zip(titles, expected_numbers):
            with self.subTest(title=title):
                self.assertEqual(get_episode_number(title), expected_number)

    def test_titles_without_episode_number(self):
        titles = [
            "Be Careful With My Heart | Highlight",
            "iWantTFC Special Presentation",
        ]
        for title in titles:
            with self.subTest(title=title):
                self.assertIsNone(get_episode_number(title))


    def test_remove_non_episode_video(self):

        videos = [
            {'title': 'Full Episode', 'episode_number': None, 'video_id': 'VIDEO_ID_5', 'url': 'URL_5'},
            {'title': 'Full Episode 3', 'episode_number': 3, 'video_id': 'VIDEO_ID_3', 'url': 'URL_3'},
            {'title': 'Full Episode 1', 'episode_number': 1, 'video_id': 'VIDEO_ID_1', 'url': 'URL_1'},
            {'title': 'Full Episode 2', 'episode_number': 2, 'video_id': 'VIDEO_ID_2', 'url': 'URL_2'},
            {'title': 'Full Episode', 'episode_number': None, 'video_id': 'VIDEO_ID_2', 'url': 'URL_4'},
        ]

        expected_videos = [
            {'title': 'Full Episode 3', 'episode_number': 3, 'video_id': 'VIDEO_ID_3', 'url': 'URL_3'},
            {'title': 'Full Episode 1', 'episode_number': 1, 'video_id': 'VIDEO_ID_1', 'url': 'URL_1'},
            {'title': 'Full Episode 2', 'episode_number': 2, 'video_id': 'VIDEO_ID_2', 'url': 'URL_2'},
        ]

        episode_videos = remove_non_episode_video(videos)

        # Assert that videos with no episode number are removed
        self.assertEqual(episode_videos, expected_videos)


    def test_sort_videos(self):

        # INPUTS
        with_numbered_videos = [
            {'title': 'Full Episode 3', 'episode_number': 3, 'video_id': 'VIDEO_ID_3', 'url': 'URL_3'},
            {'title': 'Full Episode 1', 'episode_number': 1, 'video_id': 'VIDEO_ID_1', 'url': 'URL_1'},
            {'title': 'Full Episode 2', 'episode_number': 2, 'video_id': 'VIDEO_ID_2', 'url': 'URL_2'},
        ]

        with_non_numbered_videos = [
                {'title': 'Full Episode', 'episode_number': None, 'video_id': 'VIDEO_ID_5', 'url': 'URL_5'},
                {'title': 'Full Episode 3', 'episode_number': 3, 'video_id': 'VIDEO_ID_3', 'url': 'URL_3'},
                {'title': 'Full Episode 1', 'episode_number': 1, 'video_id': 'VIDEO_ID_1', 'url': 'URL_1'},
                {'title': 'Full Episode 2', 'episode_number': 2, 'video_id': 'VIDEO_ID_2', 'url': 'URL_2'},
                {'title': 'Full Episode', 'episode_number': None, 'video_id': 'VIDEO_ID_2', 'url': 'URL_4'},
        ]

        # OUTPUT
        expected_videos = [
            {'title': 'Full Episode 1', 'episode_number': 1, 'video_id': 'VIDEO_ID_1', 'url': 'URL_1'},
            {'title': 'Full Episode 2', 'episode_number': 2, 'video_id': 'VIDEO_ID_2', 'url': 'URL_2'},
            {'title': 'Full Episode 3', 'episode_number': 3, 'video_id': 'VIDEO_ID_3', 'url': 'URL_3'},
        ]


        # Assert that videos are sorted by episode number
        self.assertEqual(get_sorted_videos(with_numbered_videos), expected_videos)
        self.assertEqual(get_sorted_videos(with_non_numbered_videos), expected_videos)

    
    def test_removing_duplicate_videos(self):
        repetead_videos = [
                {'title': 'Full Episode 3', 'episode_number': 3, 'video_id': 'VIDEO_ID_3', 'url': 'URL_3'},
                {'title': 'Full Episode 1', 'episode_number': 1, 'video_id': 'VIDEO_ID_1', 'url': 'URL_1'},
                {'title': 'Full Episode 2', 'episode_number': 2, 'video_id': 'VIDEO_ID_2', 'url': 'URL_2'},
                {'title': 'Full Episode 3', 'episode_number': 3, 'video_id': 'VIDEO_ID_3', 'url': 'URL_3'},
                {'title': 'Full Episode 2', 'episode_number': 2, 'video_id': 'VIDEO_ID_2', 'url': 'URL_2'},
        ]

        expected_videos = [
                {'title': 'Full Episode 3', 'episode_number': 3, 'video_id': 'VIDEO_ID_3', 'url': 'URL_3'},
                {'title': 'Full Episode 1', 'episode_number': 1, 'video_id': 'VIDEO_ID_1', 'url': 'URL_1'},
                {'title': 'Full Episode 2', 'episode_number': 2, 'video_id': 'VIDEO_ID_2', 'url': 'URL_2'},
        ]

        self.assertEqual(remove_duplicate_videos(repetead_videos), expected_videos)




if __name__ == "__main__":
    unittest.main()

