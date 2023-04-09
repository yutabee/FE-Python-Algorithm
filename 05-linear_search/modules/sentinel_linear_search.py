"""
番兵法を用いた線形探索アルゴリズム
"""
from typing import List


def sentinel_linear_search(arr: List[int], target: int) -> int:
    """
    番兵法を用いた線形探索アルゴリズムを実装した関数です。
    指定されたターゲットが配列内に存在する場合、そのインデックスを返します。
    存在しない場合は -1 を返します。

    Args:
        arr (List[int]): 探索対象の配列
        target (int): 探索する要素

    Returns:
        int: ターゲット要素のインデックス。見つからなかった場合は -1 を返す。
    """
    arr.append(target)  # 番兵を仕込む
    i = 0
    while arr[i] != target:  # ターゲットが一致しなければインクリメント
        i += 1
    arr.pop()  # 番兵を取り出す
    
    if i < len(arr):
        return i
    return -1
