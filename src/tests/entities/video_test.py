from entities.video import Video
import unittest

class TestVideo(unittest.TestCase):
    def setUp(self):
        self.author = "Richard Paul A."
        self.url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        self.music_video = Video("Not Ever in The Mindset of Handing You Away", self.author, self.url)

    def test_video_author_is_correct(self):
        self.assertEqual(self.music_video.author, self.author)
    
    def test_video_url_is_correct(self):
        self.assertEqual(self.music_video.url, self.url)

    def test_string_representation(self):
        self.assertEqual(str(self.music_video), "Not Ever in The Mindset of Handing You Away (video), Author: Richard Paul A., URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ")
