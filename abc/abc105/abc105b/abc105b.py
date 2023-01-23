N = int(input())

ans = "No"

for i in range(N):
    for j in range(N):
        if N == i*4 + j*7:
            ans = "Yes"


print(ans)
