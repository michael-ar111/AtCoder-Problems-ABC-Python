n,m = map(int,input().split())
dict={}

for i in range(m):
 a,b = map(int,input().split())
 #dict内にa,bの大きな値が存在しないこと
 if not max(a,b) in dict:
  #aとbの大きいdictに対して、a,bの小さい値を入れる
  dict[max(a,b)] = min(a,b)
 else:
  #dictにa,bの大きあ値が存在すれば、aとbの大きいdictに対して0を代入。
  dict[max(a,b)] = 0

ans = 0
for i in dict:
 if dict[i] != 0:
  ans +=1
print(ans)