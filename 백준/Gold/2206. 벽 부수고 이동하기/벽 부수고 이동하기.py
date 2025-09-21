from collections import deque
import sys

input = sys.stdin.readline

def bfs():
    q = deque()
    q.append((0, 0, 0))
    visited[0][0][0] = 1  

    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    while q:
        x, y, broken = q.popleft()

        if (x, y) == (n-1, m-1):
            print(visited[x][y][broken])
            return

        for dx, dy in directions:
            nx, ny = x+dx, y+dy

            if 0<=nx<n and 0<=ny<m:
                # 이동할 칸이 길인 경우!
                if graph[nx][ny] == 0 and visited[nx][ny][broken] == 0:
                    visited[nx][ny][broken] = visited[x][y][broken] + 1
                    q.append((nx, ny, broken))
                
                # 이동할 칸이 벽이고 아직 벽을 부수지 않았다
                # 해당 칸을 벽을 부수고 간 경우가 없다면
                elif graph[nx][ny] == 1 and broken == 0 and visited[nx][ny][1] == 0:
                    visited[nx][ny][1] = visited[x][y][broken] + 1
                    q.append((nx, ny, 1))

    print(-1)

n, m = map(int, input().split())  # 0: 이동 x, 1: 이동 o

graph = [[int(x) for x in input().strip()] for _ in range (n)]
visited = [[[0, 0] for _ in range(m)] for _ in range(n)]

bfs()