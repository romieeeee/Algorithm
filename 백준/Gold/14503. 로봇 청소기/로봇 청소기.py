import sys
input = sys.stdin.readline

# 북(0), 동(1), 남(2), 서(3)
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 범위를 벗어나는지 확인
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m
         
def has_uncleaned(x, y):
    """현재 위치 기준 4방향 중 청소되지 않은 칸(0)이 있는지 확인"""
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and room[nx][ny] == 0:
            return True
    return False

n, m = map(int, input().split())
x, y, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range (n)]

clean_cnt = 0

# 0 : 청소되지 않은 칸, 1: 벽!
while True:
    # 1. 현재 칸이 아직 청소되지 않은 경우
    if room[x][y] == 0: 
        room[x][y] = 2 # 청소한다! 
        clean_cnt += 1

    # 2. 청소되지 않은 빈 칸이 없는 경우
    if not has_uncleaned(x, y):
        back_dir = (d + 2) % 4 # 후진 시도
        nx, ny = x+directions[back_dir][0], y+directions[back_dir][1]

        # 벽이거나 범위 밖이면 종료
        if not in_range(nx, ny) or room[nx][ny] == 1: # 뒤가 벽...
            print(clean_cnt)
            break # 종료

        x, y = nx, ny # 후진 성공
             
    else: # 3. 청소되지 않은 빈 칸이 있다면...
        for i in range (4):
            d = (d+3)%4
            nx, ny = x+directions[d][0], y+directions[d][1]
            
            if in_range(nx, ny) and room[nx][ny] == 0:
                x, y = nx, ny # 이동
                break
    