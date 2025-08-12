from collections import deque

def bfs(sx, sy):
    global visited

    q.append((sx, sy))
    visited[sx][sy] = True

    while q:
        x, y = q.popleft()

        if (x, y) == (ex, ey):
            return board[x][y]

        for dx, dy in dir:
            nx, ny = x+dx, y+dy

            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True

                board[nx][ny] = board[x][y] + 1

dir = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]

T = int(input())
for _ in range (T):
    n = int(input())
    board = [[0] * n for _ in range (n)]
    visited = [[0] * n for _ in range (n)] 

    # 시작 좌표
    sx, sy = map(int, input().split())

    # 도착 좌표
    ex, ey = map(int, input().split())

    q = deque()

    res = bfs(sx, sy)
    print(res)