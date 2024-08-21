N = int(input())
a = list(map(int,input().split()))

#a1,a2...の合計とその数分引く
ans = sum(a) - N
print(ans)