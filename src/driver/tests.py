import unittest
import importlib
import os
import sys
from driver.database import DatabaseHandler
from constants import *
from utils import get_service_ip, create_test_file, run_tests_from_module

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
TEST_PATH = "tests"

class MoodleUnitTestBase(unittest.TestCase):
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
        actual_value = self.db.query(table, row_id, column)
        self.assertEqual(actual_value, expected_value)

    def assertDBNotEquals(self, table, row_id, column, expected_value):
        actual_value = self.db.query(table, row_id, column)
        self.assertNotEqual(actual_value, expected_value)


    @classmethod
    def tearDownClass(cls):
        cls.db.close()


def create_test_batch(name: str) -> None:
    """
    Creates and sets up folder structure for a new test batch.
    """

    batch_path = os.path.join(TEST_PATH, name)

    if os.path.exists(batch_path):
        print(f"Test batch \"{name}\" already exists")
        return
    
    os.makedirs(batch_path)
    create_test_file(os.path.join(batch_path, f"{name}.py"), name)

    print(f"Test batch \"{name}\" created successfully")

def run_test_batch(name: str) -> None:
    """
    Runs a test batch.
    """
    
    batch_path = os.path.join(TEST_PATH, name)

    if not os.path.exists(batch_path):
        print(f"Test batch \"{name}\" does not exist")
        return
    
    test_files = [f for f in os.listdir(batch_path) if f.endswith(".py")]

    if not test_files:
        print(f"No test files found in test batch \"{name}\"")
        return
    
    for test_file in test_files:
        test_path = os.path.join(batch_path, test_file)
        run_tests_from_module(test_path, test_file.split(".")[0].capitalize())
    
    print(f"Test batch \"{name}\" completed successfully")




    
