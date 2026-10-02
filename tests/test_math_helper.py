"""
Unit Tests for Math Helper - Created by Coder Agent
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.math_helper import add, subtract, multiply, safe_divide

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(10, 4) == 6

def test_multiply():
    assert multiply(3, 7) == 21

def test_safe_divide():
    assert safe_divide(10, 2) == 5.0
    try:
        safe_divide(5, 0)
        assert False, "Expected ValueError on zero division"
    except ValueError:
        pass

if __name__ == "__main__":
    test_add()
    test_subtract()
    test_multiply()
    test_safe_divide()
    print("All unit tests passed successfully!")
