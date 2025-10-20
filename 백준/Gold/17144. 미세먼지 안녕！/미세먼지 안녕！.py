import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def spread_dust(x, y):
  cnt = 0 # 확산된 방향의 개수
  amount = graph[x][y]//5 # 확산되는 양

  for i in range (4):
    nx, ny = x+dx[i], y+dy[i]

    # 인접한 방향에 칸이 없고 공기청정기가 없다면 확산
    if 0<=nx<r and 0<=ny<c and graph[nx][ny] != -1:
      temp[nx][ny] += amount
      cnt += 1

  graph[x][y] -= amount * cnt # 남은 미세먼지 양 계산!


def run_air_top():
  top = air[0]
  
  for i in range(top - 1, 0, -1):
    graph[i][0] = graph[i - 1][0]

  for i in range(c - 1):
    graph[0][i] = graph[0][i + 1]

  for i in range(top):
    graph[i][c - 1] = graph[i + 1][c - 1]

  for i in range(c - 1, 1, -1):
    graph[top][i] = graph[top][i - 1]

  graph[top][1] = 0


def run_air_bottom():
  bottom = air[1]

  for i in range(bottom + 1, r - 1):
    graph[i][0] = graph[i + 1][0]

  for i in range(c - 1):
    graph[r - 1][i] = graph[r - 1][i + 1]

  for i in range(r - 1, bottom, -1):
    graph[i][c - 1] = graph[i - 1][c - 1]

  for i in range(c - 1, 1, -1):
    graph[bottom][i] = graph[bottom][i - 1]

  graph[bottom][1] = 0

r, c, t = map(int, input().split()) # 행, 열, 초
graph = [list(map(int, input().rstrip().split())) for _ in range (r)]

air = [] # 공기 청정기
for i in range (r):
  if graph[i][0] == -1:
    air.append(i)
    
# t초 동안 수행 
for _ in range (t):

  # ===== 미세먼지 확산! =====
  temp = [[0]*c for _ in range(r)]
  for i in range(r):
    for j in range(c):
        if graph[i][j] > 0: # 미세먼지가 있는 칸
          spread_dust(i, j)
  
  # 확산 후 원본 그래프에 반영한다
  for i in range(r):
    for j in range(c):
            graph[i][j] += temp[i][j]

  # 먼지 위치 갱신...
  dust = []
  for i in range (r):
    for j in range (c):
      if graph[i][j] > 0:
        dust.append((i, j))

  # ===== 공기청정기 작동! =====
  run_air_top()
  run_air_bottom()

res = 0
for i in range (r):
  res += sum(graph[i])

print(res+2)
  