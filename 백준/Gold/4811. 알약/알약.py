while True:
    n = int(input())

    if n == 0:
        exit()

    dp = [[0] * (n + 1) for _ in range(n + 1)]

    dp[n][0] = 1  # 한 알 꺼내서 반 알로 쪼갠다
    for w in range(n, -1, -1):  # W: 온전한 약
        for h in range(n, -1, -1):  # H: 반쪽 약
            if w > 0:
                if h + 1 <= n:
                    dp[w - 1][h + 1] += dp[w][h]  # 한 알 꺼내서 반 알로 쪼개기
            if h > 0:
                dp[w][h - 1] += dp[w][h]  # 반 알 먹기

    print(dp[0][0])
