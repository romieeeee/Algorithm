import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    visited[x][y] = True

    for dx, dy in dir:
        nx, ny = x+dx, y+dy

        if  0<= nx<n and 0<=ny<m:
            if not visited[nx][ny] and graph[nx][ny] == 1:
                dfs(nx, ny)

dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]

T = int(input())
for _ in range (T):
    m, n, k = map(int, sys.stdin.readline().split()) # 가로, 세로, 위치의 개수
    
    graph = [[0] * m for _ in range (n)]
    visited = [[False] * m for _ in range(n)]
    
    for _ in range (k):
        u, v = map(int, sys.stdin.readline().split())
        graph[v][u] = 1

    cnt = 0
    for i in range (n):
        for j in range (m):

            if not visited[i][j] and graph[i][j] == 1:
                dfs(i, j)
                cnt += 1

    print(cnt)