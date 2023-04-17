from typing import List


def merge(a: List[int], b: List[int]):
    na = len(a)
    nb = len(b)
    merged_arr = [0]*(na+nb)  # マージ先の配列
    i = 0  # pointer of a
    j = 0  # pointer of b
    p = 0  # pointer of merged array

    print(a, "データA")
    print(b, "データB")

    # a, bの要素を比較してmerged_arrに格納
    while i < na and j < nb:
        if a[i] <= b[j]:
            merged_arr[p] = a[i]
            i += 1
            p += 1
        else:
            merged_arr[p] = b[j]
            j += 1
            p += 1

    # aの残りのデータをmerged_arrに格納
    while i < na:
        merged_arr[p] = a[i]
        i += 1
        p += 1
    # bの残りのデータをmerged_arrに格納
    while j < nb:
        merged_arr[p] = b[j]
        j += 1
        p += 1

    return merged_arr


if __name__ == "__main__":
    a = [1, 3, 4, 7, 8, 9]
    b = [0, 2, 5, 6]
    merged_arr = merge(a, b)
    print(merged_arr, "マージ後のデータ")
