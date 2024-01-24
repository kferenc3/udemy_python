#creating a custom context manager for ourselves

import sqlite3

class DatabaseConnection:
    def __init__(self, host):
        self.connection = None
        self.host = host

    def __enter__(self):
        self.connection = sqlite3.connect(self.host)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb): #exception type, value, traceback
        if exc_type or exc_val or exc_tb:
            self.connection.close() #in case of exception close the connection without commit
        self.connection.commit()
        self.connection.close()