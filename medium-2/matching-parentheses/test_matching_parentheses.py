'''A module to test the matching_parentheses module'''
import unittest
from matching_parentheses import is_balanced

class TestMatchingParentheses(unittest.TestCase):
    '''A class to test the matching_parentheses module'''
    def test_a_balanced_single_set_of_parentheses(self):
        '''Test text where a single set of parentheses occurs in the
           proper order'''
        text = 'What (is) this?'
        result = is_balanced(text)
        self.assertTrue(result)

    def test_an_unbalanced_single_parenthesis(self):
        '''Test text where a single parenthesis occurs'''
        text = 'What is) this?'
        result = is_balanced(text)
        self.assertFalse(result)

    def test_another_unbalanced_single_parenthesis(self):
        '''Test text where a single parenthesis occurs'''
        text = 'What (is this?'
        result = is_balanced(text)
        self.assertFalse(result)

    def test_a_balanced_text_with_multiple_sets_of_parentheses(self):
        '''Test text where several sets of parentheses occur in the
           proper order'''
        text = '((What) (is this))?'
        result = is_balanced(text)
        self.assertTrue(result)

    def test_a_text_with_several_parenthesis_one_unbalanced(self):
        '''Test text where multiple parentheses occur with one
           unbalanced'''
        text = '((What)) (is this))?'
        result = is_balanced(text)
        self.assertFalse(result)

    def test_no_parentheses(self):
        '''Test text where no parentheses occur'''
        text = 'Hey!'
        result = is_balanced(text)
        self.assertTrue(result)

    def test_a_single_set_of_parentheses_unbalanced(self):
        '''Test text where a single set parentheses occur unbalanced'''
        text = ')Hey!('
        result = is_balanced(text)
        self.assertFalse(result)

    def test_multiple_parentheses_unbalanced(self):
        '''Test text with multiple parentheses unbalanced'''
        text = 'What ((is))) up('
        result = is_balanced(text)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
