n1, n2 = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

# Please write your code here.

def tell(a,b,k):
    while b[0] in a:
        t = a.index(b[0])
        if a[t:t+k] == b:
            return ('Yes')
        else:
            a.pop(t)
    return('No')

print(tell(x,y,n2))