from collections import deque
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
  q = deque()
  q.append((0, 0))
  visited[0][0] = True

  cheeze = [] # 한 턴에 녹게 될 치즈들

  while q:
    cx, cy = q.popleft()

    for i in range (4):
      nx, ny = cx+dx[i], cy+dy[i]

      if 0<=nx<h and 0<=ny<w and not visited[nx][ny]:
        visited[nx][ny] = True

        # 공기일 경우 계속 탐색
        if graph[nx][ny] == 0:
          q.append((nx, ny))

        # 치즈일 경우 배열에 추가!
        elif graph[nx][ny] == 1:
          cheeze.append((nx, ny))

  return cheeze

h, w = map(int, input().split()) # 세로 가로
graph = [list(map(int, input().split())) for _ in range (h)] # 0: 치즈 x, 1: 치즈 o

x = y = 0
time = 0

last_cheeze = 0 # 모두 녹기 한 시간 전에 남아있는 치즈

while True:
  visited = [[False] * w for _ in range (h)]

  # ===== 녹일 치즈 탐색 =====
  melting_cheeze = bfs()

  if not melting_cheeze:
    break
  
  # ===== 녹일 치즈 개수 저장 =====
  last_cheeze = len(melting_cheeze)

  # ==== 치즈 녹이기 =====
  for x, y in melting_cheeze:
    graph[x][y] = 0 

  time += 1

print(time)
print(last_cheeze)