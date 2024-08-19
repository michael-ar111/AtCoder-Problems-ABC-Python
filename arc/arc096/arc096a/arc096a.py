def solve(A,B,C,X,Y):
    min_cost = float('inf') # 最小コストの初期値を無限大を設定

    #XYの2倍+1でABピザ分全探索
    for ab in range(max(X,Y) * 2 + 1):
        # ABピザをabマイ買った場合残すと計算
        cost = C * ab

        # 残りのAピザとBピザの必要枚数を計算。マイナスにならないため0
        remain_a =max(0, X - ab//2)
        remain_b =max(0, Y - ab//2)

        # 残りの数のAコスト
        cost += A*remain_a
        # 残りの数のBコスト
        cost += B*remain_b

        # 残りの数のAB,A,Bのコストで一番少ない数を格納
        min_cost = min(min_cost, cost)

    return min_cost


A,B,C,X,Y = map(int, input().split())

print(solve(A,B,C,X,Y))