from sum_of_min_and_max import sum_of_min_and_max
import unittest


class SumTest(unittest.TestCase):
    """ Testing nth Fibonacci number """
    def test_list_with_possitive(self):
        self.assertEqual(10, sum_of_min_and_max([1, 2, 3, 4, 9]))

    def test_list_with_negative(self):
        self.assertEqual(90, sum_of_min_and_max([-10, 5, 10, 100]))

    def test_one_element(self):
        self.assertEqual(2, sum_of_min_and_max([1]))


if __name__ == '__main__':
    unittest.main()
