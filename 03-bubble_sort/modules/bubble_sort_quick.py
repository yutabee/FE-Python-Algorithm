"""
bubble_sort_quick.py

このモジュールは、改良版バブルソートアルゴリズムを実装したものです。
リストを破壊的変更せずにソートした結果を返す関数を提供します。
"""

from typing import List


def bubble_sort_quick(arr: List[int]) -> List[int]:
    """
    改良版バブルソートアルゴリズムを使って、整数リストを昇順にソートします。
    元のリストは変更されず、新しいソート済みリストが返されます。

    Args:
        arr (List[int]): ソートする整数のリスト。

    Returns:
        List[int]: ソート済みの整数リスト。
    """
    sorted_arr = arr.copy()
    n = len(arr)
    k = 0
    while k < n:
        swapped = True  # フラグ
        last_unsorted = n - 1
        while last_unsorted > k:
            # バブルソート
            if sorted_arr[last_unsorted - 1] > sorted_arr[last_unsorted]:
                tmp = sorted_arr[last_unsorted]
                sorted_arr[last_unsorted] = sorted_arr[last_unsorted - 1]
                sorted_arr[last_unsorted - 1] = tmp
                # 交換が一度でも発生すれば(swapped = False)
                swapped = False
            last_unsorted -= 1
        
        # 最後まで交換が発生しなければ(swapped == True)で強制終了
        if swapped:
            k = n + 1  # 終了条件
        else:
            k += 1  # インクリメント
    return sorted_arr
