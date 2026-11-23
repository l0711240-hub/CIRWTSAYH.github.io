a, b = map(int, input().split())

# Please write your code here.

def out(x,y):
    if x>y:
        x+=25
        y*=2
    else:
        x*=2
        y+=25
    return x,y
a, b = out(a, b)
print(a, b)