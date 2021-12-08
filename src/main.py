from repositories.recommendation_repository import RecommendationRepository
from services.console_io_service import ConsoleIOService
from services.recommendations_service import RecommendationService
from UI.cli import CLI


def main():
    """Construct and run the application's command line interface"""
    recommendation_repository = RecommendationRepository()
    recommendation_service = RecommendationService(recommendation_repository)
    console_io_service = ConsoleIOService()
    cli = CLI(recommendation_service, console_io_service)
    cli.start()


if __name__ == '__main__':
    main()
