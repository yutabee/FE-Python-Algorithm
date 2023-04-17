import random


def merge(left, mid, right):
    buff = [0]*(right-left)  # ソート後の配列を一時的に格納
    i = left
    j = mid
    p = 0  # pointer of buff[p]
    while i < mid and j < right:
        if data[i] <= data[j]:
            buff[p] = data[i]
            i += 1
            p += 1
        else:
            buff[p] = data[j]
            j += 1
            p += 1
    while i < mid:
        buff[p] = data[i]
        i += 1
        p += 1
    while j < right:
        buff[p] = data[j]
        j += 1
        p += 1
    for n in range(left, right):
        data[n] = buff[n-left]


if __name__ == "__main__":
    n = 15
    data = [0]*n
    for i in range(n):
        data[i] = random.randint(1, 99)

    print(data, "元のデータ")
    s = 2  # 断片（部分配列）のサイズ
    while s <= n:
        loop = n//s  # sサイズに分割した部分配列の数 == loop回数
        fragment = n % s  # 部分配列のあまりの数

        for i in range(loop):
            left = i*s  # 断片の左端インデックス
            mid = i*s+(s//2)  # 断片の中央インデックス
            right = i*s+s  # 断片の右端インデックス
            merge(left, mid, right)
        if fragment > 0:
            merge((loop-1)*s, loop*s, n)
        s = s*2
    print(data, "ソート後のデータ")
