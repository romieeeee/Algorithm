from collections import deque
from itertools import permutations, product

import sys
input = sys.stdin.readline

# 90도 회전 함수
def rotate(board):
    new_board = [[0]*5 for _ in range(5)]
    
    for i in range(5):
        for j in range(5):
            new_board[j][4-i] = board[i][j]
   
    return new_board

def bfs(maze):

    # 시작점/도착점 막혀있으면 탐색 x
    if maze[0][0][0] == 0 or maze[4][4][4] == 0:
        return -1

    q = deque()
    q.append((0, 0, 0, 0))  # x, y, z, dist
    visited = [[[False] * 5 for _ in range(5)] for _ in range(5)]
    visited[0][0][0] = True

    directions = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]

    while q:
        x, y, z, dist = q.popleft()

        # 도착!
        if (x, y, z) == (4, 4, 4):
            return dist

        for dx, dy, dz in directions:
            nx, ny, nz = x + dx, y + dy, z + dz

            if 0 <= nx < 5 and 0 <= ny < 5 and 0 <= nz < 5: # range check
                if not visited[nz][nx][ny] and maze[nz][nx][ny] == 1:
                    visited[nz][nx][ny] = True
                    q.append((nx, ny, nz, dist + 1))
    return -1

# 입력
data = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]

# 각 층별로 4가지 회전 상태 미리 계산
rotations = [[] for _ in range(5)]
for i in range(5):
    cur = data[i]
    
    for _ in range(4):
        rotations[i].append(cur)
        cur = rotate(cur)

min_dist = 1e9

# 5개 층의 순서를 전부 시도 (순열)
for order in permutations(range(5), 5):

    # 5층 각각의 회전 방향을 전부 시도
    for rot_idx in product(range(4), repeat=5):

        # 현재 순서와 회전 상태를 적용한 미로 생성
        maze = []
        for layer, rot in zip(order, rot_idx):
            maze.append(rotations[layer][rot])

        dist = bfs(maze)
        
        if dist != -1:
            min_dist = min(min_dist, dist)
            
            # 최소 거리 12면 즉시 종료
            if min_dist == 12:
                print(12)
                exit(0)

# 결과 출력
if min_dist != 1e9:
    print(min_dist)
else: 
    print(-1)