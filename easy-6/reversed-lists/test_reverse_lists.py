'''A module for testing a module which mutates lists'''
import unittest
from reverse_lists import reverse_in_place

class TestReverseLists(unittest.TestCase):
    '''Test lists being reversed by reverse_lists module'''
    def test_nums_from_one_to_four(self):
        '''Test a List containing elements incrementing from one to
           four becomes elements decrementing from four to one'''
        incrementing = [1, 2, 3, 4]
        decrementing = reverse_in_place(incrementing)
        self.assertEqual(decrementing, [4, 3, 2, 1])

    def test_abc(self):
        '''Test a List containing alpha elements'''
        alphas = ['a', 'b', 'e', 'd', 'c']
        backwards_alphas = reverse_in_place(alphas)
        self.assertEqual(backwards_alphas, ["c", "d", "e", "b", "a"] )

    def test_single_element_list(self):
        '''Test a List containing a single element'''
        single_element_list = ['abc']
        backwards_single_element_list = reverse_in_place(single_element_list)
        self.assertEqual(backwards_single_element_list, ['abc'] )

    def test_empty_list(self):
        '''Test an empty List'''
        empty_list = []
        backwards_empty_list = reverse_in_place(empty_list)
        self.assertEqual(backwards_empty_list, [] )


if __name__ == '__main__':
    unittest.main()
