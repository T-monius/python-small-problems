'''A module for testing the diamonds module'''
import unittest
from diamonds import diamond

class TestDiamonds(unittest.TestCase):
    '''A class for testing the diamond module that creates strings
       which print to diamonds formed by starts/asteriscs'''
    def test_a_single_star(self):
        '''Print a diamond star'''
        num = 1
        dmd = diamond(num)
        self.assertEqual(dmd, '*\n')

    def test_a_star_of_three_lines(self):
        '''Print a diamond of three lines'''
        num = 3
        dmd = diamond(num)
        self.assertEqual(dmd, ' *\n***\n *\n')

    def test_a_star_of_five_lines(self):
        '''Print a diamond of five lines'''
        num = 5
        dmd = diamond(num)
        self.assertEqual(dmd, '  *\n ***\n*****\n ***\n  *\n')


if __name__ == '__main__':
    unittest.main()
