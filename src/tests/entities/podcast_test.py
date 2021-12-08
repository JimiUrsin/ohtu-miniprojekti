from entities.podcast import Podcast
import unittest

class TestBook(unittest.TestCase):
    def setUp(self):
        self.author = "Radio Suomipop"
        self.url = "https://www.supla.fi/ohjelmat/aamulypsy"
        self.podcast = Podcast("Aamulypsy", self.author, self.url, 0)

    def test_podcast_author_is_correct(self):
        self.assertEqual(self.podcast.author, self.author)
    
    def test_podcast_url_is_correct(self):
        self.assertEqual(self.podcast.url, self.url)

    def test_string_representation(self):
        self.assertEqual(str(self.podcast), "Aamulypsy (podcast), Author: Radio Suomipop, URL: https://www.supla.fi/ohjelmat/aamulypsy")
