import unittest
from odd_lists import odd_element_positions

class TestOddLists(unittest.TestCase):
    def test_five_ints(self):
        integer_elements = [2, 3, 4, 5, 6]
        expected_odd_positioned_elements = [2, 4, 6]
        result = odd_element_positions(integer_elements)
        self.assertEqual(result, expected_odd_positioned_elements)

    def test_two_words(self):
        word_elements = ['abc', 'def']
        expected_odd_positioned_elements = ['abc']
        result = odd_element_positions(word_elements)
        self.assertEqual(result, expected_odd_positioned_elements)

    def test_one_number(self):
        single_element = [123]
        expected_odd_positioned_elements = [123]
        result = odd_element_positions(single_element)
        self.assertEqual(result, expected_odd_positioned_elements)

    def test_empty_list(self):
        no_elements = []
        expected_odd_positioned_elements = []
        result = odd_element_positions(no_elements)
        self.assertEqual(result, expected_odd_positioned_elements)

if __name__ == '__main__':
    unittest.main()