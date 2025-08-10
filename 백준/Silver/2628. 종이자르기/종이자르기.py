n, m = map(int, input().split()) 
num_line = int(input())

w = [0, n]
h = [0, m]

for _ in range(num_line):
    a, b = map(int, input().split())

    if a == 0:
        h.append(b)
    else:
        w.append(b)

w.sort()
h.sort()

max_w = 0
for i in range(len(w)-1):
    tmp = w[i+1] - w[i]
    max_w = max(max_w, tmp)

max_h = 0
for i in range(len(h)-1):
    tmp = h[i+1] - h[i]
    max_h = max(max_h, tmp)

print(max_w * max_h)
