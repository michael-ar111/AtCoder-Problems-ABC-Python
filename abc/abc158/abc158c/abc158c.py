from math import floor

A,B = map(int, input().split())

ans = -1

for i in range(1000):
    if floor(i * 0.08) == A and floor(i * 0.10) == B:
        ans = i
        break

print(ans)