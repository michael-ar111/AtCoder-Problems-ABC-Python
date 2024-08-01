# 素数判定関数
def is_prime(n):
    # 0,1は素数とする
    if n == 0 or n == 1:
        return False
    if n == 2:
        return True

    #nは偶数でなく、3以降奇数の判定処理
    i = 2
    #平方根かの分岐。ある数 n が合成数（つまり、素数ではない）である場合、その約数の少なくとも一方は n の平方根以下
    while i * i <= n:
        #割り切れれば、合成数の約数のため素数でない
        if n % i == 0:
            return False
        i += 1
    return True

# sに100000までの素数判定を格納
s = []
for i in range(1, 10 ** 5 + 1):
    if is_prime(i) and is_prime((i + 1) // 2):
        s.append(1)
    else:
        s.append(0)

# cumsumに素数の累積和を格納
cumsum = [0] * (10 ** 5 + 1)
for i in range(1, 10 ** 5 + 1):
    cumsum[i] = cumsum[i - 1] + s[i - 1]

q = int(input())
l, r = [], []
for i in range(q):
    li, ri = map(int, input().split())
    l.append(li)
    r.append(ri)

    print(cumsum[r[i]] - cumsum[l[i] - 1])
