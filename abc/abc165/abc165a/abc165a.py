K = int(input())
A,B = map(int,input().split())
check = False

# B+1をしないとB未満となる。1,5なら、1,2,3,4となる。
for i in range(A,B+1):
    if i % K == 0:
        check = True


if check == True:
    print("OK")
else:
    print("NG")
