# from re import RegexFlag

# # S = input()
# S = "0x8"
# isStr = RegexFlag.search('[a-z]',S)

# if isStr:
#     print("error")
# else:
#     print(int(S)*2)

S = input()

try:
    print(int(S)*2)
except:
    print("error")