from typing import List


def linear_search(arr: List[int], target: int) -> int:
    arr.append(target)  # 番兵を仕込む
    i = 0
    while arr[i] != target:  # ターゲットが一致しなければインクリメント
        i += 1
    arr.pop()  # 番兵を取り出す

    if i < len(arr):
        return i
    return -1
