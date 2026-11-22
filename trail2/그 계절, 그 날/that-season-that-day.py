Y, M, D = map(int, input().split())

# Please write your code here.

many = [1, 3, 5, 7, 8, 10, 12]
less = [4, 6, 9, 11]

def year(k):
    if k % 4 != 0:
        return False
    elif (k % 4 == 0 and k%100!=0) or (k%100 ==0 and k % 400 )== 0:
        return True
    return False

def know(a, b, c):
    if a > 12 or b > 31:
        return "No"
    else:
        if a in many:
            return "Yes"
        else:
            if a in less and b <= 30:
                return "Yes"
            elif a == 2 and year(c):
                if b <= 29:
                    return "Yes"
            elif a == 2 and not year(c):
                if a == 2 and b <= 28:
                    return "Yes"
            else:
                return "No"
k = know(M, D, Y)

if k == "Yes":
    if M >= 3 and M <= 5:
        print("Spring")
    if M>=6 and M <= 8:
        print("Summer")
    if M >= 9 and M <= 11:
        print("Fall")
    if M == 12 or M <= 2:
        print("Winter")
else:
    print(-1)
