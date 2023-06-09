import random


def quick_sort(data, min, max):  # pylint: disable=W0622
    i = min  # min_index
    j = max  # max_index
    pivot = (min+max)//2  # 軸
    # ソート対象のインデックスを探索
    while True:
        while data[i] < data[pivot]:
            i = i + 1
        while data[j] > data[pivot]:
            j = j - 1
        # 無限ループ終了条件
        if i >= j:
            break
        # 交換
        tmp = data[i]
        data[i] = data[j]
        data[j] = tmp
        # 範囲を一つ狭める
        i = i + 1
        j = j - 1
    # 再帰処理
    if min < i-1:
        quick_sort(data, min, i-1)
    if max > j+1:
        quick_sort(data, j+1, max)


if __name__ == "__main__":
    n = 10
    data = [0] * n
    for i in range(n):
        data[i] = random.randint(1, 99)
    print(data, "元のデータ")
    quick_sort(data, 0, n-1)
    print(data, "ソート後のデータ")
