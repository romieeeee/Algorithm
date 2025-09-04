def dfs(cnt):
  global ans
  if cnt == change:
    tmp = int(''.join(map(str, num)))
    ans = max(ans, tmp)
    return

  for i in range (len(num)):
    for j in range (i+1, len(num)):
      num[i], num[j] = num[j], num[i]
      tmp = int(''.join(map(str, num)))

      if (cnt, tmp) not in visited:
          visited.append((cnt, tmp))
          dfs(cnt+1)
      
      num[i], num[j] = num[j], num[i] # 백트래킹

T = int(input())
for test_case in range(1, T + 1):
  n, change = map(int, input().split())
  num = [int(x) for x in str(n)]
  visited = []
  
  ans = 0
  dfs(0)
  
  print(f"#{test_case} {ans}")