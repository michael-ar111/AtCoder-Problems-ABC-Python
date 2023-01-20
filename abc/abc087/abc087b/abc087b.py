A = int(input())
B = int(input())
C = int(input())
X = int(input())

ans = 0

for a in range(0,A+1):
    for b in range(0,B+1):
        for c in range(0,C+1):
            if (a*500 + b*100 + c*50) == X:
                ans += 1

print(ans)

#0からだ。