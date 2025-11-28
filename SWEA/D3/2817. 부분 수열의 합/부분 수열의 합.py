def dfs(start, depth, now):
  global cnt
  if depth > n:
    return
  
  if now == k:
    cnt += 1
    return
    
  for i in range (start, n):
    if not visited[i]:
      visited[i] = True
      comb[depth] = a[i]
      dfs(i, depth+1, now+a[i])
      visited[i] = False
    

T = int(input())
for tc in range (1, T+1):
  n, k = map(int, input().split())
  a = list(map(int, input().split()))
  
  visited = [False] * n
  
  cnt = 0
  visited[0] = False
  
  comb = [0] * n
  dfs(0, 0, 0)
  
  print(f'#{tc} {cnt}')
  