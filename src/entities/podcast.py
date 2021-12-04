from entities.recommendation import Recommendation

class Podcast(Recommendation):
    """Class that describes an individual podcast recommendation.

    Attributes:
        title: A string value that describes the title of the podcast.
        type:  A string value that describes the recommendation's type.
        author: A string value that describes the author of the podcast.
        url: A string value that describes the web address of the podcast.
    """

    def __init__(self, title, author, url):
        """Constructor that creates a new podcast recommendation"""

        super().__init__(title, "Podcast")
        self.author = author
        self.url = url

    def __str__(self):
        return super().__str__() + f", Author: {self.author}, URL: {self.url}"
