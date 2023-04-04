def build_skip_table(pattern):
    pattern_length = len(pattern)
    skip_table = [pattern_length] * 256
    for i in range(pattern_length - 1):
        skip_table[ord(pattern[i])] = pattern_length - i - 1
    return skip_table

def boyer_moore_search(text, pattern):
    text_length = len(text)
    pattern_length = len(pattern)
    skip_table = build_skip_table(pattern)
    index = pattern_length - 1

    while index < text_length:
        match = True
        for i in range(pattern_length):
            if text[index - i] != pattern[pattern_length - 1 - i]:
                match = False
                break
        if match:
            return index + 1 - (pattern_length - 1)
        index += skip_table[ord(text[index])]

    return -1

def main():
    text = "I'm learning Python. It's interesting!"
    pattern = "Python"
    position = boyer_moore_search(text, pattern)

    print(text)
    if position != -1:
        print(f"{position}文字目に{pattern}があります")
    else:
        print(f"{pattern}は見つかりませんでした")

if __name__ == "__main__":
    main()
