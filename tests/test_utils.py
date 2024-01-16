import unittest
from src.utils import get_episode_number  

class TestEpisodeNumberExtraction(unittest.TestCase):

    def test_standard_episode_titles(self):
        titles = [
            "Full Episode 52 | Be Careful With My Heart",
            "Full Episode 602 | Be Careful With My Heart",
        ]
        expected_numbers = [52, 602]
        for title, expected_number in zip(titles, expected_numbers):
            with self.subTest(title=title):
                self.assertEqual(utils.get_episode_number(title), expected_number)

    def test_episodes_with_total_count(self):
        titles = [
            "Be Careful With My Heart Full Episode 14 of 20 | iWant BETS",
            "Be Careful With My Heart Full Episode 30 of 40 | iWantTFC Series",
        ]
        expected_numbers = [14, 30]
        for title, expected_number in zip(titles, expected_numbers):
            with self.subTest(title=title):
                self.assertEqual(utils.get_episode_number(title), expected_number)

    def test_titles_without_episode_number(self):
        titles = [
            "Be Careful With My Heart | Highlight",
            "iWantTFC Special Presentation",
        ]
        for title in titles:
            with self.subTest(title=title):
                self.assertIsNone(utils.get_episode_number(title))

if __name__ == "__main__":
    unittest.main()

