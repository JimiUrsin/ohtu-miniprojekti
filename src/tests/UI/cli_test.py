import unittest
from unittest.mock import patch, call, Mock, ANY
from UI.cli import CLI


class TestCLI(unittest.TestCase):

    def setUp(self):
        self.mock_service = Mock()
        self.mock_io = Mock()
        self.UI = CLI(self.mock_service, self.mock_io)

    def test_title_read_correctly(self):
        self.mock_io.read.side_effect=["1", "Book Name", "1", "1", "0"]
        self.UI.start()
        self.mock_io.read.assert_any_call('Is "Book Name", book, correct? 1: Yes, 2: No, reinput information ')

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
        self.mock_io.read.side_effect=["2", "0"]
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
            [call('1: ABC'), call('2: 123')])