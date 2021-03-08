import unittest
import leapYear

class TestCase(unittest.TestCase):
    def test1(self):
        result = leapYear.ly(2004)
        self.assertEqual(result, "Input year is a leap year.")

    def test2(self):
        result = leapYear.ly(2100)
        self.assertEqual(result, "Input year is not a leap year.")
        
    def test3(self):
        result = leapYear.ly(2000)
        self.assertEqual(result, "Input year is a leap year.")

    def test4(self):
        result = leapYear.ly(2001)
        self.assertEqual(result, "Input year is not a leap year.")

if __name__ == "__main__":
    unittest.main()   