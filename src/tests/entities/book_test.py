from entities.book import Book
import unittest

class TestBook(unittest.TestCase):
    def setUp(self):
        self.author = "J.K. Rowling"
        self.harry_potter = Book("Harry Potter and The Chamber of Secrets", self.author, 0)

    def test_book_author_is_correct(self):
        self.assertEqual(self.harry_potter.author, self.author)

    def test_string_representation(self):
        self.assertEqual(str(self.harry_potter), "Harry Potter and The Chamber of Secrets (book), Author: J.K. Rowling")
