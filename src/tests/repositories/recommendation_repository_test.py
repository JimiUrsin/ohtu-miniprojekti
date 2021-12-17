import unittest, sqlite3

from database_setup import DataBase
from entities.recommendation import Recommendation
from database_connection import get_test_database_connection
from repositories.recommendation_repository import RecommendationRepository

class TestRecommendationRepository(unittest.TestCase):
    def setUp(self):
        self.test_db = get_test_database_connection()
        self.repository = RecommendationRepository(self.test_db)

        self.repository._run_db_command("DROP TABLE Recommendations")
        DataBase().initialize_test_database()

        self.recom_lotr = {
            "title": "LOTR",
            "type": "book",
            "author": "J. R. R. Tolkien",
            "isbn": "978-3-16-148410-0",
            "description": "A book",
            "comment": "Nice",
        }

        self.recom_hp = {
            "title": "Harry Potter",
            "type": "video",
            "author": "Alfonso Cuarón",
            "url": "https://www.hbomax.com/",
            "description": "A movia about a book"
        }

        self.recom_ds = {
            "title": "Data Structures and Algorithms",
            "type": "blog",
            "author": "Thomas H. Cormen", 
            "url": "https://google.fi"
        }

        self.recom_mc = {
            "title": "Models of computation",
            "type": "blog",
            "author": "Thomas H. Cormen",
            "url": "https://google.fi"
        }

        self.new_values = {
            "title": "Taikuri Luttinen",
            "author": "Luikuri Tattinen",
            "type": "video",
            "url": "https://www.taikuri-luttinen.fi/",
            "description": "Taikuri Luttinen does some sick tricks",
            "comment": "I wanna learn some magic too"
        }

        self.recommendations = [self.recom_lotr, self.recom_hp, self.recom_ds]

    def test_find_all_recommendations_returns_empty_list_when_empty(self):
        self.assertEqual(len(self.repository.find_all_recommendations()), 0)

    def test_find_all_recommendations_returns_non_empty_list_when_results(self):
        self.repository.insert_recommendation(self.recom_lotr)

        self.assertEqual(len(self.repository.find_all_recommendations()), 1)

    def test_find_all_recommendations_returns_list_of_recommendation_objects(self):
        self.repository.insert_recommendation(self.recom_lotr)

        self.assertIsInstance(self.repository.find_all_recommendations()[0], Recommendation)

    def test_find_all_recommendations_returns_correct_lenght_list(self):
        for recommendation in self.recommendations:
            self.repository.insert_recommendation(recommendation)

        self.assertEqual(len(self.repository.find_all_recommendations()), 3)

    def test_find_all_recommendations_returns_sqlite3_error_object_when_db_error(self):
        self.repository._run_db_command("DROP TABLE Recommendations")

        self.assertIsInstance(self.repository.find_all_recommendations(), sqlite3.OperationalError)

    def test_find_all_recommendations_returns_correct_object_when_book(self):
        self.repository.insert_recommendation(self.recom_lotr.copy())

        recommendation = self.repository.find_all_recommendations()[0]

        self.assertEqual(recommendation.title, self.recom_lotr['title'])
        self.assertEqual(recommendation.type, self.recom_lotr['type'])
        self.assertEqual(recommendation.author, self.recom_lotr['author'])
        self.assertEqual(recommendation.isbn, self.recom_lotr['isbn'])
        self.assertEqual(recommendation.description, self.recom_lotr['description'])
        self.assertEqual(recommendation.comment, self.recom_lotr['comment'])

    def test_find_all_recommendations_returns_correct_object_when_video(self):
        self.repository.insert_recommendation(self.recom_hp.copy())

        recommendation = self.repository.find_all_recommendations()[0]

        self.assertEqual(recommendation.title, self.recom_hp['title'])
        self.assertEqual(recommendation.type, self.recom_hp['type'])
        self.assertEqual(recommendation.author, self.recom_hp['author'])
        self.assertEqual(recommendation.url, self.recom_hp['url'])
        self.assertEqual(recommendation.description, self.recom_hp['description'])

    def test_find_all_recommendations_returns_correct_object_when_blog(self):
        self.repository.insert_recommendation(self.recom_ds.copy())

        recommendation = self.repository.find_all_recommendations()[0]

        self.assertEqual(recommendation.title, self.recom_ds['title'])
        self.assertEqual(recommendation.type, self.recom_ds['type'])
        self.assertEqual(recommendation.author, self.recom_ds['author'])
        self.assertEqual(recommendation.url, self.recom_ds['url'])

    def test_find_single_recommendation_returns_list_when_no_results(self):
        self.assertIsInstance(self.repository.find_recommendation_by_title("Harry Potter"), list)

    def test_find_single_recommendation_returns_empty_list_when_no_results(self):
        self.assertEqual(len(self.repository.find_recommendation_by_title("Harry Potter")), 0)

    def test_find_single_recommendation_returns_recommendation_object_when_results(self):
        self.repository.insert_recommendation(self.recom_lotr)

        self.assertIsInstance(self.repository.find_recommendation_by_title("LOTR"), Recommendation)

    def test_find_single_recommendation_returns_sqlite3_error_object_when_db_error(self):
        self.repository._run_db_command("DROP TABLE Recommendations")

        self.assertIsInstance(self.repository.find_recommendation_by_title("Harry Potter"), sqlite3.OperationalError)

    def test_find_single_recommendation_returns_correct_object_when_book(self):
        self.repository.insert_recommendation(self.recom_lotr.copy())

        recommendation = self.repository.find_recommendation_by_title("LOTR")

        self.assertEqual(recommendation.title, self.recom_lotr['title'])
        self.assertEqual(recommendation.type, self.recom_lotr['type'])
        self.assertEqual(recommendation.author, self.recom_lotr['author'])
        self.assertEqual(recommendation.isbn, self.recom_lotr['isbn'])
        self.assertEqual(recommendation.description, self.recom_lotr['description'])
        self.assertEqual(recommendation.comment, self.recom_lotr['comment'])

    def test_find_single_recommendation_returns_correct_object_when_video(self):
        self.repository.insert_recommendation(self.recom_hp.copy())

        recommendation = self.repository.find_recommendation_by_title("Harry Potter")

        self.assertEqual(recommendation.title, self.recom_hp['title'])
        self.assertEqual(recommendation.type, self.recom_hp['type'])
        self.assertEqual(recommendation.author, self.recom_hp['author'])
        self.assertEqual(recommendation.url, self.recom_hp['url'])
        self.assertEqual(recommendation.description, self.recom_hp['description'])

    def test_find_single_recommendation_returns_correct_object_when_blog(self):
        self.repository.insert_recommendation(self.recom_ds.copy())

        recommendation = self.repository.find_recommendation_by_title(self.recom_ds['title'])

        self.assertEqual(recommendation.title, self.recom_ds['title'])
        self.assertEqual(recommendation.type, self.recom_ds['type'])
        self.assertEqual(recommendation.author, self.recom_ds['author'])
        self.assertEqual(recommendation.url, self.recom_ds['url'])

    def test_insert_recommendation_inserts_book_correctly(self):
        self.repository.insert_recommendation(self.recom_lotr.copy())

        recom = self.repository.find_recommendation_by_title("LOTR").__dict__

        database_id = recom['db_id']

        del recom['db_id']
        del recom['url']

        self.assertEqual(database_id, 1)

        for key in recom:
            self.assertEqual(recom[key], self.recom_lotr[key])

    def test_insert_recommendation_inserts_video_correctly(self):
        self.repository.insert_recommendation(self.recom_hp.copy())

        recom = self.repository.find_recommendation_by_title(self.recom_hp['title']).__dict__
        database_id = recom['db_id']

        del recom['db_id']
        del recom['isbn']
        del recom['comment']

        self.assertEqual(database_id, 1)

        for key in recom:
            self.assertEqual(recom[key], self.recom_hp[key])

    def test_insert_recommendation_inserts_blog_correctly(self):
        self.repository.insert_recommendation(self.recom_ds.copy())

        recom = self.repository.find_recommendation_by_title(self.recom_ds['title']).__dict__
        database_id = recom['db_id']

        del recom['db_id']
        del recom['isbn']
        del recom['comment']
        del recom['description']

        self.assertEqual(database_id, 1)

        for key in recom:
            self.assertEqual(recom[key], self.recom_ds[key])

    def test_insert_recommendation_returns_sqlite_error_when_db_error_on_recommendations_table(self):
        self.repository._run_db_command("DROP TABLE Recommendations")

        self.assertIsInstance(self.repository.insert_recommendation(self.recom_ds), sqlite3.OperationalError)

    def test_insert_recommendation_returns_sqlite_error_when_db_error_on_authors_table(self):
        self.repository._run_db_command("DROP TABLE Authors")

        self.assertIsInstance(self.repository.insert_recommendation(self.recom_ds), sqlite3.OperationalError)

    def test_insert_recommendation_returns_database_id_when_success(self):
        self.assertEqual(self.repository.insert_recommendation(self.recom_lotr), 1)

    def test_insert_inserts_recommendation_when_author_already_exists(self):
        for recommendation in self.recommendations:
            self.repository.insert_recommendation(recommendation)

        self.repository.insert_recommendation(self.recom_mc)

        self.assertEqual(len(self.repository.find_all_recommendations()), 4)

    def test_delete_recommendation_deletes_author_when_author_has_no_more_works_on_db(self):
        self.repository.insert_recommendation(self.recom_mc)
        self.repository.insert_recommendation(self.recom_ds)

        self.assertEqual(len(self.repository.find_all_recommendations()), 2)

        self.repository.delete_recommendation_by_id(1)
        self.assertEqual(len(self.repository.find_all_recommendations()), 1)

        query = "SELECT * FROM Authors"
        self.assertEqual(len(self.repository._read_db(query)), 1)

        self.repository.delete_recommendation_by_id(2)
        self.assertEqual(len(self.repository._read_db(query)), 0)

    def test_delete_recommendation_find_all_returns_no_results_after_delete(self):
        self.repository.insert_recommendation(self.recom_lotr)
        recommendation = self.repository.find_recommendation_by_title("LOTR")

        self.assertEqual(len(self.repository.find_all_recommendations()), 1)

        self.repository.delete_recommendation_by_id(recommendation.db_id)

        self.assertEqual(len(self.repository.find_all_recommendations()), 0)

    def test_delete_recommendation_deletes_one_row_from_results_correctly(self):
        for recommendation in self.recommendations:
            self.repository.insert_recommendation(recommendation)

        self.assertEqual(len(self.repository.find_all_recommendations()), 3)

        recommendation = self.repository.find_recommendation_by_title("LOTR")
        self.repository.delete_recommendation_by_id(recommendation.db_id)

        self.assertEqual(len(self.repository.find_all_recommendations()), 2)

    def test_delete_recommendation_deletes_two_rows_from_results_correctly(self):
        for recommendation in self.recommendations:
            self.repository.insert_recommendation(recommendation)

        recommendations = self.repository.find_all_recommendations()
        self.assertEqual(len(recommendations), 3)

        for i in range(0, 2):
            self.repository.delete_recommendation_by_id(recommendations[i].db_id)

        recommendations = self.repository.find_all_recommendations()
        self.assertEqual(len(recommendations), 1)
        self.assertEqual(recommendations[0].db_id, 3)

    def test_delete_recommendation_returns_sqlite_error_on_db_error(self):
        self.repository._run_db_command("DROP TABLE Recommendations")

        self.assertIsInstance(self.repository.delete_recommendation_by_id(1), sqlite3.OperationalError)

    def test_delete_recommendation_returns_database_id_on_success(self):
        self.repository.insert_recommendation(self.recom_lotr)

        recommendation = self.repository.find_recommendation_by_title("LOTR")
        db_id = recommendation.db_id

        self.assertEqual(self.repository.delete_recommendation_by_id(db_id), db_id)

    def test_edit_recommendation_changes_values(self):
        lotr_id = self.repository.insert_recommendation(self.recom_lotr)
        self.repository.edit_recommendation(self.new_values, lotr_id)

        edited_recommendation = self.repository.find_all_recommendations()[0]

        self.assertEqual(edited_recommendation.title, self.new_values["title"])
        self.assertEqual(edited_recommendation.type, self.new_values["type"])
        self.assertEqual(edited_recommendation.url, self.new_values["url"])
        self.assertEqual(edited_recommendation.description, self.new_values["description"])
        self.assertEqual(edited_recommendation.comment, self.new_values["comment"])

    def test_edit_recommendation_deletes_old_author(self):
        author = self.recom_lotr["author"]

        lotr_id = self.repository.insert_recommendation(self.recom_lotr)
        self.repository.edit_recommendation(self.new_values, lotr_id)

        author_list = self.repository._read_db(
            "SELECT id FROM Authors WHERE author = ?;",
            [author]
        )

        self.assertEqual(len(author_list), 0)

    def test_edit_recommendation_creates_new_author(self):
        lotr_id = self.repository.insert_recommendation(self.recom_lotr)
        self.repository.edit_recommendation(self.new_values, lotr_id)

        author_list = self.repository._read_db(
            "SELECT id FROM Authors WHERE author = ?;",
            [self.new_values["author"]]
        )

        self.assertEqual(len(author_list), 1)

    def test_edit_recommendation_creates_new_author_recommendation(self):
        lotr_id = self.repository.insert_recommendation(self.recom_lotr)

        self.repository.edit_recommendation(self.new_values, lotr_id)

        authrecoms = self.repository._read_db(
            "SELECT author_id FROM AuthorRecommendations WHERE recom_id = ?;",
            [lotr_id]
        )

        authrecom_id = authrecoms[0]["author_id"]

        authors = self.repository._read_db(
            "SELECT id FROM Authors WHERE author = ?;",
            [self.new_values["author"]]
        )

        taikuri_id = authors[0]["id"]

        self.assertEqual(authrecom_id, taikuri_id)

    def test_empty_tables_empties_tables(self):
        for recommendation in self.recommendations:
            self.repository.insert_recommendation(recommendation)

        self.assertEqual(len(self.repository.find_all_recommendations()), 3)

        self.repository.empty_tables()

        self.assertEqual(len(self.repository.find_all_recommendations()), 0)

    def test_edit_recommendation_status_gets_false_when_no_such_table_Recommendations(self):
        self.repository._run_db_command("DROP TABLE Recommendations")

        self.assertFalse(self.repository.edit_recommendation(self.recom_ds, 1))

    def test_edit_recommendation_status_gets_false_when_no_such_table_AuthorRecommendations(self):
        self.repository._run_db_command("DROP TABLE AuthorRecommendations")

        self.assertFalse(self.repository.edit_recommendation(self.recom_ds, 1))
