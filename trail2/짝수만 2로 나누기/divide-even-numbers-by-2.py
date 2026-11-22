n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def divodd(ar):
    count = 0
    for k in ar:
        if k%2 ==0:
            ar[count]=k//2
        count+=1
    return ar

arr = divodd(arr)

for e in arr:
    print(e, end=" ")