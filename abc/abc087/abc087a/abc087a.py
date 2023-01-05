X = int(input())
A = int(input())
B = int(input())
Z = X - A
if Z <= B:
    print(0)
else:
    print(Z - B*(Z // B))
