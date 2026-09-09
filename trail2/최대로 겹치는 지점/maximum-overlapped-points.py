n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
li=[0]*101
for i in range(n):
    A=segments[i][0]
    B=segments[i][1]
    for k in range(A,B+1):
        li[k]+=1

print(max(li))