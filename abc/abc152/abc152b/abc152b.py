a,b = map(str,input().split())
aConvert = ""
bConvert = ""
ans =""

for i in range(int(b)):
    aConvert += a

for i in range(int(a)):
    bConvert += b

# minは辞書的に小さい文字の判定ができる(3333,444だったら、3333がansに格納)
ans = min(aConvert,bConvert)

print(ans)