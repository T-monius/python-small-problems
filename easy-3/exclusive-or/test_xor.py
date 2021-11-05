import unittest
from xor import is_xor

def is_even(num):
    return num % 2 == 0

def is_odd(num):
    return num % 2 != 0

class TestXOR(unittest.TestCase):
    def test_false_true(self):
        to_be_false = is_even(5)
        to_be_true = is_even(4)
        boolean_result = is_xor(to_be_false, to_be_true)
        self.assertTrue(boolean_result)

    def test_true_false(self):
        to_be_true = is_odd(5)
        to_be_false = is_odd(4)
        boolean_result = is_xor(to_be_true, to_be_false)
        self.assertTrue(boolean_result)

    def test_true_true(self):
        to_be_true = is_odd(5)
        to_be_true_also = is_even(4)
        boolean_result = is_xor(to_be_true, to_be_true_also)
        self.assertFalse(boolean_result)

    def test_false_false(self):
        to_be_false = is_even(5)
        to_be_false_also = is_odd(4)
        boolean_result = is_xor(to_be_false, to_be_false_also)
        self.assertFalse(boolean_result)

if __name__ == '__main__':
    unittest.main()