import os
import sys
import unittest
import traceback

from moodle_unit_tests.testing.unttest_styling import MarkdownTestResult
from moodle_unit_tests.utils import load_module_from_path
from moodle_unit_tests.utils import create_test_file, StreamWrapper


sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
TEST_PATH = "tests"


class MarkdownTestRunner(unittest.TextTestRunner):
    def __init__(self, *args, batch_path=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.batch_path = batch_path or "./results"

    def _makeResult(self):
        return MarkdownTestResult(self.stream, self.descriptions, self.verbosity)

    def run(self, test):
        if not os.path.exists(self.batch_path):
            os.makedirs(self.batch_path)

        with open(os.path.join(self.batch_path, "test_results.md"), "w") as f:
            stream_wrapper = StreamWrapper(f)  # Wrap the file stream
            self.stream = stream_wrapper
            result = super().run(test)

        markdown = "# Test Results\n\n" + "\n".join(result.results)
        with open(os.path.join(self.batch_path, "test_results.md"), "w") as f:
            f.write(markdown)

        return result
    
def run_tests_from_module(module_path, batch_path, class_name):
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
        runner = MarkdownTestRunner(verbosity=2, batch_path=batch_path)
        runner.run(suite)
    
    except (FileNotFoundError, AttributeError) as e:
        print(f"Error: {e}")
        traceback.print_exc()
    except TypeError as e:
        print(f"TypeError: {e}")


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
        module_path = os.path.join(batch_path, test_file)
        run_tests_from_module(module_path, batch_path, test_file.split(".")[0].capitalize())
    
    print(f"Test batch \"{name}\" completed")
