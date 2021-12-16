import unittest
from unittest.mock import Mock

from entities.recommendation import Recommendation
from services.recommendations_service import RecommendationService, UserInputError
from repositories.recommendation_repository import RecommendationRepository


class TestRecommendationService(unittest.TestCase):
    def setUp(self):
        self.repo_mock = Mock()
        self.service = RecommendationService(self.repo_mock)
        self.repo_mock.find_recommendation_by_title.return_value = None
        self.repo_mock.insert_recommendation.return_value = None

    def test_create_new_recommendation_calls_create_with_correct_parameters(self):
        action = self.service.create_new_recommendation(
            {'title': "Tohtori Sykerö", 'type': 'video', 'author': 'Syhtöri Tukero', 'url': 'tohtorisykero.fi'})
        self.assertTrue(action)
        self.repo_mock.insert_recommendation.assert_called_with(
            {'title': "Tohtori Sykerö", 'type': 'video', 'author': 'Syhtöri Tukero', 'url': 'tohtorisykero.fi'})

    def test_create_new_recommendation_with_invalid_title(self):
        with self.assertRaises(UserInputError):
            value = self.service.create_new_recommendation(
                {'title': '', 'type': 'book', 'author': 'anonymous'})

    def test_create_new_recommendation_with_invalid_url(self):
        with self.assertRaises(UserInputError):
            value = self.service.create_new_recommendation(
                {'title': 'Best blog post', 'type': 'blog', 'author': 'anonymous', 'url': ''})

    def test_get_recommendations_returns_list(self):
        self.repo_mock.find_all_recommendations.return_value = []
        recommendations = self.service.get_recommendations()
        self.assertIsInstance(recommendations, list)

    def test_get_recommendations_returns_list_of_recommendations(self):
        self.repo_mock.find_all_recommendations.return_value = [
            Recommendation(Mock(), Mock(), Mock(), Mock())]

        recommendations = self.service.get_recommendations()

        self.assertIsInstance(recommendations[0], Recommendation)

    def test_get_recommendations_calls_repository(self):
        self.service.get_recommendations()

        self.repo_mock.find_all_recommendations.assert_called()

    def test_edit_recommendation_title_calls_repository_correctly(self):
        mock_recommendation = Mock()
        mock_recommendation.db_id = 1
        self.service._recommendations = [mock_recommendation]
        self.repo_mock.edit_recommendation_title.return_value = None
        self.service.edit_recommendation_title("Taikuri Luttinen", 0)
        self.repo_mock.edit_recommendation_title.assert_called_with(
            "Taikuri Luttinen", 1)

    def test_edit_recommendation_title_returns_true_when_success(self):
        mock_recommendation = Mock()
        mock_recommendation.db_id = 1
        self.service._recommendations = [mock_recommendation]
        self.repo_mock.edit_recommendation_title.return_value = None
        value = self.service.edit_recommendation_title("Taikuri Luttinen", 0)

        self.assertTrue(value)

    def test_edit_recommendation_title_raises_error_when_too_short(self):
        with self.assertRaises(UserInputError):
            mock_recommendation = Mock()
            mock_recommendation.db_id = 1
            self.service._recommendations = [mock_recommendation]
            self.repo_mock.edit_recommendation_title.return_value = None
            value = self.service.edit_recommendation_title("", 0)

    def test_edit_recommendation_type_calls_repository_correctly(self):
        mock_recommendation = Mock()
        mock_recommendation.db_id = 1
        self.service._recommendations = [mock_recommendation]
        self.repo_mock.edit_recommendation_type.return_value = None
        self.service.edit_recommendation_type("podcast", 0)
        self.repo_mock.edit_recommendation_type.assert_called_with(
            "podcast", 1)

    def test_edit_recommendation_type_returns_true_when_success(self):
        mock_recommendation = Mock()
        mock_recommendation.db_id = 1
        self.service._recommendations = [mock_recommendation]
        self.repo_mock.edit_recommendation_type.return_value = None
        value = self.service.edit_recommendation_type("podcast", 0)

        self.assertTrue(value)
