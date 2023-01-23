N = int(input())
L = list(map(int,input().split()))
# ソートしておけばA<B<Cを見なくていい。
L.sort()

ans = 0

#最後の2つは不要
for i in range(N-2):
    # iからスタート。
    for j in range(i,N-1):
        #長さが等しければスキップ。■■■とあり、N-2が■、N-1が■■の2パターンとなる。
        #iが基準値となり、初回のiとjはとばす。また、jが二回目以降でも同じ値ならとばす。
        #3要素のうち1要素が入った状態で2つ目の全探索
        if L[i] == L[j]:
            continue
        
        #3要素の内、2つが入った状態で、2つ目と3つ目の判定。3つ目は全探索。
        for k in range(j,N):
            #長さが等しければスキップ
            if L[j] == L[k]:
                continue

            # 三角形として成立しているか判定
            if L[i]+L[j] > L[k]:
                ans += 1


print(ans)