#座標の差分判定用の配列
#0:下、1:右、2：上、3：左、4：右下、5：右上、6：左上、7：左下
HD = [1,0,-1,0,1,-1,-1,1]
WD = [0,1,0,-1,1,1,-1,-1]

# 入力
H,W = map(int,input().split())
S = [input() for i in range(H)]


# Python3ではstr型変数の各文字の書き換えはできない(immutabilityなため不変)
# 答えを表す二次元配列を別途用意する（','のところは0とする）
result = [[0 if v == '.' else "#" for v in row]for row in S]

#  各マス（i,j）を順に処理
for i in range(H):
    for j in range(W):

        # 空きマス以外はそのままにする。#については処理をとばす。
        if S[i][j] != '.':
            continue

        #周囲HW,WD（0:下、1:右、2：上、3：左、4：右下、5：右上、6：左上、7：左下）を探索
        for hd,wd in zip(HD,WD):
            #i,jが各マス。i,jの周囲のマスがhdとwdを追加したni,nd
            ni,nj = i + hd, j + wd

            # マス（niがH以上はない。ndがW以上ない。またniとndが0未満になる場合は処理をとばす。
            if ni < 0 or ni >= H or nj < 0 or nj >= W:
                continue

            #対象マスの周囲に#があれば加算する
            if S[ni][nj] == "#":
                result[i][j] += 1

for row in result:
    #*配列を全て出力、sep=""で不要な余白を削除
    print(*row, sep="")