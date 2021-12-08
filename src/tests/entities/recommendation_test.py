import unittest
from entities.recommendation import Recommendation

class TestRecommendation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.title = "Merge sort algorithm"
        cls.recom_type = "Video"
        cls.db_id = 0
        cls.recommendation = Recommendation(cls.title, cls.recom_type, cls.db_id)

    def test_new_recommendation_has_correct_title(self):
        self.assertEqual(self.recommendation.title, self.title)

    def test_new_recommendation_has_correct_type(self):
        self.assertEqual(self.recommendation.type, self.recom_type)

    def test_new_recommendation_has_correct_id(self):
        self.assertEqual(self.recommendation.db_id, self.db_id)
