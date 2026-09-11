import sys

input = sys.stdin.read
data = input().split()

w_cnt, b_cnt, color = [0]*200005, [0]*200005, [0]*200005
curr = 100000

for x, d in zip(data[1::2], data[2::2]):
    x = int(x)
    rng = range(curr - x + 1, curr + 1) if d == 'L' else range(curr, curr + x)
    c_type = 1 if d == 'L' else 2
    
    for i in rng:
        if color[i] == 3: continue
        if d == 'L': w_cnt[i] += 1
        else: b_cnt[i] += 1
        
        color[i] = 3 if (w_cnt[i] >= 2 and b_cnt[i] >= 2) else c_type
        
    curr = rng[0] if d == 'L' else rng[-1]

print(color.count(1), color.count(2), color.count(3))