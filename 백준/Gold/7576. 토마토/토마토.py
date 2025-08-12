from collections import deque

def bfs():
    while q:
        x, y = q.popleft()

        for dx, dy in dir:
            nx, ny = x+dx, y+dy

            if 0<=nx<n and 0<=ny<m and farm[nx][ny] == 0:
                    farm[nx][ny] = farm[x][y] + 1
                    q.append((nx, ny))  


dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

m, n = map(int, input().split())
farm = [list(map(int, input().split())) for _ in range (n)]

q = deque()

for i in range (n):
    for j in range (m):
        if farm[i][j] == 1:
            # 익은 토마토들을 queue에 넣는다
            q.append((i, j))

bfs()

days = 0
for i in range(n):
    for j in range(m):
        
        # bfs 이후에도 아직 안 익은 토마토가 존재한다면
        if farm[i][j] == 0: 
            print(-1)
            exit(0)
        
        # 토마토가 익을 때까지의 날짜 (max를 구하면 된다)
        days = max(days, farm[i][j])

print(days - 1) 