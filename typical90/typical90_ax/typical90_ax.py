N,L = map(int,input().split())
mod = 10**9 + 7
#dp用の配列初期化
dp = [0] * (N+1)
#最初の値に1を代入
dp[0] = 1

for i in range(1 , N+1):
    # 1つ前の何通りかを代入（最初は1段しかないため1通り）
    dp[i] = dp[i-1]
    # L段はi以下でないと移動不可
    if i >= L:
        #i-L段目の移動した通りを加算
        dp[i] += dp[i-L]
    #制約条件で1000000007で割った余りをつめる
    dp[i] %= mod

print(dp[N])