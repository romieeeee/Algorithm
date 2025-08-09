from collections import deque

dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def bfs(x, y):
    global pic

    visited[x][y] = True
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for dx, dy in dir:
            nx, ny = x+dx, y+dy

            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))    
                    pic += 1

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range (n)]

q = deque()

cnt = 0
max_pic = 0

pic = 0
for i in range (n):
    for j in range (m):
        pic = 1
        if graph[i][j] == 1 and not visited[i][j]:
            cnt += 1
            bfs(i, j)

            max_pic = max(max_pic, pic)

print(cnt)
print(max_pic)