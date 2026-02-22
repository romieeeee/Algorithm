from collections import deque

def solution(maps):
    n = len(maps[0])
    m = len(maps)

    visited = [[-1] * n for _ in range (m)]
    
    dy = [-1, 1, 0, 0] 
    dx = [0, 0, -1, 1] 

    def bfs():
        q = deque()
        q.append([0, 0]) 
        visited[0][0] = 1
        
        while q:
            x, y = q.popleft()

            if x == (m-1) and y == (n-1):
                break

            for i in range (4):
                nx, ny = x+dx[i], y+dy[i] 

                # 맵 밖으로 나간 경우
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                
                # 벽인 경우
                if maps[nx][ny] == 0:
                    continue

                # 이미 방문한 경우
                if visited[nx][ny] != -1:
                    continue
                
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1 

        return visited[-1][-1]

    return bfs()

