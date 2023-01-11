A,B = map(int,input().split())

# WAになるためコメントアウト
# trimA = ""
# trimB = ""
# count = 0

# for i in range(A,B+1):
#     tmp = str(i)
#     trimA = tmp[0:2]
#     trimB = tmp[3:5]
#     if trimA == trimB:
#         count += 1

count = 0

for i in range(A,B+1):
    
    tmp = str(i)
    a = tmp[0]
    b = tmp[1]
    c = tmp[3]
    d = tmp[4]

    if a == d and b == c:
        count += 1

print(count)