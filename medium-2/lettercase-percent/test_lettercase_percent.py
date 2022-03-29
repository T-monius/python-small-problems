'''A class to test the lettercase_percent module'''
import unittest
from lettercase_percent import letter_percentages, calculate_percentage

class TestLettercasePercent(unittest.TestCase):
    '''A class to test the lettercase_percent module'''
    def test_calculating_a_percentage(self):
        '''calculate what percentage one number is of another'''
        num = 10
        other_num = 4
        percentage = calculate_percentage(num, other_num)
        self.assertEqual(percentage, 40.0)

    def test_a_string_with_all_three_case_types(self):
        '''Test a string with all three case types'''
        text = 'abCdef 123'
        percentages = letter_percentages(text)
        self.assertEqual(percentages, {
            'lowercase': 50.0,
            'uppercase': 10.0,
            'neither': 40.0,
        })

    def test_another_string_with_all_three_case_types(self):
        '''Test another string with all three case types'''
        text = 'AbCd +Ef'
        percentages = letter_percentages(text)
        self.assertEqual(percentages, {
            'lowercase': 37.5,
            'uppercase': 37.5,
            'neither': 25.0,
        })

    def test_an_all_numeric_string(self):
        '''Test an all numeric string'''
        text = '123'
        percentages = letter_percentages(text)
        self.assertEqual(percentages, {
            'lowercase': 0.0,
            'uppercase': 0.0,
            'neither': 100.0
        })


if __name__ == '__main__':
    unittest.main()
