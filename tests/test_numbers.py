""" numbers.py tests """

import unittest
from src.numbers import double

class TestDouble(unittest.TestCase):
    """
    Double function tests
    """
    def test_double_positive(self):
        """it doubles positive numbers"""
        self.assertEqual(double(1), 2)
        self.assertEqual(double(2), 4)

    def test_double_zero(self):
        """it doubles zero correctly"""
        self.assertEqual(double(0), 0)

if __name__ == '__main__':
    unittest.main()
