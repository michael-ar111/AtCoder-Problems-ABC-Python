def count_patties(L, X):
    # 各レベルのバーガーの層数とパティ数を事前計算
    # listが1つ以上存在する
    layers = [1]
    patties = [1]
    for i in range(1, L+1):
        #各層の事前の項目に対して2の乗算をし、+3
        layers.append(layers[-1] * 2 + 3)
        #各パティの事前の項目に対して2の乗算をし、+1
        patties.append(patties[-1] * 2 + 1)

    def recursive_count(level, x):
        #バーガーが0で0より大きければ、1、でなければ0        
        if level == 0:
            return 1 if x > 0 else 0
        #N層よりX層が大きければ、N層までのパティを返す
        if x >= layers[level]:
            return patties[level]
        
        #中央の層結果
        mid = (layers[level] + 1) // 2

        #指定された層（x）が中央より下にある場合、下のバーガー内を検索
        if x < mid:
            return recursive_count(level-1, x-1)
        elif x == mid:
        #指定された層（x）が中央（パティがある層）の場合
            return patties[level-1] + 1
        else:
        #指定された層（x）が中央より上にある場合、上半分のバーガーで再帰的に計算
            return patties[level-1] + 1 + recursive_count(level-1, x-mid)

    return recursive_count(L, X)

L, X = map(int, input().split())
result = count_patties(L, X)
print(result)