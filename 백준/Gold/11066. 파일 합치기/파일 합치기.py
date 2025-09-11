T = int(input())
for _ in range(T):
    n = int(input())
    data = list(map(int, input().split()))
    sum_data = [0] * (n + 1)

    dp = [[0] * n for _ in range(n)]  # i부터 j까지 파일을 합치는 최소 비용

    for i in range(n):  # 누적합
        sum_data[i + 1] = sum_data[i] + data[i]

    for i in range(1, n):  # 구간 길이
        for j in range(n - i):  # 시작점
            k = j + i  # 끝점
            dp[j][k] = float("inf")
            for x in range(j, k):
                cost = dp[j][x] + dp[x + 1][k] + sum_data[k + 1] - sum_data[j]
                dp[j][k] = min(dp[j][k], cost)

    print(dp[0][n - 1])
