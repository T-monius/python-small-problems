import unittest
from multiply_two_numbers import multiply

class TestMultiplyTwoNumbers(unittest.TestCase):
    def test_three_and_five(self):
        first_num = 3
        second_num = 5
        product = 15
        result = multiply(first_num, second_num)
        self.assertEqual(result, product)

if __name__ == '__main__':
    unittest.main()
