for test_case in range(1, 11):
    _ = int(input())
    graph = [list(map(int, input().split())) for _ in range (100)] # 크기는 항상 100*100

    # 시작 지점 찾기
    x = y = 0
    for i in range (99, -1, -1):
        for j in range (99, -1, -1):
            if graph[i][j] == 2:
                (x, y) = (i, j)

    while x > 0:

        if y > 0 and graph[x][y-1] == 1:
            while y > 0 and graph[x][y-1] == 1:
                y -= 1

        elif y < 99 and graph[x][y+1] == 1:
            while y < 99 and graph[x][y+1]:
                y += 1

        x -= 1

    print(f'#{test_case} {y}')