#hが行、wが列
h,w = map(int, input().split())
a = [""] * h
for i in range(h):
    a[i] = input()


row = [False] * h #行
col = [False] * w #列

#対象の座標が#ならTrueを代入
for i in range(h):
    for j in range(w):
        #hが行。つまり、i番目を回しているときは、h行の判定全てをする。２つ目のjはwなので、その行目の列全てを判定している。
        #iが1回目：i=0,j=0,1と、一番上から列の全てを実施する。
        #iが2回目：i=1,j=0,1と、二番目の列全てを実施する。
        #列観点でなく、行観点では1つしかjのループ中はiは一回しか変更点がない。
        if a[i][j] == "#":
            row[i] = True
            col[j] = True


for i in range(h):
    #行rowループがあり、そのなかに列colループがある。行rowにFalseがあれば、Falseが存在しない。col列にFalseがあれば、列が存在しない。
    if row[i]:
        for j in range(w):
            if col[j]:
                print(a[i][j], end="")
        print()