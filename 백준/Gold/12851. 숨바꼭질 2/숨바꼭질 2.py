from collections import deque

def bfs():
    q = deque()
    q.append(n)

    count[n] = 1 # 시작점

    while q:
        cur = q.popleft()

        if cur == k:
            print(visited[cur])
            print(count[cur])
            return

        # case1: x-1 case2:x+1 case:x+3
        for nxt in [cur+1, cur-1, 2*cur]:
            if 0<=nxt<100001:

                # 첫 방문일 경우
                # count는 cur과 동일, visited 1 증가!
                if visited[nxt] == 0:
                    visited[nxt] = visited[cur] + 1
                    count[nxt] = count[cur]
                    q.append(nxt)

                # 이미 방문한적이 있는 경우
                # 최단 시간이 같다면 count 누적
                elif visited[nxt] == visited[cur] + 1:
                    count[nxt] += count[cur]
                    

n, k = map(int, input().split())
visited = [0] * 100001 
count = [0] * 100001 # 경로 개수 누적

bfs()