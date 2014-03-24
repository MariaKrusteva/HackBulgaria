import unittest
from is_prime import is_prime


class IsPrimeTest(unittest.TestCase):
    def test_one(self):
        self.assertFalse(is_prime(1))

    def test_two(self):
        self.assertTrue(is_prime(2))

    def test_three(self):
        self.assertFalse(is_prime(8))

    def test_four(self):
        self.assertTrue(is_prime(11))

    def test_is_prime_with_negative_number(self):
        self.assertFalse(is_prime(-10))

if __name__ == '__main__':
    unittest.main()
