def dfs(depth, start):
    global arr

    if depth == m:
        print(*arr)
        return

    for i in range (start, n+1):
        arr[depth] = i
        dfs(depth+1, i)

n, m = map(int, input().split())
arr = [0] * m

dfs(0, 1)