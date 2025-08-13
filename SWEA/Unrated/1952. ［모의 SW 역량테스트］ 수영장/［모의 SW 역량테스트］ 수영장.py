def solve(c, s):
    global res

    if s >= res:
        return
    
    if c >= 12:
        res = s
    else:
        solve(c+1, s+(day_fee * using[c]))
        solve(c+1, s+month_fee)
        solve(c+3, s+month3_fee)

T = int(input())
for test_case in range(1, T + 1):
    day_fee, month_fee, month3_fee, year_fee = map(int, input().split())
    using = list(map(int, input().split()))

    res = year_fee
    solve(0, 0)

    print(f'#{test_case} {res}')
