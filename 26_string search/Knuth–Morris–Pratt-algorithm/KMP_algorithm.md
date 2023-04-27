# KMP algorithm

KMP アルゴリズム（Knuth-Morris-Pratt アルゴリズム）を Python で実装する例を以下に示します。この実装では、検索パターンがテキスト内で見つかった場合、その開始位置を返します。

```python
def kmp_search(text, pattern):
    def compute_lps(pattern):
        length = 0
        lps = [0] * len(pattern)
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    lps = compute_lps(pattern)
    text_index = 0
    pattern_index = 0

    while text_index < len(text):
        if pattern[pattern_index] == text[text_index]:
            text_index += 1
            pattern_index += 1
        if pattern_index == len(pattern):
            return text_index - pattern_index
        elif text_index < len(text) and pattern[pattern_index] != text[text_index]:
            if pattern_index != 0:
                pattern_index = lps[pattern_index - 1]
            else:
                text_index += 1

    return -1

# 使用例
text = "こんにちは、私はAIです。質問があればどうぞ。"
pattern = "質問"

result = kmp_search(text, pattern)
print(result)  # 17 と表示されます。
```

このコードは、テキスト内で検索パターンが見つかった場合、その開始位置を返します。見つからなかった場合は、-1 が返されます。ただし、この実装は単純な例であり、実際の問題に応じて改良が必要な場合があります。例えば、大文字と小文字を区別しない検索や、検索パターンが複数回出現する場合など、要件に応じて実装を変更してください。
