graph = [[0] * 100 for _ in range (100)] # x, y는 100 이하의 정수
square = [list(map(int, input().split())) for _ in range (4)]

# 행 칠하기 
for sx, sy, ex, ey in square:
        for i in range (sx, ex):
            for j in range (sy, ey):
                graph[i][j] = 1

cnt = 0
for i in range (100):
    for j in range (100):
        if graph[i][j] == 1:
            cnt += 1

print(cnt)