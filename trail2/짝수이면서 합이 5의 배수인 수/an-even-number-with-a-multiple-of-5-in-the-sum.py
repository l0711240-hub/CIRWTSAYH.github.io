n = int(input())

# Please write your code here.

def is_magicnumber(num):
    s = sum(map(int, str(num)))
    if num % 2 == 0 and s % 5 == 0:
        print("Yes")
    else:
        print("No")

is_magicnumber(n)