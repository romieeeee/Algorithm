import sys
input = sys.stdin.readline

n = int(input())

time = []
price = []

for _ in range (n):
  t, p = map(int, input().split())
  time.append(t)
  price.append(p)

dp = [0] * (n+1) # i일에 얻을 수 있는 최대 수익

for i in range (n-1, -1, -1):
    if i + time[i] <= n:
       dp[i] = max(dp[i+1], price[i]+dp[i+time[i]])
    else:
       dp[i] = dp[i+1]
  
print(dp[0])