import unittest
from entities.recommendation import Recommendation

class TestRecommendation(unittest.TestCase):
    
    def test_new_recommendation_returns_correct_title(self):
        title = "Merge sort algorithm"
        recommendation = Recommendation(title)

        self.assertEqual(recommendation.get_title(), title)

    def test_recommendation_returns_correct_title_after_setting_new_title(self):
        title_a = "Merge sort algorithm"
        title_b = "Consistency models"
        recommendation = Recommendation(title_a)
        recommendation.set_title(title_b)

        self.assertEqual(recommendation.get_title(), title_b)

    def test_recommendation_can_not_be_created_with_empty_title(self):
        with self.assertRaises(Exception) as exception:
            recommendation = Recommendation("")
            
            self.assertEqual("Recommendation has to have a title of at least 2 characters", exception.exception)

    def test_recommendation_title_can_not_be_set_to_empty_string(self):
        with self.assertRaises(Exception) as exception:
            recommendation = Recommendation("Merge sort algorithm")
            recommendation.set_title("")

            self.assertEqual("Recommendation has to have a title of at least 2 characters", exception.exception)
