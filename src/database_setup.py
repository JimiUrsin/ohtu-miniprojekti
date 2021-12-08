import os
from database_connection import get_database_connection, get_test_database_connection

dirname = os.path.dirname(__file__)

class DataBase:
    def create_tables(self, connection):
        """Executes schema.sql using the given connection and returns True on success"""
        cursor = connection.cursor()
        with open(os.path.join(dirname, "..", "schema.sql"), encoding="utf-8") as schema:
            cursor.executescript(schema.read())
        return True

    def drop_tables(self,connection):
        """Drops the Recommendations table using the given connection and returns True on success"""
        cursor = connection.cursor()
        cursor.execute("DROP TABLE IF EXISTS Recommendations;")
        return True

    def initialize_database(self):
        """Drops and recreates the Recommendations table in the main database"""
        connection = get_database_connection()
        connection.isolation_level = None

        self.drop_tables(connection)
        self.create_tables(connection)

    def initialize_test_database(self):
        """Drops and recreates the Recommendations table in the test database"""
        connection = get_test_database_connection()
        connection.isolation_level = None

        self.drop_tables(connection)
        self.create_tables(connection)

db = DataBase()
db.initialize_database()
db.initialize_test_database()
