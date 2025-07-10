n, d = input().split() # d의 빈도수

arr = [str(x) for x in range (1, int(n)+1)]

cnt = 0
for a in arr:
    cnt += a.count(d)

print(cnt)