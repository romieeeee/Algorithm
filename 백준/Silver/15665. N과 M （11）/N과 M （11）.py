def dfs(depth):
    global arr

    if depth == m:
        print(*arr)
        return
    
    prev = -1
    for i in range (n):
        if nums[i] != prev:

            arr[depth] = nums[i]
            
            prev = nums[i]

            dfs(depth+1)

n, m = map(int, input().split())
nums = list(map(int, input().split()))

arr = [0] * m

nums.sort()
dfs(0)