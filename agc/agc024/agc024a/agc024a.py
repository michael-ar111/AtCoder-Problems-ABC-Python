A,B,C,K = map(int,input().split())
#周期生
#Kが奇数の時A-Bの1になる。#Kが偶数の時B-Aの-1になる。
print(A-B if K%2 == 0 else B-A) 
