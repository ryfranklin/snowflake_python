import snowflake.connector
import os
from dotenv import load_dotenv

load_dotenv()


class SnowflakeConnector:
    def __init__(self):
        self.conn = snowflake.connector.connect(
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            account=os.getenv("ACCOUNT")
        )
        self.cs = self.conn.cursor()

    def create_warehouse(self):
        print('creating warehouse...')
        sql = "CREATE WAREHOUSE IF NOT EXISTS project_warehouse"
        self.cs.execute(sql)

    def create_database(self):
        print('creating database...')
        sql = "CREATE DATABASE IF NOT EXISTS project_database"
        self.cs.execute(sql)

    def use_database(self):
        print('using database...')
        sql = "USE DATABASE project_database"
        self.cs.execute(sql)

    def create_schema(self):
        print('creating schema...')
        sql = "CREATE SCHEMA IF NOT EXISTS project_schema"
        self.cs.execute(sql)

    def use_warehouse(self):
        sql = "USE WAREHOUSE project_warehouse"
        self.cs.execute(sql)

    def use_schema(self):
        sql = "USE SCHEMA project_schema"
        self.cs.execute(sql)

    def create_table(self):
        print("create a table...")
        sql = ("CREATE OR REPLACE TABLE project_comments"
               " (ID integer, comments string)")
        self.cs.execute(sql)

    def insert_rows(self):
        print('insert a few rows...')
        sql = ("INSERT INTO project_comments (ID, comments)"
               "VALUES (1, 'my comments about the project!')"
               )
        self.cs.execute(sql)
        sql = ("INSERT INTO project_comments (ID, comments)"
               "VALUES (2, 'some more comments about the project!')"
               )
        self.cs.execute(sql)
        sql = ("INSERT INTO project_comments (ID, comments)"
               "VALUES (3, 'even more comments about the project!')"
               )
        self.cs.execute(sql)

    def read_rows(self):
        print('read some rows...')
        sql = "SELECT * FROM project_comments"
        self.cs.execute(sql)
        rows = [row for row in self.cs.fetchall()]
        return rows

    def close_connection(self):
        self.cs.close()
        self.conn.close()
