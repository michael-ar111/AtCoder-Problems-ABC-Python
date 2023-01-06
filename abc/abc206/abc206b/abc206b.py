N = int(input())
count = 0

for i in range(N+1):
    count += i
    if (count >= N):
        print(i)
        break
