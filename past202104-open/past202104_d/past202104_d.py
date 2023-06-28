N,K = map(int,input().split())
A = list(map(int,input().split()))
num = [0]*(N+1)

#累積和の代入。[i+1]でnumの0を飛ばして、累積はN個分格納
for i in range(0,N):
    num[i+1]=num[i]+A[i]

#K番目以降の累積和出力
for i in range(N-K+1):
    print(num[i+K]-num[i])