class StringHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash(self, key: str) -> int:
        h = 0
        for i in key:
            h = h + ord(i)
        return h % self.size

    def insert(self, key: str):
        hash_index = self._hash(key)

        if self.table[hash_index] is None:
            self.table[hash_index] = key
        else:
            self.open_addressing(key, hash_index)

    def open_addressing(self, key: str, hash_index: int):
        for _ in range(self.size - 1):
            hash_index = (hash_index + 1) % self.size

            if self.table[hash_index] is None:
                self.table[hash_index] = key
                return

        print("No available space to store data.")

    def search(self, key: str) -> str:
        hash_index = self._hash(key)

        if self.table[hash_index] == key:
            return key

        for _ in range(self.size - 1):
            hash_index = (hash_index + 1) % self.size

            if self.table[hash_index] == key:
                return key

        return None
