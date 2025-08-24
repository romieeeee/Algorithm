n = int(input())

p = [] # 피보나치 수열

p.append(0)
p.append(1)
for i in range(2, n+1):
    p.append(p[i-1] + p[i-2])

print(p[n])