N = int(input())
H = list(map(int,input().split()))
# N = 4
# H = [6,5,6,8]
H1 = H[0]
ans = 0

for i in range(len(H)):
    # print((H[0:1+i]))
    if H[i] >= max(H[0:1+i]):
    # if i >= H1:
        ans += 1


print(ans)