S = input()
T = input()

ans = False

for i in range(len(S)):
    if S == T:
        ans = True
        break
    else:
        S = S[-1] + S[:len(S)-1]

if ans:
    print("Yes")
else:
    print("No")