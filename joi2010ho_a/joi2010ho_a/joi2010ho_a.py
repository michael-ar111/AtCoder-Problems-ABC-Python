#n宿泊個数、m旅の日数
n,m = map(int, input().split())
#nの数だけ配列0の初期化
sm = [0 for i in range(n)]
#nの配列に累積和計算
for i in range(n - 1):
  sm[i + 1] = sm[i] + int(input())
pos = 0; ans = 0

#mの回数繰り返す
for i in range(m):
  #移動地点
  move = int(input())
  #移動前後の累積和距離
  ans += abs(sm[pos + move] - sm[pos])
  pos += move
#絶対値をもとめるため
print(ans % 100000)