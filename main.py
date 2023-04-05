from snowflake_connector import SnowflakeConnector

snowflake_connector = SnowflakeConnector()

try:
    snowflake_connector.create_warehouse()
    snowflake_connector.create_database()
    snowflake_connector.use_database()
    snowflake_connector.create_schema()
    snowflake_connector.use_warehouse()
    snowflake_connector.use_schema()
    snowflake_connector.create_table()
    snowflake_connector.insert_rows()
    snowflake_connector.read_rows()
    print('complete.')
finally:
    snowflake_connector.close_connection()
