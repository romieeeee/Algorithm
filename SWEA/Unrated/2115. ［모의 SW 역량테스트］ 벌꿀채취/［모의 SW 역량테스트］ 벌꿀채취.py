def get_max_profit(idx, total, profit):
    global max_profit
    if total > c:  
        return
    
    if idx == m: 
        max_profit = max(max_profit, profit)
        return

    # 현재 꿀 선택
    get_max_profit(idx+1, total + tmp_arr[idx], profit + tmp_arr[idx]**2)
   
    # 현재 꿀 선택하지 않음
    get_max_profit(idx+1, total, profit)


T = int(input())
for test_case in range(1, T+1):
    # 벌통의 크기, 선택할 수 있는 벌통의 개수, 채취할 수 있는 최대 양
    n, m, c = map(int, input().split())

    honey = [list(map(int, input().split())) for _ in range (n)]
    profit = [[0] * n for _ in range (n)]


    tmp_arr = []
    for i in range (n):
        for j in range (n-m+1):
            # m개의 벌통 선택
            tmp_arr = honey[i][j:j+m]

            max_profit = 0
            get_max_profit(0, 0, 0)

            profit[i][j] = max_profit


    res = 0
    for i in range(n):
        for j in range(n-m+1):
            for x in range(i, n):
                # 같은 행이면 겹치지 않게
                if i == x:
                    start = j+m
                else:
                    start = 0
                for y in range(start, n - m + 1):
                    res = max(res, profit[i][j] + profit[x][y])

    print(f"#{test_case}", res)