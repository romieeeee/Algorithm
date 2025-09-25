import sys

input = sys.stdin.readline

def dfs(depth, value, plus, minus, mul, div):
    global max_val, min_val

    if depth == n:
        max_val = max(max_val, value)
        min_val = min(min_val, value)
        return
    
    if plus > 0:
        dfs(depth+1, value+nums[depth], plus-1, minus, mul, div)
    
    if minus > 0:
        dfs(depth+1, value-nums[depth], plus, minus-1, mul, div)
    
    if mul > 0:
        dfs(depth+1, value*nums[depth], plus, minus, mul-1, div)
    
    if div > 0:
        if value < 0:
            tmp = -(-value//nums[depth])
        else:
            tmp = value//nums[depth]
            
        dfs(depth+1, tmp, plus, minus, mul, div-1)


n = int(input()) # 수의 개수
nums = list(map(int, input().split()))
ops = list(map(int, input().split())) # +, -, *, / 

max_val = -1e9
min_val = 1e9

dfs(1, nums[0], ops[0], ops[1], ops[2], ops[3])

print(int(max_val))
print(int(min_val))