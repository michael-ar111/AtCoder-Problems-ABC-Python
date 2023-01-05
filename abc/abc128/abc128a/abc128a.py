A,P = map(int,input().split())

X = P + (A * 3)
if X <= 2:
    print(0)
else:
    print(X // 2)