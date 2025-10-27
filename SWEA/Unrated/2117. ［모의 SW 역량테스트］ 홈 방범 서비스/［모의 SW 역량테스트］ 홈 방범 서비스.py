T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]

    res = 0
    
    # 집만 배열에 담는다
    houses = [(i, j) for i in range(n) for j in range(n) if graph[i][j] == 1]

    for x in range(n):
        for y in range(n):
            
            # 서비스 범위
            for k in range(1, n + 2): 
                
                # 비용 계산
                cost = k * k + (k - 1) * (k - 1)
                cnt = 0
                
                for hx, hy in houses:
                    if abs(hx - x) + abs(hy - y) < k:
                        cnt += 1
                        
                # 손해를 보지 않는 선에서 최대값을 구한다
                if cnt * m >= cost:
                    res = max(res, cnt)

    print(f'#{test_case} {res}')
