'''A module to test the fibonacci_numbers module'''
import unittest
from fibonacci_numbers import recursive_fibonacci, procedural_fibonacci, fibonacci_last

class TestCalculatingFibonacciNumbers(unittest.TestCase):
    '''A class for testing the fibonacci_numbers module'''
    def test_the_first_number(self):
        '''Calculate the first number in the Fibonacci series'''
        nth = 1
        first = recursive_fibonacci(nth)
        self.assertEqual(first, 1)

    def test_the_second_number(self):
        '''Calculate the second number in the Fibonacci series'''
        nth = 2
        second = recursive_fibonacci(nth)
        self.assertEqual(second, 1)

    def test_the_third_number(self):
        '''Calculate the third number in the Fibonacci series'''
        nth = 3
        third = recursive_fibonacci(nth)
        self.assertEqual(third, 2)

    def test_the_fourth_number(self):
        '''Calculate the fourth number in the Fibonacci series'''
        nth = 4
        fourth = recursive_fibonacci(nth)
        self.assertEqual(fourth, 3)

    def test_the_fifth_number(self):
        '''Calculate the fifth number in the Fibonacci series'''
        nth = 5
        fifth = recursive_fibonacci(nth)
        self.assertEqual(fifth, 5)

    def test_the_twelfth_number(self):
        '''Calculate the twelfth number in the Fibonacci series'''
        nth = 12
        twelfth = recursive_fibonacci(nth)
        self.assertEqual(twelfth, 144)

    def test_the_twentieth_number(self):
        '''Calculate the twentieth number in the Fibonacci series'''
        nth = 20
        twentieth = recursive_fibonacci(nth)
        self.assertEqual(twentieth, 6765)

    def test_the_thirtieth_number(self):
        '''Calculate the thirtieth number in the Fibonacci series'''
        nth = 30
        thirtieth = recursive_fibonacci(nth)
        self.assertEqual(thirtieth, 832040)

    def test_the_first_number_procedurrally(self):
        '''Calculate the first number in procedurally'''
        nth = 1
        first = procedural_fibonacci(nth)
        self.assertEqual(first, 1)

    def test_the_second_number_procedurrally(self):
        '''Calculate the second number in procedurally'''
        nth = 2
        second = procedural_fibonacci(nth)
        self.assertEqual(second, 1)

    def test_the_third_number_procedurrally(self):
        '''Calculate the third number in procedurally'''
        nth = 3
        third = procedural_fibonacci(nth)
        self.assertEqual(third, 2)

    def test_the_fourth_number_procedurrally(self):
        '''Calculate the third number in procedurally'''
        nth = 4
        third = procedural_fibonacci(nth)
        self.assertEqual(third, 3)

    def test_the_thirtieth_number_procedurally(self):
        '''Calculate the thirtieth number procedurally'''
        nth = 30
        thirtieth = procedural_fibonacci(nth)
        self.assertEqual(thirtieth, 832040)

    def test_the_fourtieth_number(self):
        '''Calculate the fourtieth number in the Fibonacci series'''
        nth = 40
        fourtieth = procedural_fibonacci(nth)
        self.assertEqual(fourtieth, 102334155)

    def test_the_hundredth_number_procedurally(self):
        '''Calculate the hundredth number procedurally'''
        nth = 100
        hundredth = procedural_fibonacci(nth)
        self.assertEqual(hundredth, 354224848179261915075)

    @unittest.skip('Such a big number.')
    def test_the_hundredth_thousand_first_number_procedurally(self):
        '''Calculate the hundredth number procedurally'''
        nth = 100_001
        hundredth = procedural_fibonacci(nth)
        self.assertEqual(hundredth, '4202692702.....8285979669707537501')

class TestCalculatingLastDigitOfAFibonacciNumber(unittest.TestCase):
    '''A class for testing a number retrieved by calculations from the
       fibonacci_numbers module'''
    def test_last_digit_of_fifteenth(self):
        '''Calculate the last digit of the 15th number in the Fibobacci
           series'''
        nth = 15
        last_digit = fibonacci_last(nth)
        self.assertEqual(last_digit, 0)

    def test_last_digit_of_twentieth(self):
        '''Calculate the last digit of the 20th number in the Fibobacci
           series'''
        nth = 20
        last_digit = fibonacci_last(nth)
        self.assertEqual(last_digit, 5)

    def test_last_digit_of_hundredth(self):
        '''Calculate the last digit of the 100th number in the Fibobacci
           series'''
        nth = 100
        last_digit = fibonacci_last(nth)
        self.assertEqual(last_digit, 5)

    def test_last_digit_of_hundred_thousand_first(self):
        '''Calculate the last digit of the 100,001st number in the
           Fibobacci series'''
        nth = 100_001
        last_digit = fibonacci_last(nth)
        self.assertEqual(last_digit, 1)

    @unittest.skip('Too big of a number.')
    def test_last_digit_of_million_seventh(self):
        '''Calculate the last digit of the one million seventh number
           in the Fibobacci series'''
        nth = 100_000_007
        last_digit = fibonacci_last(nth)
        self.assertEqual(last_digit, 3)

    @unittest.skip('Too big of a number.')
    def test_last_digit_of_another_million_something_digit_number(self):
        '''Calculate the last digit of the million somethingth number
           in the Fibobacci series'''
        nth = 123456789
        last_digit = fibonacci_last(nth)
        self.assertEqual(last_digit, 4)


if __name__ == '__main__':
    unittest.main()
