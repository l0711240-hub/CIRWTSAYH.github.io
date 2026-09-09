n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

li = [0]*201
for i in range(n):
    A = segments[i][0]
    B = segments[i][1]
    for i in range(A,B):
        li[i] += 1

print(max(li))
