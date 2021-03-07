import unittest
import fizzBuzz

class TestCase(unittest.TestCase):
    def test1(self):
        result = fizzBuzz.fb(1)
        self.assertEqual(result, 1)

    def test2(self):
        result = fizzBuzz.fb(3)
        self.assertEqual(result, "Fizz")

if __name__ == "__main__":
    unittest.main()   