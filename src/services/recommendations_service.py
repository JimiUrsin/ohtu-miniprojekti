from repositories.recommendation_repository import RecommendationRepository as default_repo

class RecommendationService:
    def __init__(self, recommendation_repository=default_repo()):
        self._recommendation_repository = recommendation_repository
        self._recommendations = None

    def create_new_recommendation(self, title, type):
        validated = self._validate_recommendation(title, type)

        if validated:
            value = self._recommendation_repository.insert_recommendation(title, type)

            return True if value is None else False

        return False

    def get_recommendations(self):
        self._recommendations = self._recommendation_repository.find_all_recommendations()

        return self._recommendations

    def edit_recommendation_title(self, new_title, index):
        validated = self._validate_recommendation(new_title, self._recommendations[index].type)

        if validated:
            value = self._recommendation_repository.edit_recommendation_title(
                new_title,
                self._recommendations[index].db_id
            )
        
            return True if value is None else False

        return False

    def edit_recommendation_type(self, new_type, index):
        validated = self._validate_recommendation(self._recommendations[index].title, new_type)

        if validated:
            value = self._recommendation_repository.edit_recommendation_type(
                new_type,
                self._recommendations[index].db_id
            )

            return True if value is None else False

        return False

    def delete_recommendation(self, index):
        value = self._recommendation_repository.delete_recommendation_by_id(
            self._recommendations[index].db_id
        )
        
        return True if value is None else False

    def _validate_recommendation(self, title, type):
        valid_types = ["book", "video", "blog", "podcast"]

        if len(title) < 2:
            return False
        if type.lower() not in valid_types:
            return False
        
        return True
