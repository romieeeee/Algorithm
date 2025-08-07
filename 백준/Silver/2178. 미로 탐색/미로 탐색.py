from collections import deque

def bfs(x, y):
    q = deque()
    q.append([x, y])

    while q:
        x, y = q.popleft()

        for i in range (4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 길이 있고, 아직 방문하지 않았다면
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and maze[nx][ny] == 1:
                    maze[nx][ny] = maze[x][y] + 1

                    q.append([nx, ny])

    print(maze[n-1][m-1])

n, m = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(n)]

visited = [[False] * m for _ in range (n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


min_steps = float('inf')

bfs(0, 0)