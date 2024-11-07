import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
TEST_PATH = "tests"

def create_test_batch(name: str) -> None:
    """
    Creates and sets up folder structure for a new test batch.
    """

    batch_path = os.path.join(TEST_PATH, name)

    if os.path.exists(batch_path):
        print(f"Test batch {name} already exists")
        return
    
    os.makedirs(batch_path)
    os.makedirs(os.path.join(batch_path, "expected"))
    os.makedirs(os.path.join(batch_path, "actual"))

    print(f"Test batch \"{name}\" created successfully")
    