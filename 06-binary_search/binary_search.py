def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # 要素が見つからない場合、-1を返す

# ソートされたリストと探すべき要素
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17]
target = 11

# 二分探索関数を呼び出して結果を表示
result = binary_search(arr, target)
if result != -1:
    print(f"要素 {target} はインデックス {result} にあります。")
else:
    print(f"要素 {target} はリスト内に存在しません。")
