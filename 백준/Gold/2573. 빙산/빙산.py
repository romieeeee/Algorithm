import sys
from collections import deque

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx+dx[i], cy+dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] > 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))

# 해당 칸에 동서남북 방향으로 붙어있는 0이 저장된 칸의 개수만큼 줄어든다
def melt(graph):
    # 이번 해에 녹을 좌표와 녹는 양만 기록
    melt_list = []
    for x in range(n):
        for y in range(m):
            if graph[x][y] > 0:
                cnt = 0
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                        cnt += 1
                if cnt > 0:
                    melt_list.append((x, y, cnt))
    
    # 한 번에 녹이기
    for x, y, cnt in melt_list:
        graph[x][y] = max(0, graph[x][y] - cnt)

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

year = 0

while True:
    visited = [[False] * m for _ in range(n)]

    # ===== 덩어리 세기 =====
    cnt = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0 and not visited[i][j]:
                visited[i][j] = True
                bfs(i, j)
                cnt += 1

    if cnt == 0:
        print(0)
        break
    
    if cnt >= 2:
        print(year)
        break
    
    # ===== 빙하 녹이기 =====
    melt(graph)
    year += 1
