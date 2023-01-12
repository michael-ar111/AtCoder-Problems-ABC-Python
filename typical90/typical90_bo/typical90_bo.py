def decimalNumber(n):

    if n == 0:
        return 0

    # 10進数に変換
    convertTen = int(str(n),8)

    convertNine = ""

    while convertTen:
        #9進法に変換
        convertNine = str(convertTen%9) + convertNine
        convertTen = convertTen // 9

    #8を5に変換
    convertNine = convertNine.replace("8","5")

    return int(convertNine)


N,K = map(int,input().split())
ans = N

for i in range(K):
    ans = decimalNumber(ans)

print(ans)