from collections import deque
from functools import lru_cache
import sys

input = sys.stdin.readline

directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def bfs(start_x, start_y):
    visited = [[-1] * w for _ in range(h)]

    q = deque()
    q.append((start_x, start_y))
    visited[start_x][start_y] = 0

    while q:
        x, y = q.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] != 'x' and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

    return visited


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
         break
        
    graph = []
    points = [] # 시작점, 더러운 칸 위치 저장

    x = y = 0

    for i in range (h):
        row = list(input().rstrip())

        for j in range (w):
            if row[j] == 'o':  # 시작 위치
                x, y = i, j
            elif row[j] == '*':  # 더러운 칸
                points.append((i, j))

        graph.append(row)
             
    points.insert(0, [x, y]) # 시작 위치 추가
    n = len(points)

    dist = [[-1] * n for _ in range (n)]

    # 각 포인트 사이의 최단 거리 구하기
    for i in range (n):
        res = bfs(points[i][0], points[i][1]) 

        for j in range (n):
            dist[i][j] = res[points[j][0]][points[j][1]]
            
    # 도달하지 못한 더러운 칸이 있다면
    impossible = False
    for i in range(n):
        for j in range(n):
            if dist[i][j] == -1:
                print(-1)
                impossible = True
                break
        if impossible:
            break

    if impossible:
        continue
    
    # 비트마스크 DP (TSP)
    @lru_cache(None)
    def tsp(pos, mask):
        if mask == (1 << n) - 1:  # 모든 칸 청소 완료
            return 0

        res = float('inf')
        for nxt in range(1, n):  # 시작점 제외
            if not (mask & (1 << nxt)):
                res = min(res, dist[pos][nxt] + tsp(nxt, mask | (1 << nxt)))
        return res

    answer = tsp(0, 1)  # 시작점은 이미 방문
    print(answer)