#Nの入力値
N = int(input())

#Nの回数分、aの入力リスト
a = [int(input())-1 for i in range(N)]

#aのポジション管理
pos = 0

#posが2に到着すれば
goal = False

for i in range(N):
 
 #aの現在地を次の現在地を代入
 pos = a[pos]

 # posが目標位置に達成すれば
 if pos == 1:
  goal = True
  print(i+1)
  break

# posが目標位置に達成されなければ
if not(goal):
  print(-1)