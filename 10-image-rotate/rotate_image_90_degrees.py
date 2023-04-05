def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()

def rotate_image_90_degrees(image):
    n = len(image)
    rotated_image = [[0] * n for _ in range(n)]

    print("元の画像:")
    print_matrix(image)

    for x in range(n):
        for y in range(n):
            rotated_image[y][n - 1 - x] = image[x][y]
            print(f"({x}, {y}) -> ({y}, {n - 1 - x}) の値: {image[x][y]}")
            print("途中経過:")
            print_matrix(rotated_image)

    return rotated_image

image = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

rotated_image = rotate_image_90_degrees(image)
print("回転後の画像:")
print_matrix(rotated_image)
