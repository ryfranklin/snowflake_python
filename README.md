# Snowflake Connect with Python

## Create a virtual environment
```shell
$ python -m venv venv
```

----------
## Install the Python connector
```shell
$ pip install snowflake-connector-python
```

----------
## Snowflake Connector
This Python module provides a "SnowflakeConnector" class for connecting to and working with a Snowflake database.  The "SnowflakeConnector" class uses the 'snowflake-connector-python' library to establish a connection to Snowflake.

### Usage
To use the 'SnowflakeConnector' class, you first need to import it.
```python
from snowflake_connector import SnowflakeConnector
```

Then, create an instance of the 'SnowflakeConnector' class:
```python
snowflake_connector = SnowflakeConnector()
```

You can then use the 'SnowflakeConnector' instance to create a warehouse, database, schema, table, and insert rows into the table, like so:
```python
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

```