"""
main
"""
from modules.insertion_sort import insertion_sort

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = insertion_sort(arr)
    print("Original array:", arr)  # [64, 34, 25, 12, 22, 11, 90] と出力される
    print("Sorted array:", sorted_arr)  # [11, 12, 22, 25, 34, 64, 90] と出力される
