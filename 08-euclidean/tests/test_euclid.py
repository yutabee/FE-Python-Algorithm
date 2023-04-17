import unittest
# from modules.euclid import euclid


class TestEuclid(unittest.TestCase):

    def test_euclid_with_same_numbers(self):
        self.assertEqual(euclid(5, 5), 5)

    def test_euclid_with_coprime_numbers(self):
        self.assertEqual(euclid(17, 13), 1)

    def test_euclid_with_common_divisor(self):
        self.assertEqual(euclid(44, 28), 4)

    def test_euclid_with_larger_first_number(self):
        self.assertEqual(euclid(105, 45), 15)

    def test_euclid_with_larger_second_number(self):
        self.assertEqual(euclid(45, 105), 15)


if __name__ == '__main__':
    unittest.main()
