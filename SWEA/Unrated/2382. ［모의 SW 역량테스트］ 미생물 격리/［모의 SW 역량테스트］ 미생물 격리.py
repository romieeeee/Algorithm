# 상하좌우
d = [(), (-1, 0), (1, 0), (0, -1), (0, 1)]

# 현재 셀이 빨간 약 위치에 있는지
def isRedCell(x, y):
    return x == 0 or y == 0 or x == n-1 or y == n-1

# 방향을 반대로 바꿔준다
def setDirection(di):
    if di == 1: return 2
    if di == 2: return 1
    if di == 3: return 4
    if di == 4: return 3

T = int(input())
for test_case in range (1, T+1):
    n, m, k = map(int, input().split()) # 셀의 개수, 격리 시간, 미생물 군집의 개수
    micro = [list(map(int, input().split())) for _ in range (k)] # 세로, 가로, 미생물 수, 이동방향
    
    for _ in range (m): # m시간 동안 이동한다
        temp = [[[] for _ in range(n)] for _ in range(n)] # 임시 저장소

        # ===== 이동 시작 =====
        for x, y, cnt, di in micro:
            nx, ny = x + d[di][0], y + d[di][1]
            
            if isRedCell(nx, ny): # 빨간셀을 만나면...
                cnt //= 2 # 반으로 줄어든다 
                di = setDirection(di) # 방향 반대
                
            if cnt > 0:  # 미생물이 0이면 소멸 (저장하지 않는다)
                temp[nx][ny].append((cnt, di))
            
            
        # ===== 이동 후 병합 =====
        new_micro = []
                    
        for i in range (n):
            for j in range (n):
                
                if len(temp[i][j]) == 1: # 군집이 하나일 경우 append!
                    c, di = temp[i][j][0]
                    new_micro.append([i, j, c, di])
                    
                elif len(temp[i][j]) > 1: # 군집이 여러개일 경우 병합
                    total_cnt = sum(c for c, _ in temp[i][j]) # 미생물의 합
                    max_cnt, new_dir = max(temp[i][j])  # 미생물 수 가장 많은 방향 유지
                    new_micro.append([i, j, total_cnt, new_dir])

        
        # ===== 갱신 =====
        micro = new_micro

    res = sum(c for _, _, c, _ in micro)
    print(f"#{test_case} {res}")