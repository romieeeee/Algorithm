from collections import deque
import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def spreadWater():
  for _ in range (len(water)):
    x, y = water.popleft()

    for i in range (4):
      nx, ny = x+dx[i], y+dy[i]
      
      if 0<=nx<r and 0<=ny<c and graph[nx][ny] == '.':
        graph[nx][ny] = '*'
        water.append((nx, ny)) 
  
def bfs(sx, sy):
  q = deque()
  q.append((sx, sy))
  visited[sx][sy] = 0

  while q:
    spreadWater() # 물 확장...

    for _ in range (len(q)):
      x, y = q.popleft()

      if (x, y) == (ex, ey):
        print(visited[x][y])
        return

      for i in range (4):
        nx, ny = x+dx[i], y+dy[i]

        if 0<=nx<r and 0<=ny<c and not visited[nx][ny]:
          if graph[nx][ny] != '*' and graph[nx][ny] != 'X': # 물이나 돌이 아니면 이동

            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))


  print('KAKTUS')
  return
  

r, c = map(int, input().split())
graph = [[x for x in input().rstrip()] for _ in range (r)]

visited = [[0] * c for _ in range (r)]

water = deque()

sx = sy = 0
ex = ey = 0

for i in range (r):
  for j in range (c):
    if graph[i][j] == 'S': # 고슴도치 S
      sx, sy = i, j
    elif graph[i][j] == 'D': # 도착점 D
      ex, ey = i, j
    elif graph[i][j] == '*': # 물...
      water.append((i, j))

bfs(sx, sy)