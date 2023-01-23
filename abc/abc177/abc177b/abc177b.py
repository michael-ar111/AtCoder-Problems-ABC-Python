T = input()
S = input()
tl = len(T)
sl = len(S)

ans = sl

for i in range(tl-sl+1):
    tmp = 0
    for j in range(sl):
        #iを起点にj回分確認する。
        if T[i+j] != S[j]:
            tmp += 1
    
    ans = min(ans,tmp)

print(ans)