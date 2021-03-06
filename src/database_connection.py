import os
import sqlite3

dirname = os.path.dirname(__file__)

def get_database_connection():
    """Connects to the main database and returns the Connection object"""
    connection = sqlite3.connect(os.path.join(dirname, "..", "data", "database.sqlite"))
    connection.row_factory = sqlite3.Row
    return connection

def get_test_database_connection():
    """Connects to the test database and returns the Connection object"""
    connection = sqlite3.connect(os.path.join(dirname, "..", "data", "test_database.sqlite"))
    connection.row_factory = sqlite3.Row
    return connection
