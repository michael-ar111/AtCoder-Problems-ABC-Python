# N = int(input())

# a = list(map(int, input().split()))
# #N個リストを作成する
# G = [[] for i in range(N)]

# for i in range(1, N):
#     #aのリストを参照し、1なら0とし、appendは適当な値を追加する。aにはプラスの値が入っているので、そこからインデックスの値で参照する。
#     G[a[i - 1] - 1].append(i - 1)

# for i in G:
#     print(len(i))

#20240830:復習
N = int(input())
A = list(map(int, input().split()))

subordinates = [0] * N

#各社員分まわす
for i in A:
    #各社員の一つ上の上司に部下の数を加算
    subordinates[i-1] += 1

#各社員の部下の数を出力
for count in subordinates:
    print(count)