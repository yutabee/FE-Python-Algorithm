from typing import List


def bubble_sort(arr: List[int]) -> List[int]:
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
    return arr


if __name__ == "__main__":
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(input_arr)
    print("Result:", input_arr)
