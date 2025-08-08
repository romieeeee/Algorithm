def dfs(v):
    global virus
    visited[v] = True

    for nxt in graph[v]:
        if graph[nxt] and not visited[nxt]:
            virus += 1
            dfs(nxt)

n = int(input())
net = int(input())

graph = [[] for _ in range (n+1)]
for _ in range (net):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n+1)

virus = 0
dfs(1) # 1번 컴퓨터부터 시작

print(virus)