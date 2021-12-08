from entities.recommendation import Recommendation

class Blog(Recommendation):
    """Class that describes an individual blog recommendation.

    Attributes:
        title: A string value that describes the title of the blog.
        type:  A string value that describes the recommendation's type.
        author: A string value that describes the author of the blog
        url: A string value that describes the web address of the blog
    """

    def __init__(self, title, author, url, db_id):
        """Constructor that creates a new blog recommendation"""

        super().__init__(title, "blog", db_id)
        self.author = author
        self.url = url

    def __str__(self):
        return super().__str__() + f", Author: {self.author}, URL: {self.url}"
