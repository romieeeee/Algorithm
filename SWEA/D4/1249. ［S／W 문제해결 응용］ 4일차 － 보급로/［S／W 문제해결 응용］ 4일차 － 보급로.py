from collections import deque

d = [[1, 0], [0 , 1], [-1, 0], [0, -1]]

def bfs():
  
  while q:
    x, y = q.popleft()

    for dx, dy in d:
      nx, ny = x+dx, y+dy

      if 0<=nx<n and 0<=ny<n: # 범위 내에 있고
        if dist[x][y] + graph[nx][ny] < dist[nx][ny]:
          dist[nx][ny] = dist[x][y] + graph[nx][ny]
          
          q.append([nx, ny])

T = int(input())
for test_case in range(1, T + 1):
  n = int(input())
  graph = []

  for _ in range (n):
    row = [int(x) for x in input()]
    graph.append(row)

  dist = [[1e9] * n for _ in range (n)]
  dist[0][0] = graph[0][0]

  q = deque()
  q.append([0, 0])

  bfs()
  print(f'#{test_case} {dist[n-1][n-1]}')

    