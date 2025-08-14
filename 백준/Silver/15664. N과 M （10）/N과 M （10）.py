def dfs(depth, start):
    global arr

    if depth == m:
        print(*arr)
        return
    
    prev = -1
    for i in range (start, n):
        if not visited[i] and prev != nums[i]:
            visited[i] = True
            arr[depth] = nums[i]

            prev = nums[i]

            dfs(depth+1, i)

            visited[i] = False

n, m = map(int, input().split())
nums = list(map(int, input().split()))

arr = [0] * m
visited = [False] * n

nums.sort()
dfs(0, 0)