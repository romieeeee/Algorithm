T = int(input())

# 방향 순서 (0: 상, 1: 우, 2: 좌, 3: 하)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def change_dir(block, d):
    if block == 1:
        if d == 0: d = 2
        elif d == 1: d = 3
        elif d == 2: d = 1
        elif d == 3: d = 0
    elif block == 2:
        if d == 0: d = 1
        elif d == 1: d = 3
        elif d == 2: d = 0
        elif d == 3: d = 2
    elif block == 3:
        if d == 0: d = 3
        elif d == 1: d = 2
        elif d == 2: d = 0
        elif d == 3: d = 1
    elif block == 4:
        if d == 0: d = 2
        elif d == 1: d = 0
        elif d == 2: d = 3
        elif d == 3: d = 1
    elif block == 5: # 현재방향의 반대
        d = (d + 2) % 4
    
    return d

def solution(x, y, d):
    sx, sy = x, y
    score = 0

    while True:
        x += dx[d]
        y += dy[d]

        # 1) 벽에 부딪힌 경우
        if x < 0 or x >= n or y < 0 or y >= n:
            d = (d + 2) % 4
            score += 1
            continue

        # 2) 블랙홀 or 시작점 복귀
        if (x, y) == (sx, sy) or graph[x][y] == -1:
            return score

        # 3) 빈칸이면 계속 진행
        if graph[x][y] == 0:
            continue

        # 4) 블록(1~5)
        if 1 <= graph[x][y] <= 5:
            d = change_dir(graph[x][y], d)
            score += 1
            continue

        # 5) 웜홀(6~10)
        if 6 <= graph[x][y] <= 10:
            num = graph[x][y]
            for wx, wy in holes[num]:
                if (wx, wy) != (x, y):  # 현재 위치 제외한 짝으로 이동
                    x, y = wx, wy
                    break



for test_case in range (1, T+1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]

    holes = [[] for _ in range (11)]
    for i in range (n):
        for j in range (n):
            if 0 <= graph[i][j] <= 10:
                holes[graph[i][j]].append((i, j))


    # ===== 완전 탐색(모든 빈칸에서 4방향 모두 탐색) =====
    max_val = 0
    for i in range (n):
        for j in range(n):
            if graph[i][j] == 0:
                for d in range (4): 
                    max_val = max(max_val, solution(i, j, d))

    print(f"#{test_case} {max_val}")
