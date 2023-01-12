k = int(input())

a, b = map(int,input().split())

#kは基数を表す。a,bの基数が整数のintとなる。
a_10 = int(str(a),k)
b_10 = int(str(b),k)

ans = a_10 * b_10

print(ans)