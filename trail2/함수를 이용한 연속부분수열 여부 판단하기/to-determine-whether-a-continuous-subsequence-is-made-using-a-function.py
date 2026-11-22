n1, n2 = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

# Please write your code here.

def tell(a,b,k):
    while b[0] in a:
        if a[a.index(b[0]):a.index(b[0])+k] == b:
            return ('Yes')
        else:
            a.pop(a.index(b[0]))
    return('No')

print(tell(x,y,n2))