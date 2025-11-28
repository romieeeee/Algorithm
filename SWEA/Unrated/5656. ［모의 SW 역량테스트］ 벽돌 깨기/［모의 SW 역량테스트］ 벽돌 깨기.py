from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def drop(temp):
  for c in range(w):
    stack = []
    
    # 아래에서 위로 벽돌만 모으기
    for r in range(h-1, -1, -1):
      if temp[r][c] > 0:
        stack.append(temp[r][c])

    # 다시 아래에서부터 채우기
    r = h-1
    for brick in stack:
      temp[r][c] = brick
      r -= 1

    # 남은 칸 빈칸으로 채우기
    for rr in range(r, -1, -1):
      temp[rr][c] = 0

    
def simulation(perm):
  temp = [row[:] for row in graph]

  for idx in range (n):
    sy = perm[idx]
    
    # ===== idx 번째의 벽돌을 깨자 =====
    sx = -1 
    for row in range (h): # 해당 열에서 첫번째 벽돌 찾기
      if temp[row][sy] > 0:
        sx = row
        break
      
    # 해당 열에 벽돌이 없다면 넘어가기
    if sx == -1: continue
    
    # ===== 폭발 시작 =====
    q = deque()
    q.append((sx, sy, temp[sx][sy]))
    temp[sx][sy] = 0
    
    while q:
      x, y, power = q.popleft()

      for d in range (4):
        nx, ny = x, y
        
        for _ in range (power-1):
          nx += dx[d]
          ny += dy[d]
          
          if nx < 0 or nx >= h or ny < 0 or ny >= w:
            break
          
          if temp[nx][ny] > 0: # 
            q.append((nx, ny, temp[nx][ny]))
            
          temp[nx][ny] = 0 
    
    # ===== 한턴 끝나고 벽돌 다 내리기 =====       
    drop(temp)
    
  # ===== 남은 벽돌 세기 =====
  block = 0
  for r in range(h):
    for c in range(w):
      if temp[r][c] > 0: block += 1

  return block
    

def dup_perm(depth):
  global min_block
  
  if depth == n:
    res = simulation(perm)
    min_block = min(min_block, res)
    return
  
  for i in range (w):
    perm[depth] = i
    dup_perm(depth+1)


T = int(input())
for tc in range (1, T+1):
  n, w, h = map(int, input().split()) # 던질 벽돌 개수, 너비, 높이
  graph = [list(map(int, input().split())) for _ in range (h)] # h줄에 걸쳐 1줄에 w개씩 주어진다
  
  min_block = 1e9
  
  perm = [0] * n
  dup_perm(0)

  print(f'#{tc} {min_block}')