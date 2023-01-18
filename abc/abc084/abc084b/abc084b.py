def isYes(A,B,S):
    if S[0:A].count("-") != 0:
        return False
    
    if S[-B].count("-") != 0:
        return False

    if S.count("-") != 1:
        return False

    return True


A,B = map(int,input().split())
S = input()

print("Yes" if isYes(A,B,S) else "No")