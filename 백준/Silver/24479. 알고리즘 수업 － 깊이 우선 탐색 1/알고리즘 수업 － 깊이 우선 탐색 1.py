import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 증가 

def dfs(v):
    global cnt

    visited[v] = True
    order[v] = cnt
    cnt += 1

    for next in sorted(graph[v]):
        if not visited[next]:
            dfs(next)

n, m, r = map(int, sys.stdin.readline().split())

# 정점 개수 N이 최대 10 만이라서 인접리스트로 풀어야함
# graph = [[0] * n for _ in range (n)]

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
order = [0] * (n+1)
cnt = 1

for _ in range (m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(r)

for i in range (1, n+1):
    print(order[i])