n, k = map(int, input().split()) # 물품의 수, 버틸 수 있는 무게

data = [[0, 0]]
for _ in range (n):
    data.append(list(map(int, input().split())))

dp = [[0] * (k+1) for _ in range (n+1)]

for i in range (1, n+1):
    for j in range (1, k+1):
        w = data[i][0] # 무게
        v = data[i][1] # 가치

        if  w > j: # 현재 무게에서 이 물건을 담을 수 없다면
            dp[i][j] = dp[i-1][j] # 위의 값을 가져온다
        else: # 아니라면 현재 물품을 담을 때와 아닐때의 가치를 비교!
            dp[i][j] = max(v+dp[i-1][j-w], dp[i-1][j])

print(dp[n][k])
