from tests.stub_io import StubIO
from services.recommendations_service import RecommendationService
from repositories.recommendation_repository import RecommendationRepository
from database_connection import get_test_database_connection
from UI.cli import CLI

class RobotLibrary:
    def __init__(self):
        self._repository = RecommendationRepository(get_test_database_connection())
        self._service = RecommendationService(self._repository)

        self._io = StubIO()
        self._cli = CLI(self._service, self._io)

    def input(self, value):
        self._io.add_input(value)

    def run_application(self):
        self._cli.start()

    def output_should_contain(self, output):
        if output not in self._io.outputs:
            raise AssertionError(f"Specified output was not found in output list. Outputs were {self._io.outputs}")