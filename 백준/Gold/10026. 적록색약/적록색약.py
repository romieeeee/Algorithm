import sys
from collections import deque

def bfs(i, j, c, color):
    global visited

    q.append((i, j))
    visited[i][j] == True
    
    while q:
        x, y = q.popleft()

        for dx, dy in dir:
            nx, ny = x+dx, y+dy

            if 0<=nx<n and 0<=ny<n:
                if c == 1: # 적록색약이 아닌 사람일 경우
                    # 방문하지 않았고 같은 색상이라면
                    if not visited[nx][ny] and graph[nx][ny] == color:
                        q.append((nx, ny))
                        visited[nx][ny] = True
                else: # 적록색약의 경우
                    if not visited[nx][ny]:
                        if graph[nx][ny] == color or graph[nx][ny] == 'R' and color == 'G' or graph[nx][ny] == 'G' and color == 'R':
                            q.append((nx, ny))
                            visited[nx][ny] = True


dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

n = int(sys.stdin.readline())
graph = [list(sys.stdin.readline()) for _ in range (n)]
visited = [[False] * n for _ in range (n)]

res1 = 0 # 적록색약이 아닌 사람이 본 구역의 수
res2 = 0 # 적록색약이 본 구역의 수

q = deque()

# 적록색약 x
for i in range (n):
    for j in range (n):
        if not visited[i][j]:
            cur = graph[i][j] # 현재 탐색할 색상 선택
            bfs(i, j, 1, cur)
            res1 += 1

# 방문 배열 초기화
visited = [[False] * n for _ in range (n)]

# 적록색약 o
for i in range (n):
    for j in range (n):
        if not visited[i][j]:
            cur = graph[i][j]
            bfs(i, j, 2, cur)
            res2 += 1

print(res1, res2)