n = int(input())

# Please write your code here.

def decimal_square(n):
    count=1
    lang=''
    for i in range(n):
        for u in range(n):
            if count==10:
                count=1
            lang+=str(count)+' '
            count+=1
        print(lang)
        lang=''

decimal_square(n)