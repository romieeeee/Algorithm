# 한 방향으로 3번 회전하는 경우의 수만 고려해도 결국 모든 경로를 탐색하게 된다
d = [(1, 1), (-1, 1), (-1, -1), (1, -1)]

def dfs(x, y, di, turn, dessert):
    global sx, sy, max_value

    if turn > 3:
        return
    
    if turn == 3 and x == sx and y == sy:
        max_value = max(max_value, len(dessert))
        return
    
    # 현재 방향을 유지하거나... 회전하거나...
    for i in range (2):
        ndir = (di+i)%4
        nx, ny = x+d[ndir][0], y+d[ndir][1]

        # 범위 내에 있고 아직 먹어본적 없는 디저트라면
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] in dessert:
                continue

            dessert.append(graph[nx][ny])

            if i == 0: # 회전하지 않앗숭
                dfs(nx, ny, ndir, turn, dessert)
            else:
                dfs(nx, ny, ndir, turn+1, dessert)

            dessert.remove(graph[nx][ny])


T = int(input())
for test_case in range (1, T+1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range (n)]

    max_value = -1
    for i in range (n):
        for j in range (n):
            sx, sy = i, j
            dfs(i, j, 0, 0, []) # x, y, 현재 방향 인덱스, 회전 횟수, 방문한 디저트

    print(f'#{test_case} {max_value}')