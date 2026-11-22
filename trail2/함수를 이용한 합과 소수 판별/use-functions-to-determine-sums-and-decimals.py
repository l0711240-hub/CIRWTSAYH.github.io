a, b = map(int, input().split())

# Please write your code here.

def is_clear(num):
    for i in range(2,num):
        if num%i==0:
            return False
    if sum(map(int,str(num)))%2==1:
        return False
    return True

count = 0

for k in range(a,b+1):
    if is_clear(k):
        count+=1
print(count)