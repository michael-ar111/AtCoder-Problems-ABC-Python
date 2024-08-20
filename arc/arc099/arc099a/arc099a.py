import math

N,K = map(int,input().split())
A = list(map(int,input().split()))

#N-1：最小値(1)を含む要素を除いた要素数
#K-1：1回の操作で変更できる数
ans = math.ceil((N-1) / (K-1))

print(ans)