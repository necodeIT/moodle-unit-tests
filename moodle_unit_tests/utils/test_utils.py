import unittest
import importlib.util
import os

def load_module_from_path(module_path):
    """
    Load a Python module dynamically from a file path.
    
    Args:
        module_path (str): Path to the module file (e.g., 'path/to/test_module.py').

    Returns:
        module: The loaded Python module.
    """
    if not os.path.exists(module_path):
        raise FileNotFoundError(f"The file '{module_path}' does not exist.")
    
    module_name = os.path.splitext(os.path.basename(module_path))[0]  # Extract the module name from the file name
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def create_test_file(file_path: str, test_name: str):
    class_name = test_name.capitalize()
    content = f"""import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from moodle_unit_tests import MoodleUnitTestBase

class {class_name}(MoodleUnitTestBase):
#   def test_connection(self):
#       self.assertIsNotNone(self.db.connection)

#   def test_query(self):
#       self.assertDBEquals("mdl_user", 2, "username", "admin")
    pass
"""

    try:
        with open(file_path, "w") as file:
            file.write(content)
        print(f"File created successfully at {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

class StreamWrapper:
    def __init__(self, stream):
        self.stream = stream

    def write(self, value):
        self.stream.write(value)

    def writeln(self, value=""):
        self.stream.write(value + "\n")

    def flush(self):
        self.stream.flush()

