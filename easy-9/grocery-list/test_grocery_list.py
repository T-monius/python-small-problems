'''A module for testing the grocery_list module'''
import unittest
from grocery_list import buy_fruit

class TestGroceryList(unittest.TestCase):
    '''A class for testing the grocery_list module'''
    def test_buy_fruit(self):
        '''Test the buy_fruit function with three product types'''
        apples = ['apples', 3]
        oranges = ['orange', 1]
        bananas = ['bananas', 2]
        products = buy_fruit([apples, oranges, bananas])
        self.assertEqual(products, [
            "apples",
            "apples",
            "apples",
            "orange",
            "bananas",
            "bananas"]
        )


if __name__ == '__main__':
    unittest.main()
