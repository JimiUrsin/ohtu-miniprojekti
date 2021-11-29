from entities.recommendation import Recommendation
from repositories.recommendation_repository import recommendation_repository

class RecommendationService:
    """
    A single reading / watching / listening recommendation
    """

    def __init__(self, recommendation_repository):
        self._recommendation_repository = recommendation_repository

    def create_new_recommendation(self, title, recom_type):

        """Create a new recommendation"""

        self.validate(title, recom_type)

        recommendation = self._recommendation_repository.insert_recommendation(
            Recommendation(title, recom_type))

        return recommendation      

    def get_title(self):
        return self.__title


    def validate(self, title, recom_type):
        if len(title) < 1:
            raise Exception("Recommendation has to have a title of at least 2 characters")

        valid_recommendation = ["book", "video", "blog", "podcast"]

        if recom_type not in valid_recommendation:
            raise Exception("Recommendation type should be book, video, blog or podcast")

        self.__title = title

recommendation_repository = RecommendationService(recommendation_repository)