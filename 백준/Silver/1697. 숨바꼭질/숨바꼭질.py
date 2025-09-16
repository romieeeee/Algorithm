from collections import deque

def bfs():
    
    while q:
        x, sec = q.popleft()
        
        if x == k:
            return sec

        for nxt in [x-1, x+1, 2*x]:
            if 0<=nxt<100001 and not visited[nxt]:
                visited[nxt] = True
                q.append([nxt, sec+1])

# 점 n에서 k로 이동!
n, k = map(int, input().split())

q = deque()
visited = [False] * 100001

q.append([n, 0])
visited[n] = True

print(bfs())
