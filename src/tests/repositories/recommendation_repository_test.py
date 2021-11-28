import unittest, sqlite3
from database_setup import DataBase
from entities.recommendation import Recommendation
from database_connection import get_test_database_connection
from repositories.recommendation_repository import RecommendationRepository

class TestRecommendationRepository(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_db = get_test_database_connection()
        cls.repository = RecommendationRepository(cls.test_db)

        cls.repository.empty_tables()

        cls.recommendation_lotr = Recommendation("LOTR")
        cls.recommendation_hp = Recommendation("Harry Potter")
        cls.recommendation_ds = Recommendation("Data Structures and Algorithms")

    def test_a_insert_recommendation(self):
        case_a = self.repository.insert_recommendation(self.recommendation_lotr.get_title())
        case_b = self.repository.insert_recommendation(self.recommendation_hp.get_title())
        case_c = self.repository.insert_recommendation(self.recommendation_ds.get_title())

        self.assertIsNone(case_a)
        self.assertIsNone(case_b)
        self.assertIsNone(case_c)

    def test_b_find_all_recommendations(self):        
        results = self.repository.find_all_recommendations()

        self.assertEqual(len(results), 3)
        self.assertIsInstance(results[0], Recommendation)
        self.assertEqual(results[0].get_title(), "LOTR")
        self.assertEqual(results[-1].get_title(), "Data Structures and Algorithms")

    def test_c_find_recommendation_by_title(self):
        result = self.repository.find_recommendation_by_title("Harry Potter")

        self.assertEqual(result.get_title(), self.recommendation_hp.get_title())
        self.assertIsInstance(result, Recommendation)
        self.assertEqual(len(self.repository.find_recommendation_by_title("AIs")), 0)
        self.assertIsInstance(self.repository.find_recommendation_by_title("AIs"), list)

    def test_d_empty_tables(self):
        self.assertEqual(len(self.repository.find_all_recommendations()), 3)

        return_value = self.repository.empty_tables()

        self.assertIsNone(return_value)
        self.assertEqual(len(self.repository.find_all_recommendations()), 0)

    def test_e_empty_database(self):
        self.repository._run_db_command("DROP TABLE Recommendations")

        results = self.repository.find_all_recommendations()
        result = self.repository.find_recommendation_by_title("Harry Potter")
        insert_return = self.repository.insert_recommendation("Pippa Possun retket")
        empty_tables_return = self.repository.empty_tables()

        self.assertIsInstance(result, sqlite3.OperationalError)
        self.assertIsInstance(results, sqlite3.OperationalError)
        self.assertIsInstance(insert_return, sqlite3.OperationalError)
        self.assertIsInstance(empty_tables_return, sqlite3.OperationalError)

        DataBase().initialize_test_database()
