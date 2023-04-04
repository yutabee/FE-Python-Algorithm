class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size

    def hash_function(self, data):
        return (data % 10) + 1

    def insert(self, data):
        index = self.hash_function(data)
        if self.table[index] is None:
            self.table[index] = data
        else:
            print(f"Collision occurred at index {index}. Data {data} cannot be inserted.")

    def search(self, data):
        index = self.hash_function(data)
        if self.table[index] == data:
            return index
        else:
            print(f"Data {data} not found.")
            return None

    def display(self):
        print(self.table)


hash_table = HashTable()
hash_table.insert(15)
hash_table.insert(25)
hash_table.insert(35)
hash_table.insert(45)
hash_table.insert(55)

hash_table.display()

print(hash_table.search(15))
print(hash_table.search(55))
print(hash_table.search(65))
