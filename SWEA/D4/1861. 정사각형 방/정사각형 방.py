def dfs(x, y):
    global room, cnt, max_cnt

    dir = [[1, 0], [0,1], [-1, 0], [0, -1]]

    for d in dir:
        nx, ny = x+d[0], y+d[1]

        # 범위 내에 있고 빙문하지 않았고 현재 값보다 1 크면 
        if 0<=nx<n and 0<=ny<n:
            if graph[nx][ny] - graph[x][y] == 1:
                cnt += 1
                dfs(nx, ny)

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range (n)] # n*n 배열 생성

    room = n
    max_cnt = 0

    for i in range (n):
        for j in range (n):
            cnt = 1
            dfs(i, j)

            if cnt > max_cnt:
                max_cnt = cnt
                room = graph[i][j]

            elif cnt == max_cnt:
                room = min(room, graph[i][j])

    print(f'#{test_case} {room} {max_cnt}')