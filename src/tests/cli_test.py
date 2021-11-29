import unittest
from unittest.mock import patch, call, Mock, ANY
from UI.cli import CLI


class TestCLI(unittest.TestCase):

    def setUp(self):
        self.mock_service = Mock()
        self.UI = CLI(self.mock_service)

    @patch('builtins.input', side_effect=['1', 'Book Name', '1', '0'])
    @patch('builtins.print')
    def test_title_read_correctly(self, mock_input, mock_print):
        self.UI.start()
        mock_print.assert_has_calls(
            [call('Add "Book Name" to collection? 1: Yes, 2: No, reinput title, 0: Quit ')])

    @patch('builtins.input', side_effect=['1', 'Book Name', '1', '0'])
    def test_adding_method_called(self, mock_input):
        self.UI.start()
        self.mock_service.create_new_recommendation.assert_called()


    @patch('builtins.input', side_effect=['2', '0'])
    def test_fetch_all_method_called(self, mock_input):
        self.mock_service.fetch_all.return_value = ['']
        self.UI.start()
        self.mock_service.fetch_all.assert_called()

