"""
insertion_sort.py

このモジュールは、挿入ソートアルゴリズムを実装したものです。
リストを破壊的変更せずにソートした結果を返す関数を提供します。
"""
from typing import List


def insertion_sort(arr: List[int]) -> List[int]:
    """
    挿入ソートアルゴリズムを使って、整数リストを昇順にソートします。
    元のリストは変更されず、新しいソート済みリストが返されます。

    Args:
        arr (List[int]): ソートする整数のリスト。

    Returns:
        List[int]: ソート済みの整数リスト。
    """
    sorted_arr = arr.copy()
    n = len(sorted_arr)

    for i in range(1, n):
        for j in range(i, 0, -1):
            # sorted_arr[j]がKey ソート済み領域の方が小さければ交換
            if sorted_arr[j] < sorted_arr[j - 1]:
                tmp = sorted_arr[j]
                sorted_arr[j] = sorted_arr[j - 1]
                sorted_arr[j - 1] = tmp
                print(f'i={i},j={j},sorted_arr[j]={sorted_arr[j]}, sorted_arr[j-1]={sorted_arr[j-1]},sorted_arr={sorted_arr}')
            # ソート済みの方が小さくなったところで交換せずブレイク
            else:
                print(f'i={i},j={j},sorted_arr[j]={sorted_arr[j]},sorted_arr[j-1]={sorted_arr[j-1]},sorted_arr={sorted_arr}')
                break

    return sorted_arr
