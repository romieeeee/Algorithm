n = int(input())
juice = [int(input()) for _ in range(n)]

if n == 1:
  print(juice[0])
  exit()

if n == 2:
  print(juice[0]+juice[1])
  exit()

dp = [0] * n
dp[0] = juice[0]
dp[1] = juice[0] + juice[1]

for i in range (2, n):
  dp[i] = max(dp[i-1], dp[i-2] + juice[i], dp[i-3] + juice[i-1] + juice[i])

print(dp[n-1])