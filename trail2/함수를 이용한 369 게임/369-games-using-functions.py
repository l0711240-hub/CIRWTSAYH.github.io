a, b = map(int, input().split())

# Please write your code here.
count=0
def syg(num):    
    global count
    if not '3' in str(num) and not '6' in str(num) and not '9' in str(num):
        if num%3==0:
            count +=1
    else:
        count +=1

for i in range(a,b+1):
    syg(i)
print(count)
