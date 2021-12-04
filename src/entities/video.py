from entities.recommendation import Recommendation

class Video(Recommendation):
    """Class that describes an individual video recommendation.

    Attributes:
        title: A string value that describes the title of the video.
        type:  A string value that describes the recommendation's type.
        author: A string value that describes the author of the video.
        url: A string value that describes the web address of the video.
    """

    def __init__(self, title, author, url):
        """Constructor that creates a new video recommendation"""

        super().__init__(title, "video")
        self.author = author
        self.url = url

    def __str__(self):
        return super().__str__() + f", Author: {self.author}, URL: {self.url}"
