import unittest
from main import longest_peak


class TestLongestPeak(unittest.TestCase):

    def test_increasing(self):
        array = [1, 2, 3, 4, 5]
        longest_arrays, longest_length, highest_peak = longest_peak(array)
        self.assertEqual(longest_arrays, [])
        self.assertEqual(longest_length, 0)
        self.assertEqual(highest_peak, 0)

    def test_decreasing(self):
        array = [5, 4, 3, 2, 1]
        longest_arrays, longest_length, highest_peak = longest_peak(array)
        self.assertEqual(longest_arrays, [])
        self.assertEqual(longest_length, 0)
        self.assertEqual(highest_peak, 0)

    def test_two(self):
        array = [1, 2]
        longest_arrays, longest_length, highest_peak = longest_peak(array)
        self.assertEqual(longest_arrays, [])
        self.assertEqual(longest_length, 0)
        self.assertEqual(highest_peak, 0)

    def test_peaks(self):
        array = [1, 3, 5, 4, 2, 8, 3, 7]
        longest_arrays, longest_length, highest_peak = longest_peak(array)
        self.assertEqual(longest_arrays, [[1, 3, 5, 4, 2]])
        self.assertEqual(longest_length, 5)
        self.assertEqual(highest_peak, 5)


if __name__ == '__main__':
    unittest.main()
