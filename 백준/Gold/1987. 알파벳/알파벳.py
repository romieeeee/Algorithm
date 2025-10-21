import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y, cnt):
  global max_cnt

  if max_cnt < cnt: max_cnt = cnt

  for i in range (4):
    nx, ny = x+dx[i], y+dy[i]

    if 0<=nx<r and 0<=ny<c and not visited[nx][ny] and board[nx][ny] not in alpha:
      visited[nx][ny] = True
      alpha.add(board[nx][ny])

      dfs(nx, ny, cnt+1)
      
      visited[nx][ny] = False
      alpha.remove(board[nx][ny])


r, c = map(int, input().split())
board = [[x for x in input().rstrip()] for _ in range (r)]
visited = [[False] * c for _ in range (r)]

alpha = set()

visited[0][0] = True
alpha.add(board[0][0])

max_cnt = 0
dfs(0, 0, 0)

print(max_cnt+1)