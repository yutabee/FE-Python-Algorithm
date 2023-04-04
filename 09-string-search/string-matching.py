def find_pattern(text: str, pattern: str) -> int:
    """
    Search for the given pattern in the text and return its position.

    Args:
        text (str): The text to search in.
        pattern (str): The pattern to search for.

    Returns:
        int: The position of the pattern in the text, or -1 if not found.
    """
    text_length = len(text)
    pattern_length = len(pattern)
    
    for position in range(text_length - pattern_length + 1):
        if text[position:position + pattern_length] == pattern:
            return position
    return -1

def main():
    """
    Main function to demonstrate the usage of find_pattern.
    """
    text = "I'm learning Python. It's interesting!"
    pattern = "Python"
    position = find_pattern(text, pattern)

    print(text)
    if position != -1:
        print(f"{position + 1}文字目に{pattern}があります")
    else:
        print(f"{pattern}は見つかりませんでした")

if __name__ == "__main__":
    main()
