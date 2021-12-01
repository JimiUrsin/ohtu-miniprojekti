from UI.cli import CLI
from entities.recommendation import Recommendation
from services.recommendations_service import RecommendationService
from repositories.recommendation_repository import RecommendationRepository
from services.console_io_service import ConsoleIOService


def main():
    recommendation_repository = RecommendationRepository()
    recommendation_service = RecommendationService(recommendation_repository)
    console_io_service = ConsoleIOService()
    UI = CLI(recommendation_service, console_io_service)
    UI.start()


if __name__ == '__main__':
    main()
