import unittest
from main2 import max_min_distance


class TestMaxMinDistance(unittest.TestCase):
    def test_example(self):
        N = 5
        C = 3
        stalls = [1, 2, 8, 4, 9]
        result = max_min_distance(N, C, stalls)
        self.assertEqual(result, (3, [1, 4, 8]))

    def test_invalid_input(self):
        N = 1
        C = 3
        stalls = [1, 2, 8, 4 ,9]
        with self.assertRaises(ValueError):
            max_min_distance(N, C, stalls)


if __name__ == '__main__':
    unittest.main()
