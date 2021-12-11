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

    def test_d_delete_single_recommendation_find_by_id(self):
        results = self.repository.find_all_recommendations()
        self.assertEqual(len(results), 3)
        self.repository.delete_recommendation_by_id(2)
        results = self.repository.find_all_recommendations()
        self.assertEqual(len(results), 2)

    def test_e_edit_single_recommendation_title(self):
        self.repository.edit_recommendation_title('LOTR_version2', 1)
        results = self.repository.find_all_recommendations()
        self.assertEqual(results[0].title, "LOTR_version2")

    def test_f_edit_single_recommendation_type(self):
        self.repository.edit_recommendation_type('video', 1)
        results = self.repository.find_all_recommendations()
        print(results[0])
        print(results[0].title)
        self.assertEqual(results[0].type, "video")


    def test_g_empty_tables(self):
        self.assertEqual(len(self.repository.find_all_recommendations()), 2)

        return_value = self.repository.empty_tables()

        self.assertIsNone(return_value)
        self.assertEqual(len(self.repository.find_all_recommendations()), 0)

    def test_h_empty_database(self):
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

    def test_i_insert_recommendation_query_creator_return_correct_string(self):
        column_names = ["title", "type", "url"]
        sql_query = self.repository.create_query_for_inserting_recommendation(column_names)
        self.assertEqual(sql_query, "INSERT INTO Recommendations (title, type, url) VALUES (?, ?, ?)")

    def test_j_create_new_author(self):
        author_id = self.repository._create_author_if_needed("Antti Holma")
        self.assertEqual(author_id, 1)

    def test_k_new_author_not_created_when_already_exists(self):
        self.repository._run_db_command('INSERT INTO Authors (author) VALUES ("Antti Holma")')
        author_id_antti = self.repository._read_db('SELECT id FROM Authors WHERE author = "Antti Holma"')[0][0]
        self.assertEqual(self.repository._create_author_if_needed("Antti Holma"), author_id_antti)

    def test_l_insert_new_recommendation_successfull_and_recommendation_can_be_found(self):
        details = {"title": "WizKid - Mighty Wine (Audio)", "author": "StarBoy TV", "type": "video", "url": "https://www.youtube.com/watch?v=_KXHTdq9URg", "description": "Wizkidin biisi", "comment": "Bängeri"}
        self.assertEqual(self.repository.insert_recommendation(details), None)
        
        results = self.repository._read_db("SELECT * FROM Recommendations WHERE title = ?", ["WizKid - Mighty Wine (Audio)"])[0]
        self.assertEqual(results["id"], 1)
        self.assertEqual(results["title"], "WizKid - Mighty Wine (Audio)")
        self.assertEqual(results["type"], "video")
        self.assertEqual(results["description"], "Wizkidin biisi")
        self.assertEqual(results["comment"], "Bängeri")

    def test_m_deleting_last_recommendation_of_author_deletes_author(self):
        details = {"title": "WizKid - Mighty Wine (Audio)", "author": "StarBoy TV", "type": "video", "url": "https://www.youtube.com/watch?v=_KXHTdq9URg", "description": "Wizkidin biisi", "comment": "Bängeri"}
        self.assertEqual(self.repository.insert_recommendation(details), None)
        self.assertEqual(self.repository.delete_recommendation_by_id(1), None)

        results = self.repository._read_db("SELECT * FROM Authors")
        self.assertEqual(len(results), 0)

    def test_n_creating_recommendation_with_unvalid_information_raises_exception(self):
        with self.assertRaises(Exception) as error:
            recommendation_details = {"title": "Kaverin Puolesta Kyselen", "type": "book"}
            self.repository.insert_recommendation(recommendation_details)

        with self.assertRaises(Exception) as error:
            recommendation_details = {"title": "Kaverin Puolesta Kyselen", "author": "YLE"}
            self.repository.insert_recommendation(recommendation_details)

        with self.assertRaises(Exception) as error:
            recommendation_details = {"title": "Kaverin Puolesta Kyselen", "author": "YLE", "type": "podcast"}
            self.repository.insert_recommendation(recommendation_details)
