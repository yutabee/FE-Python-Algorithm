from typing import List


def linear_search(arr: List[int], target: int):
    """_summary_

    Args:
        arr (List[int]): 探索対象の配列
        target (int): 探索する要素

    Returns:
        int: 探索要素のインデックスを返す
        ※ 見つからなかった場合は-1を返す
    """
    for i, item in enumerate(arr):
        if item == target:
            return i
    return -1
