'''A module for testing a module for working with lists'''
import unittest
from reverse_lists import reverse_in_place, backwards

class TestReverseLists(unittest.TestCase):
    '''Test lists being reversed by reverse_lists module'''
    def test_nums_from_one_to_four_in_place(self):
        '''Test a List containing elements incrementing from one to
           four becomes elements decrementing from four to one, in
           place'''
        incrementing = [1, 2, 3, 4]
        decrementing = reverse_in_place(incrementing)
        self.assertEqual(decrementing, [4, 3, 2, 1])

    def test_abc_in_place(self):
        '''Test a List containing alpha elements, in place'''
        alphas = ['a', 'b', 'e', 'd', 'c']
        backwards_alphas = reverse_in_place(alphas)
        self.assertEqual(backwards_alphas, ["c", "d", "e", "b", "a"] )

    def test_single_element_list_in_place(self):
        '''Test a List containing a single element, in place'''
        single_element_list = ['abc']
        backwards_single_element_list = reverse_in_place(single_element_list)
        self.assertEqual(backwards_single_element_list, ['abc'] )

    def test_empty_list_in_place(self):
        '''Test an empty List, in place'''
        empty_list = []
        backwards_empty_list = reverse_in_place(empty_list)
        self.assertEqual(backwards_empty_list, [] )

    def test_nums_from_one_to_four_backwards(self):
        '''Test a List containing elements incrementing from one to
           four returning a new list decrementing from four to one'''
        incrementing = [1, 2, 3, 4]
        decrementing = backwards(incrementing)
        self.assertEqual(decrementing, [4, 3, 2, 1])

    def test_abc_backwards(self):
        '''Test a List containing alpha elements being a new
           reversed list'''
        alphas = ['a', 'b', 'e', 'd', 'c']
        backwards_alphas = backwards(alphas)
        self.assertEqual(backwards_alphas, ["c", "d", "e", "b", "a"] )

    def test_single_element_list_backwards(self):
        '''Test a List containing a single element as a new list'''
        single_element_list = ['abc']
        backwards_single_element_list = backwards(single_element_list)
        self.assertEqual(backwards_single_element_list, ['abc'] )

    def test_empty_list_backwards(self):
        '''Test an empty List to be a new empty list'''
        empty_list = []
        backwards_empty_list = backwards(empty_list)
        self.assertEqual(backwards_empty_list, [] )


if __name__ == '__main__':
    unittest.main()
