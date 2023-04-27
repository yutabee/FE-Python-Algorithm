def brute_force_search(text, pattern):
    text_length = len(text)
    pattern_length = len(pattern)

    for i in range(text_length - pattern_length + 1):
        match = True
        for j in range(pattern_length):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            return i

    # パターンが見つからない場合は、-1を返します。
    return -1


if __name__ == '__main__':
    text = "こんにちは、私はAIです。質問があればどうぞ。"
    pattern = "質問"

    result = brute_force_search(text, pattern)
    print(result)  # 17 と表示されます。
