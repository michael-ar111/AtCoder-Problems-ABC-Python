a,b,c,k = map(int,input().split())


if k <= a:
    #a以下なら、k回数分
    print(k)
elif k <= a+b:
    #a+b以下なら、a回数分
    print(a)
else:
    #上記以外ならaからk-(a+b)引いた回数分となる
    print(a - (k -(a+b)))