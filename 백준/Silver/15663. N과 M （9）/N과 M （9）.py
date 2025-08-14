def dfs(depth):
    global arr

    if depth == m:
        print(*arr)
        return
    
    prev = -1
    for i in range (n):
        if not visited[i] and nums[i] != prev: # 같은 depth에서 이전에 쓴 숫자이면 건너뛴다
            visited[i] = True
            arr[depth] = nums[i]

            prev = nums[i]

            dfs(depth+1)

            visited[i] = False

n, m = map(int, input().split())
nums = list(map(int, input().split()))

arr = [0] * m
visited = [0] * n

nums.sort()
dfs(0)