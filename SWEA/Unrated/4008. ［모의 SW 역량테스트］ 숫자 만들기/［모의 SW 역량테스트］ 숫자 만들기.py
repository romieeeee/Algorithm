def dfs(now, depth, plus, minus, mul, div):
    global max_value, min_value

    if (depth == n-1):
        # print(f'dfs! now value: {now}, depth: {depth}')
        if now < min_value: min_value = now
        if now > max_value: max_value = now
        return

    if plus > 0:
        dfs(now+nums[depth+1], depth+1, plus-1, minus, mul, div)

    if minus > 0:
        dfs(now-nums[depth+1], depth+1, plus, minus-1, mul, div)

    if mul > 0:
        dfs(now*nums[depth+1], depth+1, plus, minus, mul-1, div)

    if div > 0:
        dfs(int(now / nums[depth+1]), depth+1, plus, minus, mul, div-1)

T = int(input())
for test_case in range (1, T+1):
    n = int(input())
    ops = list(map(int, input().split())) # +, -, *, /
    nums = list(map(int, input().split()))

    max_value = -10**10
    min_value = 10**10

    dfs(nums[0], 0, ops[0], ops[1], ops[2], ops[3])

    print(f'#{test_case} {max_value-min_value}')
