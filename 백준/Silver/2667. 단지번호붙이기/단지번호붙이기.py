def dfs(x, y):
    global cnt
    visited[x][y] = True
    
    for dx, dy in dir:
        nx, ny = x+dx, y+dy

        if 0<=nx<n and 0<=ny<n:
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                cnt += 1
                dfs(nx, ny)


dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

n = int(input())
graph = [list(map(int, input())) for _ in range (n)]
visited = [[False] * n for _ in range (n)]

house = [] # 각 단지의 집 수
for i in range (n):
    for j in range (n):
        if graph[i][j] == 1 and not visited[i][j]: # 단지 시작!
            cnt = 1
            dfs(i, j)
            house.append(cnt)

print(len(house))
for h in sorted(house):
    print(h)
