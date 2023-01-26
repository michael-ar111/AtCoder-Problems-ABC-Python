N = int(input())
d = list(int(input()) for i in range(N))

ans = 0
d.sort(reverse=True)

for i in range(N):
    if i == 0:
        ans += 1
    elif d[i] < d[i-1]:
        ans += 1

print(ans)