from collections import deque

d = [[1, 0], [0, 1], [-1, 0], [0, -1]]
def dfs(x, y, dist):
    global min_dist
    
    if dist > min_dist:
        return
    
    if (x, y) == (n-1, m-1):
        if dist < min_dist: min_dist = dist
        return
    
    for dx, dy in d:
        nx, ny = x+dx, y+dy
        
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
            if graph[nx][ny] == 1:
                visited[nx][ny] = True
                dfs(nx, ny, dist+1) 
                visited[nx][ny] = False
                

def bfs():
    q.append([0, 0])
    visited[0][0] = 1
    
    while q:
        x, y = q.popleft()
        
        if (x, y) == (n-1, m-1):
            print(visited[x][y])
            return
        
        for dx, dy in d:
            nx, ny = x+dx, y+dy
        
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append([nx, ny])

n, m = map(int, input().split())
graph = [[int(x) for x in input()] for _ in range (n)]

# -- dfs --
# min_dist = 1e9
# visited = [[False] * m for _ in range (n)]

# visited[0][0] = True
# dfs(0, 0, 1)

# print(min_dist)

# -- bfs --
visited = [[0] * m for _ in range (n)]

q = deque()

bfs()