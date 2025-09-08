import sys
input = sys.stdin.readline

def dfs(day, total):
    global ans
    if day == n + 1:  
        ans = max(ans, total)
        return
    
    if day > n + 1:  
        return

    # 오늘 상담 O
    if day + time[day] <= n + 1:
        dfs(day + time[day], total + price[day])
    
    # 오늘 상담 X
    dfs(day + 1, total)

n = int(input())
time = [0] * (n + 1) 
price = [0] * (n + 1)

for i in range(1, n + 1):
    t, p = map(int, input().split())
    time[i] = t
    price[i] = p

ans = 0
dfs(1, 0) 
print(ans)
