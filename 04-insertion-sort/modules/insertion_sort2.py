from typing import List


def insertion_sort(arr: List[int]) -> List[int]:
    n = len(arr)

    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                tmp = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = tmp
    return arr


if __name__ == "__main__":
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    insertion_sort(input_arr)
    print("Result:", input_arr)
