class Recommendation:
    """Class that descripes an individual recommendation.
    
    Attributes:
        title: A string value that describes the recommendation's title.
        type:  A string value that describes what type of a recommendation is.
        """


    def __init__(self, title, recom_type):
        """Constructor that creates a new recommendation"""

        self.title = title
        self.type = recom_type