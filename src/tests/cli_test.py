import unittest
from unittest.mock import patch, call, Mock, ANY
from UI.cli import CLI


class TestCLI(unittest.TestCase):

    def setUp(self):
        self.mock_service = Mock()
        self.UI = CLI(self.mock_service)

    @patch('builtins.input', side_effect=['1', 'Book Name', '1', '1', '0'])
    @patch('builtins.print')
    def test_title_read_correctly(self, mock_input, mock_print):
        self.UI.start()
        mock_print.assert_has_calls(
            [call('Is "Book Name", a book, correct? 1: Yes, 2: No, reinput information, 0: Quit ')])

    @patch('builtins.input', side_effect=['1', 'Book Name', '1', '1', '0'])
    def test_adding_method_called_with_right_parameters(self, mock_input):
        self.UI.start()
        self.mock_service.create_new_recommendation.assert_called_with(
            'Book Name', 'book')

    @patch('builtins.input', side_effect=['2', '0'])
    def test_get_recommendations_method_called(self, mock_input):
        self.mock_service.get_recommendations.return_value = []
        self.UI.start()
        self.mock_service.get_recommendations.assert_called()
"""
    @patch('builtins.input', side_effect=['2', '0'])
    @patch('builtins.print')
    def test_correct_print_when_no_recommendations(self, mock_input, mock_print):
        self.mock_service.get_recommendations.return_value = []
        self.UI.start()
        mock_print.assert_has_calls(
            [call('You have no recommendations saved.')])

    @patch('builtins.input', side_effect=['2', '0'])
    @patch('builtins.print')
    def test_recommendations_printed_correctly(self, mock_input, mock_print):
        self.mock_service.get_recommendations.return_value = ['ABC', '123']
        self.UI.start()
        mock_print.assert_has_calls(
            [call('ABC'), call('123')]) """
