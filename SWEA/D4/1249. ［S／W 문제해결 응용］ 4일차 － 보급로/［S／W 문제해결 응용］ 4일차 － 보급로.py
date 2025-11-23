from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs():
    global min_time

    q = deque()
    q.append((0, 0)) # x, y, t
    dist[0][0] = graph[0][0]

    while q:
        x, y = q.popleft()

        for i in range (4):
            nx, ny = x+dx[i], y+dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue

            if dist[x][y]+graph[nx][ny] < dist[nx][ny]:
                dist[nx][ny] = dist[x][y]+graph[nx][ny]
                q.append((nx, ny))


T = int(input())
for test_case in range (1, T+1):
    n = int(input())
    graph = []
    for _ in range (n):
        row = [int(s) for s in input()]
        graph.append(row)

    dist = [[1e9] * n for _ in range (n)]

    bfs()

    print(f'#{test_case} {dist[n-1][n-1]}')