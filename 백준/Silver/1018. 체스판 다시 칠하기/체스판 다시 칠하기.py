n, m = map(int, input().split())

board = [list(input()) for _ in range (n)]

min_cnt = n*m
for i in range (n-7): # m-8+1
    for j in range (m-7):

        cnt1 = 0  # 'W'로 시작할 때
        cnt2 = 0  # 'B'로 시작할 때

        for x in range (8):
            for y in range (8):
                cur = board[i+x][j+y]

                # 'W' 시작 체스판일 때 
                if x % 2 == 0:  
                    if y % 2 == 0:  # 짝수 열
                        if cur != 'W':
                            cnt1 += 1
                    else:  # 홀수 열
                        if cur != 'B':
                            cnt1 += 1
                else:  # 홀수 행
                    if y % 2 == 0:  # 짝수 열
                        if cur != 'B':
                            cnt1 += 1
                    else:  # 홀수 열
                        if cur != 'W':
                            cnt1 += 1

                # 'B' 시작 체스판일 때 
                if x % 2 == 0:  # 짝수 행
                    if y % 2 == 0:  # 짝수 열
                        if cur != 'B':
                            cnt2 += 1
                    else:  # 홀수 열
                        if cur != 'W':
                            cnt2 += 1
                else:  # 홀수 행
                    if y % 2 == 0:  # 짝수 열
                        if cur != 'W':
                            cnt2 += 1
                    else:  # 홀수 열
                        if cur != 'B':
                            cnt2 += 1

        min_cnt = min(min_cnt, cnt1, cnt2)

print(min_cnt)
