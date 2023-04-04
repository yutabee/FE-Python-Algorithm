def print_colored_array(arr, sorted_end):
    """
    ソート済みの部分と未ソートの部分をカラー分けして出力する関数。

    :param arr: 整列対象のリスト
    :param sorted_end: ソート済みの部分の末尾のインデックス
    """
    green = "\033[32m"
    red = "\033[31m"
    reset = "\033[0m"

    sorted_part = f"{green}{' '.join(map(str, arr[:sorted_end + 1]))}{reset}"
    unsorted_part = f"{red}{' '.join(map(str, arr[sorted_end + 1:]))}{reset}"
    print(f"{sorted_part} {unsorted_part}")


def insert_key(arr, i):
    """
    未ソート部分の先頭要素（キー）をソート済み部分に適切な位置に挿入する関数。

    :param arr: 整列対象のリスト
    :param i: 未ソート部分の先頭要素のインデックス
    """
    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key


def insertion_sort(arr):
    """
    リストを挿入ソートで整列する関数。

    :param arr: 整列対象のリスト
    """
    n = len(arr)

    for i in range(1, n):
        print(f"i: {i}, arr: {arr}")
        print_colored_array(arr, i - 1)

        insert_key(arr, i)

        print(f"arr after step {i}: {arr}\n")
        print_colored_array(arr, i)

# 使用例
arr = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(arr)
print("Sorted array is:", arr)  # Sorted array is: [11, 12, 22, 25, 34, 64, 90]と出力される
