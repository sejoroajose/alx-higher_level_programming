import unittest
add_integer = __import__('0-add_integer').add_integer

class TestAddInteger(unittest.TestCase):
    def test_add_int(self):
        # Test addition of two integers
        self.assertEqual(add_integer(2, 6), 8)
        self.assertEqual(add_integer(-10, -5), -15)
        self.assertEqual(add_integer(22, -2), 20)

    def test_add_integer_invalid(self):
        with self.assertRaises(TypeError):
            add_integer('a', 3)
        with self.assertRaises(TypeError):
            add_integer(2, 'b')
        with self.assertRaises(TypeError):
            add_integer([], 3)

if __name__ == '__main__':
    unittest.main()
