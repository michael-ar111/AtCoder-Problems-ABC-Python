S = input()

ans = 0
count = 0

for i in S:
    #文字列にSが含まれているか
    if i == 'B':
        count +=1
    else:
    #含まれていなければ、カウントした部分までをansに追加
        ans += count

print(ans)