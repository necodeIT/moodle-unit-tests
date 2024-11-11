import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from constants import *

def baseline_file_exists():
    """
    Check if the baseline dump file exists.
    """
    return os.path.exists(os.path.join(SQL_BASELINE_DUMP_DIR, "baseline.sql"))

def create_test_file(file_path: str, test_name: str):
    class_name = test_name.capitalize()
    content = f"""import sys
import os
import unittest

sys.path.insert(0, os.path.abspath('../../src'))

from driver import MoodleUnitTestBase

class {class_name}(MoodleUnitTestBase):
#   def test_{test_name}(self):
#       self.assertDBEquals("mdl_user", 2, "email", "user@example.com")
pass

if __name__ == "__main__":
    unittest.main()
"""

    try:
        with open(file_path, "w") as file:
            file.write(content)
        print(f"File created successfully at {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")