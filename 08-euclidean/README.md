# ユークリッドの互除法について

ユークリッドの互除法は、2つの整数の最大公約数を求めるためのアルゴリズムです。

## 基本アルゴリズム

2つの整数 `a` と `b` を取り、 `a` を `b` で割った余りを `r` とすると、 `a` と `b` の最大公約数は、 `b` と `r` の最大公約数と同じであるということです。これを繰り返して、余りが 0 になるまで割り続けます。最後に、割り切れた値が最大公約数となります。

## 具体例

例えば、`a=1071`、 `b=462` の場合を考えます。最初に `1071` を `462` で割ると、余りは `147` となります。次に、 `462` を `147` で割ると、余りは `21` となります。さらに、 `147` を `21` で割ると、余りは `0` となります。この場合、最大公約数は `21` となります。

## 応用例

ユークリッドの互除法は、数学や暗号学などの分野で広く使用されています。また、2つの数の最大公約数を求めるだけでなく、最小公倍数を求めることもできます。ユークリッドの互除法は、2つの整数の大きさに依存せず、非常に効率的に動作します。