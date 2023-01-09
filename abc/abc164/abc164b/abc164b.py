import math
A,B,C,D = map(int,input().split())

E = math.ceil(A/D)
F = math.ceil(C/B)

if E >= F:
    print("Yes")
else:
    print("No")