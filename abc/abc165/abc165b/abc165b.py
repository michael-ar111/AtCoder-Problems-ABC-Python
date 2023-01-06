X = int(input())
yokin = 100

for i in range(X+1):
    #iは0からスタートするため
    if (yokin >= X):
        print(i)
        break

    #= yokin * 1.01は小数点が切り捨てにならない。
    yokin += yokin // 100
