def solution(n, arr):
    answer = 0

    visited = [False] * n 

    def dfs(cur):
        # 방문 처리
        visited[cur] = True

        # 현재 컴퓨터의 관계성 탐색
        for nxt in range (n):
            if arr[cur][nxt] == 1 and not visited[nxt]:
                dfs(nxt)

    for i in range(n):
        if not visited[i]:
            dfs(i)     
            answer += 1 
            
    return answer    