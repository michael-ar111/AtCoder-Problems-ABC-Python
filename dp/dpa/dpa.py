
def min_cost_frog(h,N):
    dp = [0] * N  # DPテーブルを初期化

    for i in range(1, N):
        #現在位置からみて1つ前の移動コスト
        cost_from_previous = dp[i-1] + abs(h[i] - h[i-1])
        dp[i] = cost_from_previous

        # 1番目以降で2つ目の
        if i > 1:
            #現在位置からみて2つ前の移動コスト
            cost_from_two_back = dp[i-2] + abs(h[i] - h[i-2])
            #1つ前の移動コストか2つ前の移動コストか
            dp[i] = min(dp[i], cost_from_two_back)

    return dp[N-1]

N = int(input())
h = list(map(int,input().split()))

min_cost = min_cost_frog(h,N)
print(min_cost)