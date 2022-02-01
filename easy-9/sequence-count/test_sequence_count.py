'''A module for testing the sequence_count module'''
import unittest
from sequence_count import sequence

class TestSequenceCount(unittest.TestCase):
    '''A class for testing the sequence_count module'''
    def test_a_range_from_one_to_five(self):
        '''Test a sequence of five cardinal numbers from one up to
           five'''
        count = 5
        initial_int = 1
        seq = sequence(count, initial_int)
        self.assertEqual(seq, [1, 2, 3, 4, 5])

    def test_multiples_of_negative_seven(self):
        '''Four multiples of negative seven'''
        count = 4
        initial_int = -7
        seq = sequence(count, initial_int)
        self.assertEqual(seq, [-7, -14, -21, -28])

    def test_three_multiples_of_zero(self):
        '''Three multiples of zero'''
        count = 3
        initial_int = 0
        seq = sequence(count, initial_int)
        self.assertEqual(seq, [0, 0, 0])

    def test_count_of_zero(self):
        '''When the count is zero'''
        count = 0
        initial_int = 1_000_000
        seq = sequence(count, initial_int)
        self.assertEqual(seq, [])


if __name__ == '__main__':
    unittest.main()
