import math

N,D = map(int,input().split())

# 距離計算用の2次元配列
l = []
for i in range(N):
    l.append(list(map(int,input().split())))

ans = 0

for i in range(N):
    # 前後の座標を計算するため。
    for j in range(i+1,N):

        # 距離の計算
        a = 0
        #iが全体のN,jが一つさきのi+1。kはNとi+1の全探索。
        for k in range(D):
            #前後の座標計算
            a+=pow(l[i][k]-l[j][k],2)

        #平方根に変更
        a=math.sqrt(a)

        #整数の判定
        b = int(a)
        if b==a:
            ans += 1


print(ans)