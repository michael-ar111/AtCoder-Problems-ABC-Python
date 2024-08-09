N = int(input())
A = list(map (int, input().split()))
ans = 0

for i in range(N):
    # 偶数かの判定
    while (A[i] % 2 == 0):
        ans += 1
        # 再度偶数か判定のため
        A[i] //= 2

print(ans)