N,M = map(int,input().split())
store = [list(map(int,input().split())) for i in range(N)]

store.sort()

answer = 0
i = 0
while True:
    #昇順にしたドリンクの値段を1本分加算する。
    answer += store[i][0]
    #M本欲しいとのことでそこから1本減ることになる。
    M -= 1
    #M本が達成していたら、ループ終了。
    if M == 0:
        break
    #storeの最大買える本数から-1する。
    store[i][1] -= 1
    #最大買える本数が0か判定。最大まで買えていたら、次の連想配列を探索のためインクリメント。
    if store[i][1] == 0:
        i += 1

print(answer)

