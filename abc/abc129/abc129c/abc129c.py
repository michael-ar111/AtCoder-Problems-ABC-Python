N,M = map(int,input().split())
# 床が壊れている箇所を集合型で持つ
broken = set(int(input()) for _ in range(M))
MOD = 1000000007 

# N回分（0からスタートのため+1）
dp = [0] * (N + 1)
# 0は最初の段で1通り
dp[0] = 1

for i in range(1, N+1):
    #床が壊れている箇所を飛ばす
    if i not in broken:
        # 1段飛ばしの場合（1段前を入れる）
        dp[i] = dp[i-1]
        if i > 1:
            # 2段飛ばしの場合（2段前を入れる）。1段目の場合はスキップ。
            dp[i] += dp[i-2]
        dp[i] %= MOD

print(dp[N])