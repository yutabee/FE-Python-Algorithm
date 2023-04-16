from typing import List


def recursive_binary_search(
        data: List[int], key: int, low: int, high: int) -> int:
    mid: int
    ans: int

    print("入口", low, high)
    if (low <= high):
        mid = (low + high) // 2
        if (data[mid] == key):  # ベースケース
            ans = mid
        else:  # 再帰的処理
            if (data[mid] > key):
                ans = recursive_binary_search(data, key, low, mid-1)
            else:
                ans = recursive_binary_search(data, key, mid+1, high)  # 修正
    else:  # 探索要素がない場合
        ans = -1
    print("コールスタック", low, high, ans)
    return ans


if __name__ == "__main__":
    input_data = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105]
    input_data.sort()
    a = recursive_binary_search(input_data, 75, 0, len(input_data)-1)
    print(a)
