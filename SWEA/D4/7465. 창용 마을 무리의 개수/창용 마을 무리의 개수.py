T = int(input())

def dfs(v):
  visited[v] = True
  
  for nxt in graph[v]:
    if not visited[nxt]:
      dfs(nxt)


for test_case in range (1, T+1):
  n, m = map(int, input().split())
  graph = [[] for _ in range (n+1)]
  visited = [False] * (n+1) 
  
  for _ in range (m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
  
  cnt = 0  
  for i in range (1, n+1):
    if not visited[i]:
      dfs(i)
      cnt += 1
  
  print(f'#{test_case} {cnt}')
  