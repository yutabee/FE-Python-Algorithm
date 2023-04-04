def find_max(arr):
    max_value = arr[0]  # 最初の要素を最大値と仮定
    for num in arr:
        if num > max_value:
            max_value = num  # より大きな値が見つかれば最大値を更新
    return max_value

# 使用例
arr = [3, 5, 2, 8, 1]
print(find_max(arr))  # 8 と出力される