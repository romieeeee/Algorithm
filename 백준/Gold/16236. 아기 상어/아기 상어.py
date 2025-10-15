from collections import deque
import sys
input = sys.stdin.readline

# 방향 벡터 (위쪽 왼쪽 먼저!)
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def bfs(x, y):
  q = deque()
  q.append((0, x, y)) # 아기 상어와의 거리, 좌표

  visited = [[False] * n for _ in range (n)]
  visited[x][y] = True

  fish = [] # 먹을 수 있는 물고기들을 담는다

  while q:
    d, cx, cy= q.popleft()

    for i in range (4):
      nx, ny = cx+dx[i], cy+dy[i]

      if 0<=nx<n and 0<=ny<n and not visited[nx][ny]: # 아기상어 이동
        if baby >= graph[nx][ny]:
          visited[nx][ny] = True

          if 0< graph[nx][ny] < baby: # 잡아먹을 수 있는 물고기라면...
            fish.append((d+1, nx, ny))
          else:
            q.append((d+1, nx, ny)) # 아니면 그냥 이동
          
  return sorted(fish) # 거리순으로 정렬해서 반환!


n = int(input()) # n*n
graph = [list(map(int, input().split())) for _ in range (n)]

baby = 2 # 아기 상어의 초기 크기는 2
eat_cnt = 0 # 먹은 상어의 개수
sec = 0 # 걸린 시간

# ===== 초기 위치 설정 =====
x = y = 0
for i in range (n):
  for j in range (n):
    if graph[i][j] == 9: # 아기 상어!
      x, y = i, j
      graph[i][j] = 0
      break

# ===== 물고기 먹기 =====
while True:
  fishes = bfs(x, y)
  
  if not fishes:
    break

  dist, nx, ny = fishes[0]

  sec += dist 
  eat_cnt += 1 # 먹어용...

  graph[nx][ny] = 0 # 먹은 칸은 빈칸이 된다
  x, y = nx, ny

  if eat_cnt == baby: # 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기 1 증가
    baby += 1
    eat_cnt = 0

print(sec)