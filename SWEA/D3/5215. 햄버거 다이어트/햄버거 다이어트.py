def dfs(idx, taste, cal):
  global max_taste
  
  if idx == n:
    if cal <= l:
      max_taste = max(max_taste, taste)
      
    return

  dfs(idx+1, taste+arr[idx][0], cal+arr[idx][1])
  dfs(idx+1, taste, cal)
    

T = int(input())
for tc in range (1, T+1):
  n, l = map(int, input().split()) # 개수, 제한 칼로리
  arr = []
  
  for _ in range (n):
    arr.append(list(map(int, input().split())))
    
  max_taste = -1e9
  dfs(0, 0, 0) # idx, taste, cal
  
  print(f'#{tc} {max_taste}')
  