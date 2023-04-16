from typing import List


def selection_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
    # 交換
    tmp = arr[i]
    arr[i] = arr[min_index]
    arr[min_index] = tmp

    return arr
