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

        cls.recom_lotr = Recommendation("LOTR", "book", 1)
        cls.recom_hp = Recommendation("Harry Potter", "video", 2)
        cls.recom_ds = Recommendation("Data Structures and Algorithms", "blog", 3)

        cls.recommendations = [cls.recom_lotr, cls.recom_hp, cls.recom_ds]

    def test_a_insert_recommendation(self):
        for recom in self.recommendations:
            self.assertIsNone(self.repository.insert_recommendation(recom.title, recom.type))

    def test_b_find_all_recommendations(self):        
        results = self.repository.find_all_recommendations()

        self.assertEqual(len(results), 3)
        self.assertIsInstance(results[0], Recommendation)
        self.assertEqual(results[0].title, "LOTR")
        self.assertEqual(results[-1].title, "Data Structures and Algorithms")
        self.assertEqual(results[-1].db_id, self.recommendations[-1].db_id)

    def test_c_find_recommendation_by_title(self):
        result = self.repository.find_recommendation_by_title("Harry Potter")

        self.assertEqual(result.title, self.recommendations[1].title)
        self.assertIsInstance(result, Recommendation)
        self.assertEqual(result.db_id, self.recommendations[1].db_id)
        self.assertEqual(len(self.repository.find_recommendation_by_title("AIs")), 0)
        self.assertIsInstance(self.repository.find_recommendation_by_title("AIs"), list)

    def test_d_delete_single_recommendation_find_by_title(self):
        results = self.repository.find_all_recommendations()
        self.assertEqual(len(results), 3)
        self.repository.delete_recommendation_by_title("Harry Potter")
        results = self.repository.find_all_recommendations()
        self.assertEqual(len(results), 2)

    def test_edit_single_recommendation(self):
        pass

    def test_e_empty_tables(self):
        self.assertEqual(len(self.repository.find_all_recommendations()), 2)

        return_value = self.repository.empty_tables()

        self.assertIsNone(return_value)
        self.assertEqual(len(self.repository.find_all_recommendations()), 0)

    def test_f_empty_database(self):
        self.repository._run_db_command("DROP TABLE Recommendations")

        results = self.repository.find_all_recommendations()
        result = self.repository.find_recommendation_by_title("Harry Potter")
        insert_return = self.repository.insert_recommendation("Pippa Possun retket", "video")
        empty_tables_return = self.repository.empty_tables()

        self.assertIsInstance(result, sqlite3.OperationalError)
        self.assertIsInstance(results, sqlite3.OperationalError)
        self.assertIsInstance(insert_return, sqlite3.OperationalError)
        self.assertIsInstance(empty_tables_return, sqlite3.OperationalError)

        DataBase().initialize_test_database()
