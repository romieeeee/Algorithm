import sys

input = sys.stdin.readline

# 범위를 벗어나는지 확인
def outOfRange(x, y):
    if 0<=x<n and 0<=y<m:
        return False
    return True
         
# 후진하는 방향 찾기
def back_direction(d):
    if d == 0: return 2
    elif d == 1: return 3
    elif d == 2: return 0
    elif d == 3: return 1

# when(d) 0: 북, 1: 동, 2: 남, 3: 서
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def rotate(d):
    if d == 0: return 3
    elif d == 1: return 0
    elif d == 2: return 1
    elif d == 3: return 2

def isAllCleaned(x, y):

    # 현재 칸을 기준으로 4방향 탐색
    for dx, dy in directions:
        nx, ny = x+dx, y+dy

        # 범위 벗어나면 무시
        if outOfRange(nx, ny): 
            continue

        # 아직 청소되지 않은 칸이 있다면
        if room[nx][ny] == 0:
            return False
            
    return True
        

n, m = map(int, input().split())
x, y, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range (n)]
res = 0

# 청소한다...
# 현재 칸 청소 xx -> 청소한다
# 바라보는 방향을 유지한채로 후진!
# 바라보는 방향의 뒤쪽칸이 벽이면 후진 ㄴㄴ
# 현재 칸의 주변 4칸 중에 청소되지 않은 빈 칸이 있다면 90도 회전
# 바라보는 방향을 기준으로 앞쪽칸이 청소되지 않으면 한칸 전진

# 0 : 청소되지 않은 칸, 1: 벽!
while True:
    # 1. 현재 칸이 아직 청소되지 않은 경우
    if room[x][y] == 0: 
        room[x][y] = 2 # 청소한다! 청소 -> 2
        # print('clean!: ', x, y)
        res += 1

    # 2. 청소되지 않은 빈 칸이 없는 경우 후진 시도
    if isAllCleaned(x, y):
        idx = back_direction(d)
        nx, ny = x+directions[idx][0], y+directions[idx][1]

        if outOfRange(nx, ny) or room[nx][ny] == 1: # 뒤가 벽...
            # for i in range (n):
            #     print(*room[i])

            # print('is Wall!!!')
            print(res)
            break # 종료
        else:
            x, y = nx, ny
             
    else: # 3. 청소되지 않은 빈 칸이 있다면...
        for i in range (1, 5):
            d = rotate(d%4)
            nx, ny = x+directions[d][0], y+directions[d][1]
            if not outOfRange(nx, ny) and room[nx][ny] == 0:
                x, y = nx, ny # 이동...
                break
    