import re

a, b = map(int, input().split())

# Please write your code here.

def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

count=0
for y in range(a,b+1):
    if is_prime(y):
        count+=y
print(count)