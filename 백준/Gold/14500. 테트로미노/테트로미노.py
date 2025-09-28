import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, depth, value):
    global max_value

    if depth == 4:
        if value > max_value: max_value = value
        return
    
    for i in range (4):
        nx, ny = x+dx[i], y+dy[i]

        if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, depth+1, value+graph[nx][ny])
            visited[nx][ny] = False


def check_extra(x, y): # 'ㅗ' 모양 탐색...
        global max_value

        # 'ㅗ'
        if x-1 >= 0 and  y-1 >= 0 and y+1 < m:    
            total = graph[x][y] + graph[x-1][y] + graph[x][y-1] + graph[x][y+1]
            if total > max_value: max_value = total

        # 'ㅜ'
        if x+1 < n and  y-1 >= 0 and y+1 < m:    
            total = graph[x][y] + graph[x+1][y] + graph[x][y-1] + graph[x][y+1]
            if total > max_value: max_value = total

        # 'ㅏ'
        if x-1 >= 0 and x+1 < n and y+1 < m:    
            total = graph[x][y] + graph[x-1][y] + graph[x+1][y] + graph[x][y+1]
            if total > max_value: max_value = total

        # 'ㅓ'
        if x-1 >= 0 and x+1 < n and  y-1 >= 0:    
            total = graph[x][y] + graph[x-1][y] + graph[x+1][y] + graph[x][y-1]
            if total > max_value: max_value = total


n, m = map(int, input().split()) # 세로, 가로
graph = [list(map(int, input().split())) for _ in range (n)]

visited = [[False] * m for _ in range (n)]

max_value = 0

for i in range (n):
    for j in range (m):
        visited[i][j] = True
        dfs(i, j, 1, graph[i][j])
        visited[i][j] = False

        check_extra(i, j)

print(max_value)