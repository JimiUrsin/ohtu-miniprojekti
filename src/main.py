from UI.cli import CLI
from entities.recommendation import Recommendation
from services.recommendations_service import RecommendationService


def main():
    print("Hello world!")
    recommendation_repository = None
    recommendation_service = RecommendationService(recommendation_repository)
    UI = CLI(recommendation_service)
    UI.start()


if __name__ == '__main__':
    main()
