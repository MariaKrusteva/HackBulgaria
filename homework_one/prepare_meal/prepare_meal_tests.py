import unittest
from prepare_meal import prepare_meal


class PrepareMealTest(unittest.TestCase):
    """testing prepare_meal"""
    def test_spam(self):
        self.assertEqual("spam", prepare_meal(3))
        self.assertEqual("spam spam spam", prepare_meal(27))

    def test_eggs(self):
        self.assertEqual("eggs", prepare_meal(5))
        self.assertEqual("eggs", prepare_meal(10))

    def test_spam_eggs(self):
        self.assertEqual("spam and eggs", prepare_meal(15))
        self.assertEqual("spam spam and eggs", prepare_meal(45))

    def test_empty(self):
        self.assertEqual("", prepare_meal(7))

if __name__ == '__main__':
    unittest.main()
