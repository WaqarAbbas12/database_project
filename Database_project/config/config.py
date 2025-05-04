import mysql.connector
from dotenv import load_dotenv
import os


def load_envs():
    load_dotenv()
    db_name = os.getenv("DB_NAME")
    username = os.getenv("USERNAME")
    host = os.getenv("HOST")
    password = os.getenv("PASSWORD")
    return db_name, username, host, password


class ConnectDB:
    def __init__(self, db_name, username, host, password):
        self.dbname = db_name
        self.username = username
        self.host = host
        self.password = password

    def connect_db(self):
        connection = mysql.connector.connect(
            host=self.host,
            user=self.username,
            password=self.password,
            database=self.dbname,
        )

        cursor = connection.cursor()
        return connection, cursor


db_name, username, host, password = load_envs()
DB = ConnectDB(db_name, username, host, password)
conn, curr = DB.connect_db()
