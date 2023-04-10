import unittest
from modules.hash_table import HashTable


class TestHashTable(unittest.TestCase):

    def setUp(self):
        self.hash_table = HashTable(10)

    def test_insert_and_search(self):
        # 名前と電話番号の挿入
        self.hash_table.insert("Alice", "123-456-7890")
        self.hash_table.insert("Bob", "234-567-8901")
        self.hash_table.insert("Charlie", "345-678-9012")
        self.hash_table.insert("David", "456-789-0123")

        # 検索テスト
        self.assertEqual(self.hash_table.search("Alice"), "123-456-7890")
        self.assertEqual(self.hash_table.search("Bob"), "234-567-8901")
        self.assertEqual(self.hash_table.search("Charlie"), "345-678-9012")
        self.assertEqual(self.hash_table.search("David"), "456-789-0123")

    def test_search_non_existent_name(self):
        # 存在しない名前の検索テスト
        self.assertIsNone(self.hash_table.search("Eve"))


if __name__ == "__main__":
    unittest.main()
