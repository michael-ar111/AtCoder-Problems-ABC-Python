N = int(input())

FizzBuzz = 0

for i in range(N+1):
    #両方ともTRUEの場合。つまり,3で割り切れない、5で割り切れない場合の時だけ加算する。
    if i % 3 != 0 and i % 5 != 0:
        FizzBuzz += i


print(FizzBuzz)
