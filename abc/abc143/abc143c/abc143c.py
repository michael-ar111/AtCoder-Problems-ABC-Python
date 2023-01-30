N = int(input())
S = input()

ans = 1
i = 0


while True:
    if i == N-1:
        break

    if not S[i] == S[i+1]:
        ans += 1
    
    i += 1


print(ans)