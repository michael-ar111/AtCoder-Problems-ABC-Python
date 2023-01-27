X = int(input())

ans = 0

for i in range(1,X+1):
    #1の冪乗は除外する。
    for j in range(2,11):

        if ans < i**j <=X:
            ans = i**j


print(ans)