from collections import deque
import sys
input = sys.stdin.readline

# 우, 하, 좌, 상
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def change_dir(idx, c):
    if c == 'D':  # 오른쪽 회전
        return (idx + 1) % 4
    else:  # 왼쪽 회전
        return (idx - 1) % 4


n = int(input()) # 보드의 크기 (n*n)
k = int(input()) # 사과의 개수

graph = [[0] * n for _ in range (n)]

for _ in range (k):
  r, c = map(int, input().split())
  graph[r-1][c-1] = 2 # 사과의 위치는 2!

l = int(input())

info = [[] for _ in range (10001)]
for _ in range(l):
  s, di = input().split()
  info[int(s)].append(di)

sec = 0 # 매 초마다 이동한다...
idx = 0 # 현재 방향...
x = y = 0 # 현재 위치...

snake = deque()
snake.append((x, y))

while True:

  # 다음 위치 계산
  x += d[idx][0]
  y += d[idx][1]

  sec += 1

  # 종료 조건
  if x < 0 or x >= n or y < 0 or y >= n  or (x, y) in snake:
    break
  
  snake.append((x, y)) # 뱀 길이 늘리기
  
  if graph[x][y] == 2:
    graph[x][y] = 0 # 사과는 없어진다
  else:
    snake.popleft() # 꼬리 지우기

  if info[sec]: # 현재 초에 방향을 바꿔야 한다면!
    idx = change_dir(idx, info[sec][0])

print(sec)