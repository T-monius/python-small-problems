'''A module for testing show_multiplicative_average module'''
import unittest
from multiplicative_average import show_multiplicative_average

class TestMultiplicativeAverage(unittest.TestCase):
    '''A class for testing avarages calculated by
       show_multiplicative_average'''
    def test_two_ints(self):
        '''Test integeres three and five in a list'''
        ints = [3, 5]
        average = show_multiplicative_average(ints)
        self.assertEqual(average, 7.500)

    def test_single_element(self):
        '''Test integeres a single element list'''
        ints = [6]
        average = show_multiplicative_average(ints)
        self.assertEqual(average, 6.000)

    def test_a_long_list(self):
        '''Test a long list of elements'''
        ints = [2, 5, 7, 11, 13, 17]
        average = show_multiplicative_average(ints)
        self.assertEqual(average, 28361.667)


if __name__ == '__main__':
    unittest.main()
