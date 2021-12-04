from entities.blog import Blog
import unittest

class TestBlog(unittest.TestCase):
    def setUp(self):
        self.author = "Google"
        self.url = "https://blog.google/"
        self.blog = Blog("The Keyword", self.author, self.url)

    def test_blog_author_is_correct(self):
        self.assertEqual(self.blog.author, self.author)
    
    def test_blog_url_is_correct(self):
        self.assertEqual(self.blog.url, self.url)

    def test_string_representation(self):
        self.assertEqual(str(self.blog), "The Keyword (blog), Author: Google, URL: https://blog.google/")
