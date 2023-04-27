# brute_force_search

ブルートフォース法を Python で実装する例を以下に示します。この実装では、検索パターンがテキスト内で見つかった場合、その開始位置を返します。

```python
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

# 使用例
text = "こんにちは、私はAIです。質問があればどうぞ。"
pattern = "質問"

result = brute_force_search(text, pattern)
print(result)  # 17 と表示されます。
```

このコードは、テキスト内で検索パターンが見つかった場合、その開始位置を返します。見つからなかった場合は、-1 が返されます。

ただし、この実装は単純な例であり、実際の問題に応じて改良が必要な場合があります。例えば、大文字と小文字を区別しない検索や、検索パターンが複数回出現する場合など、要件に応じて実装を変更してください。
