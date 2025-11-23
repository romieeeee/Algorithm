from collections import deque
import sys

input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs():
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
    

m, n = map(int, input().split())

# 1: 익토 0: 안익토 -1: x
graph = [list(map(int, input().split())) for _ in range (n)]

q = deque()
for i in range (n):
    for j in range (m):
        if graph[i][j] == 1:
            q.append((i, j))

bfs()

days = 0
for i in range(n):
    for j in range(m):
        
        # bfs 이후에도 아직 안 익은 토마토가 존재한다면
        if graph[i][j] == 0: 
            print(-1)
            exit(0)
        
        # 토마토가 익을 때까지의 날짜 (max를 구하면 된다)
        days = max(days, graph[i][j])

print(days - 1) 