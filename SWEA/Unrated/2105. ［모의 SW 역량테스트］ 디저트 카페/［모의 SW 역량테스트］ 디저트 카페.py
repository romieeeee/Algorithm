dx = [1,1,-1,-1]
dy = [-1,1,1,-1]

def dfs(x, y, d, l, now, visited):
  global res
  
  if l > 3: return
  if l == 3 and (x == sx and  y == sy):
    res = max(res, now)
  else:   
    for i in range (2):
      di = (d+i)%4
      nx, ny = x+dx[di], y+dy[di]
      
      if nx < 0 or nx >= n or ny < 0 or ny >= n:
        continue
      
      if graph[nx][ny] not in visited:
        visited.append(graph[nx][ny])
        dfs(nx, ny, di, l+i, now+1, visited)
        visited.pop()
  

T = int(input())
for test_case in range (1, T+1):
  n = int(input())
  graph = [list(map(int, input().split())) for _ in range (n)]
  
  res = -1
  for i in range (n):
    for j in range (n):
      sx, sy = i, j
      dfs(i, j, 0, 0, 0, []) # x, y, 현재 방향, 방향 전환 횟수, 방문한 디저트 가게

  print(f'#{test_case} {res}')