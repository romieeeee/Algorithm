import sys
from collections import deque

input = sys.stdin.readline

def bfs(x):
    visited = [-1] * (n+1)
    visited[x] = 0
    q = deque([x])

    while q:
        now = q.popleft()
        for nxt in graph[now]:
            if visited[nxt] == -1:
                visited[nxt] = visited[now] + 1
                q.append(nxt)

    return sum(visited[1:])

n, m = map(int, input().split()) # 유저 수, 관계 수
graph = [[] for _ in range(n + 1)]
for _ in range (m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

min_value = 1e9
res = 0

for i in range (1, n+1):
    cnt = bfs(i)

    if cnt < min_value:
        min_value = cnt
        res = i

print(res)