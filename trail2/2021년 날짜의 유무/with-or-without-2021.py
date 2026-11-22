M, D = map(int, input().split())

# Please write your code here.

many = [1,3,5,7,8,10,12]
less = [4,6,9,11]

def know(a,b):
    if a>12 or b>31:
        return "No"
    else:
        if a in many:
            return "Yes"
        else:
            if a in less and b<=30:
                return "Yes"
            elif a==2 and b<=28:
                return "Yes"
            else:
                return "No"
print(know(M,D))
            