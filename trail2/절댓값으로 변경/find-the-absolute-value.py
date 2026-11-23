n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def absol(li):
    p = []
    for i in li:
        if i<0:
            p.append(i*-1)
        else:
            p.append(i)
    return p

arr = absol(arr)

for elem in arr:
    print(elem,end=" ")