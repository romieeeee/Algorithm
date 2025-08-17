def dfs(idx, start):
    global part, cnt

    if idx == depth:
        if sum(part) == s: # 합이 s인 경우 cnt 증가
            cnt += 1
        
        return
    
    for i in range (start, n):
        if not visited[i]:
            visited[i] = True
            part[idx] = arr[i]

            dfs(idx+1, i)

            visited[i] = False

    
n, s = map(int, input().split())
arr = list(map(int, input().split()))

visited = [0] * n # 방문 확인 배열

cnt = 0 # 경우의 수 

# 1~n개의 부분수열을 생성하면서 모든 경우의 수를 확인한다
for i in range (1, n+1):
    depth = i
    part = [0] * i # 부분수열

    dfs(0, 0)

print(cnt)

