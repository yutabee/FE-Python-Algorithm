"""
# Entry Program
"""
from modules.hash_table import HashTable


if __name__ == "__main__":
    # インスタンス化
    hash_table = HashTable(10)

    # データの挿入
    hash_table.insert("Alice", "555-1234")
    hash_table.insert("Bob", "555-5678")
    hash_table.insert("Eve", "555-7777")

    # データの検索
    print(hash_table.search("Alice"))  # "555-1234"
    print(hash_table.search("Bob"))    # "555-5678"
    print(hash_table.search("Eve"))    # "555-7777"
    print(hash_table.search("Charlie"))  # None

