n, m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range (n)]

dp = [[0] * m for _ in range (n)] # i, j까지 갔을 때의 최대 사탕 개수
dp[0][0] = maze[0][0]

for i in range (n):
  for j in range (m):
    top = dp[i-1][j] if i>0 else 0
    bottom = dp[i][j-1] if j>0 else 0
    diag = dp[i-1][j-1] if i >0 and j>0 else 0
    dp[i][j] = max(top, bottom, diag) + maze[i][j]

print(dp[n-1][m-1])