N = int(input())
S = input()
min_turn = 1000000
sum_W = [0]

for i in range(0, N):
    if S[i] == 'W':
        #W基準で各リーダーが入り次第のカウントあり
        sum_W.append(sum_W[i] + 1)
    else:
        #W基準で各リーダーが入り次第のカウントなし
        sum_W.append(sum_W[i])


for i in range(0,N):
    w = sum_W[i]
    # リーダーがi番目に入った時のNの数、sum_Wの最後のカウントまでからi番目のsum_Wカウント時の次の数を引いた数。
    # つまり、リーダーが入った後のリーダーに向いてない数。
    # wはリーダーが入る前で向いていない数。
    e = (N - 1 - i) - (sum_W[N] - sum_W[i + 1])
    turn = w + e
    min_turn = min(turn, min_turn)

print(min_turn)