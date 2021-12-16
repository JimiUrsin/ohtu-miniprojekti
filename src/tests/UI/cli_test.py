import unittest
from unittest import mock
from unittest.mock import patch, call, Mock, ANY

from UI.cli import CLI
from tests.stub_io import StubIO
from services.recommendations_service import RecommendationService as test_srvc
from database_connection import get_test_database_connection as test_db
from repositories.recommendation_repository import RecommendationRepository

class TestCLI(unittest.TestCase):

    def setUp(self):
        self.mock_repo = Mock(wraps=RecommendationRepository(test_db()))
        self.mock_service = Mock(wraps=test_srvc(self.mock_repo))
        self.mock_io = Mock()#wraps=StubIO())

        self.UI = CLI(self.mock_service, self.mock_io)

        self.mock_repo.empty_tables()

    def test_start_cli_calls_io_clear(self):
        self.mock_io.read.side_effect=["0"]
        self.UI.start()
        self.mock_io.clear.assert_called()

    def test_start_cli_calls_print_welcome_message(self):
        self.mock_io.read.side_effect=["0"]
        self.UI.start()
        calls = self.mock_io.write.call_args_list

        self.assertTrue(" Welcome to your Recommendation library! " in str(calls[1].args))

    def test_start_cli_calls_add_new_when_chosen(self):
        inputs = ["1"]*8
        inputs.append("0")

        self.mock_io.read.side_effect=inputs

        self.UI.start()
        self.mock_service.create_new_recommendation.assert_called()

    def test_start_cli_calls_browse_when_chosen(self):
        self.mock_io.read.side_effect=["2", "0", "0"]
        self.UI.start()

        calls = self.mock_io.write.call_args_list
        msg = "You have no recommendations saved."
        check = any(msg in str(output.args) for output in calls)

        self.mock_service.get_recommendations.assert_called()
        self.assertTrue(check)

    def test_start_cli_calls_edit_or_delete_when_chosen(self):
        first_inputs = ["1"]*8
        second_inputs = ["3", "1", "0", "0"]
        inputs = first_inputs + second_inputs
        first_inputs.append("0")
        self.mock_io.read.side_effect=inputs

        self.UI.start()

        self.mock_service.get_recommendations.assert_called()

    """def test_title_read_correctly(self):
        self.mock_io.read.side_effect=["1", "Book Name", "1", "1", "0"]
        self.UI.start()
        self.mock_io.write.assert_any_call('Is "Book Name", book, correct?')

    def test_adding_method_called_with_right_parameters(self):
        self.mock_io.read.side_effect=["1", "Book Name", "1", "1", "0"]
        self.UI.start()
        self.mock_service.create_new_recommendation.assert_called_with(
            'Book Name', 'book')

    def test_get_recommendations_method_called(self):
        self.mock_io.read.side_effect=['2', '0']
        self.mock_service.get_recommendations.return_value = []
        self.UI.start()
        self.mock_service.get_recommendations.assert_called()

    def test_correct_print_when_no_recommendations(self):
        self.mock_io.read.side_effect=["2", "0"]
        self.mock_service.get_recommendations.return_value = []
        self.UI.start()
        self.mock_io.write.assert_any_call('You have no recommendations saved.')

    def test_recommendations_printed_correctly(self):
        self.mock_io.read.side_effect=["2", "", "0"]
        self.mock_service.get_recommendations.return_value = ['ABC', '123']
        self.UI.start()
        self.mock_io.write.assert_has_calls(
            [call('ABC'), call('123')])

    def test_correct_print_in_edit_mode_no_recommendations(self):
        self.mock_io.read.side_effect=["3", "0", "0"]
        self.mock_service.get_recommendations.return_value = []
        self.UI.start()
        self.mock_io.write.assert_has_calls(
            [call('You have no recommendations saved.')])

    def test_recommendations_printed_correctly_in_edit_mode(self):
        self.mock_io.read.side_effect=["3", "0", "0"]
        self.mock_service.get_recommendations.return_value = ['ABC', '123']
        self.UI.start()
        self.mock_io.write.assert_has_calls(
            [call('1: ABC'), call('2: 123')])"""
