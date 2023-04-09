from typing import List


def binary_search(arr: List[int], target: int) -> int:
    """二分探索アルゴリズムを使用して、ソートされた整数リスト内の目的の値のインデックスを返します。

    この関数は、ソートされた整数リストに対して二分探索アルゴリズムを実行し、
    目的の値が見つかった場合にそのインデックスを返します。目的の値がリスト内に
    存在しない場合は -1 を返します。

    Args:
        arr (List[int]): ソートされた整数リスト。
        target (int): 探索する整数。

    Returns:
        int: 目的の値のインデックス（存在する場合）または -1（存在しない場合）。
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
