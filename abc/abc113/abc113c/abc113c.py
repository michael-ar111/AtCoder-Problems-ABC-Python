N,M = map(int,input().split())
#各市を県ごとに入れるための連想配列
ken = [[] for _ in range(N+1)]
#答えを出力するための配列
ans = ["" for i in range(M)]

for i in range(M):
    p, y =map(int,input().split())
    #県ごとに入れるから、[p]にappendする。Pが県の配列、yが誕生年、iはPの中の配列番号
    #pは少なくとも1以上が格納。そのため、enumerate(ken)で0から始めても中に入っているfor j, city ...が実行されなく1から始まる。
    #以下のイメージ

    #1: [ [(28,0),(32,1),(37,2)]
    #2:   [(24,0),(35,1),(40,2)]
    #3:   [(30,0),(40,1),(45,2)] ]
    ken[p].append((y,i))

for p,k in enumerate(ken):
    #sortでなく、sort()でないとソートされない。
    #[(0,30),(1,19),(2,20)]→#[(30,0),(20,2),(19,1)]これだ。
    #各県の連想配列#1から順に実施。Pが#1,#2,#3
    k.sort()
    #enumerateのj,cityならjにインデックスの開始値1が入り、cityにkが入る。
    for j,city in enumerate(k,1):
        #iが県の中の市の番号。yはソートの為だけで、ここでは使用しない。
        #jは市の中で何番目にできたか。
        y,i = city
        #pが県の番号、jは市の中で何番目かに誕生したか。
        #zfillで6桁で0埋め。
        ans[i] = str(p).zfill(6) + str(j).zfill(6)
 
for a in ans:
    print(a)