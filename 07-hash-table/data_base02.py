HASH = 5
name = [None]*HASH
tel = [None]*HASH

def hash(key):
    h = 0
    for i in key:
        h = h + ord(i)
    return h%HASH

def open_add(n, t, h):
    flg = False
    for i in range(HASH-1):
        h = (h+1)%HASH
        if name[h] == None:
            name[h] = n
            tel[h] = t
            flg = True
            print("再ハッシュ", h, "データ格納完了")
            break
    if flg == False:
        print("データを格納できる領域がありません")

def serch_rehash(key, h):
    for i in range(HASH-1):
        h = (h+1)%HASH
        if name[h] == key:
            return h
    return -1

while True:
    n = input("名前を入力してください ")
    if n == "":
        break
    t = input("番号を入力してください ")
    h = hash(n)
    if name[h] == None:
        name[h] = n
        tel[h] = t
        print("ハッシュ値", h, "データ格納完了")
    else:
        open_add(n, t, h)

print(name)
print(tel)

while True:
    n = input("検索する名前は? ")
    if n == "":
        break
    h = hash(n)
    if name[h] == n:
        print(n+"さんの番号は"+tel[h])
    elif name[h] == "None":
        print("その名前は登録されていません")
    else:
        h = serch_rehash(n, h)
        if h == -1:
            print("その名前は登録されていません")
        else:
            print(n+"さんの番号は"+tel[h])
