def dfs(start, depth, arr, amount, profit):
  global end, max_amount, max_profit
  
  if amount > c:
    return
  
  if depth == end:
    max_amount = max(max_amount, amount)
    max_profit = max(max_profit, profit)
    return
  
  for i in range (start, m):
    if not visited[i]:
      visited[i] = True
      profit += arr[i] ** 2 
      
      dfs(i, depth+1, arr, amount+arr[i], profit)
      
      profit -= arr[i] ** 2 
      visited[i] = False
      
T = int(input())
for tc in range (1, T+1):
  n, m, c = map(int, input().split())
  graph = [list(map(int, input().split())) for _ in range (n)]
  
  max_h1 = 0
  total = 0
  res = 0
  
  for i in range (n):
    for j in range (n-m+1):
      h1 = graph[i][j:j+m]
      
      max_amount = 0
      max_profit = 0      
      for k in range (1, m+1):
        end = k
        visited = [False] * m
        
        dfs(0, 0, h1, 0, 0) # start, depth, arr, amount, profit
        
        # if max_amount == c:
        #   break
        
      max_h1 = max_profit # h1의 최대 수익

      max_h2 = 0
      for x in range (n):
        for y in range (n-m+1):
          # 같은 행에 있을 때 안겹치게
          if i == x and y < j+m:
            continue
          
          h2 = graph[x][y:y+m]
          
          max_amount = 0
          max_profit = 0
          for k in range (1, m+1):
            end = k
            visited = [False] * m
            
            dfs(0, 0, h2, 0, 0) # start, depth, arr, amount, profit
            
            # if max_amount == c:
            #   break
          max_h2 = max(max_h2, max_profit)
      
      total = max(total, max_h1+max_h2)
      
    res = max(res, total)
  
  print(f'#{tc} {res}')