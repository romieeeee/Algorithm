n = int(input())
arr = [list(map(int, input().split())) for _ in range (n)]

if n == 1:
  print(arr[0][0])
  exit()

if n == 2:
  print(max(arr[0][0]+arr[1][0], arr[0][0]+arr[1][1]))
  exit()

dp = [[0] * n for _ in range (n)]

dp[0][0] = arr[0][0] # top
dp[1][0] = dp[0][0] + arr[1][0] # 왼쪽 선택
dp[1][1] = dp[0][0] + arr[1][1] # 오른쪽 선택

for i in range (2, n):
  for j in range (i+1):
    dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + arr[i][j]

print(max(dp[n-1]))