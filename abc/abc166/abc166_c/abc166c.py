N,M = map(int, input().split())
H = list(map(int, input().split()))

# N個分の展望台初期値をTrueとして代入
good = [True]*N

# M本の道が存在する
for i in range(M):
 A,B = map(int, input().split())
 A -= 1
 B -= 1
 # A基準に隣の値が以下、イコールの場合False
 if H[A] >= H[B]:
   good[B] = False
 # B基準に隣の値が以下、イコールの場合False
 if H[A] <= H[B]:
   good[A] = False

print(sum(good))