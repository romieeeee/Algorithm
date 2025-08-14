import sys

def dfs(depth, start):
    global min_res

    # 팀 선택이 끝났다면 능력치를 비교 후 최솟값 업데이트
    if depth == p:
        cnt = 0
        for i in range (n):
            # 1팀에 없는 사람들은 2팀으로 배정
            if i not in team_1:
                team_2[cnt] = i
                cnt += 1

        # 1팀과 2팀의 능력치를 구한다
        val_1 = val_2 = 0

        for i in range(p-1):
            for j in range(i + 1, p):
                val_1 += ppl[team_1[i]][team_1[j]] + ppl[team_1[j]][team_1[i]]
                val_2 += ppl[team_2[i]][team_2[j]] + ppl[team_2[j]][team_2[i]]

        min_res = min(min_res, abs(val_1-val_2))
        
        return
    
    prev = None
    for i in range (start, n):
        if not visited[i] and i != prev:
            visited[i] = True
            team_1[depth] = i # 1팀에 사람 넣기

            prev = i

            dfs(depth+1, i)

            visited[i] = False

n = int(sys.stdin.readline()) # 1부터 n+1까지
ppl = [list(map(int, sys.stdin.readline().split())) for _ in range (n)] # n*n

visited = [False] * n

# N/2명으로 이루어진 스타트 팀과 링크 팀으로 사람들을 나눠야 한다
p = n//2
team_1 = [0] * p
team_2 = [0] * p

min_res = 1e9
dfs(0, 0)

print(min_res)
