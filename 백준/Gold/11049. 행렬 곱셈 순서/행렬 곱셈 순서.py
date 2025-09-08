import sys
input = sys.stdin.readline

n = int(input()) # 행렬의 개수
arr = [list(map(int, input().split())) for _ in range (n)]
dp = [[0] * n for _ in range (n)] # 행렬 i부터 j까지의 최소 연산 횟수

for term in range (1, n): # 구간 크기
  for i in range (n-term): # 시작 인덱스

    j = i + term # 끝 인덱스
    dp[i][j] = 10**9
    
    for k in range (i, j): # i~j 구간을 k를 기준으로 나눔
      cost = dp[i][k] + dp[k+1][j] + arr[i][0] * arr[k+1][0] * arr[j][1]

      if cost < dp[i][j]:
        dp[i][j] = cost

print(dp[0][n-1])