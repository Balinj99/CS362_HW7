import unittest
import fizzBuzz

class TestCase(unittest.TestCase):
    def test1(self):
        result = fizzBuzz.fb(1)
        self.assertEqual(result, 1)

    def test2(self):
        result = fizzBuzz.fb(3)
        self.assertEqual(result, "Fizz")
    
    def test3(self):
        result = fizzBuzz.fb(5)
        self.assertEqual(result, "Buzz")

    def test4(self):
        result = fizzBuzz.fb(15)
        self.assertEqual(result, "FizzBuzz")

if __name__ == "__main__":
    unittest.main()   