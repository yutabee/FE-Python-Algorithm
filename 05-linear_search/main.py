"""
main
"""
from modules.linear_search import linear_search


if __name__ == "__main__":
    arr = [10, 25, 32, 48, 59, 61, 72, 89, 91, 97]
    target = int(input("検索する数値を入力してください: "))   
    result = linear_search(arr, target)
    if result != -1:
        print(f"ターゲット {target} が見つかりました。インデックス: {result}")
    else:
        print(f"ターゲット {target} が見つかりませんでした。")
