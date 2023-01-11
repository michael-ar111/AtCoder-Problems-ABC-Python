N = int(input())

count = 1

#2で割り切れる数だけをNまで繰り返す。
while count*2 <= N:
        count *=2

print(count)
