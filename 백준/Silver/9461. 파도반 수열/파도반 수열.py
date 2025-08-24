T = int(input())
for _ in range (T):
    n = int(input())
    p = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9] # P(1) ~ P(10)

    for i in range (11, n+1):
        p.append(p[i-2]+p[i-3])

    print(p[n])