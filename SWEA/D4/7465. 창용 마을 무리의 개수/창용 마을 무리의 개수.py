def dfs(idx):
  for nxt in graph[idx]:
    if not visited[nxt]:
      visited[nxt] = True
      dfs(nxt)

T = int(input())
for tc in range (1, T+1):
  n, m = map(int, input().split()) # 개수, 제한 칼로리
  
  graph = [[] * n for _ in range (n+1)]
  visited = [False] * (n+1)
  
  for _ in range (m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
  
  total = 0
  for i in range (1, n+1):
    if not visited[i]:
      visited[i] = True
      
      dfs(i)
      total += 1
  
  print(f'#{tc} {total}')
  