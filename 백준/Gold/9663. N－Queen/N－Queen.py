def dfs(cur):
    global cnt
    
    if cur == n:
        cnt += 1
        return
    
    # 특정 좌표에 어떻게 퀸을 둘 수 있을까?

    for i in range (n):
        if not visited1[i] and not visited2[i+cur] and not visited3[cur-i+n-1]:
            visited1[i] = True 
            visited2[i+cur] = True 
            visited3[cur-i+n-1] = True 

            dfs(cur+1)

            visited1[i] = False 
            visited2[i+cur] = False 
            visited3[cur-i+n-1] = False 
    

n = int(input()) # n개의 퀸을 둔다
graph = [[0] * n for _ in range (n)]

visited1 = [False] * 40 # 행
visited2 = [False] * 40 # 대각선1
visited3 = [False] * 40 # 대각선2


cnt = 0 # 퀸의 개수를 저장
dfs(0)

print(cnt)