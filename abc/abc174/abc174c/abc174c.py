K = int(input())

base = 7

for i in range(K+1):
    if base % K == 0:
        print(i+1)
        exit()
    base = (base * 10 + 7) % K

print(-1)