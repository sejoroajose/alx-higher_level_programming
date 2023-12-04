import unittest
from 0-add_integer import add_integer

class TestAddInteger(unittest.TestCase):
    def test_add_int(self):
        # Test addition of two integers
        self.assertAlmostEqual(add_integer(2, 6), 8)
        self.assertAlmostEqual(add_integer(-10, -5), -15)
        self.assertAlmostEqual(add_integer(22, -2), 20)
