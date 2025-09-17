from collections import deque

def bfs():
    q = deque()
    q.append(n)

    while q:
        cur = q.popleft()

        if cur == k:
            print(visited[cur])
            return

        for nxt in [2*cur, cur-1, cur+1]:
            if 0<=nxt<100001:
                if visited[nxt] == 0:
                    if nxt == 2*cur: # 순간이동은 0초 후
                        visited[nxt] = visited[cur]
                    else:
                        visited[nxt] = visited[cur] + 1
                    
                    q.append(nxt)

n, k = map(int, input().split())
visited = [0] * 100001 

bfs()