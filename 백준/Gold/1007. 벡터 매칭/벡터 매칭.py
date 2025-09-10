def dfs(depth, start):
    global min_value
    if depth == (n // 2):
        a_x = a_y = b_x = b_y = 0

        for i in range(n):
            if visited[i]:
                a_x += coord[i][0]
                a_y += coord[i][1]
            else:
                b_x += coord[i][0]
                b_y += coord[i][1]

        dx = a_x - b_x
        dy = a_y - b_y
        value = (dx**2 + dy**2) ** 0.5

        min_value = min(min_value, value)
        return

    for i in range(start, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, i + 1)
            visited[i] = False


tc = int(input())
for _ in range(tc):
    n = int(input())
    coord = [list(map(int, input().split())) for _ in range(n)]
    visited = [False] * n

    min_value = 1e9
    dfs(0, 0)

    print(f"{min_value:.6f}")
