# python要点まとめ
## 基本文法
### 入力
* 1行入力
> a = input()
> a = int(input())
> a, b = map(int, input().split())
> a = list(map(int, input().split()))
* 複数行入力
### 出力
> print("{}".format(a))
### if
> x = "Even" if (a*b)%2==0 else x = "Odd"
### リスト
> a = []
### 追加
#### append
> a.append("hoge")

#### extend
> l = list(range(3)) # [0, 1, 2]
> l.extend([100, 101, 102]) # [0, 1, 2, 100, 101, 102]

#### insert
> l = list(range(3))
> l.insert(0, 100) # [100, 0, 1, 2]

#### スライス
> l = list(range(3))
> l[1:1] = [100, 200, 300] # [0, 100, 200, 300, 1, 2]

### 削除
#### clear
> l = list(range(10))
> l.clear() # []

#### pop
> l = list(range(10))
> l.pop(0) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
> l.pop(3) # [1, 2, 3, 5, 6, 7, 8, 9]
> l.pop(-2) # [1, 2, 3, 5, 6, 7, 9]
> l.pop() # [1, 2, 3, 5, 6, 7]

#### remove
> l = ['Alice', 'Bob', 'Charlie', 'Bob', 'Dave']
> l.remove('Alice') # ['Bob', 'Charlie', 'Bob', 'Dave']

#### リスト内包表記
> l = list(range(10))
> print([i for i in l if i % 2 == 0]) # [0, 2, 4, 6, 8]

## アルゴリズム
### for文を使用した全探索
for文を使用し，リストの中身をすべて調べる
> for i in range(len(list)):
>   # 具体的な処理を記入

### 整数の10進法表記
各桁の和を求めるときなどに使用
> n, sum = 864, 0
> while n > 100
>   sum += n % 10
>   n /= 10
> print(sum) # 18

### バケット法
予め空の（0を代入）リストを用意し，num[i] := 値iが何個あるかを調べる

### 文字列を反転
> str = "abcde"
> str = str[::-1]


## ライブラリ
### count
文字列中に出てくる特定の文字の数を返す
> masu = input() # "101"
> print("{}".format(masu.count("1")))
> 2

### type
変数の型を調べる
> n = 100
> if type(n) is int: # True

### sort
リストの中身を昇順に並び替える
> a = [1, 3, 5, 2, 4]
> a.sort() # [1, 2, 3, 4, 5]
> a.sort(reverse=True) # [5, 4, 3, 2, 1]