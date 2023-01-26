N = int(input())
all_styles = {}
count = 0

for i in range(N):
    s_letters = str(sorted(input()))

    #all_stylesの入力された文字列が存在するか。
    if s_letters in all_styles:
        #1つ目が存在したら、1加算。2以降は複数存在した分だけ加算される。1,3,4,5という順。
        count+=all_styles[s_letters]
        #1つ目が存在したことになり、存在は2のvalueになる。次は3になる。..
        all_styles[s_letters]+=1
    else:
        #存在しなければ、その文字列のvalueとなる。
        all_styles[s_letters] = 1

print(count)