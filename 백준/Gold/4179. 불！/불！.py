from collections import deque
import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def spread_fire():
  for _ in range (len(fire)):
    x, y = fire.popleft()

    for i in range (4):
        nx, ny = x+dx[i], y+dy[i]

        if 0<=nx<r and 0<=ny<c and graph[nx][ny] != '#' and graph[nx][ny] != 'F':
          graph[nx][ny] = 'F'
          fire.append((nx, ny))


def bfs():

  while jihoon:

    spread_fire()

    for _ in range (len(jihoon)):
      x, y, minute = jihoon.popleft()

      if x == 0 or x == r-1 or y == 0 or y == c-1:
        print(minute + 1)
        return
      
      for i in range (4):
        nx, ny = x+dx[i], y+dy[i]

        if 0<=nx<r and 0<=ny<c and not visited[nx][ny]:
          # 벽이랑 불이 있는 곳으로는 못간다...
          if graph[nx][ny] != '#' and graph[nx][ny] != 'F':
            visited[nx][ny] = True
            jihoon.append((nx, ny, minute+1))


    # print(f'{minute} min later...')
    # for i in range (r):
    #   print(*graph[i])

  print('IMPOSSIBLE')
  return


r, c = map(int, input().split())
graph = [[x for x in input().rstrip()] for _ in range (r)]

visited = [[False] * c for _ in range (r)]

jihoon = deque()
fire = deque()

for i in range (r):
  for j in range (c):
    if graph[i][j] == 'J': 
      visited[i][j] = True
      jihoon.append((i, j, 0))
    elif graph[i][j] == 'F':
      fire.append((i, j))

bfs()