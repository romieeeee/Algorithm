def dfs(start, depth):
  global min_diff
  
  # 조합을 만들었으면...
  if (depth == n//2):
    
    group_b = []
    for i in range (n):
      if i not in group_a:
        group_b.append(i)
    
    syn_a = syn_b = 0
    
    for i in group_a:
      for j in group_a:
        if i != j:
          syn_a += graph[i][j]
    
    for i in group_b:
      for j in group_b:
        if i != j:
          syn_b += graph[i][j]
    
    min_diff = min(min_diff, abs(syn_a-syn_b))
    return
  
  for i in range (start, n):
    if not visited[i]:
      visited[i] = True
      group_a[depth] = i
      
      dfs(i, depth+1)
      
      visited[i] = False
      
  
T = int(input())
for tc in range (1, T+1):
  n = int(input())

  graph = [list(map(int, input().split())) for _ in range (n)]
  
  # n // 2 크기의 조합을 만든다
  length = n//2
  
  visited = [False] * n
  group_a = [0] * (n//2)
  
  min_diff = 1e9
  dfs(0, 0) # start, depth
  
  print(f'#{tc} {min_diff}')