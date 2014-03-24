from nth_fibonacci import nth_fibonacci
import unittest


class Nth_fibTest(unittest.TestCase):
    """Testing the fibonacci function"""
    def test_with_one(self):
        self.assertEqual(1, nth_fibonacci(1))

    def test_with_two(self):
        self.assertEqual(1, nth_fibonacci(2))

    def test_with_three(self):
        self.assertEqual(2, nth_fibonacci(3))

    def test_with_ten(self):
        self.assertEqual(55, nth_fibonacci(10))

if __name__ == '__main__':
    unittest.main()
