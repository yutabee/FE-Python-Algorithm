def linear_search(arr, target):
    for i, item in enumerate(arr):
        if item == target:
            return i
    return -1

def main():
    arr = [10, 25, 32, 48, 59, 61, 72, 89, 91, 97]
    target = int(input("検索する数値を入力してください: "))
    
    result = linear_search(arr, target)
    
    if result != -1:
        print(f"ターゲット {target} が見つかりました。インデックス: {result}")
    else:
        print(f"ターゲット {target} が見つかりませんでした。")

if __name__ == "__main__":
    main()
