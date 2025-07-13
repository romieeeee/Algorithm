n = int(input())

f = 1
for i in range(1, n+1):
    f *= i

f_str = str(f)[::-1]    

cnt = 0
for x in f_str:
    if x == '0':
        cnt += 1
    else:
        break

print(cnt)