S = input()

ans = S

for i in range(len(S)):
    if i >= 1 and i % 2 == 0:

        if ans[:len(ans)//2] == ans[len(ans)//2:]:
            print(len(ans))
            break
        else:
            ans = ans[:len(ans)-1]
    
    else:
        ans = ans[:len(ans)-1]