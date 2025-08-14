def dfs(depth):
    global arr

    if depth == m:
        print(*arr)
        return
    
    for i in range (n):
        arr[depth] = nums[i]

        dfs(depth+1)

n, m = map(int, input().split())

arr = [0] * m
nums = list(map(int, input().split()))

nums.sort()
dfs(0)