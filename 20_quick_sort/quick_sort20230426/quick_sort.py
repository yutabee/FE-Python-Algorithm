from typing import List


def quick_sort(arr: List[int], low: int, high: int) -> None:
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index)
        quick_sort(arr, pivot_index + 1, high)


def partition(arr: List[int], low: int, high: int) -> int:
    pivot = arr[low]
    left = low + 1
    right = high

    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left = left + 1
        while arr[right] >= pivot and right >= left:
            right = right - 1

        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]

    arr[low], arr[right] = arr[right], arr[low]
    return right


if __name__ == "__main__":
    arr = [3, 6, 8, 10, 1, 2, 1]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)
