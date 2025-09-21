from collections import deque
from itertools import combinations
import copy
import sys

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(tmp):
    q = deque()

    # --- 바이러스인 위치를 모두 큐에 넣는다 ---
    for i in range (n):
        for j in range (m):
            if tmp[i][j] == 2:
                q.append((i, j))

    while q:
        x, y = q.popleft()

        for dx, dy in directions:
            nx, ny = x+dx, y+dy

            if 0<=nx<n and 0<=ny<m and tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                q.append((nx, ny))

    cnt = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                cnt += 1

    return cnt


input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range (n)]

# 빈 칸 위치 수집
empty_spaces = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            empty_spaces.append((i, j))

max_area = 0

# --- 벽 3개 세우기 ---
for walls in combinations(empty_spaces, 3): # 조합 생성
    tmp = copy.deepcopy(graph)

    for x, y in walls: # 벽 세우기...
        tmp[x][y] = 1

    area = bfs(tmp)

    if area > max_area: max_area = area # 최댓값 갱신

print(max_area)