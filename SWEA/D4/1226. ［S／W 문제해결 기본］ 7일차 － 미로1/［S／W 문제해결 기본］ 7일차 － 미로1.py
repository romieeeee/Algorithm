# def dfs(x, y):
#     global res

#     visited[x][y] = True
#     if graph[x][y] == 3:
#         res = 1
#         return

#     for dx, dy in dir:
#         nx, ny = x+dx, y+dy

#         if 0<=nx<16 and 0<=ny<16:
#             if not visited[nx][ny] and graph[nx][ny] != 1:
#                 dfs(nx, ny)

from collections import deque

def bfs():
    global q, res

    while q:
        cx, cy = q.popleft()

        # 도착점 찾으면 종료
        if graph[cx][cy] == 3:
            res = 1
            return

        for dx, dy in dir:
            nx, ny = cx+dx, cy+dy

            if 0<=nx<16 and 0<=ny<16:
                if not visited[nx][ny] and graph[nx][ny] != 1:
                    visited[nx][ny] = True
                    q.append((nx, ny))


dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for test_case in range(1, 11):
    _ = input()

    graph = [list(map(int, input())) for _ in range (16)]
    visited = [[False] * 16 for _ in range (16)]
    
    x = y= 0
    flag = False
    for i in range(16):
        for j in range (16):
            if graph[i][j] == 2:
                x, y = i, j

                flag = True
                break
        
        if flag: break

    res = 0
    # dfs(x, y)   

    q = deque()
    q.append((x, y))

    visited[x][y] = True
    
    bfs()

    print(f'#{test_case} {res}')