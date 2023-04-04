class HashTable:
    def __init__(self, size):
        self.size = size
        self.names = [None] * size
        self.phone_numbers = [None] * size

    def calculate_hash(self, key):
        return sum(ord(char) for char in key) % self.size

    def insert(self, name, phone_number):
        hash_index = self.calculate_hash(name)
        if self.names[hash_index] is None:
            self.names[hash_index] = name
            self.phone_numbers[hash_index] = phone_number
            print(f"Hash value: {hash_index}, data stored.")
        else:
            self.open_addressing(name, phone_number, hash_index)

    def open_addressing(self, name, phone_number, hash_index):
        for _ in range(self.size - 1):
            hash_index = (hash_index + 1) % self.size
            if self.names[hash_index] is None:
                self.names[hash_index] = name
                self.phone_numbers[hash_index] = phone_number
                print(f"Rehashed: {hash_index}, data stored.")
                return
        print("No available space to store data.")

    def search(self, name):
        hash_index = self.calculate_hash(name)
        if self.names[hash_index] == name:
            return self.phone_numbers[hash_index]
        elif self.names[hash_index] is None:
            return None
        else:
            return self.search_rehash(name, hash_index)

    def search_rehash(self, name, hash_index):
        for _ in range(self.size - 1):
            hash_index = (hash_index + 1) % self.size
            if self.names[hash_index] == name:
                return self.phone_numbers[hash_index]
        return None


# Entry Program
if __name__ == "__main__":
    hash_table = HashTable(5)

    while True:
        name = input("Enter name: ")
        if name == "":
            break
        phone_number = input("Enter phone number: ")
        hash_table.insert(name, phone_number)

    print(hash_table.names)
    print(hash_table.phone_numbers)

    while True:
        name = input("Enter name to search: ")
        if name == "":
            break
        phone_number = hash_table.search(name)
        if phone_number is None:
            print(f"{name} is not registered.")
        else:
            print(f"{name}'s phone number is {phone_number}.")
