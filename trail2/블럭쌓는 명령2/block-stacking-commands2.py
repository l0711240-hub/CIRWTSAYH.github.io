n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.

li=[0]*n
for z in range(k):
    A = commands[z][0]
    B = commands[z][1]
    for i in range(A-1,B):
        li[i]+=1
print(max(li))