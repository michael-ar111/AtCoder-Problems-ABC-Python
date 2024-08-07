A,B = map(int, input().split())
cnt_minus = 0
if A < 0 and B < 0:
    #負の場合の範囲
    cnt_minus = abs(A - B) + 1

#0の場合
if (A < 0 and B > 0) or A == 0 or B == 0:
    print('Zero')
#負が奇数の場合
elif(cnt_minus % 2 != 0):
    print('Negative')
#負が偶数の場合
elif(cnt_minus % 2 == 0):
    print('Positive')
