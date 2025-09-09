import sys
imput = sys.stdin.readline

def dfs(x, cnt):
    global min_cnt
    
    if x > b:
        return
    
    if x == b:
        min_cnt = min(min_cnt, cnt)
        return
    
    dfs(x*2, cnt+1)
    dfs(x*10+1, cnt+1)


a, b = map(int, input().split())

min_cnt = int(1e9)
dfs(a, 0)

if min_cnt == 1e9:
    print(-1)
else:
    print(min_cnt+1)