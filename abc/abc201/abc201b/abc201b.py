N = int(input())

data = []
for i in range(N):
    S,T = map(str,input().split())
    T = int(T)
    data.append([T,S])

#ソートは一つ目の値Tを優先しソートする。
data.sort(reverse=True)

#リストとして[]、配列として[]Sを取得
print(data[1][1])