
from entities.recommendation import Recommendation

from entities.recommendation import Recommendation

class Book(Recommendation):
    """Class that describes an individual book recommendation.

    Attributes:
        title: A string value that describes the title of the book.
        type:  A string value that describes the recommendation's type.
        author: A string value that describes the author of the book.
    """

    def __init__(self, title, author):
        """Constructor that creates a new book recommendation"""

        super().__init__(title, "book")
        self.author = author

    def __str__(self):
        return super().__str__() + f", Author: {self.author}"
