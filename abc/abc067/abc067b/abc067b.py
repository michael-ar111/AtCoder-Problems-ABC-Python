N,K = map(int,input().split())
I = list(map(int,input().split()))

I.sort(reverse=True)

ans = 0
for i in range(K):
    ans += I[i]

print(ans)