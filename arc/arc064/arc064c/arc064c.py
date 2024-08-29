N,x = map(int,input().split())
a = list(map(int,input().split()))

reuslt = 0

#初回の数列にxとの差分resultに詰めてxを代入
if a[0] > x:
    reuslt += a[0]-x
    a[0] = x

#初回以降をチェック
for i in range(N-1):
    #　隣同士がxよりも大きければ
    if x <  a[i] +  a[i+1]:
        #　隣同士をxから引いて結果に追加
        reuslt += a[i] + a[i+1] - x
        #　隣同士の右側にx-左側の値を代入
        a[i+1] = x - a[i]

print(reuslt)