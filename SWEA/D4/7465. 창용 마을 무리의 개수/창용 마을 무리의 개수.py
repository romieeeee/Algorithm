def dfs(v):
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(i)


T = int(input())
for test_case in range (1, T+1):
    n, m = map(int, input().split())

    graph = [[] * (n+1) for _ in range (n+1)]
    visited = [False] * (n+1)

    for _ in range (m):
        u, v = map(int, input().split())

        graph[u].append(v)
        graph[v].append(u)

    res = 0
    for i in range (1, n+1):
        if not visited[i]:
            res += 1
            
            visited[i] = True
            dfs(i)

            
    print(f'#{test_case} {res}')