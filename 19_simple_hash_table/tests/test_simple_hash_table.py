import unittest
# pylint: disable=E0611, E0401
from modules.simple_hash_table import SimpleHashTable


class TestSimpleHashTable(unittest.TestCase):
    def test_init(self):
        ht = SimpleHashTable()
        self.assertEqual(ht.size, 10)
        self.assertEqual(ht.table, [None] * 10)

    def test_hash(self):
        ht = SimpleHashTable()
        self.assertEqual(ht._hash(15), 5)  # pylint:disable=W0212

    def test_put(self):
        ht = SimpleHashTable()
        ht.put(15, "test_value")
        self.assertEqual(ht.table[5], "test_value")

    def test_get(self):
        ht = SimpleHashTable()
        ht.put(15, "test_value")
        self.assertEqual(ht.get(15), "test_value")

    def test_delete(self):
        ht = SimpleHashTable()
        ht.put(15, "test_value")
        ht.delete(15)
        self.assertIsNone(ht.table[5])


if __name__ == "__main__":
    unittest.main()
