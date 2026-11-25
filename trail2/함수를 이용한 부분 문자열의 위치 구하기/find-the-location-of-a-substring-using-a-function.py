text = input()
pattern = input()

# Please write your code here.

def check():
    if pattern not in text:
        return -1
    else:
        return text.find(pattern)

print(check())