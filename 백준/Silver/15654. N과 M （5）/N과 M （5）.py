def dfs(depth):
    global arr
    
    if depth == m:
        print(*arr)
        return

    for i in range (n):
        if not visited[i]:
            visited[i] = True
            arr[depth] = nums[i]

            dfs(depth+1)

            visited[i] = False

n, m = map(int, input().split())
nums = list(map(int, input().split()))

arr = [0] * m
visited = [False] * (n) # 중복이 없어야 하기 때문에

nums.sort()
dfs(0)