def dfs(x, y):
    global flag
    visited[x][y] = True

    if graph[x][y] == 3:
        flag = True
        return

    for dx, dy in dir:
        nx, ny = x+dx, y+dy

        if 0<=nx<16 and 0<=ny<16:
            if graph[nx][ny] != 1 and not visited[nx][ny]:
                dfs(nx, ny)

for test_case in range(1, 11):
    _ = int(input())

    # 0: 길, 1: 벽, 2, 시작점, 3: 도착점
    graph = [list(map(int, input())) for _ in range (16)]
    visited = [[False] * 16 for _ in range (16)]

    dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    flag = False
    dfs(1, 1) # (1, 1)에서 시작

    print(f'#{test_case} {1 if flag else 0}')