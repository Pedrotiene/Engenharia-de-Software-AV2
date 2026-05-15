import sqlite3


class Database:

    _instance = None

    def __new__(cls):

        if cls._instance is None:

            cls._instance = super(Database, cls).__new__(cls)

            cls._instance.conn = sqlite3.connect(
                "database/banco.db"
            )

            cls._instance.cursor = cls._instance.conn.cursor()

        return cls._instance

    def get_connection(self):
        return self.conn

    def get_cursor(self):
        return self.cursor