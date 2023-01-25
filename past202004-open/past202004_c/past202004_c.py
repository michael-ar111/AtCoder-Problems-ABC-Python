N = int(input())
#リストでないと実施不可だった。各要素[".","#"]とするため、listでないと[".#"]となる。
S = [list("...") for _ in range(N)]

ans = []


#N-2から引いた数から-1ずつ引いていく。-1まで、つまり0を実施して終了。
for i in range(N-2, -1, -1):
    #
    for j in range(2*N-1):
        if S[i][j] == "#":
            #ここの理解が必要！
            if S[i+1][j-1] == "X" or S[i+1][j] == "X" or S[i+1][j+1] == "X":
                S[i][j] = "X"

#ここの理解が必要！
for t in S: print("".join(t))

# for i in range(N):
#     ans[i] = "".join(S[i])
#     print(ans[i])