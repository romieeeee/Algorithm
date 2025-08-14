def perm(depth):
    global arr

    if depth == m:
        print(*arr)  # 현재 순열 출력
        return
    
    for i in range (1, n+1):
        if not visited[i]:
            visited[i] = True
            arr[depth] = i
            perm(depth+1)
            visited[i] = False


n, m = map(int, input().split()) 

arr = [0] * m
visited = [False] * (n+1)

perm(0)