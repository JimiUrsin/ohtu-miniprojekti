import unittest
from entities.recommendation import Recommendation


class TestRecommendation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.title = "Merge sort algorithm"
        cls.recom_type = "video"
        cls.db_id = 0
        cls.author = 'Videoperson'
        cls.url = 'www.video-address.fi'
        cls.isbn = None
        cls.description = 'Video on this algorithm'
        cls.comment = 'Good'
        cls.recommendation = Recommendation(
            cls.title, cls.recom_type, cls.db_id, cls.author, cls.url, cls.isbn, cls.description, cls.comment)

    def test_new_recommendation_has_correct_title(self):
        self.assertEqual(self.recommendation.title, self.title)

    def test_new_recommendation_has_correct_type(self):
        self.assertEqual(self.recommendation.type, self.recom_type)

    def test_new_recommendation_has_correct_id(self):
        self.assertEqual(self.recommendation.db_id, self.db_id)

    def test_string_representation(self):
        self.assertEqual(str(self.recommendation),
                         "Merge sort algorithm (video), Author: Videoperson, URL: www.video-address.fi, Description: Video on this algorithm, Comment: Good")

    def test_string_representation_with_ISBN(self):
        book_recommendation = Recommendation(
            'A book name', 'book', '0', 'Writer', None, '123')
        self.assertEqual(str(book_recommendation),
                         "A book name (book), Author: Writer, ISBN: 123")
