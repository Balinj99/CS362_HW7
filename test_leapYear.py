import unittest
import leapYear

class TestCase(unittest.TestCase):
    def test1(self):
        result = leapYear.ly(2004)
        self.assertEqual(result, "That year is a leap year.")

if __name__ == "__main__":
    unittest.main()   