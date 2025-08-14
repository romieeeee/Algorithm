def dfs(depth):
    global arr

    if depth == m:
        print(*arr)
        return
    
    for i in range (1, n+1):
        arr[depth] = i
        dfs(depth+1)

n, m = map(int, input().split())
arr = [0] * m

dfs(0) # depth 0 부터 시작