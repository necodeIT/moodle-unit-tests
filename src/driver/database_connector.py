import sys
import os
import unittest
from sqlalchemy import create_engine, Column, Integer, String, MetaData, text
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import OperationalError

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from constants import *
from utils import get_service_ip

class DatabaseHandler:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def query(self, model, row_id, column):
        # Generalized query to get a column's value based on model and row_id
        row = self.session.query(model).filter_by(id=row_id).first()
        return getattr(row, column, None) if row else None
    
    def reset_to_baseline(self):
        # Code to reset the database to the baseline state
        # This could involve dropping and recreating tables, or reloading data from a file
        self.session.rollback()
        
        # Reset logic goes here, e.g., restoring from a baseline file
        pass

    def close(self):
        self.session.close()


class TestDatabaseConnection(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Define your database URL
        cls.db = DatabaseHandler(f"mysql+pymysql://{MARIADB_USER}@{get_service_ip(MARIADB_CONTAINER_NAME)}:{MARIADB_PORT}/{MARIADB_DATABASE}")
        cls.engine = cls.db.engine
        
    def test_connection(self):
        try:
            # Attempt to connect and execute a simple query
            with self.engine.connect() as connection:
                result = connection.execute(text("SELECT 1"))
                self.assertEqual(result.scalar(), 1)
        except OperationalError as e:
            self.fail(f"Database connection failed: {e}")

    @classmethod
    def tearDownClass(cls):
        cls.engine.dispose()  # Close the engine connection

# Run the test
if __name__ == "__main__":
    unittest.main()