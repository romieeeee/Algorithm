from collections import deque

d = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def bfs():
    q = deque()
    q.append([0, 0, 0]) # x, y, break_cnt
    visited[0][0] = True
    
    while q:
        x, y, cnt = q.popleft()

        if (x, y) == (n-1, m-1):
            return cnt
        
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if graph[nx][ny] == 0: # 0이면 그냥 가
                    visited[nx][ny] = True
                    q.appendleft([nx, ny, cnt])
                else: # 1이면 부시고 가
                    visited[nx][ny] = True
                    q.append([nx, ny, cnt+1])
        
m, n = map(int, input().split())
graph = [[int(x) for x in input()] for _ in range (n)]

visited = [[False] * m for _ in range (n)]

res = bfs()

if (res): 
    print(res) 
else: 
    print(0) 