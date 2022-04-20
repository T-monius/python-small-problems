'''A module for testing the seeing_stars module'''
import unittest
from seeing_stars import star_power_grid

SEVEN_ROW_GRID = '*  *  *\n' \
                 ' * * *\n' \
                 '  ***\n' \
                 '*******\n' \
                 '  ***\n' \
                 ' * * *\n' \
                 '*  *  *\n'


NINE_ROW_GRID = '*   *   *\n' \
                 ' *  *  *\n' \
                 '  * * *\n' \
                 '   ***\n' \
                 '*********\n' \
                 '   ***\n' \
                 '  * * *\n' \
                 ' *  *  *\n' \
                 '*   *   *\n'

class TestSeeingStars(unittest.TestCase):
    '''A class for testing the seeing_stars module'''
    def test_seven_rows(self):
        '''Test creating a 7x7 grid'''
        rows = 7
        grid = star_power_grid(rows)
        self.assertEqual(grid, SEVEN_ROW_GRID)

    def test_nine_rows(self):
        '''Test creating a 9x9 grid'''
        rows = 9
        grid = star_power_grid(rows)
        self.assertEqual(grid, NINE_ROW_GRID)


if __name__ == '__main__':
    unittest.main()
