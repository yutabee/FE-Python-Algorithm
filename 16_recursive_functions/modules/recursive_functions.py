import os


def factorial(n):
    if n == 0 or n == 1:  # ベースケース
        return 1
    else:  # 再帰ステップ
        return n * factorial(n - 1)


def fibonacci(n):
    if n == 0:  # ベースケース
        return 0
    elif n == 1:  # ベースケース
        return 1
    else:  # 再帰ステップ
        return fibonacci(n - 1) + fibonacci(n - 2)


def binary_search(arr, low, high, target):
    if low > high:  # ベースケース
        return -1

    mid = (low + high) // 2
    if arr[mid] == target:  # ベースケース
        return mid
    elif arr[mid] < target:  # 再帰ステップ
        return binary_search(arr, mid + 1, high, target)
    else:  # 再帰ステップ
        return binary_search(arr, low, mid - 1, target)


def dfs_directory(path, depth=0):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)

        if os.path.isdir(item_path):
            print("  " * depth + item)
            dfs_directory(item_path, depth + 1)
        else:
            print("  " * depth + item)
