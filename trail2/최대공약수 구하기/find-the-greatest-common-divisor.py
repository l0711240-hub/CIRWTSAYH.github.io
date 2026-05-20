n, m = map(int, input().split())

# Please write your code here.


def gcd(a,b):
    r=1
    while r!=0:
        r = b % a
        b=a
        a=r
    print(b)

if n>m:
    b = n
    a = m
    gcd(a,b)
elif n<m:
    b = m 
    a = n
    gcd(a,b)
else:
    print(n)

