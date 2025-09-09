def dfs(depth, taste, kcal):
  global max_taste

  if kcal > l:
    return
  
  max_taste = max(max_taste, taste)

  if depth == n:
    return

  dfs(depth+1, taste+arr[depth][0], kcal+arr[depth][1]) # 현재 햄버거 선택
  dfs(depth+1, taste, kcal) # 선택 x

T = int(input())
for test_case in range (1, T+1):

  n, l = map(int, input().split()) # 재료의 수, 제한 칼로리

  arr = [list(map(int, input().split())) for _ in range (n)]
  visited = [False] * n

  max_taste = 0
  dfs(0, 0, 0)

  print(f'#{test_case} {max_taste}')