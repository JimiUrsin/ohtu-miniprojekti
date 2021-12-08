from database_connection import get_database_connection, get_test_database_connection
import os

dirname = os.path.dirname(__file__)

class DataBase:
    def create_tables(self, connection):
        cursor = connection.cursor()
        with open(os.path.join(dirname, "..", "schema.sql")) as schema:
            cursor.executescript(schema.read())
        return True

    def drop_tables(self,connection):
        cursor = connection.cursor()
        cursor.execute("DROP TABLE IF EXISTS Recommendations;")
        return True

    def initialize_database(self):
        connection = get_database_connection()
        connection.isolation_level = None

        self.drop_tables(connection)
        self.create_tables(connection)

    def initialize_test_database(self):
        connection = get_test_database_connection()
        connection.isolation_level = None

        self.drop_tables(connection)
        self.create_tables(connection)

db = DataBase()
db.initialize_database()
db.initialize_test_database()
