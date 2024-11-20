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

def run_tests_from_module(module_path, class_name):
    """
    Load a test module from a file path and run the tests in a specified class.
    
    Args:
        module_path (str): Path to the test module.
        class_name (str): Name of the test class to run.
    """
    try:
        # Load the module from the file path
        test_module = load_module_from_path(module_path)
        
        # Get the test class dynamically
        test_class = getattr(test_module, class_name)
        
        # Verify the class is a subclass of unittest.TestCase
        if not issubclass(test_class, unittest.TestCase):
            raise TypeError(f"{class_name} is not a unittest.TestCase subclass")
        
        # Create and run the test suite
        suite = unittest.TestSuite()
        suite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_class))
        runner = unittest.TextTestRunner()
        runner.run(suite)
    
    except (FileNotFoundError, AttributeError) as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"TypeError: {e}")

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

# Example usage:
if __name__ == "__main__":
    # Replace these with the actual path and class name
    module_path = "/home/nepo/Github/moodle-unit-tests/test/main.py"
    class_name = "TestDatabaseHandler"
    run_tests_from_module(module_path, class_name)
