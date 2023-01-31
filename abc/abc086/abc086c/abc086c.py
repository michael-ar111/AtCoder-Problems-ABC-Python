def solve():
    N = int(input())

    #各途中のタイム、x軸、y軸の設定
    tt,xt,yt = 0,0,0

    for i in range(N):
        t,x,y = map(int,input().split())

        #移動先の情報
        T,X,Y = t - tt, abs(x-xt), abs(y-yt)

        #TよりX+Yが大きければ辿り着けない。
        if T < X+Y:
            return False
        
        #パリティ（偶数奇数が揃っていないと進めない。）
        if T % 2 != (X+Y) % 2:
            return False
        
        #前回情報を更新
        tt,xt,yt = T,X,Y

    return True


print("Yes" if solve() else "No")