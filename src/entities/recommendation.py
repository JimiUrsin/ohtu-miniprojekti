class Recommendation:
    """Class that describes an individual recommendation.

    Attributes:
        title: A string value that describes the recommendation's title.
        type:  A string value that describes what type of a recommendation is.
        """

    def __init__(self, title, recom_type, db_id, author, url=None, isbn=None, description=None, comment=None):
        """Constructor that creates a new recommendation"""

        self.title = title
        self.type = recom_type
        self.db_id = db_id
        self.author = author
        self.url = url
        self.isbn = isbn
        self.description = description
        self.comment = comment

    def __str__ (self):
        recom_string = f'{self.title} ({self.type}), Author: {self.author}'
        if self.type != 'book':
            recom_string += f', URL: {self.url}'
        elif self.isbn:
            recom_string += f', ISBN: {self.isbn}'
        if self.description:
            recom_string += f', Decription: {self.description}'
        if self.comment:
            recom_string += f', Comment: {self.comment}'
        return recom_string
