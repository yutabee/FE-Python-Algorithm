"""
main
"""
from modules.HashTable import HashTable


if __name__ == "__main__":
    hash_table = HashTable()

    while True:
        n = input("名前を入力してください ")
        if n == "":
            break
        t = input("番号を入力してください ")
        hash_table.store(n, t)

    print(hash_table.name)
    print(hash_table.tel)

    while True:
        n = input("検索する名前は? ")
        if n == "":
            break
        result = hash_table.search(n)
        if result is not None:
            print(n + "さんの番号は" + result)
        else:
            print("その名前は登録されていません")
