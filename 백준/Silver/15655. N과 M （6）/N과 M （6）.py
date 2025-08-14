def dfs(depth, start):
    global arr
    
    if depth == m:
        print(*arr)
        return

    for i in range (start, n):
        if not visited[i]:
            visited[i] = True
            arr[depth] = nums[i]

            dfs(depth+1, i)
            
            visited[i] = False

n, m = map(int, input().split())
nums = list(map(int, input().split()))

visited = [0] * n
arr = [0] * m

nums.sort()
dfs(0, 0)