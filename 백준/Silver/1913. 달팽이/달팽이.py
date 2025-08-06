n = int(input())
target = int(input()) # 찾고자 하는 숫자

graph = [[0]*n for _ in range(n)]

dir = 0 # 초기 방향 값
dx = [-1, 0, 1, 0]  
dy = [0, 1, 0, -1]

x = y = n//2 # 시작 위치

num = 1
step = 1 # 방향으로 step 만큼 이동 (증가)

# -- 초기 값 설정 --
graph[x][y] = num
num += 1

ans_x = ans_y = x+1 # target의 위치
while num <= n*n:
    for _ in range(2):  # 두 번 반복
        
        for _ in range(step):
            x, y = x+dx[dir], y+dy[dir]
            
            if num > n*n:
                break  # 먼저 종료 확인

            graph[x][y] = num

            # if num == target:
            #     ans_x, ans_y = x+1, y+1

            num += 1
            
            if num > n*n:
                break
        
        dir = (dir + 1) % 4
    
    step += 1

for i in range (n):
    for j in range (n):
        if graph[i][j] == target:
            ans_x, ans_y = i+1, j+1

for row in graph:
    print(*row)
print(ans_x, ans_y)
