N,X = map(int, input().split())
L = list(map(int, input().split()))
ans = 1
tmp = 0

for i in L:
    tmp += i
    if tmp <= X:
        ans += 1


print(ans)