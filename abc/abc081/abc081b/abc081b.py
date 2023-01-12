N = int(input())
A = list(map(int,input().split()))

ans = 0

#全体をwhileで括るのを忘れていた。
while True:

    can_do = True
    #格桁が2で割れない数があるか判定
    for i in range (N):
        if A[i] % 2 == 1:
            can_do = False
    
    #2桁で割れない数があれば終了。
    if not can_do:
        break

    #2でリストの要素を全て割る
    for i in range(N):
        A[i] = A[i] / 2


    ans += 1


print(ans)