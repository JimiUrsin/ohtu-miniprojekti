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

        query = (
            "SELECT Recommendations.id, Recommendations.title, Recommendations.type, "
            "Authors.author, Recommendations.url, Recommendations.isbn, Recommendations.description, "
            "Recommendations.comment "
            "FROM Recommendations, AuthorRecommendations, Authors "
            "WHERE Recommendations.id = AuthorRecommendations.recom_id "
            "AND Authors.id = AuthorRecommendations.author_id"
        )
        results = self._read_db(query)

        if isinstance(results, list):
            recommendations = []
            for result in results:
                recommendation = Recommendation(
                    result['title'],
                    result['type'],
                    result['id'],
                    result['author'],
                    result['url'],
                    result['isbn'],
                    result['description'],
                    result['comment']
                )
                recommendations.append(recommendation)
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

        query = (
            "SELECT Recommendations.id, Recommendations.title, Recommendations.type, "
            "Authors.author, Recommendations.url, Recommendations.isbn, Recommendations.description, "
            "Recommendations.comment "
            "FROM Recommendations, AuthorRecommendations, Authors "
            "WHERE title = ? "
            "AND Recommendations.id = AuthorRecommendations.recom_id "
            "AND Authors.id = AuthorRecommendations.author_id"
        )
        results = self._read_db(query, [title])

        if isinstance(results, list) and len(results) > 0:
            recommendation = Recommendation(
                    results[0]['title'],
                    results[0]['type'],
                    results[0]['id'],
                    results[0]['author'],
                    results[0]['url'],
                    results[0]['isbn'],
                    results[0]['description'],
                    results[0]['comment']
                )
            return recommendation

        return results

    """def _find_recommendation_author(self, recommendation_id):
        Finds the author of a given recommendation
      
        Args:
            recommendation_id: id of recommendation

        Returns:
            Name of author
        
        results = self._read_db("SELECT author_id FROM AuthorRecommendations WHERE recom_id = ?", [recommendation_id])
        author_id = results[0]["author_id"]

        results = self._read_db("SELECT author FROM Authors WHERE id = ?", [author_id])
        name_of_author = results[0]["author"]
        return name_of_author"""
    # TÄTÄ METODIA EI VAIKUTA KÄYTETTÄVÄN AINAKAAN VIELÄ MIHINKÄÄN?

    def insert_recommendation(self, recom_details):
        """Inserts a recommendation to database.
            This method checks that a Recommendation has the required values and
            raises an Exception if the fields are not found. The requirements are
            as follows (required fields marked with *):
            - Book: Title*, Author*, ISBN, Description, Comment
            - Video: Title*, Author*, URL*, Description, Comment
            - Blog: Title*, Author*, URL*, Description, Comment
            - Podcast: Title*, Author*, URL*, Description, Comment

        Args:
            author: Name of author
            recom_details: A dictionary containing the details of given recommendation. Example:
                {
                    "title": "My Day",
                    "author": "Sita Salminen",
                    "type": "video",
                    "url": "https://youtube.com",
                    "description": "Video Sitan päivästä",
                    "comment": "Ihan hyvä video"
                }

        Returns:
            Database id if success, sqlite3.OperationalError object if db error
        """

        ###############################################################
        check = self._check_insertion_fields(recom_details)

        if check is False:
            return False
        ## TÄMÄ CHECK TARPEETON KUNHAN TARKISTUS ON SIIRRETTY SERVICEEN

        author = recom_details["author"]
        del recom_details["author"]

        query_recommendation_insertion = self._create_query_for_inserting_recommendation(recom_details.keys())
        recommendation_id = self._write_db(query_recommendation_insertion, list(recom_details.values()))

        if not isinstance(recommendation_id, int):
            # Database Error, return OperationalError object
            return recommendation_id

        author_id = self._create_author_if_needed(author)

        if not isinstance(author_id, int):
            # Database Error, return OperationalError object
            return author_id

        result = self._write_db(
            "INSERT INTO AuthorRecommendations (recom_id, author_id) VALUES (?, ?)",
            [recommendation_id, author_id]
        )

        return result

    def _check_insertion_fields(self, recom_details):

         ## TÄMÄ CHECK SIIRRETÄÄN SERVICE-LUOKAN HOMMIKSI, EI EXCEPTIONEJA SILLÄ KÄYTTÄJÄLLE EI SAA NÄKYÄ MITÄÄN TRACEBACKEJA

        #Handles checking that necessary fields for creating a Recommendation are provided
        if "title" not in recom_details or "type" not in recom_details or "author" not in recom_details:
            return False
            #raise Exception("Missing required information for creating Recommendartion")

        if recom_details["type"] != "book":
            # Blog, video or podcast must have URL
            if "url" not in recom_details:
                return False
                #raise Exception("Missing required information for creating Recommendartion")"""

    def _create_author_if_needed(self, author):
        """Check if author is already present in the database. If author not present,
            creates an entry of it in Authors table.

        Args:
            author: Name of the author

        Returns:
            Id of author
        """

        author_query = "SELECT id FROM Authors WHERE author = ?"
        results = self._read_db(author_query, [author])

        if isinstance(results, list) and len(results) > 0:
            author_id = results[0][0]
            return author_id

        author_id = self._write_db("INSERT INTO Authors (author) VALUES (?)", [author])

        return author_id

    def delete_recommendation_by_id(self, db_id):
        """Delete recommendation by its id. Also removes connection to
            its Author (deleted by SQL trigger DeleteAuthorConnectionWithRecommendation).
            If last recommendation associated with an author is deleted,
            then the author is deleted aswell (SQL Trigger DeleteAuthorWithLastRecommendation)
        Args:
            db_id: An id of the recommendation

        Return:
            None if success, sqlite3.OperationalError object if db error
        """

        query_delete_recommendation = "DELETE FROM Recommendations WHERE id = ?"

        return self._write_db(query_delete_recommendation, [db_id])

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

    def _create_query_for_inserting_recommendation(self, column_names):
        """A method that generates a SQL query string for inserting values to DB table

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
            If success:     A database id of the row inserted/edited/deleted
            If db error:    sqlite3.OperationalError object
        """

        try:
            with self.connection:
                cursor = self.connection.cursor()

                cursor.execute(query, values)
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
