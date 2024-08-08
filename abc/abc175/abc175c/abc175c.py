X,K,D = map(int,input().split())

#現在位置
cur = abs(X)
rem = K

#移動回数(Kよりcur//Dは大きい移動は不可)
cnt = min(cur//D,K)
#移動後の現在位置
cur -= D * cnt
#移動回数を引いた残り回数
rem -= cnt

if rem > 0:
    if rem % 2 == 1:
        #奇数の場合は負の位置に移動する。
        cur = cur - D

ans = abs(cur)
print(ans)