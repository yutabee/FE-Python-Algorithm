def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]  # 未ソート部分の先頭要素
        j = i - 1

        print(f"i: {i}, key: {key}, j: {j}")  # デバッグ出力1

        # ソート済み部分を右から左に走査し、適切な位置に挿入
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

            print(f"  j: {j}, arr: {arr}")  # デバッグ出力2

        arr[j + 1] = key  # 未ソート部分の先頭要素を適切な位置に挿入
        print(f"arr after step {i}: {arr}\n")  # デバッグ出力3

# 使用例
arr = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(arr)
print("Sorted array is:", arr)  # Sorted array is: [11, 12, 22, 25, 34, 64, 90]と出力される
