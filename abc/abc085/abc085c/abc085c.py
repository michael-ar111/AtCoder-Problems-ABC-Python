N,Y = map(int,input().split())

#1万円の枚数
for i in range(N+1):
    #5千円の枚数
    for j in range(N+1):
        #1万円と5千円の枚数を引いた1千円の数。
        z = N -i -j
        if 0 <= z <= 2000 and i*10000 + j*5000 + 1000*z == Y:
            print(i,j,z)
            exit()
        else:
            continue

print(-1,-1,-1)