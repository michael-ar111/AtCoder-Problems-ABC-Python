def isAc(S):
    
    if S[0] != "A":
        return False
    
    if S[2:-1].count("C") != 1:
        return False

    if sum(map(str.isupper,S)) != 2:
        return False
    
    return True


print("AC" if isAc(str(input())) else "WA")

# 別解
# S = str(input())
#
# if S[0] == "A" and 1 == S[2:-1].count("C"):
#     S = S.replace("A","")
#     S = S.replace("C","")
#     if S.islower():
#         print("AC")
#     else:
#         print("WA")
# #何も出力されないケースを入れていない為WAとなる。
# else:
#     print("WA")