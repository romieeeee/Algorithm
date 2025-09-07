import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

dx = [0, 1]
dy = [1, 0]

def dfs(x, y):
    if (x, y) == (n-1, n-1): # 종착점
        return 1

    if dp[x][y] != -1: # 이미 계산된 값
        return dp[x][y]
    
    dp[x][y] = 0
    jump = board[x][y]

    if jump == 0: # 0이면 갈 수 없음
        return 0

    for i in range (2):
        nx = x + dx[i] * jump
        ny = y + dy[i] * jump

        if 0<=nx<n and 0<=ny<n:
            dp[x][y] += dfs(nx, ny)

    return dp[x][y]

n = int(input())
board = [list(map(int, input().split())) for _ in range (n)]

# i, j부터 종착점까지의 갈 수 있는 경로의 수
dp = [[-1]* n for _ in range (n)] 

print(dfs(0, 0))