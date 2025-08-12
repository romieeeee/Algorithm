import sys
from collections import deque

def bfs():
    while q:
        z, x, y = q.popleft()

        for dz, dx, dy in dir:
            nz, nx, ny = z+dz, x+dx, y+dy

            if 0<=nz<h and 0<=nx<n and 0<=ny<m:
                if tomato[nz][nx][ny] == 0:
                    tomato[nz][nx][ny] = tomato[z][x][y] + 1
                    
                    q.append((nz, nx, ny))

dir = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

m, n, h = map(int, sys.stdin.readline().split())

# 1: 익은 토마토, 0: 익지 않은 토마토, -1: 토마토가 들어있지 않은 칸

tomato = []
for _ in range (h):
    tomato.append([list(map(int, sys.stdin.readline().split())) for _ in range (n)])

q = deque()

for z in range (h):
    for x in range (n):
        for y in range (m):

            # 익은 토마토들을 큐에 먼저 넣는다
            if tomato[z][x][y] == 1: 
                q.append((z, x, y))

bfs()

days = 0
for z in range (h):
    for x in range (n):
        for y in range (m):
            # 아직 안 익은 토마토가 있다면
            if tomato[z][x][y] == 0: 
                print(-1)
                exit(0)

            days = max(days, tomato[z][x][y]) 

print(days-1)