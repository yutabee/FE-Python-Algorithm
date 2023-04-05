def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()

def expand_image(image, scale_factor):
    original_width = len(image[0])
    original_height = len(image)

    expanded_width = original_width * scale_factor
    expanded_height = original_height * scale_factor
    expanded_image = [[0] * expanded_width for _ in range(expanded_height)]

    for x in range(original_width):
        for y in range(original_height):
            value = image[x][y]
            for i in range(scale_factor):
                for j in range(scale_factor):
                    expanded_image[x * scale_factor + i][y * scale_factor + j] = value

    return expanded_image
