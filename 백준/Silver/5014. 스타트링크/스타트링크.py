from collections import deque

def bfs():
    while q:
        now, cnt = q.popleft()

        if now == g:
            print(cnt)
            return
        
        up = now+u
        down = now-d

        if 1<=up<=f and not visited[up]:
            visited[up] = True
            q.append((up, cnt+1))

        if 1<=down<=f and not visited[down]:
            visited[down] = True
            q.append((down, cnt+1))
    else:
        print('use the stairs')

f, s, g, u, d = map(int, input().split())
visited = [False] * (f+1)

q = deque()

q.append((s, 0))
visited[s] = True

bfs()
