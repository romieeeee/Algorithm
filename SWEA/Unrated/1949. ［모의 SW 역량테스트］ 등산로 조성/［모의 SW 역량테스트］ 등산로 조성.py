# 가장 높은 봉우리에서 시작한다
# 높이가 같거나 낮은 지형은 갈 수 없다

dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def dfs(x, y, depth, used):
    global max_depth
    max_depth = max(max_depth, depth)

    visited[x][y] = True

    for dy, dx in dir:
        nx, ny = x+dx, y+dy

        if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
            if graph[nx][ny] < graph[x][y]:
                dfs(nx, ny, depth+1, used)
            elif not used: # 공사를 아직 안한 경우
                if graph[nx][ny] - k < graph[x][y]: 
                    temp = graph[nx][ny]

                    graph[nx][ny] = graph[x][y] - 1
                    dfs(nx, ny, depth+1, True)

                    graph[nx][ny] = temp

    visited[x][y] = False

T = int(input())
for test_case in range (1, T+1):
    n, k = map(int, input().split()) 
    graph = [(list(map(int, input().split()))) for _ in range (n)]

    visited = [[False] * n for _ in range (n)]

    start = 0
    for i in range (n):
        start = max(start, max(graph[i]))

    max_depth = 0
    for i in range (n):
        for j in range (n):

            if graph[i][j] == start:
                # x, y, depth, 공사 여부
                dfs(i, j, 1, False)

    print(f'#{test_case} {max_depth}')
            