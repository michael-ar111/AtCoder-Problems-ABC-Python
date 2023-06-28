N = int(input())
#2次元の配列を2つ作成する。
S = [[0] * (N+1) for _ in range(2)]

for i in range(N):
    c,p = map(int, input().split())
    #2次元の配列を1か2に値を代入する。
    S[c - 1][i + 1] = p

# 累積和をとる。
for i in range(2):
    tmp = 0
    for j in range(1,N+1):
        tmp += S[i][j] 
        S[i][j] = tmp

Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())
    #クラス1と2のl番目、r番目の累積和
    a = S[0][r] - S[0][l-1]
    b = S[1][r] - S[1][l-1]
    print(a, b)

