#Xは横軸として、Yは縦軸として書き換えています。
H,W,Y,X = map(int,input().split())
S = [input() for _ in range(H)]

#配列でX,Yを参照するため、-1引く。
X -=1 #横
Y -=1 #縦
ans = 1 #XYは#でないため。

#Y列下方向のカウント
#range(1,H - Y)で1行目から。
#range引数1つ目はstart,2つ目はstop（range(1,1)だったら実施しない。）
#0からはスタートしない。カウントアップする。初期のY,Xは除外のため。
for i in range(1,H - Y):
    if S[Y+i][X] == "#":
        break
    ans += 1

#Y列上方向のカウント
#HがY未満、1からY+1回まで続ける理由がわからない。Yを元に
#一つ目の引数を設定するとそこで止まる。つまり、1,4だったら1,2,3しか回らない。
#Yが0なら1,1となりとばすことになる。
for i in range(1,Y + 1):
    if S[Y-i][X] == "#":
        break
    ans += 1

#X列右方向のカウント
for i in range(1,W - X):
    if S[Y][X+i] == "#":
        break
    ans += 1

#X列左方向のカウント
for i in range(1,X + 1):
    if S[Y][X-i] == "#":
        break
    ans += 1

print(ans)