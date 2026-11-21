n, m = map(int, input().split())
# Please write your code here.
b=m
def gcd(a,b): 
    r=1
    while r!=0:
        r=a%b
        a=b
        b=r
    return a
print(int(n*m/gcd(n,m)))