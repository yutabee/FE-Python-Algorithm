from expand_image import print_matrix,expand_image


def main():
    image = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0]
    ]

    print("元の画像:")
    print_matrix(image)

    scale_factor = 2
    expanded_image = expand_image(image, scale_factor)
    print(f"拡大された画像 (倍率: {scale_factor}):")
    print_matrix(expanded_image)
