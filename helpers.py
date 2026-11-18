# Helper Utilities Module
import os
import sys
from datetime import datetime


def get_project_root():
    """Return the absolute path to the project root."""
    return os.path.dirname(os.path.abspath(__file__))


def timestamp():
    """Return current ISO timestamp."""
    return datetime.now().isoformat()


def read_file(path):
    """Read and return file contents."""
    with open(path, "r") as f:
        return f.read()


def file_exists(path):
    """Check if a file exists."""
    return os.path.isfile(path)
