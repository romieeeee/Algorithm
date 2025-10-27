from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs():
  tmp = []
  for _ in range(len(cells)):
    life, x, y, remain, isactive = cells.popleft()

    if not isactive:
      if remain > 1:
        cells.append((life, x, y, remain-1, 0))
      elif remain == 1:
        cells.append((life, x, y, life, 1))
    else:
      for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if graph[nx][ny] == 0:
          tmp.append((life, nx, ny, life, 0))
      if remain > 1:
        cells.append((life, x, y, remain-1, 1))

  tmp.sort(reverse=True)
  for life, tx, ty, remain, isactive in tmp:
    if graph[tx][ty] == 0:
      graph[tx][ty] = life
      cells.append((life, tx, ty, remain, isactive))

T = int(input())
for test_case in range(1, T+1):
  n, m, k = map(int, input().split())
  graph = [[0]*(m+2*k) for _ in range(n+2*k)]

  cells = deque()
  for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
      if row[j] > 0:
        x, y, life = i+k, j+k, row[j]
        graph[x][y] = life
        cells.append((life, x, y, life, 0))

  for _ in range(k):
    bfs()

  print(f'#{test_case} {len(cells)}')
