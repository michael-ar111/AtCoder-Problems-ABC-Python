O = str(input())
E = str(input())

ans = ""

for i in range(len(O)):

    # OがE以上になる。そのため、インデックスを超える場合はOのみansに追加
    if i >= len(E):
        ans += O[i]
    else:
        ans += O[i] + E[i]


print(ans)