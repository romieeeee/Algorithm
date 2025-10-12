T = int(input())
for test_case in range (1, T+1):

    def catchFlies(x, y):
        total_plus = graph[x][y]  # '+' 모양
        for i in range(1, m):
            if x - i >= 0: # 상
                total_plus += graph[x - i][y]

            if x + i < n: # 하
                total_plus += graph[x + i][y]

            if y - i >= 0: # 좌
                total_plus += graph[x][y - i]

            if y + i < n: # 우
                total_plus += graph[x][y + i]


        total_diag = graph[x][y] # 'x' 모양
        for i in range(1, m):

            if x - i >= 0 and y - i >= 0: # 좌상
                total_diag += graph[x - i][y - i]

            if x - i >= 0 and y + i < n: # 우상
                total_diag += graph[x - i][y + i]

            if x + i < n and y - i >= 0: # 좌하
                total_diag += graph[x + i][y - i]

            if x + i < n and y + i < n: # 우하
                total_diag += graph[x + i][y + i]

        return max(total_plus, total_diag)
            

    n, m = map(int, input().split()) # m칸의 파리...
    graph = [list(map(int, input().split())) for _ in range (n)] # n*n

    max_flies = 0

    for i in range(n):
        for j in range(n):
            flies = catchFlies(i, j) 
            if flies > max_flies: max_flies = flies


    print(f"#{test_case} {max_flies}")
