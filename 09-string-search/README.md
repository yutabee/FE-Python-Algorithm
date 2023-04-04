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

# boyer_moore
This module provides an implementation of the Boyer-Moore string search algorithm for finding a pattern within a given text.

Functions:
- build_skip_table(pattern: str) -> List[int]:
    Constructs a skip table based on the input pattern. The skip table is used to determine how many characters to skip when a mismatch occurs during the Boyer-Moore search.

- boyer_moore_search(text: str, pattern: str) -> int:
    Searches for the given pattern in the input text using the Boyer-Moore algorithm. Returns the starting index of the pattern in the text if found, otherwise returns -1.

- main():
    Demonstrates the usage of the boyer_moore_search function by searching for the pattern "Python" in a sample text.
 
# build_skip_table(pattern: str) -> List[int]
`build_skip_table(pattern: str) -> List[int]`関数は、Boyer-Moore検索アルゴリズムの効率性を高めるために使用されるスキップテーブルを構築します。関数の手順は以下の通りです。

1. パターンの長さを取得し、`pattern_length`に格納します。

2. 長さ256のリスト`skip_table`を作成し、すべての要素に`pattern_length`を格納します。このリストは、ASCII文字セットの各文字に対応するスキップ値を格納するために使用されます。最初に、全ての要素を`pattern_length`で初期化して、見つからなかった文字に対するデフォルトのスキップ値を設定します。

3. パターンの各文字について、以下の処理を実行します。
   - パターンの文字のASCIIコードを取得し、`skip_table`の対応するインデックスにスキップ値を設定します。スキップ値は、パターンの長さから現在の文字のインデックス`i`を引いてから、さらに1を引いた値になります。これにより、検索中に不一致が発生した際に、どれだけの文字をスキップするかが決定されます。

4. 完成した`skip_table`を返します。

`build_skip_table`関数によって、検索アルゴリズムが効率的に実行されるためのスキップテーブルが生成されます。このスキップテーブルは、`boyer_moore_search`関数内で使用され、不一致が発生した際にどれだけの文字をスキップするかを助けることで、検索プロセスを高速化します。