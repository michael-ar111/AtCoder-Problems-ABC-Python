N, Q = map(int,input().split())
#N個分[set(),set(),set()..]ができる。
G = [set() for i in range(N+1)]

for i in range(Q):
    #パターン1は[1,2,3]ならs=1 a = [2,3]
    s, *a = map(int, input().split())
    #パターン1:aがbをフォローする
    if s == 1:
     G[a[0]].add(a[1])
    #パターン2:フォロー返し
    elif s == 2:
     for j in range(1, N+1):
       #対象ユーザーがフォローしているか判定
       if a[0] in G[j]:
         #Gの中の*aにあたる数が対象
         G[a[0]].add(j)
    #パターン3:フォローフォロー
    else:
      tmp = []
      #aがフォローしているユーザーをtmpに詰める。
      for k in G[a[0]]:
        tmp.append(k)
      #tmpの分回す
      for t in tmp:
        #tmpフォローがフォローしている、ユーザーをaに追加する。
        for v in G[t]:
          G[a[0]].add(v)


Ans = []
for i in range(1,N+1):
  ans = ""
  for j in range(1,N+1):
    #自分自身はフォローしないためN
    if i==j:
      ans += 'N'
    #j番目にGの値があればYとなる。
    elif j in G[i]:
      ans += 'Y'
    else:
      ans += 'N'
  Ans.append(ans)

for i in range(1,N+1):
  print(Ans[i-1])