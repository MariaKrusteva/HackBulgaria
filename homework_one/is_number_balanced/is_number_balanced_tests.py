import unittest
from is_number_balanced import is_number_balanced


class IsNumberBalancedTest(unittest.TestCase):
    def test_one(self):
        self.assertTrue(is_number_balanced(9))

    def test_two(self):
        self.assertTrue(is_number_balanced(11))

    def test_three(self):
        self.assertFalse(is_number_balanced(13))

    def test_four(self):
        self.assertTrue(is_number_balanced(121))

    def test_five(self):
        self.assertTrue(is_number_balanced(4518))

    def test_six(self):
        self.assertFalse(is_number_balanced(28471))

    def test_seven(self):
        self.assertTrue(is_number_balanced(1238033))

if __name__ == '__main__':
    unittest.main()
