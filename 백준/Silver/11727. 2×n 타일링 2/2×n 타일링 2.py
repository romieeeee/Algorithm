n = int(input())

if n == 1:
  print(1)
  exit()
if n == 2:
  print(3)
  exit()

dp = [0] * n
dp[0] = 1 # 2*1 직사각형은 2*1로만 채워요
dp[1] = 3 # 2*1, 1*2, 2*2 를 사용

for i in range (2, n):
  dp[i] = dp[i-1] + 2*dp[i-2]

print(dp[-1]%10007)