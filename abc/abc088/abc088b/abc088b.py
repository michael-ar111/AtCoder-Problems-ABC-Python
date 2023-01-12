N = int(input())
a = list(map(int,input().split()))

# N = 4
# a = [20,18,2,18]

a = sorted(a,reverse=True)

A = 0
B = 0
count = 1

for i in a:
    if count % 2 == 1:
        A += i
    else:
        B += i
    
    count += 1

print(A-B)    