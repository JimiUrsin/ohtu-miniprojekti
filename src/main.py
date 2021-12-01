from UI.cli import CLI
from entities.recommendation import Recommendation
from services.recommendations_service import RecommendationService
from repositories.recommendation_repository import RecommendationRepository


def main():
    recommendation_repository = RecommendationRepository()
    recommendation_service = RecommendationService(recommendation_repository)
    UI = CLI(recommendation_service)
    UI.start()


if __name__ == '__main__':
    main()
