from typing import List


def binary_search(arr: List[int], target: int) -> int:
    low: int = 0
    high: int = len(arr) - 1
    mid: int

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17]
    target = 11

    result = binary_search(arr, target)
    if result != -1:
        print(f"要素 {target} はインデックス {result} にあります。")
    else:
        print(f"要素 {target} はリスト内に存在しません。")
