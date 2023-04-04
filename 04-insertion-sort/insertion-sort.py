def print_colored_array(arr, sorted_end, i=None, j=None):
    def format_element(index, value):
        element = f"{value}"
        if index == j:
            element = f"j:{element}"
        if index == i:
            element = f"i:{element}"
        return element

    green = "\033[32m"
    red = "\033[31m"
    reset = "\033[0m"

    colored_elements = [format_element(index, value) for index, value in enumerate(arr)]
    sorted_part = f"{green}{' '.join(colored_elements[:sorted_end + 1])}{reset}"
    unsorted_part = f"{red}{' '.join(colored_elements[sorted_end + 1:])}{reset}"

    return f"{sorted_part} {unsorted_part}"


def insert_key(arr, i):
    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
        print(print_colored_array(arr, j, i, j))

    arr[j + 1] = key


def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        print(f"Before step {i}: {print_colored_array(arr, i - 1, i)}")
        insert_key(arr, i)
        print(f"After step {i}: {print_colored_array(arr, i)}\n")


arr = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(arr)
print("Sorted array is:", arr)
