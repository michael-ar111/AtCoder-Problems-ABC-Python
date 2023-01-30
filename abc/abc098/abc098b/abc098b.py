N = int(input())
S = input()

ans = 0

for i in range(N):
    cnt = 0

    #文字の切り抜き。:iまで切り抜く。
    #文字の切り抜き。:i以降を切り抜く。
    #種類数なためsetで重複部分を削除
    x = set(S[:i])
    y = set(S[i:])

    #x回回して、yに何個ふくまれているかカウント。
    for j in x:
        if j in y:
            cnt += 1
    
    #区切った部分で一番多い部分をans
    ans = max(ans,cnt)

print(ans)