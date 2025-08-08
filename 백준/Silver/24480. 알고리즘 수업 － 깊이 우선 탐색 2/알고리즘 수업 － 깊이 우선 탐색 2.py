import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 증가 

def dfs(v):
    global order_cnt
    visited[v] = True

    order[v] = order_cnt
    order_cnt += 1

    for nxt in sorted(graph[v], reverse=True): # 인접 정점은 내림차순으로 방문한다
        if not visited[nxt]:
            dfs(nxt)

n, m, r = map(int, sys.stdin.readline().split())

# graph = [[0] * n for _ in range (n)]
graph = [[] for _ in range((n+1))]

for _ in range (m):
    u, v = map(int, sys.stdin.readline().split())

    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n+1)

order = [0] * (n+1)
order_cnt = 1

dfs(r)

for i in range (1, n+1):
    print(order[i])