import sys
input = sys.stdin.readline

def dfs(depth, value, plus, minus, mul, div):
    global max_res, min_res
    if depth == n:  
        max_res = max(max_res, value)
        min_res = min(min_res, value)
        return

    if plus > 0:
        dfs(depth+1, value + nums[depth], plus-1, minus, mul, div)
    if minus > 0:
        dfs(depth+1, value - nums[depth], plus, minus-1, mul, div)
    if mul > 0:
        dfs(depth+1, value * nums[depth], plus, minus, mul-1, div)
    if div > 0:
        if value < 0:
            dfs(depth+1, -(-value // nums[depth]), plus, minus, mul, div-1)
        else:
            dfs(depth+1, value // nums[depth], plus, minus, mul, div-1)

n = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))  # [+, -, *, /] 

max_res = -int(1e9)  
min_res = int(1e9)

dfs(1, nums[0], ops[0], ops[1], ops[2], ops[3])

# 결과 출력
print(max_res)
print(min_res)