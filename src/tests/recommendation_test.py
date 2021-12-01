import unittest
from entities.recommendation import Recommendation

class TestRecommendation(unittest.TestCase):
    
    def test_new_recommendation_has_correct_values(self):
        title = "Merge sort algorithm"
        recom_type = "Video"
        recommendation = Recommendation(title, recom_type)

        self.assertEqual(recommendation.title, title)
        self.assertEqual(recommendation.type, recom_type)

