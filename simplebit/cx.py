import sqlite3

from simplebit import settings


connection = None


def init(db_name=None):
    global connection
    if not db_name:
        db_name = settings.DB_NAME
    connection = sqlite3.connect(db_name, check_same_thread=False)
    connection.row_factory = sqlite3.Row
    connection.execute('PRAGMA foreign_keys = ON;')


def get():
    return connection
