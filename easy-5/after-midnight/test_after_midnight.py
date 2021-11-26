import unittest
from after_midnight import before_midnight, after_midnight

class TestAfterAndBeforeMidnight(unittest.TestCase):
    def test_zero_after_midnight(self):
        timestring = '00:00'
        mins = after_midnight(timestring)
        self.assertEqual(mins, 0)

    def test_zero_before_midnight(self):
        timestring = '00:00'
        mins = before_midnight(timestring)
        self.assertEqual(mins, 0)

    def test_twelve_thirty_four_after(self):
        timestring = '12:34'
        mins = after_midnight(timestring)
        self.assertEqual(mins, 754)

    def test_twelve_thirty_four_before(self):
        timestring = '12:34'
        mins = before_midnight(timestring)
        self.assertEqual(mins, 686)

    def test_twenty_four_after(self):
        timestring = '24:00'
        mins = after_midnight(timestring)
        self.assertEqual(mins, 0)

    def test_twenty_four_after(self):
        timestring = '24:00'
        mins = before_midnight(timestring)
        self.assertEqual(mins, 0)


if __name__ == '__main__':
    unittest.main()