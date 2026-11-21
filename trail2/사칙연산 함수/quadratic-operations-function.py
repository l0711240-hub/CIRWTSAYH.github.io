s=input()
a, o, c = s.split()
a = int(a)
c = int(c)

# Please write your code here.

if o == '+':
    print(s+' '+'='+' '+f'{a+c}')
elif o == '-':
    print(s+' '+'='+' '+f'{a-c}')
elif o == '*':
    print(s+' '+'='+' '+f'{a*c}')
elif o == '/':
    print(s+' '+'='+' '+f'{int(a/c)}')
else:
    print(False)
