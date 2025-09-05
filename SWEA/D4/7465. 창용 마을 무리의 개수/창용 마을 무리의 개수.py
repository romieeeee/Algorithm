def dfs(x):
  visited[x] = True
  for nxt in graph[x]:
      if not visited[nxt]:
          dfs(nxt)

T = int(input())
for test_case in range(1, T + 1):
  n, m = map(int, input().split())
  graph = [[] for _ in range(n+1)] 

  visited = [False] * (n+1)

  cnt = 0 # 무리의 개수

  for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)  
    graph[v].append(u)

  for i in range (1, n+1):
    if not visited[i]:
      cnt += 1
      dfs(i)
    
  print(f'#{test_case} {cnt}')