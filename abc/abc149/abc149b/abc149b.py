a,b,k = map(int,input().split())

#a-kでaの残り、マイナスなら0。
ans_a = max(0, a-k)
#k-aで残りのk回をカウント。マイナスなら0をbから引く。マイナスならb。
ans_b = max(0, b-max(0,k-a))

print(ans_a,ans_b)