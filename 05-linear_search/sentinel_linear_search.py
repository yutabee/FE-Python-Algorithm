def sentinel_linear_search(arr, target):
    arr.append(target)
    i = 0
    while arr[i] != target:
        i += 1
    arr.pop()
    
    if i < len(arr):
        return i
    return -1

def main():
    arr = [10, 25, 32, 48, 59, 61, 72, 89, 91, 97]
    target = int(input("検索する数値を入力してください: "))
    
    result = sentinel_linear_search(arr, target)
    
    if result != -1:
        print(f"ターゲット {target} が見つかりました。インデックス: {result}")
    else:
        print(f"ターゲット {target} が見つかりませんでした。")

if __name__ == "__main__":
    main()
