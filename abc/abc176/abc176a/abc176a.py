N,X,T = map(int,input().split())
#N個達成するまでにはX分から-1を足す。そしてXで割る。
time = (N + X - 1) // X
print(time * T)