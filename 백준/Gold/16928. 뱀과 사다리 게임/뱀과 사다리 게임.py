import sys
from collections import deque
input = sys.stdin.readline

def bfs():
  while q:
    x = q.popleft()

    if x == 100:  
      return

    for i in range (1, 7): # 주사위 굴리기
      nx = x+i # 이동할 위치 (현재 위치 + 주사위 값)

      if nx <= 100:
        nx = board[nx] # 사다리 또는 뱀!

        if not visited[nx]:
          q.append(nx)
          dice[nx] = dice[x] + 1  
          visited[nx] = True

n, m = map(int, input().split())
board = [x for x in range (101)]

for _ in range (n+m):
  x, y = map(int, input().split())
  board[x] = y

visited = [False] * 101
dice = [0] * 101

q = deque()
q.append(1)
visited[1] = True

bfs()

print(dice[-1])