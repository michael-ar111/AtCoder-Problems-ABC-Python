a = [list(map(int,input().split())) for _ in range(3)]
n = int(input())
b = list(int(input())  for _ in range(n))


#行のループ
for i in range(3):
    #列のループ
    for j in range(3):
        #b(n)のループ
        for k in range(n):
            #a[i][j]の時に、bの全ての値と判定する。あっていれば0を代入する。
            if a[i][j] == b[k]:
                a[i][j] = 0


ans = "No"

for i in range(3):
    #各行の判定
    if a[i][0] + a[i][1] + a[i][2] == 0:
        ans = "Yes"
    #各列の判定    
    if a[0][i] + a[1][i] + a[2][i] == 0:
        ans = "Yes"

#右斜めの判定
if a[0][0] + a[1][1] + a[2][2] == 0:
    ans = "Yes"

#左斜めの判定
if a[0][2] + a[1][1] + a[2][0] == 0:
    ans = "Yes"

print(ans)