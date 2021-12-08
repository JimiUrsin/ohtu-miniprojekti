import unittest
from unittest.mock import Mock

from entities.recommendation import Recommendation
from services.recommendations_service import RecommendationService
from repositories.recommendation_repository import RecommendationRepository

class TestRecommendationService(unittest.TestCase):
    def setUp(self):
        self.repo_mock = Mock(wraps=RecommendationRepository())
        self.service = RecommendationService(self.repo_mock)

    def test_create_new_recommendation_calls_create_with_correct_parameters(self):
        action = self.service.create_new_recommendation("Tohtori Sykerö", "video")

        self.assertTrue(action)
        self.repo_mock.insert_recommendation.assert_called_with("Tohtori Sykerö", "video")

    def test_create_new_recommendation_with_invalid_title(self):
        value = self.service.create_new_recommendation("a", "book")

        self.assertFalse(value)

    def test_create_new_recommendation_with_invalid_type(self):
        value = self.service.create_new_recommendation("Star", "Wars")

        self.assertFalse(value)

    def test_get_recommendations_returns_list(self):
        recommendations = self.service.get_recommendations()

        self.assertIsInstance(recommendations, list)

    def test_get_recommendations_returns_list_of_recommendations(self):
        self.service.create_new_recommendation("Tohtori Sykerö", "video")

        recommendations = self.service.get_recommendations()

        self.assertIsInstance(recommendations[0], Recommendation)

    def test_get_recommendations_calls_repository(self):
        self.service.get_recommendations()

        self.repo_mock.find_all_recommendations.assert_called()

    def test_edit_recommendation_title_calls_repository_correctly(self):
        self.service.get_recommendations() # creates the list
        self.service.edit_recommendation_title("Taikuri Luttinen", 0)
        # 0 is object id at the list

        self.repo_mock.edit_recommendation_title.assert_called_with("Taikuri Luttinen", 1)

    def test_edit_recommendation_title_returns_true_when_success(self):
        self.service.get_recommendations() # creates the list

        value = self.service.edit_recommendation_title("Taikuri Luttinen", 0)

        self.assertTrue(value)

    def test_edit_recommendation_title_returns_false_when_not(self):
        self.service.get_recommendations() # creates the list

        value = self.service.edit_recommendation_title("a", 0)

        self.assertFalse(value)

    def test_edit_recommendation_type_calls_repository_correctly(self):
        self.service.get_recommendations() # creates the list
        self.service.edit_recommendation_title("podcast", 0)
        # 0 is object id at the list

        self.repo_mock.edit_recommendation_title.assert_called_with("podcast", 1)

    def test_edit_recommendation_type_returns_true_when_success(self):
        self.service.get_recommendations() # creates the list

        value = self.service.edit_recommendation_type("podcast", 0)

        self.assertTrue(value)

    def test_edit_recommendation_title_returns_false_when_not(self):
        self.service.get_recommendations() # creates the list

        value = self.service.edit_recommendation_type("stream", 0)

        self.assertFalse(value)
