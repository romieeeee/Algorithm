import sys
from collections import deque

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]      

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited = [[0] * m for _ in range (n)]
    visited[x][y] = 1

    value = 0
    while q:
        cx, cy = q.popleft()

        for dx, dy in directions:
            nx, ny = cx+dx, cy+dy
            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny] and graph[nx][ny] == 'L':
                    q.append((nx, ny))
                    visited[nx][ny] = visited[cx][cy] + 1

                    if visited[nx][ny] > value: value = visited[nx][ny]

    return value

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[x for x in input().strip()] for _ in range (n)] # 'L' or 'W'

max_res = 0
for i in range (n):
    for j in range (m):
        if graph[i][j] == 'L':
            res = bfs(i, j)

            if res > max_res: max_res = res

print(max_res-1)