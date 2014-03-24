import unittest
from count_words import count_words


class CountWordsTest(unittest.TestCase):
    """testing count_words"""
    def test_one(self):
        self.assertEqual({'apple': 2, 'pie': 1, 'banana': 1}, count_words(["apple", "banana", "apple", "pie"]))

    def test_two(self):
        self.assertEqual({'ruby': 1, 'python': 3}, count_words(["python", "python", "python", "ruby"]))


if __name__ == '__main__':
    unittest.main()