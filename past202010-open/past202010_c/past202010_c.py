n,m=map(int,input().split())
mat=[input() for i in range(n)]

for i in range(n):
    s=""
    for j in range(m):
        cnt=0
        for dx in range(-1,2):
            for dy in range(-1,2):
                if(0<=i+dx and i+dx<n and 0<=j+dy and j+dy<m and mat[i+dx][j+dy]=='#'):
                    cnt+=1
        s+=str(cnt)
    print(s)
