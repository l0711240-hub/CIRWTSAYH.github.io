A = input()

# Please write your code here.

string = list(map(str,A))

def tell(st):
    dict={}
    for i in st:
        if dict.get(i)==None:
            dict[i] = 1
        else:
            dict[i] += 1
    if len(dict.keys()) >= 2:
        return "Yes"
    else:
        return "No"


print(tell(string))
        