import pytest
from calculator import sum, subtract, multiply, divide

def test_sum():
    assert sum(3, 5) == 8
    assert sum(-1, 1) == 0
    assert sum(-1, -1) == -2
    assert sum(0, 0) == 0
def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(-1, 1) == -2
    assert subtract(-1, -1) == 0
    assert subtract(0, 0) == 0
def test_multiply():
    assert multiply(3, 5) == 15
    assert multiply(-1, 1) == -1
    assert multiply(-1, -1) == 1
    assert multiply(0, 100) == 0
def test_divide():
    assert divide(10, 2) == 5
    assert divide(-4, 2) == -2
    assert divide(-4, -2) == 2
    assert divide(0, 1) == 0
    assert divide(5, 0) == "Error! Division by zero."
    
#python -m pytest .\test_calculator.py -v    