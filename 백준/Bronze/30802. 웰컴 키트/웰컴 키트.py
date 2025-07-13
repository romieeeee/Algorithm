n = int(input()) # 참가자 수
size = list(map(int, input().split()))

t, p = map(int, input().split()) # 티셔츠와 펜의 묶음 수

t_cnt = 0 # 주문해야 할 티셔츠 묶음 수
p_cnt = 0 # 주문해야 할 펜의 묶음 수

for i in range (6):
    if size[i] == 0:
        continue
    else:
        if size[i] % t == 0:
            t_cnt += size[i] // t
        else:
            t_cnt += (size[i] // t) + 1

p_cnt = n // p
pp = n % p

print(t_cnt)
print(p_cnt, pp)