n = int(input()) # 계단의 개수
stairs = [int(input()) for _ in range (n)]

# 예외 처리
if n == 1:
    print(stairs[0])
    exit()
elif n == 2:
    print(stairs[0] + stairs[1])
    exit()

dp = [0] * 300

dp[0] = stairs[0] # 한 칸은 한 계단 올라가기
dp[1] = stairs[0] + stairs[1] # 두번째 칸은 두 칸 다 밟기 
dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

for i in range (3, n):
  dp[i] = max(dp[i-2], dp[i-3]+stairs[i-1]) + stairs[i]

print(dp[n-1])