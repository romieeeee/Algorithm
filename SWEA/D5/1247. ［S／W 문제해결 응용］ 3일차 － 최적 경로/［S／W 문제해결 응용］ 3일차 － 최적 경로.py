def dfs(x, y, depth, cur_distance):
  global min_distance
  
  # 현재까지의 거리가 이미 최솟값보다 크다면 더이상 확인하지 않는다
  if cur_distance > min_distance:
    return
  
  if depth == n: # 다 방문했으면 집까지의 거리까지 계산
    min_distance = min(min_distance, cur_distance+abs(ex-x)+abs(ey-y))
  
  for i in range (n):
    if not visited[i]:
      visited[i] = True
      nx, ny = coord[i][0], coord[i][1]

      dfs(nx, ny, depth+1, cur_distance+abs(x-nx)+abs(y-ny))
      
      visited[i] = False

T = int(input())
for test_case in range(1, T + 1):
  
  # 회사에서 출발하여 n명을 모두 방문하고 집으로 돌아오는 최단경로!!

  n = int(input()) # 고객의 수
  data = list(map(int, input().split()))
  
  visited = [False] * n

  coord = []
  sx, sy = data.pop(0), data.pop(0) # 회사 좌표 == 시작 좌표
  ex, ey = data.pop(0), data.pop(0) # 집 좌표 == 끝 좌표
  
  # 고객 집 추출
  for i in range (n):
    coord.append([data.pop(0), data.pop(0)])

  min_distance = 1e9
  dfs(sx, sy, 0, 0)
    
  print(f"#{test_case} {min_distance}")