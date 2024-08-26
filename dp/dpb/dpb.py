N,K = map(int,input().split())
H = list(map(int,input().split()))

#dpの仮の値無限を代入
INF = 1001001001
dp = [INF] * N
#初期は移動不要のため0
dp[0] = 0

#1からNまでの移動コスト
for i in range(1,N):
    tmp = []
    #iの移動までに各K分前のコストがいくらかになるか。-はないため0を最大
    for j in range(max(0,i-K),i):
        #各K分前のコストで一番低いものをdp[i]に格納
        tmp.append(dp[j] + abs(H[i] - H[j]))
    
    dp[i] = min(tmp)


#結果の出力
print(dp[N-1])