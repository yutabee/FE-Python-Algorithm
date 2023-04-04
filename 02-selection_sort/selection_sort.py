def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j  # 最小値のインデックスを更新
        arr[i], arr[min_index] = arr[min_index], arr[i]  # 最小値と先頭要素を交換

#使用例
arr = [64, 34, 25, 12, 22, 11, 90]
selection_sort(arr)
print("Sorted array is:", arr)  # Sorted array is: [11, 12, 22, 25, 34, 64, 90]と出力される