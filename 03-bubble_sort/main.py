"""
main
"""
from modules.bubble_sort import bubble_sort
from modules.bubble_sort_quick import bubble_sort_quick


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = bubble_sort_quick(arr)
    print("Result:", sorted_arr)
