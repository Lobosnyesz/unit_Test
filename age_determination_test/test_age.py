import unittest
from age import categorize_by_age

class TestAgeCategorization(unittest.TestCase):

    def test_child_age(self):
        self.assertEqual(categorize_by_age(5), "Child")
        self.assertEqual(categorize_by_age(0), "Child")
        self.assertEqual(categorize_by_age(9), "Child")

    def test_teenager_age(self):
        self.assertEqual(categorize_by_age(10), "Teenager")
        self.assertEqual(categorize_by_age(15), "Teenager")
        self.assertEqual(categorize_by_age(18), "Teenager")

    def test_adult_age(self):
        self.assertEqual(categorize_by_age(19), "Adult")
        self.assertEqual(categorize_by_age(30), "Adult")
        self.assertEqual(categorize_by_age(64), "Adult")

    def test_golden_age(self):
        self.assertEqual(categorize_by_age(65), "Golden Age")
        self.assertEqual(categorize_by_age(80), "Golden Age")
        self.assertEqual(categorize_by_age(120), "Golden Age")

    def test_invalid_age(self):
        self.assertEqual(categorize_by_age(-1), "Invalid age: -1")
        self.assertEqual(categorize_by_age(121), "Invalid age: 121")
        self.assertEqual(categorize_by_age(150), "Invalid age: 150")

import pytest
from age import categorize_by_age

def test_categorize_by_age():
    assert categorize_by_age(5) == "Child"
    assert categorize_by_age(0) == "Child"
    assert categorize_by_age(9) == "Child"
    
    assert categorize_by_age(10) == "Teenager"
    assert categorize_by_age(15) == "Teenager"
    assert categorize_by_age(18) == "Teenager"
    
    assert categorize_by_age(19) == "Adult"
    assert categorize_by_age(30) == "Adult"
    assert categorize_by_age(64) == "Adult"
    
    assert categorize_by_age(65) == "Golden Age"
    assert categorize_by_age(80) == "Golden Age"
    assert categorize_by_age(120) == "Golden Age"
    
    assert categorize_by_age(-1) == "Invalid age: -1"
    assert categorize_by_age(121) == "Invalid age: 121"
    assert categorize_by_age(150) == "Invalid age: 150"

#python -m pytest .\test_age.py -v
