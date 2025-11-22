dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def dfs(x, y,):
    global cnt 

    for i in range (4):
        nx, ny = x+dx[i], y+dy[i]

        if 0<=nx<n and 0<=ny<n and graph[x][y]+1 == graph[nx][ny]:
                cnt += 1
                dfs(nx, ny)

T = int(input())
for test_case in range (1, T+1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range (n)]

    start_num = 0
    max_cnt = 0
    for i in range (n):
        for j in range (n):
            cnt = 1
            dfs(i, j)

            if cnt > max_cnt:
                max_cnt = cnt
                start_num = graph[i][j]

            if cnt == max_cnt:
                start_num = min(start_num, graph[i][j])

    print(f'#{test_case} {start_num} {max_cnt}')