# 文字列の個数
N = int(input())

# T, c1, c2, c3を求める
T, c1, c2, c3 = 0,0,0,0

for i in range(N):
#文字列の入力
 S = input()

 T += S.count("AB")

 # パターン 1
 if S[0] == "B" and S[-1] == "A":
  c1 += 1
 # パターン 2
 elif S[-1] == "A":
  c2 += 1
 # パターン 3
 elif S[0] == "B":
  c3 += 1

# c2, c3の値に応じて出力
if c2 == 0 and c3 == 0:
  print(T + max(c1 -1 ,0))
else:
  print(T + c1 + min(c2,c3))