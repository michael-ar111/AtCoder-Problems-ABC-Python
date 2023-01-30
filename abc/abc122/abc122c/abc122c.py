N,Q = map(int,input().split())
S = input()

CS = [0]* (N+1)

for i in range(1,N):
    # Trueの時はCS[i]に1を加算となる。
    CS[i + 1] = CS[i] + (S[i - 1:i + 1] == "AC")

for q in range(Q):

    l,r = map(int,input().split())

    l -= 1

    #l,rでl以降となるので、lまでの数をrから引くことでlr内の累積和となる。
    print(CS[r] - CS[l+1])

