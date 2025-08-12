from collections import deque

def bfs(x, y):
    global safe
    visited[x][y] = True

    while q:
        x, y = q.popleft()

        for dx, dy in dir:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] > cur and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))


dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# 일정한 높이 이하의 모든 지점은 물에 잠긴다고 가정
# 물에 잠기지 않는 안전한 영역의 최대 개수를 계산

n = int(input())
graph = [list(map(int, input().split())) for _ in range (n)]
visited = [[False] * n for _ in range (n)]

q = deque()

h = max(map(max, graph))  
rain = [x for x in range (h+1)] # 비 높이를 모두 고려한다

safe = 0 # 안전 영역 개수
max_safe = 0 # 최대 안전 영역 개수

for i in range (len(rain)):
    safe = 0
    cur = rain[i]

    for x in range (n):
        for y in range (n):
            if graph[x][y] > cur and not visited[x][y]:
                safe += 1
                q.append((x, y))
                bfs(x, y)

                if safe > max_safe: max_safe = safe

    # 높이가 바뀔 때마다 방문 배열 초기화
    visited = [[False] * n for _ in range (n)]

print(max_safe)