def dfs(idx, height):
  global min_diff
  
  if idx == n:
    if height >= b:
      min_diff = min(min_diff, abs(b-height))
    return

  dfs(idx+1, height+people[idx])
  dfs(idx+1, height)
    

T = int(input())
for tc in range (1, T+1):
  n, b = map(int, input().split())
  people = list(map(int, input().split()))
    
  min_diff = 1e9
  dfs(0, 0)
  
  print(f'#{tc} {min_diff}')
  