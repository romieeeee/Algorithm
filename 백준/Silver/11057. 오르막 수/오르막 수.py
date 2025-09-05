n = int(input())

if n == 1:
  print(10)
  exit()

dp = [[0] * 10 for _ in range (n)]

for i in range (10):
  dp[0][i] = (i+1)

for i in range (1, n):
  for j in range (10):
    dp[i][j] = dp[i][j-1] + dp[i-1][j]

print(dp[n-1][-1]%10007)