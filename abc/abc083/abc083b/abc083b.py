# 整数n桁の和を求める関数
def calc_sum_digit(N):
    sumDigit = 0
    while N > 0:
        #10で割れなければ一桁を足す。
        sumDigit += N % 10
        #Nを桁数を一桁目を削除。1桁だけになったら0を返す。
        N //= 10
    return sumDigit

N,A,B = map(int,input().split())

result = 0

for i in range(1, N+1):

    #整数N桁の和がA以上、B以下の場合
    if A <= calc_sum_digit(i) <=B:
        result += i

print(result)
