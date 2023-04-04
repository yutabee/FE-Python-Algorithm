# find_patter関数の解説
```python
def find_pattern(text: str, pattern: str) -> int:
```

まず、関数の定義があります。`find_pattern`関数は、2つの文字列（`text`および`pattern`）を引数として受け取り、整数値（パターンの開始位置または-1）を返します。

```python
    text_length = len(text)
    pattern_length = len(pattern)
```

次に、`text`と`pattern`の長さを計算し、それぞれ`text_length`と`pattern_length`に格納します。これにより、次のステップでループを効率的に行うことができます。

```python
    for position in range(text_length - pattern_length + 1):
```

`text`内で`pattern`を探すために、`position`が0から`text_length - pattern_length`までの範囲でループを実行します。この範囲は、`pattern`が`text`内で見つかる可能性のある最後の位置を示します。

```python
        if text[position:position + pattern_length] == pattern:
            return position
```

`text`の現在の`position`から、`pattern_length`だけスライスして取得した部分文字列が、`pattern`と一致するかどうかを確認します。一致する場合、その時点で`position`を返し、関数を終了します。これにより、最初に見つかったパターンの位置が返されます。

```python
    return -1
```

もし`pattern`が`text`内に見つからない場合、ループが終了します。その後、-1が返されます。これは、パターンが見つからなかったことを示す標準的な方法です。

全体として、`find_pattern`関数は、与えられた`pattern`が`text`内に存在するかどうかを判断し、存在する場合はその位置を返します。存在しない場合は、-1を返します。この関数を使用して、任意のテキストとパターンの組み合わせで簡単に検索を行うことができます。