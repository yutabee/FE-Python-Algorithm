from typing import List


def flip_horizontal(matrix: List[List[int]]) -> List[List[int]]:
    n = len(matrix)
    flipped_matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            flipped_matrix[i][n - 1 - j] = matrix[i][j]
    return flipped_matrix


def flip_vertical(matrix: List[List[int]]) -> List[List[int]]:
    n = len(matrix)
    flipped_matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            flipped_matrix[n - 1 - i][j] = matrix[i][j]
    return flipped_matrix


def flip_both(matrix: List[List[int]]) -> List[List[int]]:
    n = len(matrix)
    flipped_matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            flipped_matrix[n - 1 - i][n - 1 - j] = matrix[i][j]
    return flipped_matrix


def rotate_left(matrix: List[List[int]]) -> List[List[int]]:
    n = len(matrix)
    rotated_matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            rotated_matrix[i][j] = matrix[j][n - 1 - i]
    return rotated_matrix


def rotate_right(matrix: List[List[int]]) -> List[List[int]]:
    n = len(matrix)
    rotated_matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            rotated_matrix[i][j] = matrix[n - 1 - j][i]
    return rotated_matrix


def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()


if __name__ == "__main__":
    image = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
    print("Image")
    print_matrix(image)
    flipped_horizontal_image = flip_horizontal(image)
    flipped_vertical_image = flip_vertical(image)
    flipped_both_image = flip_both(image)
    rotated_left_image = rotate_left(image)
    rotated_right_image = rotate_right(image)
    print("Flipped Horizontal")
    print_matrix(flipped_horizontal_image)
    print("Flipped Vertical")
    print_matrix(flipped_vertical_image)
    print("Flipped Both")
    print_matrix(flipped_both_image)
    print("Rotated Left")
    print_matrix(rotated_left_image)
    print("Rotated Right")
    print_matrix(rotated_right_image)
