from repositories.recommendation_repository import RecommendationRepository as default_repo


class RecommendationService:
    """Provides functionality for safely communicating with the database repository"""

    def __init__(self, recommendation_repository=default_repo()):
        self._recommendation_repository = recommendation_repository
        self._recommendations = None

    def create_new_recommendation(self, recom_details):
        """Inserts a new recommendation into the database

        Args:
            recom_details: Dictionary containing information of the recommendation to be added

        Returns:
            True if insertion was successful
            False otherwise
        """

        # validated = self._validate_recommendation(recom_details)
        validated = True

        if validated:
            value = self._recommendation_repository.insert_recommendation(recom_details)

            return value is None

        return False

    def get_recommendations(self):
        """Retrieves all recommendations from the database and returns them"""
        self._recommendations = self._recommendation_repository.find_all_recommendations()

        return self._recommendations

    def edit_recommendation_title(self, new_title, index):
        """Edits the title of a given recommendation in the database

        Args:
            new_title: New title for the recommendation to be changed
            index: Recommendation list index of the recommendation to be changed

        Returns:
            True if the change was successful
            False otherwise
        """
        # validated = self._validate_recommendation({'title': new_title})
        validated = True

        if validated:
            value = self._recommendation_repository.edit_recommendation_title(
                new_title,
                self._recommendations[index].db_id
            )

            return value is None

        return False

    def edit_recommendation_type(self, new_type, index):
        """Edits the type of a given recommendation in the database

        Args:
            new_type: New type for the recommendation to be changed
            index: Recommendation list index of the recommendation to be changed

        Returns:
            True if the change was successful
            False otherwise
        """

        # validated = self._validate_recommendation({'type': new_type})
        validated = True

        if validated:
            value = self._recommendation_repository.edit_recommendation_type(
                new_type,
                self._recommendations[index].db_id
            )

            return value is None

        return False

    def delete_recommendation(self, index):
        """Deletes a recommendation based on its index, returns True if successful"""

        value = self._recommendation_repository.delete_recommendation_by_id(
            self._recommendations[index].db_id
        )

        return value is None

    def _validate_recommendation(self, title, recom_type):
        valid_types = ["book", "video", "blog", "podcast"]

        if len(title) < 2:
            return False
        if recom_type.lower() not in valid_types:
            return False

        return True
