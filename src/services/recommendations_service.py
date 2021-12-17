from repositories.recommendation_repository import RecommendationRepository as default_repo


class UserInputError(Exception):
    pass


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

        validated = self._validate_recommendation(recom_details)
        unique = self._check_uniqueness(recom_details['title'])

        if validated and unique:
            value = self._recommendation_repository.insert_recommendation(
                recom_details)

            return value is None

        return False

    def get_recommendations(self):
        """Retrieves all recommendations from the database and returns them"""
        self._recommendations = self._recommendation_repository.find_all_recommendations()

        return self._recommendations

    def edit_recommendation(self, recom_details, index):
        """Edits a recommendation to match new values
        Checks to see if the new values given are valid
        Args:
            recom_details: A dictionary with all the attributes required for the recommendation type
            index: Recommendation list index of the recommendation to be edited
        Returns:
            True if the edit was successful
            False otherwise
        """
        try:
            self._validate_recommendation(recom_details)
        except UserInputError:
            return False

        db_id = self._recommendations[index].db_id
        self._recommendation_repository.edit_recommendation(
            recom_details, db_id)
        return True

    def delete_recommendation(self, index):
        """Deletes a recommendation based on its index, returns True if successful"""

        value = self._recommendation_repository.delete_recommendation_by_id(
            self._recommendations[index].db_id
        )

        if value is None:
            raise UserInputError("Deleting Recommendation was not successful")
        value is int

    def _validate_recommendation(self, recom_details):
        """Make sure that titles are unique and check that necessary fields for creating a Recommendation
        are provided"""
        for field in ('title', 'type', 'author'):
            if field in recom_details and len(recom_details[field]) < 1:
                raise UserInputError(
                    "Missing required information for creating Recommendation")

        if 'type' in recom_details and 'url' in recom_details and recom_details["type"] != "book":
            if len(recom_details["url"]) < 1:
                raise UserInputError(
                    "Missing required information for creating Recommendation")

        for field in recom_details:
            if len(recom_details[field]) > 1000:
                raise UserInputError(
                    f"{field} is too long")

        return True

    def _check_uniqueness(self, title):
        existing = self._recommendation_repository.find_recommendation_by_title(
            title)
        if existing:
            raise UserInputError(
                "Recommendation already exists with this title")
        return True
