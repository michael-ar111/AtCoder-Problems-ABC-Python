N = int(input())
A = list(map(int,input().split()))

count = {}
#各リストの重複している数のカウント
for a in A:
    count[a] = count.get(a,0)+1

lengths = []
#辞書のitems()でキーと値のペアをイテレータとして返す。l長さ、c回数
for l, c in count.items():
    if c >= 2:
        lengths.append(l)

#降順にソート
lengths = sorted(lengths, reverse=True)

#lenghts内に2つ以上の辺が存在しなければ
if len(lengths) < 2:
    print(0) #長方形はできない
else:
    #lenghts内に4つ以上あるかcountのdictionaryに参照チェック
    if count[lengths[0]] >= 4:
        print(lengths[0] * lengths[0])  #最大の変が4辺の場合
    else:
        print(lengths[0] * lengths[1]) #最大の変が2辺とその次の辺が2辺の場合