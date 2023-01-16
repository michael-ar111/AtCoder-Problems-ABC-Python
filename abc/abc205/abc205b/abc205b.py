N = int(input())
A = list(map(int,input().split()))

A = set(A)

if N == len(A):
    print("Yes")
else:
    print("No")