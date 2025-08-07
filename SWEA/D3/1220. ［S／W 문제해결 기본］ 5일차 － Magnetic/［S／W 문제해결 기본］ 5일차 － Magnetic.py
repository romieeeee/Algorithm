for test_case in range(1, 11):
    n = int(input()) # 항상 100
    graph = [list(map(int, input().split())) for _ in range (n)] # 크기는 항상 100*100

    # N극: 1, S극: 2
    flag_n = False

    res = 0

    # 열로 비교
    for i in range (n):
        col = [graph[x][i] for x in range (n)]

        for j in range (100):
            if col[j] == 1:
                flag_n = True

            if flag_n and col[j] == 2:
                res += 1

                flag_n = False

        flag_n = False

    print(f'#{test_case} {res}')