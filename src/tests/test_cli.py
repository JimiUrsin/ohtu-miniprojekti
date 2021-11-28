import unittest
from unittest.mock import patch, call, Mock, ANY
from cli import CLI

class TestCLI(unittest.TestCase):

    def setUp(self):
        self.UI = CLI(Mock())

    @patch('builtins.input', side_effect = ['1', 'Book Name', '1', '0'])
    @patch('builtins.print')
    def test_title_read_correctly(self, mock_input, mock_print):
        self.UI.start()
        mock_print.assert_has_calls([call('Add "Book Name" to collection? 1: Yes, 2: No, reinput title, 0: Quit ')])