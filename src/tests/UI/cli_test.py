import unittest
from unittest.mock import call, Mock

from UI.cli import CLI

class TestCLI(unittest.TestCase):

    def setUp(self):
        self.mock_repo = Mock()
        self.mock_service = Mock()
        self.mock_io = Mock()

        self.UI = CLI(self.mock_service, self.mock_io)

        self.recommendation_mock = Mock()
        self.recommendation_mock.title = "Harry Potter 1"
        self.recommendation_mock.type = "book"
        self.recommendation_mock.id = 1
        self.recommendation_mock.author = "JK Rowling"
        self.recommendation_mock.isbn = "12345"
        self.recommendation_mock.description = "Harry Potter does stuff"
        self.recommendation_mock.comment = "Great book"

    def test_start_cli_calls_io_clear(self):
        self.mock_io.read.side_effect=["0"]
        self.UI.start()
        self.mock_io.clear.assert_called()

    def test_start_cli_calls_print_welcome_message(self):
        self.mock_io.read.side_effect=["0"]
        self.UI.start()

        self.mock_io.write.assert_any_call("┃ Welcome to your Recommendation library! ┃")

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

        edit_item_inputs = [
            "3",
            "1", # Select the first one
            "1", # Select Edit
            "Harry Potter 2", # New details
            "JRR Tolkien",
            "1",
            "",
            "",
            "",
            "1", # Confirm
            "0"
        ]

        self.mock_io.read.side_effect = edit_item_inputs

        self.mock_service.get_recommendations.return_value = [self.recommendation_mock]

        self.UI.start()

        self.mock_service.edit_recommendation.assert_called()

    def test_title_read_correctly(self):
        self.mock_io.read.side_effect=["1", "Book Name", "Author", "1", "", "", "", "1", "0"]
        self.UI.start()
        self.mock_io.write.assert_any_call("Title: Book Name")

    def test_adding_method_called_with_right_parameters(self):
        self.mock_io.read.side_effect=["1", "Book Name", "Author", "1", "", "", "", "1", "0"]
        self.UI.start()
        self.mock_service.create_new_recommendation.assert_called_with({
            "title": "Book Name",
            "author": "Author",
            "type": "book"
        })

    def test_get_recommendations_method_called(self):
        self.mock_io.read.side_effect=['2', "", '0']
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
        self.mock_service.get_recommendations.return_value = ["String 1", "String 2"]
        self.UI.start()

        self.mock_io.write.assert_any_call("String 1")
        self.mock_io.write.assert_any_call("String 2")

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
            [call('1: ABC'), call('2: 123')])
