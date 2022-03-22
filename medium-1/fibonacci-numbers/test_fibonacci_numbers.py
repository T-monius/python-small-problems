'''A module to test the fibonacci_numbers module'''
import unittest
from fibonacci_numbers import recursive_fibonacci

class TestFibonacciNumbers(unittest.TestCase):
    '''A class for testing the fibonacci_numbers module'''
    def test_the_first_number(self):
        '''Calculate the first number in the Fibonacci series'''
        num = 1
        first = recursive_fibonacci(num)
        self.assertEqual(first, 1)

    def test_the_second_number(self):
        '''Calculate the second number in the Fibonacci series'''
        num = 2
        second = recursive_fibonacci(num)
        self.assertEqual(second, 1)

    def test_the_third_number(self):
        '''Calculate the third number in the Fibonacci series'''
        num = 3
        third = recursive_fibonacci(num)
        self.assertEqual(third, 2)

    def test_the_fourth_number(self):
        '''Calculate the fourth number in the Fibonacci series'''
        num = 4
        fourth = recursive_fibonacci(num)
        self.assertEqual(fourth, 3)

    def test_the_fifth_number(self):
        '''Calculate the fifth number in the Fibonacci series'''
        num = 5
        fifth = recursive_fibonacci(num)
        self.assertEqual(fifth, 5)

    def test_the_twelfth_number(self):
        '''Calculate the twelfth number in the Fibonacci series'''
        num = 12
        twelfth = recursive_fibonacci(num)
        self.assertEqual(twelfth, 144)

    def test_the_twentieth_number(self):
        '''Calculate the twentieth number in the Fibonacci series'''
        num = 20
        twentieth = recursive_fibonacci(num)
        self.assertEqual(twentieth, 6765)


if __name__ == '__main__':
    unittest.main()
