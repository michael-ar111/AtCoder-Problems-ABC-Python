S,T = map(int,input().split())

ans = 0

# a+b+c <= Sは下記の3重ループで実現
# Sが5なら、iが0を含めて5回。jの二つ目のループはiが0の時はjは5回だが、iが1のときは4回となる。
for i in range(S+1):
    for j in range(S+1-i):
        for k in range(S+1-i-j):
            if i*j*k <= T:
                ans += 1

print(ans)
