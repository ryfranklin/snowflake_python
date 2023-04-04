import snowflake.connector
import os
from dotenv import load_dotenv

load_dotenv()

conn = snowflake.connector.connect(
    user=os.getenv("USER"),
    password=os.getenv("PASSWORD"),
    account=os.getenv("ACCOUNT")
)
cs = conn.cursor()
try:
    cs.execute("Select current_version()")
    row = cs.fetchone()
    print(row[0])
    print('creating warehouse...')
    sql = "CREATE WAREHOUSE IF NOT EXISTS project_warehouse"
    cs.execute(sql)
    print('creating database...')
    sql = "CREATE DATABASE IF NOT EXISTS project_database"
    cs.execute(sql)
    print('using database...')
    sql = "USE DATABASE project_database"
    cs.execute(sql)
    print('creating schema...')
    sql = "CREATE SCHEMA IF NOT EXISTS project_schema"
    cs.execute(sql)
    print('creation complete!')
    sql = "USE WAREHOUSE project_warehouse"
    cs.execute(sql)
    sql = "USE DATABASE project_database"
    cs.execute(sql)
    sql = "USE SCHEMA project_schema"
    cs.execute(sql)
    print("create a table...")
    sql = ("CREATE OR REPLACE TABLE project_comments"
           " (ID integer, comments string)")
    cs.execute(sql)
    print('insert a few rows...')
    sql = ("INSERT INTO project_comments (ID, comments)"
           "VALUES (1, 'my comments about the project!')"
           )
    cs.execute(sql)
    sql = ("INSERT INTO project_comments (ID, comments)"
           "VALUES (2, 'some more comments about the project!')"
           )
    cs.execute(sql)
    sql = ("INSERT INTO project_comments (ID, comments)"
           "VALUES (3, 'even more comments about the project!')"
           )
    cs.execute(sql)
    print('read some rows...')
    sql = "SELECT * FROM project_comments"
    cs.execute(sql)
    for row in cs.fetchall():
        print(row)
    print('complete.')
finally:
    cs.close()
conn.close()
