import unittest
from typing import List, Tuple
from linear_search import linear_search  # pylint: disable=E0401


class TestLinearSearch(unittest.TestCase):

    def test_linear_search(self):
        test_cases: List[Tuple[List[int], int, int]] = [
            ([1, 3, 5, 7, 9], 3, 1),
            ([1, 3, 5, 7, 9], 7, 3),
            ([1, 3, 5, 7, 9], 0, -1),
            ([1, 3, 5, 7, 9], 9, 4),
            ([], 1, -1),
            ([1], 1, 0),
            ([1], 2, -1)
        ]

        for arr, target, expected in test_cases:
            with self.subTest(arr=arr, target=target, expected=expected):
                self.assertEqual(linear_search(arr, target), expected)


if __name__ == '__main__':
    unittest.main()
