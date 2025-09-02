def dfs(depth, cur_per):
  global max_per
  
  if cur_per <= max_per:
    return
  
  if depth == n:
    max_per = max(max_per, cur_per)
    return

  for j in range (n):
    if per[depth][j] == 0:
      continue
    
    if not visited[j]:
      visited[j] = True # j번째 일 선택!
      dfs(depth+1, cur_per*(per[depth][j]/100))
      
      visited[j] = False
      
    
T = int(input())
for test_case in range(1, T + 1):
  n = int(input())
  per = [list(map(int, (input().split()))) for _ in range (n)]
  visited = [False] * n

  selected = [] # 선택한 일 저장...

  max_per = 0 # 주어진 일이 모두 성공할 확률의 최댓값
  dfs(0, 1.0)
  
  print(f"#{test_case} {max_per*100:.6f}")