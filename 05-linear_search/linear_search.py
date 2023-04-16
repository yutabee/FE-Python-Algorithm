from typing import List


def linear_search(arr: List[int], target: int):
    n = len(arr)
    for i in range(n):
        if arr[i] == target:
            return i
    return -1


if __name__ == "__main__":
    arr = [10, 25, 32, 48, 59, 61, 72, 89, 91, 97]
    target = 91
    result = linear_search(arr, target)
    if result != -1:
        print(f"ターゲット: {target} のインデックス: {result}")
    else:
        print(f"ターゲット: {target} が見つかりませんでした。")
