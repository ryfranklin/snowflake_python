import unittest
from snowflake_connector import SnowflakeConnector


class TestSnowflakeConnector(unittest.TestCase):
    def setUp(self):
        self.snowflake_connector = SnowflakeConnector()

    def tearDown(self):
        self.snowflake_connector.close_connection()

    def test_read_rows(self):
        sql = ("USE DATABASE project_database")
        self.snowflake_connector.cs.execute(sql)
        self.snowflake_connector.create_table()
        self.snowflake_connector.insert_rows()
        rows = self.snowflake_connector.read_rows()
        print(type(rows))
        self.assertEqual(len(rows), 3)


if __name__ == '__main__':
    unittest.main()
