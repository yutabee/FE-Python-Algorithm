HASH = 5
name = [None]*HASH
tel = [None]*HASH

def hash(key):
    h = 0
    for i in key:
        h = h + ord(i)
    return h%HASH

while True:
    n = input("名前を入力してください ")
    if n == "":
        break
    t = input("番号を入力してください ")
    h = hash(n)
    name[h] = n
    tel[h] = t
    print("ハッシュ値", h, "データ格納完了")

print(name)
print(tel)

while True:
    n = input("検索する名前は? ")
    if n == "":
        break
    h = hash(n)
    if name[h] == n:
        print(n+"さんの番号は"+tel[h])
    else:
        print("その名前は登録されていません")
