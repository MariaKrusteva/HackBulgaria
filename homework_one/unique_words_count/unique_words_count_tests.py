import unittest
from unique_words_count import unique_words_count


class UniqueWordsCountTest(unittest.TestCase):
    """testing unique_words_count"""
    def test_one(self):
        self.assertEqual(3, unique_words_count(["apple", "banana", "apple", "pie"]))

    def test_two(self):
        self.assertEqual(2, unique_words_count(["python", "python", "python", "ruby"]))

    def test_three(self):
        self.assertEqual(1, unique_words_count(["HELLO!"] * 10))

if __name__ == '__main__':
     unittest.main() 