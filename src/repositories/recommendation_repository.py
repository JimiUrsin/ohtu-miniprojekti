from database_connection import get_database_connection
from entities.recommendation import Recommendation

class RecommendationRepository:
    """
    A class which provides an interface for a database operations
    """

    def __init__(self) -> None:
        """The constructor, inits database connection"""

        self.connection = get_database_connection()

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
            recommendations = [Recommendation(result['title']) for result in results]
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

        if len(results) > 1 and isinstance(results, list):
            result = Recommendation(results[0]['title'])
        else:
            result = results

        return result

    def insert_recommendation(self, title):
        """Inserts a recommendation to database with title

        Args:
            title: A title of recommendation

        Returns:
            None if success, sqlite3.OperationalError object if db error
        """

        query = "INSERT INTO Recommendations (title) VALUES (?)"

        return self._write_db(query, [title])

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
