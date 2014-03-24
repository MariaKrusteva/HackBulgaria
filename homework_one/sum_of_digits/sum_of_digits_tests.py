from sum_of_digits import sum_of_digits
import unittest


class SumOfDigitsTests(unittest.TestCase):
    """Testing sum of digits"""
    def test_with_a_looong_number(self):
        self.assertEqual(43, sum_of_digits(1325132435356))

    def test(self):
        self.assertEqual(6, sum_of_digits(123))

    def test_with_six(self):
        self.assertEqual(6, sum_of_digits(6))

    def test_with_negative_number(self):
        self.assertEqual(1, sum_of_digits(-10))

if __name__ == '__main__':
    unittest.main()
