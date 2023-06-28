N = int(input())
A = list(map(int, input().split()))

# サイズNの配列A N分の[0][0]..作成
S = [0] * (N+1)
for i in range(N):
    #Sの1から順にAの値を累積和を代入
    S[i+1] = S[i] + A[i]

C = []
D = []

for k in range(1,N+1):
    for i in range(N+1-k):
        #Sは累積和の配列。S[i+k]-S[i]により、i番目からi+k番目までの要素の和。
        #つまり、Aのi番目からi+k番目までの連続した部分配列の和
        C.append(S[i+k]-S[i])
    D.append(max(C))
    # リストの初期化
    C=list()


for i in D:
    print(i)
