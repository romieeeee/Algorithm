import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) 

def dfs(x):
    global cnt

    visited[x] = True

    for nxt in graph[x]:
        if not visited[nxt]:
            dfs(nxt)

n, m = map(int, input().split()) # 정점의 개수, 간선의 개수

graph = [[] for _ in range (n+1)]
visited = [False] * (n + 1)

for _ in range (m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
for i in range (1, n+1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)