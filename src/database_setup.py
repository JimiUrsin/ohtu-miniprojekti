from database_connection import get_database_connection, get_test_database_connection

class DataBase:
    def create_tables(self, connection):
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE Recommendations
                        (id INTEGER PRIMARY KEY,
                        title TEXT,
                        type TEXT
                        );""")
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
