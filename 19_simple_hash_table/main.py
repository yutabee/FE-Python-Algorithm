# pylint: disable=E0611, E0401
from modules.simple_hash_table import SimpleHashTable


if __name__ == "__main__":
    hash_map = SimpleHashTable()

    hash_map.put(1, "apple")
    hash_map.put(12, "banana")
    hash_map.put(23, "orange")

    print(hash_map.get(12))  # banana

    hash_map.delete(1)
    print(hash_map.get(1))  # None
