import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from constants import *

def baseline_file_exists():
    """
    Check if the baseline dump file exists.
    """
    return os.path.exists(os.path.join(SQL_BASELINE_DUMP_DIR, "baseline.sql"))
