N = int(input())
#リストでないと実施不可だった。各要素[".","#"]とするため、listでないと[".#"]となる。
S = [list(input()) for _ in range(N)]

#N-2から引いた数から-1ずつ引いていく。-1まで、つまり0を実施して終了。
for i in range(N-2, -1, -1):
    for j in range(2*N-1):
        if S[i][j] == "#":
            #i+1 一つ下の、j-1で左。i+1 一つ下の、jで真ん中。i+1 一つ下の、j+1で右。
            if S[i+1][j-1] == "X" or S[i+1][j] == "X" or S[i+1][j+1] == "X":
                S[i][j] = "X"

#連想配列として渡して、一つの配列は一つjoinで一つの文字列。連想配列で2つ目に改行。
for t in S: print("".join(t))
