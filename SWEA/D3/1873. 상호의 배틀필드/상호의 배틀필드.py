T = int(input())
for test_case in range (1, T+1):

    dest = [[-1, 0], [1, 0], [0, -1], [0, 1]] # up down left right

    def isTank(str):
        if str in ['^', 'v', '<', '>']:
            return True  

        return False

    def outOfRange(x, y):
        if x < 0 or y < 0 or x >= h or y >= w: # 범위를 벗어나면
            return True
        
        return False

    h, w = map(int, input().split()) # 높이, 너비
    graph = [[x for x in input()] for _ in range (h)]

    n = int(input())
    tank = input() # up down left right shoot

    # 게임 맵 밖일 경우 이동 x

    x = y = 0
    d = [0, 0]

    # 시작 탱크 찾기
    find = False
    for i in range (h):
        for j in range (w):
            if isTank(graph[i][j]):
                find = True
                x, y = i, j # 탱크 위치 set

                if graph[i][j] == '^': # 위를 바라보는 전차
                    d = dest[0]
                elif graph[i][j] == 'v':
                    d = dest[1]
                elif graph[i][j] == '<':
                    d = dest[2]
                elif graph[i][j] == '>':
                    d = dest[3]

            if find:
                break
        
        if find:
            break
                

    for i in range (n):
        if tank[i] == 'U':
            d = dest[0] # 바라보는 방향을 위로 바꾸고

            nx = x+d[0]
            ny = y+d[1]
            graph[x][y] = '^'
            
            if not outOfRange(nx, ny) and graph[nx][ny] == '.':
                graph[x][y] = '.'
                x, y = nx, ny 
                graph[x][y] = '^'


        elif tank[i] == 'D':
            d = dest[1] 
            
            nx = x + d[0]
            ny = y + d[1]
            graph[x][y] = 'v'

            if not outOfRange(nx, ny) and graph[nx][ny] == '.':
                graph[x][y] = '.'
                x, y = nx, ny
                graph[x][y] = 'v'


        elif tank[i] == 'L':
            d = dest[2]

            nx = x+d[0]
            ny = y+d[1]
            graph[x][y] = '<'

            if not outOfRange(nx, ny) and graph[nx][ny] == '.':
                graph[x][y] = '.'
                x, y = nx, ny
                graph[x][y] = '<'


        elif tank[i] == 'R':
            d = dest[3] 

            nx = x+d[0]
            ny = y+d[1]
            graph[x][y] = '>'

            if not outOfRange(nx, ny) and graph[nx][ny] == '.':
                graph[x][y] = '.'
                x, y = nx, ny
                graph[x][y] = '>'


        elif tank[i] == 'S':
        # 포탄은 벽에 부딪히면 소멸, 벽돌벽은 파괴되고 강철벽 or 게임 맵 밖은 아무일도 일어나지 않는다
            
            nx, ny = x, y

            while True:
                nx += d[0]
                ny += d[1]

                # 포탄 발사 -> 벽돌 벽 or 강철 벽 or 게임 밖 만날 때까지 직진
                if outOfRange(nx, ny):
                    break

                if graph[nx][ny] == '#':
                    break
                
                if graph[nx][ny] == '*':
                    graph[nx][ny] = '.'
                    break
                
                
    print(f"#{test_case}", end = ' ')
    
    for row in graph:
        print(''.join(row))
