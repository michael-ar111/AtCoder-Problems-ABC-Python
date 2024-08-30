# n, m = map(int, input().split())
# # グラフの実装
# # 連想配列
# G = [[] for i in range(n)]
# for i in range(m):
#     u,v = map(int, input().split())
#     u -= 1
#     v -= 1
#     # u,vの位置の配列に値をいれる。appendの値は何でもいい。最終的な個数を出力するため。
#     G[u].append(v)
#     G[v].append(u)
# for i in range(n):
#     print(len(G[i]))

#20240830:復習
N,M = map(int, input().split())
#各都市間の道路初期化
road_count = [0] * N

for _ in range(M):
    a,b = map(int,input().split())
    #a都市間の道路数加算
    road_count[a - 1] += 1
    #b都市間の道路数加算
    road_count[b - 1] += 1

#各都市の道路数
for count in road_count:
    print(count)