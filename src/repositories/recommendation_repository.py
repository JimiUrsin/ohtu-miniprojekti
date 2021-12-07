from database_connection import get_database_connection, get_test_database_connection
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
            recommendations = [Recommendation(result['title'], result['type']) for result in results]
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
            result = Recommendation(results[0]['title'], results[0]['type'])
            print(result)
        else:
            result = results

        return result

    def insert_recommendation(self, title, recom_type):
        """Inserts a recommendation to database with title and recommendation type

        Args:
            title: A title of recommendation

        Returns:
            None if success, sqlite3.OperationalError object if db error
        """

        query = "INSERT INTO Recommendations (title, type) VALUES (?,?)"

        return self._write_db(query, [title, recom_type])

    def delete_recommendation_by_title(self, title):
        """Delete a recommendation by title from database
        
        Args:
            title: A tilte of recommendation

        Return:
            None if success, sqlite3.OperationalError object if db error 
        """

        query = "DELETE FROM Recommendations WHERE title = ?"

        return self._write_db(query, [title])

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

recommendation_repository = RecommendationRepository(get_database_connection)
