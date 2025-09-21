from collections import deque
import sys

def bfs():
    q = deque()
    q.append((0, 0, 0))

    visited[0][0][0] = 1

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while q:
        x, y, broken = q.popleft()

        if (x, y) == (n-1, m-1):
            print(visited[x][y][broken])
            return
        

        for dx, dy in directions:
            nx, ny = x+dx, y+dy 

            if 0<=nx<n and 0<=ny<m: # 범위 확인

                # 이동할 칸이 길인 경우
                if graph[nx][ny] == 0 and not visited[nx][ny][broken]:
                    visited[nx][ny][broken] = visited[x][y][broken] + 1
                    q.append((nx, ny, broken))

                # 이동할 칸이 벽이고 부술 수 있는 벽의 개수가 k 보다 작다면
                elif graph[nx][ny] == 1 and broken < k and not visited[nx][ny][broken+1]:
                    visited[nx][ny][broken+1] = visited[x][y][broken] + 1
                    q.append((nx, ny, broken+1))

    print(-1)

input = sys.stdin.readline

n, m, k = map(int, input().split())

graph = [[int(x) for x in input().strip()] for _ in range (n)]

visited = [[[0] * (k+1) for _ in range(m)] for _ in range(n)]

bfs()
