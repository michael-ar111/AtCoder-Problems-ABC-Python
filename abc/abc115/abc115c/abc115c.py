N,K = map(int,input().split())
hhh = [int(input()) for i in range(N)]
hhh.sort()
#float('inf')で無限大という意味になる。
ans = float('inf')

#NからK個の整数を選ぶ。パターン的にはN-K+1パターンで十分となる。
for i in range(N-K+1):
    
    #hminを固定すると、hmaxが決まる。
    ans = min(ans,hhh[i+K-1] - hhh[i])

print(ans)