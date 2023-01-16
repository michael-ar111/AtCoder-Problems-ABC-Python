N = int(input())

T,A = map(int,input().split())
H = list(map(int,input().split()))

ans = 0
dmin = 1000

for i in range(len(H)):
    tmp = T - H[i] * 0.006
    #気温差の絶対値が小さい温度と比較する。-と-は合算しておおきな絶対値を返す。
    tmpmin = abs(A - tmp)
    if dmin >= tmpmin:
        dmin = tmpmin
        ans = i

print (ans + 1)