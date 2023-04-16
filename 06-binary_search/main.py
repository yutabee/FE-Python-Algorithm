from modules.binary_search import binary_search


if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17]
    target = 11

    # 二分探索関数を呼び出して結果を表示
    result = binary_search(arr, target)
    if result != -1:
        print(f"要素 {target} はインデックス {result} にあります。")
    else:
        print(f"要素 {target} はリスト内に存在しません。")
