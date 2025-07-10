while(True):
    n = int(input())
    if n == -1:
        break

    s = [] # n의 소수 배열
    for i in range (1, n//2+1):
        if n % i == 0:
            s.append(i)

    if n == sum(s):
        s_str = ' + '.join(map(str, s))
        print(f'{n} = {s_str}')
    else:
        print(f'{n} is NOT perfect.')