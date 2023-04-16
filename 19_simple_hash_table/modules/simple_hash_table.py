class SimpleHashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size

    def _hash(self, key):
        return key % 10

    def put(self, key, value):
        index = self._hash(key)
        self.table[index] = value

    def get(self, key):
        index = self._hash(key)
        return self.table[index]

    def delete(self, key):
        index = self._hash(key)
        self.table[index] = None


if __name__ == "__main__":
    hash_map = SimpleHashTable()

    hash_map.put(1, "apple")
    hash_map.put(12, "banana")
    hash_map.put(23, "orange")

    print(hash_map.get(12))  # banana

    hash_map.delete(1)
    print(hash_map.get(1))  # None
