# 백준 1018
n, m = map(int, input().split())
board = [list(x for x in input()) for _ in range (n)]

# 색칠해야하는 경우의 수 
# 행 별로 검사하면 된다
paint = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
         ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']] 

min_cnt = n*m
for i in range(n - 7):
    for j in range(m - 7):
        cnt1 = cnt2 = 0
        for x in range(8):
            for y in range(8):
                if (x + y) % 2 == 0:
                    if board[i + x][j + y] != 'W':
                        cnt1 += 1
                    if board[i + x][j + y] != 'B':
                        cnt2 += 1
                else:
                    if board[i + x][j + y] != 'B':
                        cnt1 += 1
                    if board[i + x][j + y] != 'W':
                        cnt2 += 1
        min_cnt = min(min_cnt, cnt1, cnt2)

print(min_cnt)
