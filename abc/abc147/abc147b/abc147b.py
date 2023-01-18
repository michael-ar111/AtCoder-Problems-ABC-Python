S = str(input())

ans = 0

L = int(len(S))
I = len(S)//2
for i in range(I):
    if S[i] != S[L - 1 -i]:
        ans += 1

print(ans)