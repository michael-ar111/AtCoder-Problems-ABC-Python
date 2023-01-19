P = list(map(int,input().split()))

ans = ""

for i in P:
    ans += chr(97 + (i - 1))

print(ans)