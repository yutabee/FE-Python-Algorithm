import unittest
# pylint: disable=E0401, E0611
from modules.recursive_binary_search import recursive_binary_search


class TestRecursiveBinarySearch(unittest.TestCase):
    def setUp(self):
        self.data = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105]
        self.data.sort()

    def test_found_key(self):
        self.assertEqual(recursive_binary_search(
            self.data, 75, 0, len(self.data)-1), 6)

    def test_not_found_key(self):
        self.assertEqual(recursive_binary_search(
            self.data, 100, 0, len(self.data)-1), -1)

    def test_empty_data(self):
        self.assertEqual(recursive_binary_search([], 75, 0, -1), -1)

    def test_single_element_data_found(self):
        self.assertEqual(recursive_binary_search([75], 75, 0, 0), 0)

    def test_single_element_data_not_found(self):
        self.assertEqual(recursive_binary_search([50], 75, 0, 0), -1)


if __name__ == "__main__":
    unittest.main()
