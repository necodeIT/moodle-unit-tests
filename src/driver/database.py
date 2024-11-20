import sys
import os
import mysql.connector
from driver.baseline import sql_restore_baseline

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from constants import *

class DatabaseHandler:
    def __init__(self, db_config):
        self.connection = mysql.connector.connect(**db_config)
        self.cursor = self.connection.cursor(dictionary=True)
    
    def query(self, table, row_id, column):
        query = f"SELECT {column} FROM {table} WHERE id = %s"
        self.cursor.execute(query, (row_id,))
        result = self.cursor.fetchone()
        return result[column] if result else None
    
    def reset_to_baseline(self):
        sql_restore_baseline()
    
    def close(self):
        self.cursor.close()
        self.connection.close()