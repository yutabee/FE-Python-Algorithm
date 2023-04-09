"""
main
"""
from modules.selection_sort import selection_sort

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = selection_sort(arr)
    print(sorted_arr)  # [11, 12, 22, 25, 34, 64, 90] と出力される
    print(arr)  # 元のリストが変更されない: [64, 34, 25, 12, 22, 11, 90] と出力される
