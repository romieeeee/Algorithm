def dfs(depth, start):
    global arr

    if depth == m:
        print(*arr)
        return
    
    prev = None
    for i in range (start, n):
        if nums[i] != prev:

            arr[depth] = nums[i]
            
            prev = nums[i]

            dfs(depth+1, i)

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

arr = [0] * m

dfs(0, 0)