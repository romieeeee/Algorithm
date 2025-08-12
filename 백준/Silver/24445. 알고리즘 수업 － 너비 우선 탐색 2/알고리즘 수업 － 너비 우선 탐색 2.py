import sys
from collections import deque

def bfs():
    global cnt, order
    while q:
        cur = q.popleft()

        for nxt in sorted(graph[cur], reverse=True):  
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)
                cnt += 1
                order[nxt] = cnt

n, m, r = map(int, sys.stdin.readline().split()) # 정점, 간선, 시작 정점

graph = [[] for _ in range (n+1)]
visited = [False] * (n+1)

for _ in range (m):
    u, v = map(int, sys.stdin.readline().split())

    # 무방향 그래프
    graph[u].append(v)
    graph[v].append(u)

q = deque()

q.append(r)
visited[r] = True

cnt = 1

order = [0] * (n+1)
order[r] = cnt

bfs() 

for o in order[1:]:
    print(o)