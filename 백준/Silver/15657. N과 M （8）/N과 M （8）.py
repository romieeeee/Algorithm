def dfs(depth, start):
    global arr

    if depth == m:
        print(*arr)
        return
    
    for i in range (start, n):
        arr[depth] = nums[i]
        dfs(depth+1, i)

n, m = map(int, input().split())

arr = [0] * m
nums = list(map(int, input().split()))

nums.sort()
dfs(0, 0)