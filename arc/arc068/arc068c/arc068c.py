N = int(input())
#Nを11(5,6)で1ペアの商として、2回回すこととする
ans = (N // 11)*2
#ansに加算する値のための剰余
x = N % 11

#ans後に回す必要ない場合0
if x == 0:
    pass
#ans後に回した数が6の場合
elif x <= 6:
    ans += 1
#ans後に回した数が5の場合
else:
    ans +=2

print(ans)