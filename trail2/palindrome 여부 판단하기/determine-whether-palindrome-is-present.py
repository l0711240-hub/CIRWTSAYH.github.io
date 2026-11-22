A = input()

# Please write your code here.

def palindrome(string):
    _list = list(map(str,string))
    _list.reverse()
    s = ''
    for i in _list:
        s+=i
    return s

if A == palindrome(A):
    print("Yes")
else:
    print("No")