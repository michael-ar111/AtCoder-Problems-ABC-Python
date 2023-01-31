N = int(input())
*A, = map(int, input().split())
B = {}
s = 0
ans = 0
B[0] = 1
for a in A:
    s += a
    #getで値があれば、それを返す。なければNoneだが、引数が0のように設定していれば、0を返す。+と-が関係なく値で判定している。
    ans += B.get(s, 0)
    #キーがなければ0とプラス1の合計1を返す。キーがなければ累積和,1となる。
    B[s] = B.get(s, 0) + 1
print(ans)