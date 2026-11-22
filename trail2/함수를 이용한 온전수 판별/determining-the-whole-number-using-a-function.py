a, b = map(int, input().split())

# Please write your code here.

def is_full(num):
    if num%2==0:
        return False
    if num%10==5:
        return False
    if num%3==0 and num%9!=0:
        return False
    return True

count=0
for i in range(a,b+1):
    if is_full(i):
        count+=1
print(count)