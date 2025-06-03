self_num = []
for i in range(1, 10001):
    num = i
    for i in str(num):
        num += int(i)
        
    self_num.append(num)

self_num.sort()

for i in range (1, 10001):
    if i not in self_num:
        print(i)