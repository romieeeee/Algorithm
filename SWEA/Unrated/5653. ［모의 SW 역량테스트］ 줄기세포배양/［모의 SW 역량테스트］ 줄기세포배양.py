from collections import deque

dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

T = int(input())
for tc in range(1, T + 1):
    n, m, k = map(int, input().split())
    board = [[0] * (m + 2*k) for _ in range(n + 2*k)]
    cells = deque()

    # 초기 세포 배치 (중앙에 위치시키기)
    for i in range(n):
        row = list(map(int, input().split()))
        for j in range(m):

            # 세포가 존재하면 전부 큐에 담는다
            if row[j] > 0:
                x, y = i+k, j+k
                life = row[j]
                board[x][y] = life
                cells.append([x, y, life, life, 0])  
                # (x,y, 생명력, 남은시간, 상태:0비활성/1활성)

    # 줄기세포 번식
    for t in range(1, k+1):
        new_cells = []
        size = len(cells)

        for _ in range(size):
            x, y, life, remain, state = cells.popleft()

            if state == 0:  # 비활성
                if remain > 1:
                    cells.append([x, y, life, remain-1, 0])
                else:  # 활성화 시작
                    cells.append([x, y, life, life, 1])

            elif state == 1:  # 활성
                
                # 번식 시도
                for dx, dy in dir:
                    nx, ny = x+dx, y+dy

                    if board[nx][ny] == 0:  
                        new_cells.append((nx, ny, life))
                
                # 생존 시간 감소
                if remain > 1:
                    cells.append([x, y, life, remain-1, 1])
                # remain == 1 이면 죽음 (큐에 안넣음)

        # 번식 처리 (생명력 큰 세포가 우선)
        new_cells.sort(key=lambda x: -x[2])
        for nx, ny, life in new_cells:
            if board[nx][ny] == 0:
                board[nx][ny] = life
                cells.append([nx, ny, life, life, 0])

    print(f"#{tc} {len(cells)}")
