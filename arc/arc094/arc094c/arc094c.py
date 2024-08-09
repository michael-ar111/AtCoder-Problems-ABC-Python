A, B, C = map(int, input().split())

#最大値を取得    
max_val = max(A, B, C)

#最大値から各値を引く
dA = max_val - A
dB = max_val - B
dC = max_val - C

#トータルの最低加算回数（偶数奇数を含む）
total_diff = dA + dB + dC

if total_diff % 2 == 0:
    #トータルの最低加算回数（偶数）
    print(total_diff // 2)
else:
    #トータルの最低加算回数（奇数）
    print(total_diff // 2 + 2)