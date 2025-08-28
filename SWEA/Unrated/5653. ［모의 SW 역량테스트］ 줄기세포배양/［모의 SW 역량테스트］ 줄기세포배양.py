from collections import deque

direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# 번식 처리 함수
def reproduction(new_cells, board):
    global cells

    # 생명력(x[2]) 큰 순서대로 번식 처리
    new_cells.sort(key=lambda x: x[2], reverse=True)

    for nx, ny, life in new_cells:
        
        # 빈 칸이면 번식 성공
        if board[nx][ny] == 0:
            board[nx][ny] = life
            cells.append([nx, ny, life, life, 0])  # 새로 태어난 세포 추가

# 한 시간 동안 세포 상태 업데이트
def update_cells(board, direction):
    global cells

    new_cells = []            # 이번 시간에 번식할 후보 세포
    size = len(cells)             # 현재 살아있는 세포 수
    
    for _ in range(size):
        x, y, life, remain, state = cells.popleft()
        
        if state == 0:  # 비활성 상태
            if remain > 1:
                cells.append([x, y, life, remain-1, 0])
            else:
                cells.append([x, y, life, life, 1])
        
        elif state == 1:  # 활성 상태
            for dx, dy in direction:
                nx, ny = x+dx, y+dy
                if board[nx][ny] == 0:
                    new_cells.append((nx, ny, life))
           
            # 생존 시간 감소
            if remain > 1:
                cells.append([x, y, life, remain-1, 1])
            
            # remain == 1이면 세포 사망!
    
    # 번식 처리
    reproduction(new_cells, board)

T = int(input())
for tc in range(1, T + 1):
    n, m, k = map(int, input().split())
    board = [[0] * (m + 2*k) for _ in range(n + 2*k)] 

    cells = deque()  # 살아있는 세포 큐

    # 초기 세포 배치
    for i in range(n):
        row = list(map(int, input().split()))
        for j in range(m):
            if row[j] > 0:
                x, y = i+k, j+k
                life = row[j]
                board[x][y] = life
                cells.append([x, y, life, life, 0])  # 초기에는 비활성 상태

    # K시간 동안 세포 상태 업데이트
    for _ in range(k):
        update_cells(board, direction)

    print(f"#{tc} {len(cells)}")
