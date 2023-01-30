n, m = map(int, input().split())
# グラフの実装
# 連想配列
G = [[] for i in range(n)]
for i in range(m):
    u,v = map(int, input().split())
    u -= 1
    v -= 1
    # u,vの位置の配列に値をいれる。appendの値は何でもいい。最終的な個数を出力するため。
    G[u].append(v)
    G[v].append(u)
for i in range(n):
    print(len(G[i]))
