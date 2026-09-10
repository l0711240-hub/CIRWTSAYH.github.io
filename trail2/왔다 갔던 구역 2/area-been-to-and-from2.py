n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.
line = [0]*2001
loc = 0
for i in range(n):
    if dir[i] == 'L':
        for k in range(1001+loc-x[i],1001+loc):
            line[k]+=1
        loc -= x[i]
    else:
        for k in range(1001+loc,1001+loc+x[i]):
            line[k]+=1
        loc += x[i]
count=0
for z in line:
    if z>=2:
        count+=1
    

print(count)