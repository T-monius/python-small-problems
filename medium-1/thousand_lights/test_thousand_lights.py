'''A module to test the 'thousand_lights' module'''
import unittest
from thousand_lights import switches_toggled_on_from_toggling_n_switches_n_times

class TestToggleNLightsNTimes(unittest.TestCase):
    '''A Class to test the thousand_lights module'''
    def test_5_lights(self):
        '''Test toggling lights divisible by a given iteration during 5
           iterations for five lights'''
        num = 5
        lights_on = switches_toggled_on_from_toggling_n_switches_n_times(num)
        self.assertEqual(lights_on, [1, 4])

    def test_10_lights(self):
        '''Test toggling lights divisible by a given iteration during
           10 iterations for ten lights'''
        num = 10
        lights_on = switches_toggled_on_from_toggling_n_switches_n_times(num)
        self.assertEqual(lights_on, [1, 4, 9])


if __name__ == '__main__':
    unittest.main()
