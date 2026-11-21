y = int(input())

# Please write your code here.

def tell(year):
    if year%4!=0:
        return False
    if year%100==0 and year%400!=0:
        return False
    return True

if tell(y):
    print('true')
else:
    print('false')