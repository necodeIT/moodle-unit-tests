import unittest

from moodle_unit_tests.constants import *
from moodle_unit_tests.driver.database import DatabaseHandler
from moodle_unit_tests.utils import get_service_ip

class MoodleUnitTestBase(unittest.TestCase):
    """
    Base class for Moodle unit tests.
    
    Provides utility methods for interacting with the database."""
    @classmethod
    def setUpClass(cls):
        db_config = {
            'user': MARIADB_USER,
            'host': get_service_ip(MARIADB_CONTAINER_NAME),
            'database': MARIADB_DATABASE,
            'collation': 'utf8mb4_general_ci',
        }
        cls.db = DatabaseHandler(db_config)

    def setUp(self):
        self.db.reset_to_baseline()

    
    def assertDBEquals(self, table, row_id, column, expected_value):
        """
        Asserts that the value of a column in a row of a table is equal to the expected value.
        
        :param table: The name of the table
        :param row_id: The ID of the row
        :param column: The name of the column"""
        actual_value = self.db.query(table, row_id, column)
        self.assertEqual(actual_value, expected_value)


    def assertDBNotEquals(self, table, row_id, column, expected_value):
        """
        Asserts that the value of a column in a row of a table is not equal to the expected value.
        
        :param table: The name of the table
        :param row_id: The ID of the row
        :param column: The name of the column"""
        actual_value = self.db.query(table, row_id, column)
        self.assertNotEqual(actual_value, expected_value)


    @classmethod
    def tearDownClass(cls):
        cls.db.close()