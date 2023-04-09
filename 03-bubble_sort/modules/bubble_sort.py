"""
bubble_sort.py

バブルソートアルゴリズムを実装するモジュールです。

このモジュールは、バブルソートアルゴリズムを使用して整数のリストを昇順にソートします。
"""

from typing import List


def bubble_sort(arr: List[int], trace: bool = True) -> List[int]:
    """
    配列を昇順にソートするためのバブルソートアルゴリズムです。

    Args:
        arr (List[int]): 整数のリスト。
        trace (bool): 途中経過を出力するかどうか。デフォルトは False。

    Returns:
        List[int]: ソート済みの整数のリスト。元のリストは変更されません。
    """
    sorted_arr = arr.copy()
    n = len(sorted_arr)

    # 外側のループがリスト全体を走査
    for i in range(0, n - 1, 1):
        # 内側のループが隣接要素を比較・交換
        for j in range(0, n - 1 - i, 1):
            print(f'j={j}', end=",")
            # 左側の要素が右側の要素より大きい場合、交換
            if sorted_arr[j] > sorted_arr[j + 1]:
                tmp = sorted_arr[j]
                sorted_arr[j] = sorted_arr[j+1]
                sorted_arr[j+1] = tmp
                print(f'{sorted_arr[j+1]}->{sorted_arr[j]}交換')
        if trace:
            print(f"i={i}: {sorted_arr}")

    return sorted_arr
