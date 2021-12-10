from database_connection import get_database_connection
from entities.recommendation import Recommendation

class RecommendationRepository:
    """
    A class for providing an interface for a database operations
    """

    def __init__(self, db_connection=get_database_connection()):
        """The constructor, inits database connection

        Args:
            db_connection: The database connection. Defaults to get_database_connection().
        """

        self.connection = db_connection

    def find_all_recommendations(self):
        """Fetches all the recommendations from database

        Returns:
            If results:     a list of Recommendation objects
            If not:         an empty list
            If db error:    sqlite3.OperationalError object
        """

        query = "SELECT * FROM Recommendations"
        results = self._read_db(query)

        if isinstance(results, list):
            recommendations = [Recommendation(result['title'], result['type'], result['id']) for result in results]
        else:
            recommendations = results

        return recommendations

    def find_recommendation_by_title(self, title):
        """Fetches a single recommendation from database by title

        Args:
            title: A title of recommendation

        Returns:
            If results:     a Recommendation object
            If not:         an empty list
            If db error:    sqlite3.OperationalError object
        """

        query = "SELECT * FROM Recommendations WHERE title = ?"
        results = self._read_db(query, [title])

        if isinstance(results, list) and len(results) > 0:
            result = Recommendation(results[0]['title'], results[0]['type'], results[0]['id'])
            print(result)
        else:
            result = results

        return result

    def insert_recommendation(self, author, recom_details):
        """Inserts a recommendation to database with title and recommendation type

        Args:
            title: A title of recommendation
            recom_type: Type of recommendation (blog, book, video, podcast)
            author: Name of author
            recom_details: A dictionary containing the details of given recommendation.

        Returns:
            None if success, sqlite3.OperationalError object if db error
        """

        if "title" not in recom_details or "type" not in recom_details:
            raise Exception("Missing required information for creating Recommendartion")
            
        if recom_details["type"] != "book":
            # Handle inserting blog, video or podcast
            if "url" not in recom_details:
                raise Exception("Missing required information for creating Recommendartion")
            
        

       # write = self._write_db(query, recom_details.values())
        
        # query_find_id = "SELECT id FROM Recommendations WHERE title = ? AND url = ?"
        query = self.create_query_for_inserting_recommendation(recom_details.keys())
        rec_id = self._write_db_return_id(query, list(recom_details.values()))

        print(rec_id)

        query_add_author = "INSERT INTO Authors (recom_id, author) VALUES (?,?)"
        return self._write_db(query_add_author, [str(rec_id), author])

    def delete_recommendation_by_id(self, db_id):
        """Delete a recommendation by title from database

        Args:
            db_id: An id of the recommendation

        Return:
            None if success, sqlite3.OperationalError object if db error
        """

        query = "DELETE FROM Recommendations WHERE id = ?"

        return self._write_db(query, [db_id])

    def edit_recommendation_title(self, new_value, db_id):
        """Edit recommendation title in database

        Args:
            new_value: new title from the user
            db_id: An id of the recommendation

        Return:
            None if success, sqlite3.OperationalError object if db error
        """

        query = "UPDATE Recommendations SET title = ? WHERE id = ?"

        return self._write_db(query, [new_value, db_id])

    def edit_recommendation_type(self, new_value, db_id):
        """Edit recommendation type in database

        Args:
            new_value: new title from the user
            db_id: An id of the recommendation

        Return:
            None if success, sqlite3.OperationalError object if db error
        """
        query = "UPDATE Recommendations SET type = ? WHERE id = ?"

        return self._write_db(query, [new_value, db_id])

    def empty_tables(self):
        """Empties whole Recommendations table from database"""

        return self._run_db_command("DELETE FROM Recommendations")

    def _read_db(self, query, variables=False):
        """A method for fetching data by queries

        Args:
            query [str]:    SQL query as str
            variables[list]:Query variables, e.g. a title. Defaults to False.

        Returns:
            If results:     Fetched items as a list of sqlite3.Row objects
            If not:         An empty list
            If db error:    sqlite3.OperationalError object
        """

        try:
            with self.connection:

                if variables is False:
                    results = self.connection.execute(query).fetchall()
                else:
                    results = self.connection.execute(query, variables).fetchall()

                return results

        except self.connection.Error as error:
            return error

    def create_query_for_inserting_recommendation(self, column_names):
        """A method that generates a SQL query for inserting values to DB tabel

        Args:
            column_names[list]: List of names of columns, where data will be inserted
                with the query
        """

        variables = ""
        question_marks = ""
        for index, value in enumerate(column_names):
            variables = f"{variables}{value}"
            question_marks = f"{question_marks}?"

            if index < len(column_names) - 1:
                variables = f"{variables}, "
                question_marks = f"{question_marks}, "

        sql_query = f"INSERT INTO Recommendations ({variables}) VALUES ({question_marks})"
        return sql_query


    def _write_db(self, query, values):
        """A method for writing data to the database

        Args:
            query[str]:     SQL query
            values[list]:   Query variables, e.g. a title

        Returns:
            If success:     None
            If db error:    sqlite3.OperationalError object
        """

        try:
            with self.connection:

                self.connection.execute(query, values)
                self.connection.commit()

                return None

        except self.connection.Error as error:
            return error

    def _write_db_return_id(self, query, values):
        """A method for writing data to the database

        Args:
            query[str]:     SQL query
            values[list]:   Query variables, e.g. a title

        Returns:
            If success:     None
            If db error:    sqlite3.OperationalError object
        """

        try:
            with self.connection:
                cursor = self.connection.cursor()
                self.connection.execute(query, values)
                self.connection.commit()

                return cursor.lastrowid

        except self.connection.Error as error:
            return error

    def _run_db_command(self, command):
        """An inner method for running various database commands,
        especially for testing purposes.

        Args:
            command:    A command to run

        Returns:
            None if success, sqlite3.OperationalError object if not
        """

        try:
            with self.connection:

                self.connection.execute(command)
                self.connection.commit()

            return None

        except self.connection.Error as error:
            return error

