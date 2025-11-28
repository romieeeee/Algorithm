def dfs(idx, now):
  global cnt
  
  if idx == n:
    if now == k:
      cnt += 1
    return
  

  dfs(idx+1, now+a[idx])
  dfs(idx+1, now)
    

T = int(input())
for tc in range (1, T+1):
  n, k = map(int, input().split())
  a = list(map(int, input().split()))
    
  cnt = 0
  dfs(0, 0)
  
  print(f'#{tc} {cnt}')
  