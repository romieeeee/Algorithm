N = int(input()) # 컴퓨터의 수
M = int(input()) # 간선의 수

def dfs(idx):
    global visited, count

    visited[idx] = True
    count += 1

    for next in range(N+1):
        if(not visited[next] and graph[idx][next]):
            dfs(next)

graph = [[False] * (N+1) for _ in range (N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

visited = [False] * (N+1)

count = 0
dfs(1) # 1번 컴퓨터가 웜 바이러스에 걸렸을 때!

print(count-1) # 1번 컴퓨터 제외