def bubble_sort(arr):
    n = len(arr)

    # 外側のループがリスト全体を走査
    for i in range(n - 1):
        # 内側のループが隣接要素を比較・交換
        for j in range(n - 1 - i):
            # 左側の要素が右側の要素より大きい場合、交換
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# 使用例
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array is:", arr)  # Sorted array is: [11, 12, 22, 25, 34, 64, 90]と出力される