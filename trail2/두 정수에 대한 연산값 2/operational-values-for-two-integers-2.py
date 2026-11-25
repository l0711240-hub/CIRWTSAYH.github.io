a, b = map(int, input().split())

# Please write your code here.

def trans(n,m):
    if n>m:
        n*=2
        m+=10
    else:
        n+=10
        m*=2
    return n,m

a,b = trans(a,b)

print(a, b)