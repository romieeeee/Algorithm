n, m = map(int, input().split())
floor = [list(input()) for _ in range (n)]

cnt = 0

for i in range (n):
    j = 0
    while j < m:
        if floor[i][j] == '-':
            cnt += 1

            while j < m and floor[i][j] == '-': # 인접한 두 행이 다를 때까지 찾기
                j += 1
        else:
            j += 1
        

for j in range (m):
    col = [floor[x][j] for x in range (n)]

    i = 0
    while i<n:
        if col[i] == '|':
            cnt += 1

            while i<n and col[i] == '|':
                i += 1

        else:
            i += 1

print(cnt)