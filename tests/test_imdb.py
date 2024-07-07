# tests/test_imdb.py

import unittest
from showcaser.sites.imdb import IMDb

class TestIMDb(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("""
    Setting up expected results for IMDb tests.
    This test will check if the IMDb class can extract
    all season URLs from a show URL, extract ratings
    for each episode in a specific season, and extract
    ratings for each episode in all seasons of a show.

    - File: tests/test_imdb.py
    - Class: TestIMDb
        """)

    def setUp(self):
        self.imdb = IMDb()

        # # # THIS IS FOR THE TV-SHOW BREAKING BAD # # #
        self.show_url = "https://www.imdb.com/title/tt0903747"
        self.expected_season_urls = [
            'https://www.imdb.com//title/tt0903747/episodes/?season=1',
            'https://www.imdb.com//title/tt0903747/episodes/?season=2',
            'https://www.imdb.com//title/tt0903747/episodes/?season=3',
            'https://www.imdb.com//title/tt0903747/episodes/?season=4',
            'https://www.imdb.com//title/tt0903747/episodes/?season=5'
        ]
        self.expected_ratings = {
            1: {1: 9, 2: 8.6, 3: 8.7, 4: 8.2, 5: 8.3, 6: 9.3, 7: 8.8},
            2: {1: 8.6, 2: 9.3, 3: 8.3, 4: 8.2, 5: 8.2, 6: 8.8, 7: 8.6, 8: 9.2, 9: 9.1, 10: 8.4, 11: 8.9, 12: 9.3, 13: 9.2},
            3: {1: 8.5, 2: 8.6, 3: 8.4, 4: 8.2, 5: 8.5, 6: 9.3, 7: 9.6, 8: 8.7, 9: 8.4, 10: 7.9, 11: 8.4, 12: 9.5, 13: 9.7},
            4: {1: 9.2, 2: 8.2, 3: 8, 4: 8.5, 5: 8.6, 6: 8.4, 7: 8.8, 8: 9.3, 9: 8.9, 10: 9.6, 11: 9.7, 12: 9.5, 13: 9.9},
            5: {1: 9.2, 2: 8.8, 3: 8.8, 4: 8.8, 5: 9.7, 6: 9, 7: 9.6, 8: 9.6, 9: 9.4, 10: 9.2, 11: 9.6, 12: 9.1, 13: 9.8, 14: 10, 15: 9.7, 16: 9.9}
        }
        # # # # # #

    def test_get_all_season_urls(self):
        season_urls = self.imdb.get_all_season_urls(self.show_url)
        self.assertEqual(season_urls, self.expected_season_urls, "The season URLs should match the expected URLs.")

    def test_get_specific_season_ratings_season_1(self):
        season_url = self.expected_season_urls[0]
        ratings = self.imdb.get_specific_season_ratings(season_url)
        self.assertEqual(ratings, self.expected_ratings[1], "The ratings for season 1 should match the expected ratings.")

    def test_get_specific_season_ratings_season_2(self):
        season_url = self.expected_season_urls[1]
        ratings = self.imdb.get_specific_season_ratings(season_url)
        self.assertEqual(ratings, self.expected_ratings[2], "The ratings for season 2 should match the expected ratings.")

    def test_get_specific_season_ratings_season_3(self):
        season_url = self.expected_season_urls[2]
        ratings = self.imdb.get_specific_season_ratings(season_url)
        self.assertEqual(ratings, self.expected_ratings[3], "The ratings for season 3 should match the expected ratings.")

    def test_get_specific_season_ratings_season_4(self):
        season_url = self.expected_season_urls[3]
        ratings = self.imdb.get_specific_season_ratings(season_url)
        self.assertEqual(ratings, self.expected_ratings[4], "The ratings for season 4 should match the expected ratings.")

    def test_get_specific_season_ratings_season_5(self):
        season_url = self.expected_season_urls[4]
        ratings = self.imdb.get_specific_season_ratings(season_url)
        self.assertEqual(ratings, self.expected_ratings[5], "The ratings for season 5 should match the expected ratings.")

    def test_get_show_ratings(self):
        show_ratings = self.imdb.get_show_ratings(self.show_url)
        self.assertEqual(show_ratings, self.expected_ratings, "The ratings should match the expected ratings.")

if __name__ == '__main__':
    unittest.main()
