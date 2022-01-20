'''A module to test the welcome_stranger module'''
import unittest
from welcome_stranger import greetings

class TestWelcomeStranger(unittest.TestCase):
    '''A class to test the welcome_stranger module'''
    def test_john_doe_with_title_and_ocupation(self):
        '''Greet a Master Plumber named John Q. Doe'''
        names = ['John', 'Q', 'Doe']
        work = { 'title': 'Master', 'occupation': 'Plumber' }
        greeting = greetings(names, work)
        self.assertEqual(
            greeting,
            'Hello, John Q Doe! Nice to have a Master Plumber around.'
        )

    def test_john_doe_without_title(self):
        '''Greet a Plumber named John Q. Doe'''
        names = ['John', 'Q', 'Doe']
        work = { 'occupation': 'Plumber' }
        greeting = greetings(names, work)
        self.assertEqual(
            greeting,
            'Hello, John Q Doe! Nice to have a Plumber around.'
        )


if __name__ == '__main__':
    unittest.main()
