def dfs(idx, arr, amount, profit):
  global max_profit
  
  if amount > c:
    return
  
  if idx == m:
    max_profit = max(max_profit, profit)
    return
  
  dfs(idx + 1, arr, amount + arr[idx], profit + arr[idx] ** 2)
  
  dfs(idx + 1, arr, amount, profit)
      
T = int(input())
for tc in range (1, T+1):
  n, m, c = map(int, input().split())
  graph = [list(map(int, input().split())) for _ in range (n)]
  
  total = 0
  res = 0
  
  max_h1 = 0
  for i in range (n):
    for j in range (n-m+1):
      h1 = graph[i][j:j+m]
      
      max_profit = 0      
      for k in range (1, m+1):
        dfs(0, h1, 0, 0) # idx, arr, amount, profit
        
      max_h1 = max_profit # h1의 최대 수익

      max_h2 = 0
      for x in range (n):
        for y in range (n-m+1):
          # 같은 행에 있을 때 안겹치게
          if i == x and y < j+m:
            continue
          
          h2 = graph[x][y:y+m]
          
          max_profit = 0
          for k in range (1, m+1):
            dfs(0, h2, 0, 0) # idx, arr, amount, profit
            
          max_h2 = max(max_h2, max_profit)
      
      total = max(total, max_h1+max_h2)
      
    res = max(res, total)
  
  print(f'#{tc} {res}')