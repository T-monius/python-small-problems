'''A module to test the grade_book module'''
import unittest
from grade_book import get_grade, average_of_three, letter_grade

class TestGradeBook(unittest.TestCase):
    '''A class for testing the grade_book module'''
    def test_average_of_three_numbers(self):
        '''Get the average of 95, 90, and 93'''
        num = 95
        num_one = 90
        num_two = 93
        integer_average = average_of_three(num, num_one, num_two)
        self.assertEqual(integer_average, 92)

    def test_letter_grade(self):
        '''Find the letter grade from a score'''
        score = 91
        letter = letter_grade(score)
        self.assertEqual(letter, 'A')

    def test_bad_letter_grade(self):
        '''Find the letter grade from a score'''
        score = -5
        letter = letter_grade(score)
        self.assertEqual(letter, 'Indeterminable')

    def test_an_A_grade(self):
        '''Average three scores in the 90s that are an A'''
        grade_one = 95
        grade_two = 90
        grade_three = 93
        letter = get_grade(grade_one, grade_two, grade_three)
        self.assertEqual(letter, 'A')

    def test_a_D_grade(self):
        '''Average three scores that are a D'''
        grade_one = 50
        grade_two = 50
        grade_three = 95
        letter = get_grade(grade_one, grade_two, grade_three)
        self.assertEqual(letter, 'D')


if __name__ == '__main__':
    unittest.main()
