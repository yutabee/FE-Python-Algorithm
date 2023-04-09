"""
選択ソートアルゴリズムを実装するモジュールです。

このモジュールは、選択ソートアルゴリズムを使用して整数のリストを昇順にソートします。
"""

from typing import List


def selection_sort(arr: List[int]) -> List[int]:
    """
    配列を昇順にソートするための選択ソートアルゴリズムです。

    Args:
        arr (List[int]): 整数のリスト。

    Returns:
        List[int]: ソート済みの整数のリスト。元のリストは変更されません。
    """
    sorted_arr = arr.copy()
    n = len(sorted_arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if sorted_arr[j] < sorted_arr[min_index]:
                min_index = j  # 最小値のインデックスを更新
        if min_index != i:  # 無駄な交換を避けるための条件
            tmp = sorted_arr[i]            # 一時変数 tmp に現在の値を格納
            sorted_arr[i] = sorted_arr[min_index]  # 最小値を現在の位置に設定
            sorted_arr[min_index] = tmp    # 元の値を最小値の位置に設定

    return sorted_arr
